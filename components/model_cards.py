import streamlit as st


def render_model_cards(
    class_basic, conf_basic, display_basic,
    class_mob,   conf_mob,   display_mob,
):
    """
    Renders the two model prediction cards and the agreement banner.
    Returns (agree: bool) so the caller knows whether to show extra warnings.
    """
    st.markdown('<div class="section-label">Model Predictions</div>', unsafe_allow_html=True)

    mc1, mc2 = st.columns(2)

    with mc1:
        st.markdown(f"""
        <div class="model-card">
            <div class="model-name">🧠 Basic CNN</div>
            <div class="model-disease">Detected: <span>{display_basic}</span></div>
            <div class="conf-label"><span>Confidence</span><span>{conf_basic:.1f}%</span></div>
            <div class="conf-bar-bg">
                <div class="conf-bar-fill"
                     style="width:{conf_basic}%;
                            background: linear-gradient(90deg, #e67e22, #f39c12);">
                </div>
            </div>
            <div class="metrics-row">
                <div class="metric-chip"><b>{conf_basic:.1f}%</b>Image Score</div>
                <div class="metric-chip"><b>Basic</b>Architecture</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with mc2:
        st.markdown(f"""
        <div class="model-card winner">
            <div class="model-badge">✦ Best Model</div>
            <div class="model-name">🚀 MobileNetV2</div>
            <div class="model-disease">Detected: <span>{display_mob}</span></div>
            <div class="conf-label"><span>Confidence</span><span>{conf_mob:.1f}%</span></div>
            <div class="conf-bar-bg">
                <div class="conf-bar-fill" style="width:{conf_mob}%;"></div>
            </div>
            <div class="metrics-row">
                <div class="metric-chip"><b>{conf_mob:.1f}%</b>Image Score</div>
                <div class="metric-chip"><b>Transfer</b>Architecture</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Agreement banner
    agree = (class_basic == class_mob)
    st.markdown(f"""
    <div style="background:{'rgba(57,211,83,0.06)' if agree else 'rgba(240,180,41,0.06)'};
         border:1px solid {'rgba(57,211,83,0.2)' if agree else 'rgba(240,180,41,0.2)'};
         border-radius:10px; padding:10px 16px; font-size:13px;
         color:{'#39d353' if agree else '#f0b429'}; margin-bottom:24px;">
        {'✅ Both models agree on the diagnosis.'
         if agree else
         '⚠️ Models disagree — MobileNetV2 result shown below (higher accuracy model).'}
    </div>
    """, unsafe_allow_html=True)

    return agree
