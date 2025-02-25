# 🛡️ Credit Card Fraud Detection App  
🚀 **Real-time fraud detection using Machine Learning & Streamlit**  

---

## **📌 Overview**  
This project is a **credit card fraud detection system** that uses **machine learning** to classify transactions as **fraudulent or legitimate**. It is deployed as a **Streamlit web app** for real-time predictions.  

---

## **🖥️ Demo**  
🔗 **Live App**: [https://credit-card-fraud-detection-app-jpkpnyvalsob7fccwzdrlb.streamlit.app/]  

---

## **📂 Project Structure**  
```
fraud-detection-app/
│── fraud_detection_app.py      # Main Streamlit app
│── requirements.txt            # Dependencies
│── model/                      # Trained ML model
│   ├── fraud_model.pkl
│── utils/                      # Helper functions
│   ├── credit-card-fraud.ipynb
│   ├── fraud_detection_app.py
    ├── fraud-detection-deploy.ipynb
    ├── fraud-detection-model.ipynb 
│── README.md                   # Project documentation
│── .gitignore                   # Files to ignore
```

---

## **⚙️ Features**  
✅ **ML-based fraud detection** using logistic regression/random forest  
✅ **Real-time predictions** using a trained model  
✅ **User-friendly Streamlit interface**  
✅ **Interactive visualizations** (if added)  

---

## **📊 Dataset**  
- The dataset used is **creditcard.csv**.
- It contains anonymized **transaction features** and a `Class` column (`0 = Legit, 1 = Fraud`).  

---

## **🚀 Installation & Usage**  
### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/vishwasbhairab/fraud-detection-app.git
cd fraud-detection-app
```

### **2️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **3️⃣ Run the Streamlit App**  
```bash
streamlit run fraud_detection_app.py
```
The app will open in your browser at `http://localhost:8501/`.

---

## **🛠️ Technologies Used**  
- **Python**  
- **Streamlit** (for UI)  
- **Scikit-Learn** (for ML)  
- **Pandas & NumPy** (for data processing)  
- **Joblib** (for model saving)  

---

## **📚 License**  
This project is open-source and free to use.  

---

## **👌 Contributing**  
Want to improve the app? Feel free to fork the repo and submit a PR!  

---

