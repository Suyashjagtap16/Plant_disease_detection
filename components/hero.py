import streamlit as st


def render_hero():
    st.markdown("""
<div class="hero">

  <!-- LEFT: Branding + Stats -->
  <div class="hero-left">
    <div class="hero-tag">🌿 AI-Powered Agriculture</div>
    <div class="hero-title">Leaf<span>Scan</span> </div>
    <div class="hero-tagline">Plant Disease Detection System</div>
    <div class="hero-subtitle">
      Upload a plant leaf photo and get instant AI-powered disease diagnosis,
      severity assessment, and step-by-step treatment guidance — powered by two
      trained deep learning models.
    </div>
    <div class="hero-stats">
      <div class="stat-item"><span class="stat-num">38</span><span class="stat-label">Disease Classes</span></div>
      <div class="stat-item"><span class="stat-num">14</span><span class="stat-label">Crop Species</span></div>
      <div class="stat-item"><span class="stat-num">2</span><span class="stat-label">AI Models</span></div>
      <div class="stat-item"><span class="stat-num">54K+</span><span class="stat-label">Training Images</span></div>
    </div>
  </div>

  <!-- RIGHT: Feature cards + Crop pills -->
  <div class="hero-right">
    <div>
      <div class="hero-section-mini-label">What this tool does</div>
      <div class="hero-feat-grid">
        <div class="hero-feat">
          <span class="hero-feat-icon">🔬</span>
          <div class="hero-feat-title">Dual Model Diagnosis</div>
          <div class="hero-feat-desc">Basic CNN &amp; MobileNetV2 both analyse your leaf and compare results.</div>
        </div>
        <div class="hero-feat">
          <span class="hero-feat-icon">💊</span>
          <div class="hero-feat-title">Treatment Guidance</div>
          <div class="hero-feat-desc">Get specific fungicide, bactericide, or organic treatment steps.</div>
        </div>
        <div class="hero-feat">
          <span class="hero-feat-icon">🛡️</span>
          <div class="hero-feat-title">Prevention Plans</div>
          <div class="hero-feat-desc">Actionable prevention strategies tailored to each disease class.</div>
        </div>
        <div class="hero-feat">
          <span class="hero-feat-icon">⚡</span>
          <div class="hero-feat-title">Severity Rating</div>
          <div class="hero-feat-desc">Each result is rated from Moderate → Critical so you prioritise correctly.</div>
        </div>
      </div>
    </div>
    <div>
      <div class="hero-section-mini-label">Supported crops</div>
      <div class="hero-disease-strip">
        <span class="hero-disease-pill">🍎 Apple</span>
        <span class="hero-disease-pill">🍅 Tomato</span>
        <span class="hero-disease-pill">🥔 Potato</span>
        <span class="hero-disease-pill">🌽 Corn</span>
        <span class="hero-disease-pill">🍇 Grape</span>
        <span class="hero-disease-pill">🍑 Peach</span>
        <span class="hero-disease-pill">🍒 Cherry</span>
        <span class="hero-disease-pill">🍊 Orange</span>
        <span class="hero-disease-pill">🫑 Pepper</span>
        <span class="hero-disease-pill">🍓 Strawberry</span>
        <span class="hero-disease-pill">🫐 Blueberry</span>
        <span class="hero-disease-pill">🌿 Soybean</span>
        <span class="hero-disease-pill">🎃 Squash</span>
        <span class="hero-disease-pill">🫐 Raspberry</span>
      </div>
    </div>
  </div>

</div>
""", unsafe_allow_html=True)
