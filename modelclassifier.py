import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
<<<<<<< HEAD
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
=======
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
>>>>>>> origin/main

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
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluasi model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
report = classification_report(y_test, predictions)

print(f"Akurasi model: {accuracy}")
print(f"Classification Report:\n{report}")

# Menyimpan data train ke dalam file CSV
train_result = pd.concat([X_train, y_train], axis=1)
<<<<<<< HEAD
train_result.to_csv("data-train/train_data.csv", index=False)

# Menyimpan data test ke dalam file CSV
test_result = pd.concat([X_test, y_test], axis=1)
test_result.to_csv("data-test/test_data.csv", index=False)

# Visualisasi
# Plot distribusi kelas pada data train
plt.figure(figsize=(8, 6))
sns.countplot(x='booking_status', data=train_result)
plt.title('Distribution of Classes in Train Data')
plt.show()

# Plot distribusi kelas pada data test
plt.figure(figsize=(8, 6))
sns.countplot(x='booking_status', data=test_result)
plt.title('Distribution of Classes in Test Data')
plt.show()

# Confusion Matrix untuk data test
cm = confusion_matrix(y_test, predictions)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=label_encoder.classes_, yticklabels=label_encoder.classes_)
plt.title('Confusion Matrix for Test Data')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()
=======
train_result.to_csv("train_data.csv", index=False)

# Menyimpan data test ke dalam file CSV
test_result = pd.concat([X_test, y_test], axis=1)
test_result.to_csv("test_data.csv", index=False)
>>>>>>> origin/main
