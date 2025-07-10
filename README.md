# ProjectPulse.AI

ProjectPulse.AI is an AI-powered project monitoring and oversight platform designed for Development Finance Institutions (DFIs) like the DBSA, AfDB, and municipalities.

## MVP Features
- **Upload & Parse Project Documents**: Accepts PDFs, Word, Excel; extracts key fields; OCR for scanned docs; auto-classifies document type.
- **Risk Signal Engine**: Flags risk signals (budget overruns, delays, missing docs, suspicious vendors) using rules and basic ML.
- **Interactive Dashboard**: Streamlit dashboard with sortable risk scores, drill-down views, timelines, flagged risks, and AI summaries.
- **AI Summarization & Voice Note Parser**: Summarizes docs/voice notes, highlights risks, and suggests stakeholder updates.
- **Admin Panel**: Basic auth, project upload, risk dashboard.
- **Config & Deployment**: YAML config, Dockerfile, docker-compose.

## Structure
- `/src/api/` - FastAPI endpoints
- `/src/services/` - Business logic, ML, NLP, OCR
- `/src/models/` - Pydantic models, DB schemas
- `/data/` - Sample/test data
- `/config/` - Config files
- `/notebooks/` - Prototyping, EDA

## Install & Run
```bash
git clone <repo-url>
cd ProjectPulse.AI
pip install -r requirements.txt
uvicorn src.api.main:app --reload
streamlit run src/api/dashboard.py
```

For Docker:
```bash
docker-compose up --build
```

# Achilles, Neural Network to Predict Commodities 
Integration with Trading Bot for Automatic Trading 🖤🤖🖤     💲Ready to Predict the Future?💲

Achilles Is a LSTM (Long Short Term Memory) Architecture made and optimized to predict GOLD Vs USD. For this implementation we take the power of LSTM, we process our data with two techinal indicators (EMA, RSI)
We make predictions with our model. Then we scrapt the news from 3 different websites, Implementing sentiment analysis and Forward Prediction we integrate these components in a trading bot for automatic trading

After a one-month period testing our model had 162% return in capital. Demostrating that Machine Learning with LSTM Can predict the stock market and can be integrated into automatic trading without human intervention.


----->> First Component: (Achilles) LSTM Neural Network trained on seasonal Times Frames 15 Minutes, 5 Minutes and 1 Minute data of the S&P500 Market, with this model we'll try to predict the future market during 30 days or 33000 minutes
We're getting the estimate prices of the market and we'll save this into a CSV file for our trading bot

----->>Second Component: FINbert Sentiment Analysis to scratch and estimate the news in 3 different WebSites:

  -https://www.benzinga.com (XAU-USD)
  
  -https://www.investing.com (XAU-USD)
  
  -https://www.ft.com (General Market News)

----->> Third Component: Trading bot Used in mt5 in a Paper account. Based on the predictions made by Achilles and the real-time sentiment news the model trades, sending buy and sell orders. The bot runs each minute since the predictions are in a minute-by-minute timeframe. This allows our model to take profit fast in the market and reduce large fluctuations. 

You can see the paper we have on this link:   https://arxiv.org/pdf/2410.21291
(Working in a Journal Paper for Updated Version of Achilles)
