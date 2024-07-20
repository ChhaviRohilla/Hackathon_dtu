# from flask import Flask, request, jsonify
# import joblib
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import classification_report, roc_auc_score
# from imblearn.over_sampling import SMOTE
# from flask_cors import CORS

# # Set up Flask API
# app = Flask(__name__)
# CORS(app)

# # Load and preprocess data
# data = pd.read_csv('transactions.csv')
# data['transaction_time'] = pd.to_datetime(data['transaction_time'])
# data['transaction_hour'] = data['transaction_time'].dt.hour

# # Define features and target variable
# features = ['amount', 'user_id', 'merchant_id', 'transaction_hour']
# X = data[features]
# y = data['is_fraud']

# # Train-test split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Standardize features
# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)

# # Handle class imbalance with SMOTE
# smote = SMOTE(random_state=42)
# X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

# # Train model with oversampled data
# model = RandomForestClassifier(random_state=42)
# model.fit(X_train_res, y_train_res)

# # Evaluate model
# y_pred = model.predict(X_test)
# y_prob = model.predict_proba(X_test)[:, 1]
# print(classification_report(y_test, y_pred))
# print("ROC AUC Score:", roc_auc_score(y_test, y_prob))

# # Save model and scaler
# joblib.dump(model, 'fraud_detection_model.pkl')
# joblib.dump(scaler, 'scaler.pkl')

# # Load the model and scaler
# model = joblib.load('fraud_detection_model.pkl')
# scaler = joblib.load('scaler.pkl')

# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.json
#     df = pd.DataFrame(data)
    
#     # Preprocess data
#     df['transaction_time'] = pd.to_datetime(df['transaction_time'])
#     df['transaction_hour'] = df['transaction_time'].dt.hour
#     df = df[features]
#     df = scaler.transform(df)
    
#     # Make predictions
#     predictions = model.predict(df)
#     probabilities = model.predict_proba(df)[:, 1]
    
#     return jsonify({'predictions': predictions.tolist(), 'probabilities': probabilities.tolist()})

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')

# ------------------------------------------------------------------------------

# from flask import Flask, request, jsonify
# import joblib
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import classification_report, roc_auc_score
# from imblearn.over_sampling import SMOTE
# from flask_cors import CORS

# # Set up Flask API
# app = Flask(__name__)
# CORS(app)

# # Define features and target variable
# features = ['amount', 'user_id', 'merchant_id', 'transaction_hour']

# # Load and preprocess data
# data = pd.read_csv('transactions.csv')
# data['transaction_time'] = pd.to_datetime(data['transaction_time'])
# data['transaction_hour'] = data['transaction_time'].dt.hour
# X = data[features]
# y = data['is_fraud']

# # Train-test split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Standardize features
# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)

# # Handle class imbalance with SMOTE
# smote = SMOTE(random_state=42)
# X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

# # Train model with oversampled data
# model = RandomForestClassifier(random_state=42)
# model.fit(X_train_res, y_train_res)

# # Evaluate model
# y_pred = model.predict(X_test)
# y_prob = model.predict_proba(X_test)[:, 1]
# print(classification_report(y_test, y_pred))
# print("ROC AUC Score:", roc_auc_score(y_test, y_prob))

# # Save model and scaler
# joblib.dump(model, 'fraud_detection_model.pkl')
# joblib.dump(scaler, 'scaler.pkl')

# # Load the model and scaler
# model = joblib.load('fraud_detection_model.pkl')
# scaler = joblib.load('scaler.pkl')

# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.json
#     df = pd.DataFrame(data)
    
#     # Preprocess data
#     df['transaction_time'] = pd.to_datetime(df['transaction_time'])
#     df['transaction_hour'] = df['transaction_time'].dt.hour
#     df = df[features]
#     df = scaler.transform(df)
    
#     # Make predictions
#     predictions = model.predict(df)
#     probabilities = model.predict_proba(df)[:, 1]
    
#     return jsonify({'predictions': predictions.tolist(), 'probabilities': probabilities.tolist()})

# @app.route('/predict_old_data', methods=['GET'])
# def predict_old_data():
#     # Load old transaction data
#     old_data = pd.read_csv('transactions.csv')
#     old_data['transaction_time'] = pd.to_datetime(old_data['transaction_time'])
#     old_data['transaction_hour'] = old_data['transaction_time'].dt.hour
    
#     # Preprocess data
#     X_old = old_data[features]
#     X_old = scaler.transform(X_old)
    
#     # Make predictions
#     predictions = model.predict(X_old)
#     probabilities = model.predict_proba(X_old)[:, 1]
    
#     old_data['predictions'] = predictions
#     old_data['probabilities'] = probabilities
    
#     # Convert the DataFrame to a JSON response
#     result = old_data.to_dict(orient='records')
#     return jsonify(result)

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')

# ---------------------------------------------------------------------------------------------------------
from flask import Flask, request, jsonify
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
from imblearn.over_sampling import SMOTE
from flask_cors import CORS

# Set up Flask API
app = Flask(__name__)
CORS(app)

# Define features and target variable
features = ['amount', 'user_id', 'merchant_id', 'transaction_hour']

# Load and preprocess data
data = pd.read_csv('transactions.csv')
data['transaction_time'] = pd.to_datetime(data['transaction_time'])
data['transaction_hour'] = data['transaction_time'].dt.hour
X = data[features]
y = data['is_fraud']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Handle class imbalance with SMOTE
smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

# Train model with oversampled data
model = RandomForestClassifier(random_state=42)
model.fit(X_train_res, y_train_res)

# Evaluate model
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]
print(classification_report(y_test, y_pred))
print("ROC AUC Score:", roc_auc_score(y_test, y_prob))

# Save model and scaler
joblib.dump(model, 'fraud_detection_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

# Load the model and scaler
model = joblib.load('fraud_detection_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame(data)
    
    # Preprocess data
    df['transaction_time'] = pd.to_datetime(df['transaction_time'])
    df['transaction_hour'] = df['transaction_time'].dt.hour
    df = df[features]
    df = scaler.transform(df)
    
    # Make predictions
    predictions = model.predict(df)
    probabilities = model.predict_proba(df)[:, 1]
    
    return jsonify({'predictions': predictions.tolist(), 'probabilities': probabilities.tolist()})

@app.route('/transactions', methods=['GET'])
def get_transactions():
    # Load old transaction data
    old_data = pd.read_csv('transactions.csv')
    old_data['transaction_time'] = pd.to_datetime(old_data['transaction_time'])
    old_data['transaction_hour'] = old_data['transaction_time'].dt.hour
    
    # Convert the DataFrame to a JSON response
    result = old_data.to_dict(orient='records')
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
