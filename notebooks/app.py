import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import json
from PIL import Image

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="Plant Disease Detector 🌿", layout="centered")

# =========================
# PREMIUM CSS
# =========================
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #141e30, #243b55);
    color: white;
}

/* Title Glow */
.glow {
    font-size: 42px;
    font-weight: bold;
    text-align: center;
    color: #ffffff;
    animation: glow 2s ease-in-out infinite alternate;
}

@keyframes glow {
    from {
        text-shadow: 0 0 10px #00c6ff, 0 0 20px #00c6ff;
    }
    to {
        text-shadow: 0 0 25px #00c6ff, 0 0 50px #00c6ff;
    }
}

/* Glass Card */
.card {
    background: rgba(255, 255, 255, 0.08);
    padding: 20px;
    border-radius: 20px;
    backdrop-filter: blur(15px);
    transition: 0.3s ease;
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    margin-bottom: 20px;
}

/* Hover */
.card:hover {
    transform: scale(1.04);
    box-shadow: 0 0 30px rgba(0,255,255,0.6);
}

/* Upload box spacing */
.upload-box {
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.markdown('<div class="glow">🌿 Plant Disease Detection</div>', unsafe_allow_html=True)
st.markdown("### Upload a leaf image and analyze disease")

# =========================
# DISEASE INFO
# =========================
disease_info = {
    "Tomato___Early_blight": {
        "desc": "Fungal disease causing dark spots on leaves.",
        "solution": "Use fungicides and remove infected leaves."
    },
    "Potato___Late_blight": {
        "desc": "Serious fungal infection causing leaf decay.",
        "solution": "Apply fungicide and avoid overwatering."
    },
    "Apple___Apple_scab": {
        "desc": "Causes dark scabby lesions on leaves.",
        "solution": "Use resistant varieties and fungicide spray."
    }
}

# =========================
# LOAD MODELS
# =========================
@st.cache_resource
def load_models():
    basic = load_model("notebooks/models/basic_cnn_model.keras")
    mobilenet = load_model("notebooks/models/mobilenetv2_finetuned.keras")
    return basic, mobilenet

basic_model, mobilenet_model = load_models()

# =========================
# LOAD CLASS NAMES
# =========================
with open("notebooks/models/class_names.json", "r") as f:
    class_names = json.load(f)

# =========================
# MODEL ACCURACY
# =========================
model_accuracies = {
    "Basic CNN": 65.0,
    "MobileNetV2": 92.5
}

# =========================
# IMAGE UPLOAD
# =========================
uploaded_file = st.file_uploader("📤 Upload Leaf Image", type=["jpg", "png", "jpeg"])

# =========================
# MAIN LOGIC
# =========================
if uploaded_file is not None:

    # Show image
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Preprocess
    img = img.resize((160,160))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    # Predictions
    pred_basic = basic_model.predict(img_array)
    class_basic = class_names[np.argmax(pred_basic)]
    conf_basic = np.max(pred_basic) * 100

    pred_mob = mobilenet_model.predict(img_array)
    class_mob = class_names[np.argmax(pred_mob)]
    conf_mob = np.max(pred_mob) * 100

    # =========================
    # RESULTS
    # =========================
    st.markdown("## 🔍 Prediction Results")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div class="card">
        <h3>🧠 Basic CNN</h3>
        <p><b>Disease:</b> {class_basic}</p>
        <p><b>Confidence:</b> {conf_basic:.2f}%</p>
        <p><b>Accuracy:</b> {model_accuracies['Basic CNN']}%</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="card">
        <h3>🚀 MobileNetV2</h3>
        <p><b>Disease:</b> {class_mob}</p>
        <p><b>Confidence:</b> {conf_mob:.2f}%</p>
        <p><b>Accuracy:</b> {model_accuracies['MobileNetV2']}%</p>
        </div>
        """, unsafe_allow_html=True)

    # =========================
    # DISEASE DETAILS
    # =========================
    st.markdown("## 🌿 Disease Details")

    final_class = class_mob
    if "Background" in final_class:
     st.warning("⚠️ Please upload a clear leaf image")
    
    info = disease_info.get(final_class)

    if info:
        st.markdown(f"""
        <div class="card">
        <h4>Description</h4>S   
        <p>{info['desc']}</p>

        <h4>Prevention / Treatment</h4>
        <p>{info['solution']}</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("No detailed info available for this disease yet.")
        
        