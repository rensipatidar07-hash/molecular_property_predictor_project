import streamlit as st
import numpy as np
from src.config import DATASETS
from src.data_loader import download_data, smiles_to_fingerprints
from src.model import train_and_test

# Page configuration and titles
st.set_page_config(page_title="Molecular Property Predictor", layout="centered")
st.title("Molecular Property Predictor")
st.markdown("Select a property and input a molecule to get a prediction.")

# Dataset selection sidebar
selected_dataset = st.sidebar.selectbox("Select Dataset", list(DATASETS.keys()))

# Molecule input section with pre-defined examples
st.subheader("Input Molecule")
examples = {
    "Custom (Type your own)": "",
    "Ethanol (Alcohol)": "CCO",
    "Aspirin": "CC(=O)Oc1ccccc1C(=O)O",
    "Caffeine": "CN1C(=O)N(C)c2ncn(C)c2C1=O",
    "Water": "O"
}
selected_example = st.selectbox("Choose an example molecule:", list(examples.keys()))
placeholder_smiles = examples[selected_example]
smiles_input = st.text_input("Enter SMILES string:", value=placeholder_smiles)

# Machine learning pipeline execution
if st.button("Predict"):
    if not smiles_input:
        st.warning("Please enter or select a SMILES string!")
    else:
        with st.spinner("Downloading dataset and training model..."):
            info = DATASETS[selected_dataset]
            df = download_data(info['link'])
            X_train_full = smiles_to_fingerprints(df['smiles'].tolist())
            
            model, score = train_and_test(X_train_full, df, info)
            user_fp = smiles_to_fingerprints([smiles_input])
            
            # Display results based on regression or classification task
            if info['type'] == 'regression':
                prediction = model.predict(user_fp)[0]
                st.success(f"Model Trained! Test RMSE: {score:.4f}")
                st.metric(label=f"Predicted {info['target']}", value=f"{prediction:.4f}")
            else:
                prob = model.predict_proba(user_fp)[0, 1]
                st.success(f"Model Trained! Test ROC-AUC: {score:.4f}")
                label = "Positive" if prob > 0.5 else "Negative"
                st.metric(label="Prediction Class", value=label)
                st.info(f"Probability of being positive: {prob:.2%}")
