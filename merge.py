import numpy as np
import pandas as pd

np.random.seed(42)

N = 1000

patients = pd.DataFrame({
    "patient_id": range(10001, 10001 + N),
    "age": np.random.randint(18, 90, N),
    "sex": np.random.choice(["F", "M"], N),
    "bmi": np.round(np.random.normal(27, 5, N), 1),
    "smoker": np.random.choice([0, 1], N, p=[0.75, 0.25]),
    "hypertension": np.random.choice([0, 1], N, p=[0.65, 0.35]),
    "diabetes": np.random.choice([0, 1], N, p=[0.80, 0.20])
})

patients["bmi"] = patients["bmi"].clip(15, 50)

# Create a synthetic risk score
risk_score = (
    0.02 * patients["age"]
    + 0.08 * patients["bmi"]
    + 0.8 * patients["smoker"]
    + 0.9 * patients["hypertension"]
    + 1.1 * patients["diabetes"]
)

probability = 1 / (1 + np.exp(-(risk_score - 4.5)))

patients["adverse_outcome"] = np.random.binomial(
    1,
    probability
)

print(patients.head(10))

print("\nDataset shape:")
print(patients.shape)

print("\nAverage age:")
print(round(patients["age"].mean(), 2))

print("\nAdverse outcome rate:")
print(round(patients["adverse_outcome"].mean(), 3))

patients.to_csv("patients.csv", index=False)

print("\nSaved synthetic patient data to patients.csv")