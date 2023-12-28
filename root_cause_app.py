import streamlit as st
import torch
from transformers import DistilBertForSequenceClassification, DistilBertTokenizer
import numpy as np
import joblib
import os

# Load the model
save_dir = r"C:\Users\shiri\root_cause_analysis\jupyter_notebooks"
model_path = os.path.join(save_dir, "distilbert_root_cause_model3")
model = DistilBertForSequenceClassification.from_pretrained(model_path)

# Load the tokenizer
tokenizer_path = os.path.join(save_dir, "distilbert_tokenizer3")
tokenizer = DistilBertTokenizer.from_pretrained(tokenizer_path)

# Load the label encoder
label_encoder_path = os.path.join(save_dir, "label_encoder3.pkl")
label_encoder = joblib.load(label_encoder_path)

# Function to predict root causes
def predict_root_causes(contact_driver_text):
    # Tokenize the input text
    inputs = tokenizer(contact_driver_text, return_tensors="pt", truncation=True, padding=True, max_length=512)

    # Get model predictions (logits)
    with torch.no_grad():
        logits = model(**inputs).logits
    
    # Apply softmax to convert logits to probabilities
    probabilities = torch.nn.functional.softmax(logits, dim=1).flatten()

    # Get the indices of the top 5 predictions
    top5_indices = torch.argsort(probabilities, descending=True)[:5]

    # Convert indices to class names
    top5_classes = [label_encoder.classes_[i] for i in top5_indices]

    return top5_classes

# Streamlit UI
st.title("Root Cause Predictor")

# Input text box
user_input = st.text_area("Please enter your Contact Driver:")

if st.button("Predict"):
    if user_input:
        # Call the prediction function
        predicted_root_causes = predict_root_causes(user_input)
        st.write("Top 5 predicted Root Causes:")
        for cause in predicted_root_causes:
            st.write(cause)
    else:
        st.warning("Please enter a Contact Driver text.")