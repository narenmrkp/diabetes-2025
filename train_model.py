from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle
import os

# Load dataset
data = load_diabetes()
X, y = data.data, data.target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Ensure app folder exists
os.makedirs("app", exist_ok=True)

# Save model
with open("app/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved to app/model.pkl")
