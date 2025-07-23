import streamlit as st
from PIL import Image
import requests
import os
from dotenv import load_dotenv
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

# Load environment variables from .env
load_dotenv()
CALORIENINJAS_API_KEY = os.getenv("CALORIENINJAS_API_KEY")

# Load BLIP model and processor from Hugging Face
st.info("🔄 Loading BLIP model... please wait (only once)")
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Generate caption from image
def get_caption_from_image(image):
    image = image.convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    output = model.generate(**inputs)
    caption = processor.decode(output[0], skip_special_tokens=True)
    return caption.strip()

# CalorieNinjas API function
def analyze_with_calorieninjas(food_text):
    url = "https://api.calorieninjas.com/v1/nutrition"
    headers = {
        "X-Api-Key": CALORIENINJAS_API_KEY
    }
    params = {
        "query": food_text
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}

# Streamlit UI
st.set_page_config(page_title="Calories Advisor APP")
st.title("🍽️ Calories Advisor App")

uploaded_file = st.file_uploader("Upload a food image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

if st.button("Tell me the total calories"):
    st.info("🔍 Analyzing image with BLIP model...")
    caption = get_caption_from_image(image)
    st.write("Generated Caption:", caption)

    if not caption or caption.strip() == "":
        st.error("No food detected in the image.")
    else:
        st.success(f"✅ Food detected: **{caption}**")
        st.write("Sending to CalorieNinjas:", caption)

        st.info("Fetching nutrition data from CalorieNinjas...")
        result = analyze_with_calorieninjas(caption)

        if "error" in result:
            st.error("CalorieNinjas API Error:")
            st.code(result["error"])
        else:
            st.header("🥗 Nutrition Breakdown:")
            items = result.get("items", [])
            if items:
                for item in items:
                    st.subheader(f"🍽️ {item['name'].capitalize()}")
                    st.write(f"- Calories: {item['calories']} kcal")
                    st.write(f"- Carbohydrates: {item['carbohydrates_total_g']} g")
                    st.write(f"- Protein: {item['protein_g']} g")
                    st.write(f"- Fat: {item['fat_total_g']} g")
                    st.markdown("---")
            else:
                st.warning("No detailed nutrition data found.")
