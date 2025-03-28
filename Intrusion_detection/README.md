# AI-Powered Intrusion Detection & Threat Prediction

## Overview

As cyber threats evolve, traditional security solutions struggle to keep up with sophisticated attacks. This project introduces an AI-driven Intrusion Detection System (IDS) that leverages deep learning and machine learning techniques to identify and mitigate cyber threats in real-time. The system adapts to new attack patterns using sequential learning models and graph-based threat analysis.

## Features

1. Data Collection & Preprocessing

Uses the CIC-IDS-2017 dataset for model training.

Converts timestamps and handles missing values.

Extracts key network traffic features like packet entropy and request frequency.

Encodes labels and normalizes numerical features for better model performance.

2. AI-Based Threat Detection

Implements LSTM/GRU for sequential anomaly detection.

Uses Graph Neural Networks (GNNs) to model attack propagation.

Employs Isolation Forests and XGBoost to detect anomalies.

Enhances explainability with SHAP values to interpret model decisions.

3. Model Performance & Optimization

Evaluates models based on:

Accuracy

False Positive Rate (FPR)

False Negative Rate (FNR)

Optimizes models for edge deployment to enable low-latency threat detection.

4. Real-Time Intrusion Detection API

A Flask-based API processes real-time network traffic and classifies it as normal or malicious.

Deploys on cloud infrastructure for scalable and high-performance threat analysis.

## Technologies & Tools Used

Programming Language: Python

Machine Learning Libraries: TensorFlow, PyTorch, Scikit-learn, XGBoost

Feature Engineering: Pandas, NumPy, MinMaxScaler

Deployment: Flask API, Cloud Hosting (Google Colab, AWS, or similar)

## Installation

Prerequisites

Ensure the following libraries are installed:

pip install pandas numpy scikit-learn tensorflow torch torch_geometric xgboost shap flask

Dataset

Download the CIC-IDS-2017 dataset from CIC-IDS-2017 Dataset and place it in the appropriate directory.

## Usage

1. Data Preprocessing

Run the preprocessing script to clean and prepare the dataset:

python preprocess.py

2. Model Training

Train the deep learning models for intrusion detection:

python train_models.py

3. Real-Time Detection API

Launch the Flask-based API for real-time traffic classification:

python app.py

## Performance Metrics

Confusion Matrix Analysis to determine FPR & FNR.

Feature Importance Analysis using SHAP values.

Comparison of ML/DL Models:

LSTM/GRU for sequential threat detection.

GNNs for attack propagation modeling.

Isolation Forests & XGBoost for anomaly detection.

## Future Enhancements

Integration with SIEM tools for enterprise security.

Edge deployment for low-latency detection.

Adaptive learning to detect emerging attack patterns.

## Contributors

Priyanshu Gupta - Lead Developer

Collaborators - Suryanshi Chauhan

## Acknowledgments

CIC-IDS-2017 Dataset for providing real-world network traffic.

Open-source ML/DL communities for extensive libraries and tools.
