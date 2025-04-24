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
import matplotlib.pyplot as plt
from collections import Counter

# Count predicted categories
counts = Counter(predicted_labels)
labels, sizes = zip(*counts.items())

# Sort categories by size descending
sorted_pairs = sorted(zip(sizes, labels), reverse=True)
sizes, labels = zip(*sorted_pairs)

# Filter out categories < 3% and group them as 'Other'
total = sum(sizes)
filtered_labels = []
filtered_sizes = []
other_total = 0

for label, size in zip(labels, sizes):
    if size / total >= 0.03:
        filtered_labels.append(label)
        filtered_sizes.append(size)
    else:
        other_total += size

if other_total > 0:
    filtered_labels.append("Other")
    filtered_sizes.append(other_total)

# Explode largest slice
explode = [0.08 if i == 0 else 0 for i in range(len(filtered_sizes))]

# Create donut-style pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    filtered_sizes,
    labels=filtered_labels,
    autopct="%1.1f%%",
    startangle=140,
    explode=explode,
    textprops={"fontsize": 10},
    wedgeprops=dict(width=0.4),
    pctdistance=0.8
)

# Add center circle
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

# Style and layout
plt.setp(autotexts, size=9, weight="bold", color="black")
plt.title("Predicted Headline Categories (Filtered)", fontsize=14, fontweight="bold", y=1.02)
plt.axis('equal')
plt.tight_layout()
plt.show()

