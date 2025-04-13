---

# 🧠 Disease Diagnosis ML Project

This project is a Machine Learning-based **Disease Diagnosis System** that predicts potential diseases based on physiological and demographic input features. It has been developed using a modular coding approach and follows an end-to-end ML workflow.

---

## 📂 Project Structure

```bash
.
├── artifacts/                   # Stores model and preprocessor files
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── raw.csv
│   ├── train.csv
│   └── test.csv
│
├── notebook/                   # Contains notebooks and SQL/data
│   ├── data/                  
│   ├── data_creation.sql
│   ├── eda.ipynb
│   ├── model.ipynb
│   └── final.csv
│
├── src/                        # Source code
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_training.py
│   ├── pipelines/
│   │   └── __init__.py
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── logs/                       # Logging directory
│
├── app.py                      # Flask API script to launch the service
└── README.md                   # Project README file
```

---

## 🎯 Objective

To build a disease prediction system that uses input features such as blood pressure, heart rate, temperature, glucose level, and more to classify the disease category.

---

## 🧾 Input Features

### 🔢 Numerical Columns:
- `Blood_Pressure_systolic`
- `Blood_Pressure_diastolic`
- `Heart_Rate`
- `Respiratory_Rate`
- `Temperature_Celsius`
- `Glucose_Level`
- `Cholesterol_Level`
- `Diagnosis_Code`
- `Age`
- `Oxygen_Saturation`

### 🧬 Categorical Column:
- `Gender`

---

## 🚀 How to Run

1. **Install Dependencies**  
   Run the following to install required packages:
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the Application**
   ```bash
   python app.py
   ```

3. **Access the URL**
   Once you run the app, the console will log the local URL to access the prediction endpoint. You can find this URL inside the `logs/` folder (check the latest `.log` file).

---

## 🔧 Key Features

- 🧠 Machine Learning model training and inference
- 🧹 Data preprocessing pipeline
- 📊 EDA and feature engineering notebooks
- 📁 Modular code structure
- 🌐 REST API with Flask
- 📜 Logging mechanism for debugging

---

## 📤 Output

The model returns a predicted disease class based on input features via the API.

---

## 📌 To Do
- [ ] Add unit tests
- [ ] Model interpretability with SHAP
- [ ] Frontend dashboard

---

## 🤝 Contributors

- **Abhishek Upadhyay**  
  [LinkedIn](https://www.linkedin.com/in/abhishek-upadhyay-35b183259/) • [GitHub](https://github.com/Abhishek4209)

---

