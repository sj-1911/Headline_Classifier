import pickle
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import matplotlib.pyplot as plt
from collections import Counter

# === Load your model and tools ===
model = load_model("huff_classifier.keras")

with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

with open("label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

# === Load your scraped headlines ===
with open("Headlines.txt", "r", encoding="utf-8") as f:
    headlines = [line.strip() for line in f if line.strip()]

# === Tokenize and pad them ===
sequences = tokenizer.texts_to_sequences(headlines)
padded = pad_sequences(sequences, maxlen=20, padding='post')

# === Predict categories ===
predictions = model.predict(padded)
predicted_indices = np.argmax(predictions, axis=1)
predicted_labels = label_encoder.inverse_transform(predicted_indices)

# === Show a few results ===
print("\n🧠 Sample Predictions:")
for i in range(min(10, len(headlines))):
    print(f"[{predicted_labels[i]}] {headlines[i]}")

# === Optional: Save to CSV ===
df_out = pd.DataFrame({
    "Category": predicted_labels,
    "Headline": headlines
})
df_out.to_csv("PredictedHeadlines.csv", index=False)
print("\n✅ All predictions saved to PredictedHeadlines.csv")

# === Optional: Show pie chart ===
counts = Counter(predicted_labels)
plt.figure(figsize=(8, 6))
plt.pie(counts.values(), labels=counts.keys(), autopct='%1.1f%%', startangle=140)
plt.title("Predicted Headline Categories")
plt.axis('equal')
plt.tight_layout()
plt.show()
