# 🍽️ Calories Advisor App

An AI-powered web app that detects food from uploaded images and provides estimated **calorie and nutrition details** using **Hugging Face's BLIP model** and the **CalorieNinjas API**.

---

## 🔍 Features

- 📸 Upload food images
- 🧠 Detects food items using the BLIP image captioning model
- 🔬 Retrieves calories, protein, fat, and carbohydrate values via CalorieNinjas API
- ⚡ Built using **Streamlit**, **Transformers**, and **PIL**

---

## 🚀 How It Works

1. Upload a food image (JPG, JPEG, or PNG).
2. The app uses the **BLIP model** to generate a caption describing the food.
3. The caption is sent to the **CalorieNinjas API**.
4. The app displays detailed nutritional information.

---

## 🧰 Tech Stack

- Python
- Streamlit
- Hugging Face Transformers (`BLIP`)
- CalorieNinjas API
- PIL (Python Imaging Library)
- dotenv

---

## 📦 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/calories-advisor-app.git
cd calories-advisor-app

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Set Up Environment Variable
Create a .env file in the project root and add your CalorieNinjas API key:
CALORIENINJAS_API_KEY=your_api_key_here

### 4. Run the App
streamlit run app.py

📸 Example Use
Upload an image of a food plate → BLIP detects: A bowl of salad with vegetables → Nutritional data retrieved from CalorieNinjas and displayed.

📌 Note
This app is for educational/demo purposes only.
Nutritional values are estimates from the CalorieNinjas API and may not be 100% accurate.

🛠️ Future Enhancements
Support multiple food items per image
Add portion size estimation
Export nutrition report as PDF
Add voice input and OCR support

📄 License
This project is licensed under the MIT License.
