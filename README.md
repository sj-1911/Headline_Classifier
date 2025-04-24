# 📰 Headline Classifier

A software system that scrapes real-world news headlines, classifies them into 42 HuffPost categories using a trained TensorFlow model, and visualizes the results — all powered by Python and software design patterns.

---

## 📌 Features

- ✅ Scrapes headlines from CNN/BBC using BeautifulSoup
- ✅ Sorts headlines using the **Strategy Design Pattern**
- ✅ Applies decorators (filter, truncate, timestamp) using the **Decorator Design Pattern**
- ✅ Parses site-specific headlines with **Factory Design Pattern**
- ✅ Trains a TensorFlow classifier using the **HuffPost News Category Dataset**
- ✅ Predicts categories for new headlines and visualizes with a pie chart
- ✅ Saves predictions to CSV

---

## 🧠 Machine Learning Model

- Framework: TensorFlow + Keras
- Input: Headline text
- Output: One of 42 categories (e.g., `POLITICS`, `WELLNESS`, `SPORTS`)
- Accuracy: ~48% (20k sample headlines)
- Tokenizer + LabelEncoder saved for reuse

---

## 🛠️ How to Run

### 1. Clone the repo

```bash
git clone https://github.com/sj-1911/Headline_Classifier.git
cd Headline_Classifier
