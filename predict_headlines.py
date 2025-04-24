import matplotlib
matplotlib.use('TkAgg')  # 👈 forces GUI-compatible backend
import matplotlib.pyplot as plt

from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import load_model
import numpy as np

# === Same labels and tokenizer training as before ===
labels = [
    "Science", "Sports", "Health", "Politics", "Science", 
    "Technology", "Politics", "Health", "Politics", "Lifestyle", 
    "Politics", "Lifestyle", "Technology", "Sports", "Science"
]

training_headlines = [
    "113 million-year-old ‘hell ant’ found in Brazil is the oldest ever found, scientists say",
    "2025 NFL draft",
    "A 3-week-old baby received a heart transplant 14 years ago and gained a ‘donor mom’",
    "A billionaire Trump supporter has harsh words for the president about his trade war",
    "An ancient ‘terror crocodile’ became a dinosaur-eating giant. Scientists say they now know why",
    "Apple’s new MacBook Air M4 just hit a new low price",
    "Canadian voters",
    "Concerned about US vaccine misinformation and access, public health experts start Vaccine Integrity Project",
    "DNC pushes back on David Hogg’s plans to support primary challenges against Democratic incumbents",
    "Fake tan, fancy nails: How marathons became a catwalk for beauty",
    "Gunman in 2022 mass shooting at suburban Chicago July Fourth parade sentenced to life in prison",
    "How to make exterior wood window shutters",
    "Motorola’s iconic flip phone gets an AI reboot",
    "Simone Biles says gymnastics rivalry with friend Rebeca Andrade has ‘pushed the sport forward’",
    "Zoo welcomes baby elephant born through artificial insemination"
]

# Label encoding + tokenizer must match training
label_encoder = LabelEncoder()
label_encoder.fit(labels)

tokenizer = Tokenizer(num_words=10000, oov_token="<OOV>")
tokenizer.fit_on_texts(training_headlines)

# === Load new headlines from file ===
with open("Headlines.txt", "r", encoding="utf-8") as f:
    new_headlines = [line.strip() for line in f.readlines() if line.strip()]

# Tokenize and pad the new headlines
new_sequences = tokenizer.texts_to_sequences(new_headlines)
new_padded = pad_sequences(new_sequences, padding='post', maxlen=20)

# === Build the same model architecture ===
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, GlobalAveragePooling1D, Dense

model = Sequential([
    Embedding(input_dim=10000, output_dim=16, input_length=20),
    GlobalAveragePooling1D(),
    Dense(16, activation='relu'),
    Dense(len(label_encoder.classes_), activation='softmax')
])

# Retrain the model on the original 15 examples
encoded_labels = label_encoder.transform(labels)
training_sequences = tokenizer.texts_to_sequences(training_headlines)
training_padded = pad_sequences(training_sequences, padding='post', maxlen=20)

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(training_padded, encoded_labels, epochs=30, verbose=0)

# === Predict new headlines ===
pred_probs = model.predict(new_padded)
predicted_classes = np.argmax(pred_probs, axis=1)
predicted_labels = label_encoder.inverse_transform(predicted_classes)

# === Visualize in pie chart ===
from collections import Counter
category_counts = Counter(predicted_labels)

plt.figure(figsize=(8, 6))
plt.pie(category_counts.values(), labels=category_counts.keys(), autopct="%1.1f%%", startangle=140)
plt.title("Headline Category Distribution (Predicted)")
plt.axis('equal')
plt.tight_layout()
plt.show()


# (your pie chart code here)

plt.show()  # 👈 This is the line that makes the plot appear!
