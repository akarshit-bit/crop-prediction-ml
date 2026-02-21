📌 Project Overview
The Crop Prediction Model is a machine learning-based web application that predicts the most suitable crop to grow based on soil and environmental conditions.
This project helps farmers and agricultural planners make data-driven decisions to improve crop yield and reduce losses.
The prediction is based on input parameters like:

* Temperature
* Humidity
* pH value
* Rainfall

 🎯 Objective

The main objective of this project is:

* To recommend the best crop based on soil nutrients and climate conditions.
* To improve agricultural productivity using Machine Learning.
* To reduce guesswork in crop selection.
* To support smart farming techniques.

🧠 Machine Learning Algorithms Used

I implemented and compared **three algorithms**:
1. **Random Forest**
2. **Decision Tree**
3. **K-Nearest Neighbors (KNN)**

✅ Final Selected Model: Random Forest

**Why Random Forest?**

* Higher accuracy compared to other models.
* Handles overfitting better.
* Works well with classification problems.
* More stable and reliable predictions.

📊 Dataset Information

The dataset contains soil and weather parameters with corresponding crop labels.

**Features:**

| Feature     | Description              |
| ----------- | ------------------------ |
| Temperature | In degree Celsius        |
| Humidity    | In percentage            |
| pH          | Soil pH value            |
| Rainfall    | In mm                    |

**Target Variable:** Crop Name

 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Flask
* HTML
* CSS

---

⚙️ Project Workflow

1. Data Collection
2. Data Preprocessing
3. Model Training
4. Model Evaluation
5. Model Selection
6. Deployment using Flask
7. User Input through Web Interface
8. Crop Prediction Output

 📈 Model Performance

| Algorithm     | Accuracy |
| ------------- | -------- |
| Decision Tree | ~90%     |
| KNN           | ~92%     |
| Random Forest | ~96%     |

(Random Forest gave the best performance and was selected for deployment.)

---

🌐 Web Application Features

* Simple and user-friendly interface
* Input form for soil and weather data
* Instant crop prediction
* Lightweight and fast

---

 📂 Project Structure

```
Crop-Prediction-ML/
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── crop_model.pkl
├── app.py
├── model_training.py
├── dataset.csv
└── README.md

🔍 Future Improvements
* Add real-time weather API integration
* Deploy on cloud platforms (AWS/Heroku)
* Add fertilizer recommendation system
* Mobile application version
* Add regional language support

📚 Conclusion

This project demonstrates how Machine Learning can be applied in agriculture to make smarter crop selection decisions.
By analyzing soil nutrients and environmental conditions, the system predicts the most suitable crop with high accuracy, helping farmers increase productivity and reduce risk.

👨‍💻 Author
Akarshit Shrivastava
B.Tech Student | Machine Learning Enthusiast

Just tell me which version you want.
