# PeakLoadNet ⚡
**Real-Time National Peak Electricity Load Prediction Using Machine Learning**

---

## 🔍 Description
PeakLoadNet predicts the national electricity peak load using regional hourly demand data. The project implements multiple models to compare performance and accuracy, including Linear Regression, Neural Networks, and Random Forest.

---

## 🧠 Models Used
- **Linear Regression** – Simple baseline for prediction.  
- **MLPRegressor (Neural Network)** – Multi-layer Perceptron for non-linear relationships.  
- **Random Forest Regressor** – Ensemble method to improve prediction accuracy.

---

## 📊 Features & Workflow
1. **Data Collection & Cleaning** – Regional hourly electricity demand.  
2. **Train-Test Split** – 80% training, 20% testing.  
3. **Model Training** – Linear Regression, Neural Network, Random Forest.  
4. **Prediction & Evaluation** – Accuracy measured using R² score.  

---

## ⚙️ Tools & Libraries
- Python 3.x  
- [Scikit-learn](https://scikit-learn.org/)  
- [Pandas](https://pandas.pydata.org/)  
- Google Colab  

---

## 🧾 Accuracy
| Model | R² Accuracy |
|-------|------------|
| Linear Regression | ~100% |
| Neural Network (MLPRegressor) | 99.90% |
| Random Forest Regressor | 99.90% |

---

## 💻 Usage
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/PeakLoadNet.git
