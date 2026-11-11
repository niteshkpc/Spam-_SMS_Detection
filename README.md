# 📩 SMS Spam Detection

An AI/ML-based project that classifies SMS messages as **Spam** or **Ham (Not Spam)** using Natural Language Processing (NLP) and machine learning techniques.

## 📌 Project Overview

SMS Spam Detection is a machine learning application designed to identify unwanted, fraudulent, and promotional text messages. It analyzes the content of an SMS and predicts whether the message is spam or legitimate.

The project uses text preprocessing and machine learning classification to detect suspicious messages efficiently.

## ✨ Features

- 📱 Classifies SMS messages as Spam or Ham.
- 🧹 Cleans and preprocesses text data.
- 🔤 Uses NLP techniques for text processing.
- 🤖 Applies machine learning for message classification.
- 📊 Evaluates model performance using classification metrics.
- ⚡ Provides quick predictions for user-entered messages.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Machine Learning:** Scikit-learn
- **NLP:** NLTK
- **Data Processing:** Pandas, NumPy
- **Feature Extraction:** TF-IDF / CountVectorizer
- **Model:** Multinomial Naive Bayes
- **Development Environment:** Jupyter Notebook / VS Code

*Technologies listed above are suggested components; adjust them to match your actual implementation.*

## 📂 Project Structure

SMS-Spam-Classification/
│
├── .devcontainer/
│   └── devcontainer.json
│
├── .idea/
│   ├── inspectionProfiles/
│   ├── .gitignore
│   ├── misc.xml
│   ├── modules.xml
│   └── sms-spam-classification.iml
│
├── Minor_peoject.ipynb
├── app.py
├── main.py
├── model.pkl
├── requirements.txt
├── spam.csv
├── vectorizer.pkl
└── README.md

*Your actual folder structure may differ depending on how the project is implemented.*

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/SMS-Spam-Detection.git
```

### 2. Navigate to the Project Directory

```bash
cd SMS-Spam-Detection
```

### 3. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the Project

If your project uses a Python script:

```bash
python app.py
```

