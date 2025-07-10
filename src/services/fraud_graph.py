import pandas as pd
import networkx as nx
from typing import Dict, Any, List, Union
import os
import json

def load_network_data(file_path: str) -> pd.DataFrame:
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".csv":
        return pd.read_csv(file_path)
    elif ext == ".json":
        with open(file_path, "r") as f:
            data = json.load(f)
        return pd.DataFrame(data)
    else:
        raise ValueError("Unsupported file format")

def detect_fraud_patterns(df: pd.DataFrame) -> Dict[str, Any]:
    suspicious = {"collusion": [], "recycled_subcontractors": [], "high_amounts": []}
    # Collusion: same contractor+insider pair on multiple projects
    pairs = df.groupby(["contractor", "insider"]).size()
    for (contractor, insider), count in pairs.items():
        if count > 2:
            suspicious["collusion"].append({"contractor": contractor, "insider": insider, "count": int(count)})
    # Recycled subcontractors: same subcontractor on >2 projects
    subs = df["subcontractor"].value_counts()
    for sub, count in subs.items():
        if count > 2:
            suspicious["recycled_subcontractors"].append({"subcontractor": sub, "count": int(count)})
    # High contract amounts (arbitrary threshold for MVP)
    for _, row in df.iterrows():
        if row["amount"] > 1100000:
            suspicious["high_amounts"].append({"project_id": row["project_id"], "contractor": row["contractor"], "amount": row["amount"]})
    return suspicious

def analyze_vendor_network(file_path: str) -> Dict[str, Any]:
    df = load_network_data(file_path)
    suspicious = detect_fraud_patterns(df)
    # Optionally: build and return a graph summary
    G = nx.Graph()
    for _, row in df.iterrows():
        G.add_edge(row["contractor"], row["subcontractor"], project=row["project_id"], insider=row["insider"], amount=row["amount"])
    return {"suspicious": suspicious, "num_nodes": G.number_of_nodes(), "num_edges": G.number_of_edges()}