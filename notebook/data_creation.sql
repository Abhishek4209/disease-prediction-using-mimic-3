SHOW DATABASES;

USE DISEASE;

-- CREATE lab_results TABLE USING GIVEN TABLE:

CREATE TABLE IF NOT EXISTS lab_results AS
SELECT
    le.subject_id,
    le.hadm_id,
    le.charttime,
    
    MAX(CASE WHEN le.itemid IN (50809, 50931) THEN le.valuenum END) AS Glucose_Level,
    MAX(CASE WHEN le.itemid IN (50910, 50813) THEN le.valuenum END) AS Cholesterol_Level

FROM labevents le

WHERE le.itemid IN (
    50809, 50931, -- Glucose
    50910, 50813  -- Cholesterol
)
AND le.valuenum IS NOT NULL

GROUP BY le.subject_id, le.hadm_id, le.charttime;
select * from lab_results;

-- CREATE VITAL_SIGNS TABLE USING GIVEN TABLE IN MIMIC 3 DATABASE:

CREATE TABLE IF NOT EXISTS vital_sign AS
SELECT
    ce.subject_id,
    ce.hadm_id,
    ce.icustay_id,
    ce.charttime,

    MAX(CASE WHEN ce.itemid IN (51, 442, 455, 6701, 220179, 220050) THEN ce.valuenum END) AS Blood_Pressure_systolic,
    MAX(CASE WHEN ce.itemid IN (8368, 8440, 8441, 8555, 220180, 220051) THEN ce.valuenum END) AS Blood_Pressure_diastolic,
    MAX(CASE WHEN ce.itemid IN (211, 220045) THEN ce.valuenum END) AS Heart_Rate,
    MAX(CASE WHEN ce.itemid IN (618, 615, 220210, 224690) THEN ce.valuenum END) AS Respiratory_Rate,
    MAX(CASE WHEN ce.itemid IN (223761, 678) THEN ce.valuenum END) AS Temperature_Celsius,
    MAX(CASE WHEN ce.itemid IN (220277, 646) THEN ce.valuenum END) AS Oxygen_Saturation

FROM chartevents ce

WHERE ce.itemid IN (
    51, 442, 455, 6701, 220179, 220050,
    8368, 8440, 8441, 8555, 220180, 220051,
    211, 220045,
    618, 615, 220210, 224690,
    223761, 678,
    220277, 646
)
AND ce.valuenum IS NOT NULL
AND (ce.error IS NULL OR ce.error != 1)

GROUP BY ce.subject_id, ce.hadm_id, ce.icustay_id, ce.charttime;

SELECT * FROM vital_sign;



-- CREATE A TABLE icd9_codes BY USING GIVEN TABLE DIAGNOSES_ICD WHICH CONTAINING subject_id,hadm_id, icd9_code, short_title, long_title  

CREATE TABLE if not EXISTS icd9_codes AS
SELECT 
    d.subject_id,
    d.hadm_id,
    d.seq_num,
    d.icd9_code,
    dd.short_title AS diagnosis
FROM diagnoses_icd d
LEFT JOIN d_icd_diagnoses dd
    ON d.icd9_code = dd.icd9_code;

select * from icd9_codes;

-- CREATE FINAL TABLE WHICH CONTAIN VALUABLE INFORMATION ABOUT PATIENTS CONSTIONS:


CREATE TABLE IF NOT EXISTS diagnoses AS
SELECT
    p.subject_id AS Patient_ID,
    p.gender AS Gender,
    p.dob AS Date_of_Birth,
    v.Blood_Pressure_systolic AS Blood_Pressure_systolic,
    v.Blood_Pressure_diastolic AS Blood_Pressure_diastolic,
    v.heart_rate AS Heart_Rate,
    v.respiratory_rate AS Respiratory_Rate,
    v.Temperature_Celsius AS Temperature_Celsius,
    v.Oxygen_Saturation AS Oxygen_Saturation,
    l.Glucose_Level AS Glucose_Level,
    l.Cholesterol_Level AS Cholesterol_Level,
    d.icd9_code AS Diagnosis_Code,
    icd.diagnosis AS Diagnosis
FROM
    patients p
JOIN
    vital_signs v ON p.subject_id = v.subject_id
JOIN
    lab_results l ON p.subject_id = l.subject_id
JOIN
    diagnoses_icd d ON p.subject_id = d.subject_id
JOIN
    icd9_codes icd ON d.icd9_code = icd.icd9_code
-- WHERE
--     v.charttime BETWEEN 'start_date' AND 'end_date'
    -- AND 
    -- d.diagnosis != 'Unknown'
ORDER BY
    p.subject_id;


SELECT * FROM  diagnoses;