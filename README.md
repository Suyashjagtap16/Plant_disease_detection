# 🌿 Plant Disease Detection System using Deep Learning

## 📌 Overview

This project focuses on detecting plant diseases from leaf images using deep learning techniques.
It is trained on a structured dataset and evaluated on a real-world dataset to test how well the model performs outside controlled conditions.

The goal is to build a practical system that can assist in early disease detection for crops.

---

## 🚀 Features

* 🌱 Disease classification using leaf images
* 🧠 Deep Learning model (CNN / TensorFlow-based)
* 📊 Trained on PlantVillage dataset
* 🌿 Tested on real-world plant images
* 🖥️ Simple interface for predictions
* 📁 Modular project structure

---

## 📂 Project Structure

```bash
PlantDiseaseProject/
│
├── app.py                      # Main application (prediction interface)
├── test_realworld.py           # Script to test model on real-world dataset
│
├── notebooks/                  # Jupyter notebooks (training & experiments)
│   ├── plantdiseases.ipynb
│   ├── predict.ipynb
│   └── models/                 # Saved trained models (.h5 / .keras)
│
├── components/                 # Core modules (UI, model handling, etc.)
├── config/                     # Configuration files (disease info, mappings)
├── styles/                     # UI styling
│
├── dataset/                    # Training dataset (not included in repo)
├── realworlddataset/           # Real-world test dataset (not included)
│
├── requirements.txt            # Dependencies
└── README.md                   # Project documentation
```

---

## 📊 Datasets

### 1. 🌱 PlantVillage Dataset (Training)

* Used to train the model
* Contains labeled images of plant leaves
* Well-structured dataset for supervised learning

---

### 2. 🌿 Real-World Dataset (Testing)

* Used to evaluate real-world performance
* More challenging and less structured than training data

---

## 📥 Dataset Download

⚠️ Due to large size (~2GB), datasets are not included in this repository.

👉 Download from Google Drive:
**https://drive.google.com/drive/folders/1VUVnyHVlmPq5qHaivcrGP8mDjE6yQbEc?usp=sharing**

### Files included:

* `plantvillage_dataset.zip` → Training dataset
* `realworld_test_dataset.zip` → Testing dataset
* `PlantDiseaseProject.rar` → Contains whole project zip (including datasets 


---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Suyashjagtap16/Plant_disease_detection.git
cd PlantDiseaseProject
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Download and extract datasets

* Download datasets from the link above
* Extract them into the project directory

Expected structure:

```bash
PlantDiseaseProject/
│
├── dataset/              # training data
├── realworlddataset/     # testing data
```

---

### 4. Run the application

#### ▶️ Run main app

```bash
streamlit run app.py
```

---

#### 🧪 Test model on real-world dataset

```bash
python test_realworld.py
```

---

## 🧠 Model Information

* Built using TensorFlow / Keras
* Trained on PlantVillage dataset
* Saved model files:

  * `basic_cnn_model.h5`
  * `basic_cnn_model.keras`

---

## 📈 Objective

* Improve plant disease detection accuracy
* Evaluate model performance on real-world data
* Build a practical ML-based agricultural solution

---

## ⚠️ Notes

* Ensure datasets are placed correctly before running
* Model performance may vary on real-world images
* Large files (models & datasets) may take time to download

---

## 🔮 Future Improvements
* Adding Grad cam functionality
* Deploy as web or mobile application
* Add real-time prediction support
* Expand dataset diversity

---

## 👨‍💻 Author

**Suyash Jagtap**

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
