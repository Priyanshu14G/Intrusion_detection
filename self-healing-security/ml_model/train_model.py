# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import hashlib
import joblib

# Load the dataset (replace with your correct file path)
# df = pd.read_csv('import pandas as pd')

# Corrected path with forward slashes
df = pd.read_csv('D:/priyanshu backup/CPP/Deep_Learning/Intrusion_detection/self-healing-security/ml_model/ton-iot.csv')

# Check for missing values and drop them if necessary
df = df.dropna()

# Hash IP addresses if they exist in the dataset
if 'src_ip' in df.columns and 'dst_ip' in df.columns:
    def hash_ip(ip):
        return int(hashlib.md5(ip.encode()).hexdigest(), 16) % 10**8
    
    df['src_ip'] = df['src_ip'].apply(hash_ip)
    df['dst_ip'] = df['dst_ip'].apply(hash_ip)

# Automatically encode all categorical columns
label_encoder = LabelEncoder()
for col in df.select_dtypes(include=['object']).columns:
    df[col] = label_encoder.fit_transform(df[col])

# Define features (X) and target (y)
X = df.drop('label', axis=1)
y = df['label']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the RandomForest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
accuracy = model.score(X_test, y_test)
print(f"✅ Model training successful! Accuracy: {accuracy * 100:.2f}%")

# Save the trained model
joblib.dump(model, 'ton-iot_model.sav')
print("✅ Model saved successfully!")
