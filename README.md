# Store Sales Prediction Project 🛍️📈

Welcome to the **Store Sales Prediction Project**! This project aims to predict item sales using a variety of powerful tools and libraries. Below, you'll find an overview of the project, the dependencies used, and how to get it up and running in your local environment. Let's dive in! 🚀

project link : storesales.streamlit.app

---

## 📌 Project Overview

The goal of this project is to build a robust machine learning model that can accurately predict store sales. By leveraging historical sales data, we aim to forecast future sales trends, helping businesses optimize inventory, plan marketing strategies, and improve overall decision-making.

---

## 🛠️ Dependencies

To ensure the project runs smoothly, we rely on the following libraries and frameworks:

- **Pandas** 🐼: For data manipulation and analysis.
- **NumPy** 🔢: For numerical computations.
- **Scikit-learn** 🤖: For machine learning algorithms and model evaluation.
- **Seaborn** 🌊: For data visualization.
- **Matplotlib** 📊: For creating static, animated, and interactive visualizations.
- **CatBoost** 🐱: For gradient boosting on decision trees.
- **XGBoost** ⚡: For optimized distributed gradient boosting.
- **Dill** 🥒: For serializing and deserializing Python objects.
- **Flask** 🌐: For creating a web application to serve the model.

---

## 🚀 Running the Project Locally

To get this project up and running on your local machine, follow these steps:

1. **Clone the Repository** 📂
   ```bash
   git clone https://github.com/yourusername/store-sales-prediction.git
   cd store-sales-prediction
   ```

2. **Set Up a Virtual Environment** 🐍
   ```cmd
   conda create -p venv python==3.12 -y
   ```

3. **Install Dependencies** 📦
   ```cmd
   pip install -r requirements.txt
   ```

4. **Run the Flask Application** 🌐
   ```cmd
   python app.py or streamlit run streamlit_app.py
   ```

5. **Access the Web Application** 🌍
   Open your browser and navigate to `http://127.0.0.1:5000/` to interact with the sales prediction model.

---

## 📊 Model Training and Evaluation

The model training process involves the following steps:

1. **Data Preprocessing** 🧹
   - Cleaning the dataset.
   - Handling missing values.
   - Encoding categorical variables.

2. **Feature Engineering** 🛠️
   - Creating new features from existing data.
   - Scaling and normalizing features.

3. **Model Training** 🏋️‍♂️
   - Training the model using CatBoost and XGBoost.
   - Tuning hyperparameters for optimal performance.

4. **Model Evaluation** 📝
   - Evaluating the model using metrics such as RMSE, MAE, and R².
   - Visualizing the results using Seaborn and Matplotlib.

---

## 🌟 Key Features

- **Accurate Predictions**: Leveraging state-of-the-art machine learning algorithms.
- **User-Friendly Interface**: Built with Flask for easy interaction.
- **Scalable**: Designed to handle large datasets efficiently.
- **Visual Insights**: Comprehensive visualizations to understand sales trends.

---


## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Special thanks to the open-source community for providing the tools and libraries that made this project possible.
- Inspiration and dataset credits go to [Kaggle](https://www.kaggle.com/).

---

Happy predicting! 🎉📊

---

Feel free to reach out if you have any questions or need further assistance. Let's make sales prediction smarter and more efficient! 🚀📈