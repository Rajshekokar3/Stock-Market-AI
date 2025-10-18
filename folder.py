import os

# Define folder structure
folders = [
    "stock-sentiment-ai/data/raw",
    "stock-sentiment-ai/data/processed",
    "stock-sentiment-ai/notebooks",
    "stock-sentiment-ai/src/data",
    "stock-sentiment-ai/src/models",
    "stock-sentiment-ai/src/utils",
    "stock-sentiment-ai/src/app/components",
    "stock-sentiment-ai/models",
    "stock-sentiment-ai/results",
    "stock-sentiment-ai/logs",
    "stock-sentiment-ai/deployment"
]

# Define files to create with optional starter content
files = {
    "stock-sentiment-ai/README.md": "# Stock Sentiment AI\n\nAI-powered project for stock sentiment and price prediction.",
    "stock-sentiment-ai/requirements.txt": "pandas\nnumpy\nmatplotlib\ntensorflow\nscikit-learn\nnltk\nspacy\nyfinance\nstreamlit\nbeautifulsoup4\nrequests\nseaborn",
    "stock-sentiment-ai/.gitignore": "*.pyc\n__pycache__/\n.env\nmodels/*.h5\nlogs/\n*.csv",
    "stock-sentiment-ai/src/__init__.py": "",
    "stock-sentiment-ai/src/data/collect_data.py": "# Fetch stock & news data\n",
    "stock-sentiment-ai/src/data/preprocess_text.py": "# Clean and tokenize text\n",
    "stock-sentiment-ai/src/data/preprocess_stock.py": "# Normalize stock prices\n",
    "stock-sentiment-ai/src/models/sentiment_lstm.py": "# Build LSTM model for sentiment analysis\n",
    "stock-sentiment-ai/src/models/stock_lstm.py": "# Build LSTM model for stock prediction\n",
    "stock-sentiment-ai/src/models/hybrid_model.py": "# Combine sentiment + stock models\n",
    "stock-sentiment-ai/src/utils/helper.py": "# Common helper functions\n",
    "stock-sentiment-ai/src/utils/visualization.py": "# Plot graphs & trends\n",
    "stock-sentiment-ai/src/app/main.py": "# Streamlit main app\n",
    "stock-sentiment-ai/src/app/components/sentiment_section.py": "# Streamlit section for sentiment\n",
    "stock-sentiment-ai/src/app/components/stock_section.py": "# Streamlit section for stock data\n",
    "stock-sentiment-ai/src/app/components/hybrid_section.py": "# Streamlit section for hybrid model\n",
    "stock-sentiment-ai/logs/training_logs.txt": "",
    "stock-sentiment-ai/logs/errors.log": "",
    "stock-sentiment-ai/deployment/streamlit_app.py": "# Streamlit app entry point\n",
    "stock-sentiment-ai/deployment/Dockerfile": "# Dockerfile for deployment\n",
    "stock-sentiment-ai/deployment/setup.sh": "#!/bin/bash\n# Setup script\n"
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for filepath, content in files.items():
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ Project structure created successfully at 'stock-sentiment-ai/'")
