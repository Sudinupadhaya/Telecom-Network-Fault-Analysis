# Customer Churn Prediction

A machine learning project that predicts whether a telecom customer is likely to churn. The project demonstrates a practical end-to-end data science workflow: data cleaning, exploratory data analysis, feature engineering, model training, model evaluation, and an optional Streamlit dashboard for interactive prediction.

## Project Objective

Customer churn is a major business problem for subscription-based companies. The goal of this project is to identify customers who are at high risk of leaving so that the business can take retention actions early.

This project answers questions such as:

- Which customer groups are more likely to churn?
- Which features have the strongest relationship with churn?
- Can a machine learning model predict churn from customer profile and service data?
- How can predictions be presented in a simple dashboard?

## Dataset

- Dataset: Telco Customer Churn Dataset
- Rows: 7,043 customers
- Target variable: `Churn` (`Yes` / `No`)
- Feature categories:
  - Customer demographics
  - Account information
  - Contract type
  - Monthly and total charges
  - Internet and phone services
  - Support and security services

> Note: Place the dataset file at `data/telco_churn.csv` before running the training pipeline.

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib / Seaborn
- Streamlit
- Jupyter Notebook

## Machine Learning Workflow

1. Load and inspect the dataset
2. Clean missing or inconsistent values
3. Encode categorical variables
4. Perform exploratory data analysis
5. Split data into training and testing sets
6. Train classification models
7. Evaluate model performance
8. Save model outputs and visualizations
9. Use the trained model for prediction
10. Present results through a Streamlit dashboard

## Project Structure

```text
Customer-Churn-Prediction/
│
├── data/                    # Dataset files
├── src/                     # Source code
│   ├── preprocess.py        # Data cleaning and preprocessing
│   ├── train_model.py       # Model training and evaluation
│   └── predict.py           # Prediction script
│
├── models/                  # Saved trained models
├── results/                 # Evaluation plots and output files
├── dashboard/               # Streamlit dashboard
│   └── app.py
│
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Sudinupadhaya/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add the dataset

Place the dataset file here:

```text
data/telco_churn.csv
```

### 5. Train the model

```bash
python -m src.train_model
```

### 6. Run prediction

```bash
python -m src.predict
```

### 7. Launch the Streamlit dashboard

```bash
streamlit run dashboard/app.py
```

## Model Evaluation

The project is designed to evaluate classification performance using metrics such as:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC score
- Confusion matrix

Example expected outputs:

- Confusion matrix visualization
- Feature importance chart
- Model performance summary
- Churn probability prediction

## Key Insights

Typical churn-related factors in telecom datasets include:

- Contract type
- Tenure
- Monthly charges
- Internet service type
- Online security service
- Tech support availability
- Payment method

These insights can help a business design better retention strategies.

## Business Value

This project is useful for understanding how machine learning can support customer retention. Instead of reacting after customers leave, companies can identify high-risk customers early and target them with better support, offers, or engagement campaigns.

## Future Improvements

- Add model comparison between Logistic Regression, Random Forest, and XGBoost
- Add hyperparameter tuning
- Add cross-validation
- Improve dashboard UI
- Add SHAP-based model explainability
- Deploy the dashboard online

## Author

**Sudin Upadhaya**

- GitHub: Sudinupadhaya
- Focus areas: Data Analysis, Machine Learning, Python, and Software Engineering
