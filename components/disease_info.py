import streamlit as st
from config.disease_db import DISEASE_DB, SEVERITY_COLORS


def render_disease_info(final_class: str):
    """Renders the full Diagnosis & Treatment section for the given class name."""

    st.markdown('<div class="section-label">Diagnosis & Treatment</div>', unsafe_allow_html=True)

    info = DISEASE_DB.get(final_class)

    if not info:
        # Class exists in model but not in our DB yet
        st.markdown(f"""
        <div style="background:var(--bg-card); border:1px solid var(--border);
             border-radius:12px; padding:20px 24px; color:var(--text-muted);">
            <b style="color:var(--text-primary);">Detected:</b>
            {final_class.replace('___',' — ').replace('_',' ')}<br><br>
            Detailed disease info for this class is not yet in the database.
            Please consult a local agricultural extension officer for treatment guidance.
        </div>
        """, unsafe_allow_html=True)
        return

    is_healthy = (info.get("type") == "Healthy")
    sev        = info.get("severity", "Unknown")
    sev_color, _ = SEVERITY_COLORS.get(sev, SEVERITY_COLORS["Unknown"])

    # ── Healthy banner ──────────────────────────────────────────────────────
    if is_healthy:
        st.markdown(f"""
        <div class="healthy-banner">
            <div class="healthy-icon">{info['emoji']} ✅</div>
            <div class="healthy-title">Healthy Plant!</div>
            <div class="healthy-text">
                Your <b>{info['plant']}</b> leaf shows no signs of disease, infection, or pest damage.
                The plant appears to be in excellent condition.
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ── Disease header ──────────────────────────────────────────────────────
    else:
        st.markdown(f"""
        <div class="disease-header">
            <div class="disease-emoji">{info['emoji']}</div>
            <div>
                <div class="disease-title">{info['display']}</div>
                <div class="desc-text">{info['description']}</div>
                <div class="disease-meta">
                    <span class="meta-tag">🌱 {info['plant']}</span>
                    <span class="meta-tag">🔬 {info['type']}</span>
                    <span class="severity-tag"
                          style="background:rgba(0,0,0,0.3);
                                 border:1px solid {sev_color}40;
                                 color:{sev_color};">
                        ⚡ {sev} Severity
                    </span>
                    <span class="spread-tag" style="padding:3px 10px; font-size:11px;">
                        📡 {info['spread']}
                    </span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ── Info columns (symptoms/prevention | treatment/spread) ───────────────
    d1, d2 = st.columns(2)

    with d1:
        symp_items = "".join([
            f'<div class="info-item"><div class="info-bullet"></div>{s}</div>'
            for s in info['symptoms']
        ])
        st.markdown(f"""
        <div class="info-section">
            <div class="info-section-title">🔍 Symptoms</div>
            {symp_items}
        </div>
        """, unsafe_allow_html=True)

        prev_items = "".join([
            f'<div class="info-item"><div class="info-bullet" style="background:#f0b429;"></div>{p}</div>'
            for p in info['prevention']
        ])
        st.markdown(f"""
        <div class="info-section">
            <div class="info-section-title">🛡️ Prevention</div>
            {prev_items}
        </div>
        """, unsafe_allow_html=True)

    with d2:
        treat_items = "".join([
            f'<div class="info-item"><div class="info-bullet" style="background:#e05252;"></div>{t}</div>'
            for t in info['treatment']
        ])
        st.markdown(f"""
        <div class="info-section">
            <div class="info-section-title">💊 Treatment</div>
            {treat_items}
        </div>
        """, unsafe_allow_html=True)

        if not is_healthy:
            st.markdown(f"""
            <div class="info-section">
                <div class="info-section-title">📡 How It Spreads</div>
                <div class="spread-tag">{info['spread']}</div>
            </div>
            """, unsafe_allow_html=True)
            
            

