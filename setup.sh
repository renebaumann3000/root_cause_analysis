#!/bin/bash

# Custom PyTorch CPU-only installation
pip install --index-url https://download.pytorch.org/whl/cpu torch==2.1.1

# Install other requirements
pip install -r requirements.txt

# Setup Streamlit configuration
mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
" > ~/.streamlit/config.toml