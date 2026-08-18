import sqlite3
import pandas as pd

connection = sqlite3.connect("health.db")

overall = pd.read_sql_query("""
    SELECT
        COUNT(*) AS total_patients,
        SUM(adverse_outcome) AS adverse_outcomes,
        ROUND(AVG(adverse_outcome) * 100, 2) AS outcome_rate
    FROM patients;
""", connection)

print("\nOVERALL OUTCOMES")
print(overall)


risk_factors = pd.read_sql_query("""
    SELECT
        'Smoking' AS risk_factor,
        smoker AS exposed,
        COUNT(*) AS patients,
        ROUND(AVG(adverse_outcome) * 100, 2) AS outcome_rate
    FROM patients
    GROUP BY smoker

    UNION ALL

    SELECT
        'Hypertension',
        hypertension,
        COUNT(*),
        ROUND(AVG(adverse_outcome) * 100, 2)
    FROM patients
    GROUP BY hypertension

    UNION ALL

    SELECT
        'Diabetes',
        diabetes,
        COUNT(*),
        ROUND(AVG(adverse_outcome) * 100, 2)
    FROM patients
    GROUP BY diabetes;
""", connection)

print("\nOUTCOME RATE BY RISK FACTOR")
print(risk_factors)


age_groups = pd.read_sql_query("""
    SELECT
        CASE
            WHEN age < 30 THEN '18-29'
            WHEN age < 45 THEN '30-44'
            WHEN age < 60 THEN '45-59'
            WHEN age < 75 THEN '60-74'
            ELSE '75-89'
        END AS age_group,
        COUNT(*) AS patients,
        ROUND(AVG(adverse_outcome) * 100, 2) AS outcome_rate
    FROM patients
    GROUP BY age_group
    ORDER BY outcome_rate DESC;
""", connection)

print("\nOUTCOME RATE BY AGE GROUP")
print(age_groups)


bmi_groups = pd.read_sql_query("""
    SELECT
        CASE
            WHEN bmi < 25 THEN 'Normal'
            WHEN bmi < 30 THEN 'Overweight'
            ELSE 'Obese'
        END AS bmi_group,
        COUNT(*) AS patients,
        ROUND(AVG(adverse_outcome) * 100, 2) AS outcome_rate
    FROM patients
    GROUP BY bmi_group
    ORDER BY outcome_rate DESC;
""", connection)

print("\nOUTCOME RATE BY BMI GROUP")
print(bmi_groups)


connection.close()