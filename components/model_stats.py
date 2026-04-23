import streamlit as st

def render_model_stats():
    st.markdown('<div class="section-label">Model Training Performance</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="display:flex; gap:12px; margin-bottom:24px;">

        <div style="flex:1; background:rgba(230,126,34,0.07);
             border:1px solid rgba(230,126,34,0.25);
             border-radius:14px; padding:20px 22px; text-align:center;">
            <div style="font-size:10px; letter-spacing:2px; text-transform:uppercase;
                 color:#e67e22; margin-bottom:10px; font-weight:700;">🧠 Basic CNN</div>
            <div style="font-family:'Syne',sans-serif; font-size:42px;
                 font-weight:800; color:#fff; line-height:1;">65.0<span style="font-size:22px;">%</span></div>
            <div style="font-size:11px; color:#7a9b80; margin-top:6px;">Validation Accuracy</div>
            <div style="margin-top:12px; background:rgba(255,255,255,0.05);
                 border-radius:8px; padding:8px 12px; font-size:11px; color:#7a9b80;">
                Custom CNN trained from scratch
            </div>
        </div>

        <div style="flex:1; background:rgba(57,211,83,0.07);
             border:1px solid rgba(57,211,83,0.25);
             border-radius:14px; padding:20px 22px; text-align:center;">
            <div style="font-size:10px; letter-spacing:2px; text-transform:uppercase;
                 color:#39d353; margin-bottom:10px; font-weight:700;">🚀 MobileNetV2</div>
            <div style="font-family:'Syne',sans-serif; font-size:42px;
                 font-weight:800; color:#fff; line-height:1;">92.5<span style="font-size:22px;">%</span></div>
            <div style="font-size:11px; color:#7a9b80; margin-top:6px;">Validation Accuracy</div>
            <div style="margin-top:12px; background:rgba(255,255,255,0.05);
                 border-radius:8px; padding:8px 12px; font-size:11px; color:#7a9b80;">
                Transfer learning — ImageNet pretrained
            </div>
        </div>

    </div>
    <div style="background:rgba(255,255,255,0.02); border:1px solid rgba(255,255,255,0.06);
         border-radius:10px; padding:10px 16px; font-size:11px; color:#7a9b80; text-align:center;">
        ℹ️ Trained on PlantVillage dataset &nbsp;·&nbsp; 54,000+ images &nbsp;·&nbsp; 38 disease classes
    </div>
    """, unsafe_allow_html=True)