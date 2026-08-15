-- Overall adverse outcome rate
SELECT
    AVG(adverse_outcome) AS adverse_outcome_rate
FROM patients;


-- Outcome rate by smoking status
SELECT
    smoker,
    COUNT(*) AS patient_count,
    AVG(adverse_outcome) AS outcome_rate
FROM patients
GROUP BY smoker;


-- Outcome rate by diabetes status
SELECT
    diabetes,
    COUNT(*) AS patient_count,
    AVG(adverse_outcome) AS outcome_rate
FROM patients
GROUP BY diabetes;


-- Outcome rate by hypertension status
SELECT
    hypertension,
    COUNT(*) AS patient_count,
    AVG(adverse_outcome) AS outcome_rate
FROM patients
GROUP BY hypertension;


-- Outcome rate by age group
SELECT
    CASE
        WHEN age < 30 THEN '18-29'
        WHEN age < 45 THEN '30-44'
        WHEN age < 60 THEN '45-59'
        WHEN age < 75 THEN '60-74'
        ELSE '75+'
    END AS age_group,
    COUNT(*) AS patient_count,
    ROUND(AVG(adverse_outcome), 3) AS outcome_rate
FROM patients
GROUP BY age_group
ORDER BY outcome_rate DESC;