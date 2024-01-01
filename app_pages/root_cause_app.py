import streamlit as st
import torch
from transformers import DistilBertForSequenceClassification, DistilBertTokenizer
import numpy as np
import joblib
import os
import plotly.graph_objects as go

# Dropdown options
business_types = [
    "Automotive and Energy",
    "Banking and Finance",
    "Digital Advertising",
    "Digital Banking",
    "E-Commerce",
    "Engineering Software",
    "Enterprise Software",
    "Multinational",
    "Retail",
    "Retail Banking and Brokerage",
    "SaaS",
    "Telecommunications"
]

specialisations = {
    "Automotive and Energy": ["Electric Mobility and Sustainable Energy"],
    "Banking and Finance": ["Banking Services"],
    "Digital Advertising": ["Online Ads"],
    "Digital Banking": ["Financial Technology"],
    "E-Commerce": ["Diverse Products", "Fashion", "Food", "Various"],
    "Engineering Software": ["Industrial and Engineering Solutions"],
    "Enterprise Software": ["Business Solutions"],
    "Multinational": ["Diverse Industries"],
    "Retail": ["Department Store", "General Store", "Supermarket"],
    "Retail Banking and Brokerage": ["Financial Services"],
    "SaaS": [
        "Business Banking and Payments",
        "CRM",
        "CRM and Marketing",
        "Customer Support",
        "Payment Processing",
        "Payment Solutions",
        "Survey and Feedback"
    ],
    "Telecommunications": ["Mobile and Broadband Services", "Network and Digital Services"]
}

product_categories = {
    "Banking Services": [
        "ATM Network", "Business Accounts", "Checking Accounts", "Credit Cards",
        "Cybersecurity Services", "Financial Consulting", "Fintech Partnerships",
        "Foreign Exchange", "Fund Transfer Services", "Insurance Products",
        "Investment Services", "Loan Servicing", "Mobile Banking", "Mortgages",
        "Online Banking Tools", "Payment Processing", "Personal Loans",
        "Retirement Planning", "Savings Accounts", "Wealth Management"
    ],
    "Business Banking and Payments": ["Business Banking", "Corporate Cards", "Expense Management"],
    "Business Solutions": [
        "Business Intelligence Software", "Cloud-Based Storage Solutions", "CRM System",
        "Customer Relationship Management", "ERP Software", "HR Management",
        "Human Resource Management System", "Project Management Tools",
        "Supply Chain Management"
    ],
    "CRM": [
        "Analytics Tool", "Campaign Management Tool", "CRM Software",
        "Customer Data Management", "Customer Service Module", "Customer Support Platform",
        "Document Management Module", "Lead Management System", "Marketing Automation",
        "Sales Automation Module", "Sales Automation Tool"
    ],
    "CRM and Marketing": [
        "Campaign Management Tool", "Content Management System", "Customer Support Platform",
        "Document Management Module", "Lead Management System", "Marketing Software",
        "Sales Automation Module", "Sales Software", "Service Software"
    ],
    "Customer Support": [
        "Campaign Management Tool", "Customer Support Platform", "Customer Support Software",
        "Document Management Module", "Help Center Solution", "Lead Management System",
        "Live Chat Tool", "Sales Automation Module"
    ],
    "Department Store": [
        "Apparel", "Bakery & Confectionery", "Beverages", "Electronics",
        "Fresh Produce", "Groceries", "Health & Beauty", "Home & Kitchen Essentials",
        "Home Goods", "Pharmacy"
    ],
    "Diverse Industries": [
        "Automotive Products", "Biotechnology Products", "Consumer Electronics",
        "Energy Solutions", "Home Appliances", "Industrial Equipment",
        "Information Technology Solutions", "Medical Devices", "Pharmaceuticals"
    ],
    "Diverse Products": [
        "Electronic Gadgets", "Fashion Accessories", "Health and Wellness Products",
        "Home Appliances", "Sporting Goods"
    ],
    "Electric Mobility and Sustainable Energy": [
        "Aftermarket Products", "Automotive Parts", "Automotive Software",
        "Car Accessories", "Car Care Products", "Charging Equipment",
        "Commercial Trucks", "Driver Assistance Technologies", "Electric Vehicles",
        "Energy Storage", "Fleet Services", "Hybrid Models", "Motorcycles",
        "Navigation Systems", "Passenger Cars", "Performance Kits",
        "Safety Equipment", "Solar Products", "Tires and Wheels", "Vehicle Batteries",
        "Vehicle Telematics"
    ],
    "Fashion": [
        "Accessories", "Bottoms", "Casual Wear", "Footwear", "Formal Attire", "Outerwear", "Sportswear", "Tops"
    ],
    "Financial Services": [
        "Banking Services", "Brokerage", "Business Banking Services", "Credit and Loans",
        "Investment Solutions", "Mortgage Services", "Personal Banking Services",
        "Savings and Investment Products", "Wealth Management Services"
    ],
    "Financial Technology": ["Digital Banking", "Financial Services", "Payment Cards"],
    "Food": [
        "Beverages", "Dairy & Eggs", "Fresh Produce", "Meat & Fish", "Pantry Items", "Snacks"
    ],
    "General Store": [
        "Bakery & Confectionery", "Beverages", "Clothing", "Electronics",
        "Fresh Produce", "Grocery", "Health & Beauty", "Home & Kitchen Essentials",
        "Home Goods"
    ],
    "Industrial and Engineering Solutions": [
        "Business Intelligence Software", "CAD Software", "CRM Software",
        "Document Management Systems", "ERP Systems", "Industrial Automation",
        "PLM Systems", "Project Management Tools", "Simulation Tools"
    ],
    "Mobile and Broadband Services": [
        "Broadband Services", "Cloud Services", "Cybersecurity Solutions", "Digital Solutions",
        "Internet Services", "IoT Connectivity", "Mobile Communication", "Mobile Network Packages",
        "Network Security"
    ],
    "Network and Digital Services": [
        "Broadband Services", "Cloud Computing", "Cloud Services", "Cybersecurity",
        "Cybersecurity Solutions", "Internet Services", "IoT Connectivity",
        "Mobile Network Packages", "Mobile Networks"
    ],
    "Online Ads": [
        "App Promotion", "Customer Relationship Management", "Display Ads", "Email Marketing Software",
        "Marketing Analytics", "Search Ads", "Search Engine Optimization",
        "Social Media Advertising", "Video Ads"
    ],
    "Payment Processing": [
        "Blockchain Solutions", "Financial Reporting", "Insurance Tech", "Lending Platform",
        "Merchant Services", "Payment Gateway", "Risk Management Software", "Wealth Management Solutions"
    ],
    "Payment Solutions": [
        "Fraud Management System", "Mobile Payments", "Online Payments"
    ],
    "Supermarket": [
        "Bakery", "Bakery & Confectionery", "Beverages", "Dairy", "Fresh Produce",
        "Grocery", "Health & Beauty", "Home & Kitchen Essentials", "Household Items",
        "Meat & Seafood"
    ],
    "Survey and Feedback": [
        "Customer Relationship Management", "Email Marketing Software", "Feedback Management",
        "Market Research Software", "Marketing Analytics", "Search Engine Optimization",
        "Social Media Advertising", "Survey Tool"
    ],
    "Various": [
        "Books", "Clothing", "Electronics", "Grocery", "Home & Kitchen", "Toys"
    ],
}

def root_cause_page():
    st.title("Root Cause Predictor")
    st.header("Attention")
    st.write("""
    - AI prediction can make mistakes
    - Experiment with high level contact driver categories and concrete contact drivers for better results
    """)

    # Business Type Dropdown
    selected_business_type = st.selectbox("Select Business Type", business_types)

    # Specialisation Dropdown
    if selected_business_type in specialisations:
        selected_specialisation = st.selectbox("Select Specialisation", specialisations[selected_business_type])
    else:
        selected_specialisation = None

    # Product Category Dropdown
    if selected_specialisation in product_categories:
        selected_product_category = st.selectbox("Select Product Category", product_categories[selected_specialisation])
    else:
        selected_product_category = None

    # Load the model
    save_dir = "/app/outputs/ml_pipeline"
    model_path = os.path.join(save_dir, "distilbert_root_cause_model3")
    model = DistilBertForSequenceClassification.from_pretrained(model_path)

    # Load the tokenizer
    tokenizer_path = os.path.join(save_dir, "distilbert_tokenizer3")
    tokenizer = DistilBertTokenizer.from_pretrained(tokenizer_path)

    # Load the label encoder
    label_encoder_path = os.path.join(save_dir, "label_encoder3.pkl")
    label_encoder = joblib.load(label_encoder_path)

    # Function to predict root causes and return probabilities
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
        top5_probs = probabilities[top5_indices]

        # Convert indices to class names and probabilities to a list
        top5_classes = [label_encoder.classes_[i] for i in top5_indices]
        top5_probs_values = top5_probs.tolist()

        return top5_classes, top5_probs_values

    # Input text box
    user_input = st.text_area("Please enter your Contact Driver Category:")

    if st.button("Predict"):
        if user_input:
            # Call the prediction function
            predicted_root_causes, probabilities = predict_root_causes(user_input)
            st.write("Top 5 predicted Root Causes:")
            for cause, prob in zip(predicted_root_causes, probabilities):
                st.write(f"{cause}: {prob:.2f}")

            # Create a bar chart for the predicted root causes
            fig = go.Figure(go.Bar(
                x=probabilities,
                y=predicted_root_causes,
                orientation='h'
            ))
            fig.update_layout(
                title='Predicted Root Cause Probabilities',
                xaxis_title='Probability',
                yaxis_title='Root Cause',
                yaxis=dict(autorange="reversed")  # Reverse the y-axis to show the highest probability on top
            )
            st.plotly_chart(fig, use_container_width=True)

            st.markdown("""
            ### Next Steps After Root Cause Detection

            1. **Verification of Detected Root Causes:**
            - Conduct a thorough review of the AI-identified root causes.
            - Cross-reference with existing data and reports to confirm accuracy.
            - Engage relevant departments for expert validation.

            2. **Detailed Analysis and Prioritization:**
            - Analyze each detected root cause for its impact on customer satisfaction and business operations.
            - Prioritize the root causes based on urgency, potential impact, and feasibility of resolution.

            3. **Developing Action Plans:**
            - Create specific action plans to address each prioritized root cause.
            - Involve cross-functional teams for comprehensive solution development.
            - Establish clear objectives, timelines, and responsibilities.

            4. **Integration with Existing Processes:**
            - Ensure solutions are integrated seamlessly into existing workflows.
            - Update policies and procedures as necessary to include new practices.

            5. **Implementation of Solutions:**
            - Roll out solutions in a phased or full-scale manner, depending on the nature of the root cause.
            - Monitor implementation closely for any unforeseen issues or resistance.

            6. **Training and Communication:**
            - Train staff on new processes or changes to ensure smooth adoption.
            - Communicate changes to all stakeholders, highlighting the benefits and reasons for changes.

            7. **Monitoring and Feedback Collection:**
            - Continuously monitor the outcomes of implemented solutions.
            - Collect feedback from customers and employees to gauge effectiveness.

            8. **Adjustments Based on Feedback:**
            - Analyze feedback and make necessary adjustments to the solutions.
            - Ensure a flexible approach to accommodate iterative improvements.

            9. **Documentation and Knowledge Sharing:**
            - Document the entire process, from detection to implementation and adjustments.
            - Share learnings across the organization to foster a culture of continuous improvement.

            10. **Review and Continuous Improvement:**
            - Regularly review the impact of the solutions on customer service quality.
            - Use insights from the review to drive continuous improvement in processes and customer satisfaction.

            11. **Scaling and Replication:**
            - Explore opportunities to scale successful solutions to other areas of the business.
            - Replicate the approach for ongoing root cause analysis in different departments or for new issues.
            """)
        else:
            st.warning("Please enter a Contact Driver Category text.")
