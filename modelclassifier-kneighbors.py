import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns

# Memuat dataset
data = pd.read_csv("dataset/HotelReservations.csv")

# Pemrosesan data
data = pd.get_dummies(data, columns=["type_of_meal_plan", "room_type_reserved", "market_segment_type"])
data = data.drop(['Booking_ID'], axis=1)

# Encode string labels into numerical labels for 'booking_status'
label_encoder = LabelEncoder()
data['booking_status'] = label_encoder.fit_transform(data['booking_status'])

# Pisahkan atribut dan label
X = data.drop("booking_status", axis=1)
y = data["booking_status"]

# Pembagian data train dan data test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Pelatihan model (contoh menggunakan RandomForestClassifier)
model = KNeighborsClassifier()
model.fit(X_train, y_train)

# Evaluasi model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
report = classification_report(y_test, predictions)

print(f"Akurasi model: {accuracy}")
print(f"Classification Report:\n{report}")

# Menyimpan data train ke dalam file CSV
train_result = pd.concat([X_train, y_train], axis=1)
train_result.to_csv("train-data/train_data2.csv", index=False)

# Menyimpan data test ke dalam file CSV
test_result = pd.concat([X_test, y_test], axis=1)
test_result.to_csv("test-data/test_data2.csv", index=False)

# Visualisasi
# Plot distribusi kelas pada data train, distribusi kelas pada data test, dan confusion matrix
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Plot distribusi kelas pada data train
sns.countplot(x='booking_status', data=train_result, ax=axes[0])
axes[0].set_title('Distribution of Classes in Train Data')

# Plot distribusi kelas pada data test
sns.countplot(x='booking_status', data=test_result, ax=axes[1])
axes[1].set_title('Distribution of Classes in Test Data')

# Confusion Matrix untuk data test
cm = confusion_matrix(y_test, predictions)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=label_encoder.classes_, yticklabels=label_encoder.classes_, ax=axes[2])
axes[2].set_title('Confusion Matrix for Test Data')

plt.show()