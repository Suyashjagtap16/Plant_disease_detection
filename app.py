import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import json
from PIL import Image
import time

# ── Local imports ──────────────────────────────────────────────────────────────
from styles.main_css      import CSS
from components.hero      import render_hero
from components.uploader  import render_left_panel
from components.model_cards  import render_model_cards
from components.disease_info import render_disease_info
from config.disease_db    import DISEASE_DB

# =============================================================================
# PAGE CONFIG
# =============================================================================
st.set_page_config(
    page_title="LeafScan — Plant Disease Detector",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inject CSS
st.markdown(CSS, unsafe_allow_html=True)

# =============================================================================
# HERO
# =============================================================================
render_hero()

# =============================================================================
# LOAD MODELS
# =============================================================================
@st.cache_resource
def load_models():
    basic     = load_model("notebooks/models/basic_cnn_model.keras")
    mobilenet = load_model("notebooks/models/mobilenetv2_finetuned.keras")
    return basic, mobilenet

with st.spinner("Loading AI models..."):
    basic_model, mobilenet_model = load_models()

with open("notebooks/models/class_names.json", "r") as f:
    class_names = json.load(f)

# =============================================================================
# TWO-COLUMN LAYOUT
# =============================================================================
col_left, col_right = st.columns([1, 1.7], gap="large")

# ── LEFT PANEL ─────────────────────────────────────────────────────────────────
with col_left:
    uploaded_file = render_left_panel()

# ── RIGHT PANEL ────────────────────────────────────────────────────────────────
with col_right:
    st.markdown('<div style="padding: 28px 0 0 0;">', unsafe_allow_html=True)

    if uploaded_file is None:
        # Empty state placeholder
        st.markdown("""
        <div class="placeholder-area">
            <div class="placeholder-icon">🌿</div>
            <div class="placeholder-title">No image uploaded yet</div>
            <div class="placeholder-text">
                Upload a clear photo of a plant leaf to get an instant AI disease
                diagnosis and treatment recommendations.
            </div>
        </div>
        """, unsafe_allow_html=True)

    else:
        # ── Run inference ───────────────────────────────────────────────────
        img         = Image.open(uploaded_file).convert("RGB")
        img_resized = img.resize((160, 160))
        img_array   = image.img_to_array(img_resized)
        img_array   = np.expand_dims(img_array, axis=0)

        with st.spinner("Running AI analysis..."):
            time.sleep(0.3)
            pred_basic = basic_model.predict(img_array, verbose=0)
            pred_mob   = mobilenet_model.predict(img_array, verbose=0)

        class_basic = class_names[np.argmax(pred_basic)]
        conf_basic  = float(np.max(pred_basic)) * 100
        class_mob   = class_names[np.argmax(pred_mob)]
        conf_mob    = float(np.max(pred_mob)) * 100

        # ── Guard: no leaf / blurry image detected ──────────────────────────
        # If EITHER model sees "Background", skip everything and show warning.
        if "Background" in class_mob or "Background" in class_basic:
            st.markdown("""
            <div class="no-leaf-banner">
                <span class="no-leaf-icon">📷</span>
                <div class="no-leaf-title">No Leaf Detected</div>
                <div class="no-leaf-text">
                    The uploaded image doesn't appear to contain a clear plant leaf —
                    it may be blurry, too dark, or showing a background without vegetation.<br><br>
                    Please try again with a <b style="color:#e8f5e9;">well-lit, close-up photo</b>
                    of a single leaf against a plain background.
                </div>
                <div class="no-leaf-tips">
                    <div class="no-leaf-tip">✅ Good lighting</div>
                    <div class="no-leaf-tip">✅ Single leaf, close-up</div>
                    <div class="no-leaf-tip">✅ No blur or motion</div>
                    <div class="no-leaf-tip">✅ Plain background</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        else:
            # ── Resolve display names ────────────────────────────────────────
            info_basic   = DISEASE_DB.get(class_basic, {})
            info_mob     = DISEASE_DB.get(class_mob, {})
            display_basic = info_basic.get("display", class_basic.replace("___", " — ").replace("_", " "))
            display_mob   = info_mob.get("display",   class_mob.replace("___", " — ").replace("_", " "))

            # ── Model prediction cards + agreement banner ────────────────────
            render_model_cards(
                class_basic, conf_basic, display_basic,
                class_mob,   conf_mob,   display_mob,
            )

            # ── Full disease / healthy details ───────────────────────────────
            render_disease_info(class_mob)

    st.markdown('</div>', unsafe_allow_html=True)

# =============================================================================
# FOOTER
# =============================================================================
st.markdown("""
<div style="border-top:1px solid rgba(57,211,83,0.1); padding:20px 60px;
     text-align:center; margin-top:24px;">
    <span style="font-size:12px; color:#3d5a42; letter-spacing:1px;">
        LEAFSCAN AI — Built with TensorFlow + Streamlit &nbsp;·&nbsp;
        PlantVillage Dataset &nbsp;·&nbsp; 38 Disease Classes
    </span>
</div>
""", unsafe_allow_html=True)
