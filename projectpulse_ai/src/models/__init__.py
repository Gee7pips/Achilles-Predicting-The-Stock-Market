"""Models package.

Importing this package ensures the mock model is generated at startup.
"""
from importlib import import_module

# Ensure the mock risk model file exists
import_module(__name__ + ".mock_risk_model")