# Molecular Property Predictor

A machine learning-based web application that predicts important physicochemical and biological properties of drug-like molecules directly from their molecular structure.

## Overview

This tool predicts **four key chemical properties** of drug-like molecules without requiring laboratory experiments.

Simply enter the name of a molecule (e.g., **Aspirin** or **Caffeine**) and the application predicts:

- **LogP** — Indicates how fat-soluble (lipophilic) the molecule is.
- **Aqueous Solubility (ESOL)** — Estimates how well the molecule dissolves in water.
- **Blood-Brain Barrier (BBB) Penetration** — Predicts whether the molecule can cross the blood-brain barrier.
- **Toxicity (Tox21)** — Predicts whether the molecule is likely to trigger known toxic biological pathways.

The application uses **Random Forest** machine learning models trained on publicly available datasets from **MoleculeNet**. Molecular structures are converted into **2048-bit Morgan Fingerprints** using **RDKit**, which serve as input features for the prediction models.

> **Note:** This application is intended as a rapid screening tool for early-stage drug discovery and educational purposes. It is **not** a substitute for experimental validation.

---

## Features

- Predicts four important molecular properties
- Accepts molecule names as input
- Uses RDKit for molecular fingerprint generation
- Random Forest models trained on public datasets
- Interactive web interface built with Streamlit

---

## How It Works

1. Enter a molecule name (e.g., `Aspirin` or `Caffeine`).
2. The molecular structure is retrieved and converted into a **2048-bit Morgan Fingerprint**.
3. The fingerprint is provided as input to trained Random Forest models.
4. The application predicts:
   - LogP
   - Aqueous Solubility
   - BBB Penetration
   - Toxicity

---

# Running the Project

## Run Locally

```bash
git clone https://github.com/YOURUSERNAME/molecular-property-predictor.git

cd molecular-property-predictor

python3 -m venv venv

source venv/bin/activate      # Linux / macOS
# venv\Scripts\activate       # Windows

pip install -r requirements.txt

streamlit run app.py
```

The application will open in your browser at:

```
http://localhost:8501
```

---

## Live Demo

Click here to try the deployed application:

**<your Streamlit deployment URL>**

---

## Using the Web App

1. Open the Streamlit application.
2. Select the property you want to predict from the dropdown menu.
3. Enter the molecule name (e.g., **Aspirin**, **Caffeine**, **Ibuprofen**).
4. Click **Predict**.
5. View the predicted molecular property.

---

# Technologies Used

- Python
- Streamlit
- RDKit
- Scikit-learn
- Pandas
- NumPy

---

# Machine Learning Models

| Property | Model |
|----------|-------|
| LogP | Random Forest Regressor |
| ESOL (Aqueous Solubility) | Random Forest Regressor |
| BBB Penetration | Random Forest Classifier |
| Toxicity (Tox21) | Random Forest Classifier |

---

# References

## Datasets

- Wu et al. (2018). **MoleculeNet: A Benchmark for Molecular Machine Learning**  
  https://pmc.ncbi.nlm.nih.gov/articles/PMC5868307/

- Delaney (2004). **ESOL: Estimating Aqueous Solubility Directly from Molecular Structure**  
  https://pubs.acs.org/doi/10.1021/ci034243x

- Tox21 Challenge — National Center for Advancing Translational Sciences  
  https://ncats.nih.gov/research/research-activities/Tox21

---

## Machine Learning Resources

- Coursera — Machine Learning Specialization (Week 2 Practice Lab)  
  https://www.coursera.org/learn/machine-learning/programming/jsE7w/week-2-practice-lab-linear-regression

- GeeksforGeeks — Machine Learning Tutorials  
  https://www.geeksforgeeks.org/machine-learning/

---

## Cheminformatics

- Generating Molecular Fingerprints using RDKit (YouTube)  
  https://www.youtube.com/watch?v=4jRBRDbJemM

- RDKit Getting Started Documentation  
  https://www.rdkit.org/docs/GettingStartedInPython.html

- Distill.pub — Introduction to Graph Neural Networks  
  https://distill.pub/2021/gnn-intro/

---

## Drug Discovery

- Certara — Key Properties in Drug Design: LogP, pKa, and Solubility  
  https://www.certara.com/blog/key-properties-in-drug-design-predicting-lipophilicity-pka-and-solubility/

- MODRN Yale — Aqueous and Lipid Solubility  
  https://modrn.yale.edu/education/undergraduate-curriculum/modrn-u-modules/aqueous-and-lipid-solubility

---

## Additional Reading

- https://pmc.ncbi.nlm.nih.gov/articles/PMC4292164/

- https://pubs.acs.org/doi/10.1021/ci300124c