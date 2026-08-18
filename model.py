import sqlite3
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

connection = sqlite3.connect("health.db")

df = pd.read_sql_query("""
    SELECT
        age,
        bmi,
        smoker,
        hypertension,
        diabetes,
        adverse_outcome
    FROM patients
""", connection)

connection.close()

X = df[
    [
        "age",
        "bmi",
        "smoker",
        "hypertension",
        "diabetes"
    ]
]

y = df["adverse_outcome"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("MODEL PERFORMANCE")
print(classification_report(y_test, predictions))

print("\nFEATURE COEFFICIENTS")

coefficients = pd.DataFrame({
    "feature": X.columns,
    "coefficient": model.coef_[0]
})

coefficients["odds_ratio"] = coefficients["coefficient"].apply(
    lambda x: __import__("math").exp(x)
)

print(coefficients.sort_values("odds_ratio", ascending=False))