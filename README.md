# 📈 Sales Predictor Web App

A machine learning-powered web application that predicts sales using user-input features. Built with Flask and LightGBM, this app provides real-time predictions and is deployed live using Render.

## 🌐 Live Demo

👉 [Click here to try the live app](https://sales-predicter-pro.onrender.com/)

---

## 🚀 Features

- 🔮 Predicts sales using a trained LightGBM model
- 🎯 Clean and user-friendly interface
- 🌐 Live deployed on Render
- 🧠 Uses scikit-learn and pandas for ML preprocessing

---

## 🛠️ Tech Stack

| Layer       | Tools Used                       |
|-------------|----------------------------------|
| Frontend    | HTML5, CSS3                      |
| Backend     | Flask (Python)                   |
| ML Model    | LightGBM, scikit-learn           |
| Deployment  | Render.com                       |

---

## 📂 Project Structure
sales-predictor/
├── app.py # Flask backend
├── model.pkl # Trained LightGBM model
├── requirements.txt # Python dependencies
├── templates/
│ └── index.html # Frontend template
└── static/ (optional) # CSS/JS files if used


---

## ⚙️ How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/sales-predictor.git
cd sales-predictor

# 2. Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Flask app
python app.py

# Visit http://127.0.0.1:5000 in your browser
