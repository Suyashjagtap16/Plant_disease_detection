import streamlit as st
from PIL import Image


def render_left_panel():
    """Renders the upload zone and how-to-use guide. Returns the uploaded file."""
    st.markdown('<div style="padding: 28px 0 0 0;">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">Upload Leaf Image</div>', unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Drop your leaf image here",
        type=["jpg", "png", "jpeg"],
        label_visibility="collapsed"
    )

    if uploaded_file:
        img_display = Image.open(uploaded_file)
        st.image(img_display, use_column_width=True, caption="")
        st.markdown(f"""
        <div style="display:flex; gap:10px; margin-top:12px;">
            <div class="metric-chip"><b>{img_display.size[0]}×{img_display.size[1]}</b>Resolution</div>
            <div class="metric-chip"><b>{uploaded_file.type.split('/')[1].upper()}</b>Format</div>
            <div class="metric-chip"><b>{round(uploaded_file.size/1024, 1)}KB</b>Size</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # How to use guide
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<div class="section-label">How to use</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="display:flex; flex-direction:column; gap:8px;">
        <div style="display:flex; align-items:flex-start; gap:10px; font-size:12.5px; color:#7a9b80;">
            <span style="color:#39d353; font-weight:700; font-family:Syne,sans-serif; flex-shrink:0;">01</span>
            <span>Take a clear, close-up photo of the affected plant leaf in good lighting.</span>
        </div>
        <div style="display:flex; align-items:flex-start; gap:10px; font-size:12.5px; color:#7a9b80;">
            <span style="color:#39d353; font-weight:700; font-family:Syne,sans-serif; flex-shrink:0;">02</span>
            <span>Upload it using the file uploader above (JPG or PNG).</span>
        </div>
        <div style="display:flex; align-items:flex-start; gap:10px; font-size:12.5px; color:#7a9b80;">
            <span style="color:#39d353; font-weight:700; font-family:Syne,sans-serif; flex-shrink:0;">03</span>
            <span>Both AI models will instantly analyse and diagnose the disease.</span>
        </div>
        <div style="display:flex; align-items:flex-start; gap:10px; font-size:12.5px; color:#7a9b80;">
            <span style="color:#39d353; font-weight:700; font-family:Syne,sans-serif; flex-shrink:0;">04</span>
            <span>Follow the treatment and prevention steps shown on the right.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    return uploaded_file
