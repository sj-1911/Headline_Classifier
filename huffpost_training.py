import pandas as pd
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, GlobalAveragePooling1D, Dense
import pickle

# Load data
df = pd.read_json("News_Category_Dataset_v3.json", lines=True)
df_sample = df[['headline', 'category']].dropna().sample(n=20000, random_state=42)

# Encode categories
label_encoder = LabelEncoder()
labels = label_encoder.fit_transform(df_sample['category'])

# Save label encoder
with open("label_encoder.pkl", "wb") as f:
    pickle.dump(label_encoder, f)

# Tokenize headlines
tokenizer = Tokenizer(num_words=10000, oov_token="<OOV>")
tokenizer.fit_on_texts(df_sample['headline'])
sequences = tokenizer.texts_to_sequences(df_sample['headline'])
padded = pad_sequences(sequences, maxlen=20, padding='post')

# Save tokenizer
with open("tokenizer.pkl", "wb") as f:
    pickle.dump(tokenizer, f)

# Build model
model = Sequential([
    Embedding(10000, 16, input_length=20),
    GlobalAveragePooling1D(),
    Dense(32, activation='relu'),
    Dense(len(set(labels)), activation='softmax')
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(padded, labels, epochs=10, batch_size=64, validation_split=0.1)

# Save model
model.save("huff_classifier.keras")
print("✅ Model, tokenizer, and label encoder saved.")
