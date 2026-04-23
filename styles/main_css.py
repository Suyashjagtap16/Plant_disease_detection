CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

:root {
    --bg-dark:        #0a0f0d;
    --bg-card:        #111a14;
    --bg-card2:       #0d1510;
    --green-bright:   #39d353;
    --green-mid:      #26a641;
    --green-dark:     #196127;
    --accent-amber:   #f0b429;
    --accent-red:     #e05252;
    --text-primary:   #e8f5e9;
    --text-muted:     #7a9b80;
    --border:         rgba(57, 211, 83, 0.15);
}

html, body, .stApp {
    background-color: var(--bg-dark) !important;
    font-family: 'DM Sans', sans-serif;
    color: var(--text-primary);
}

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
.stApp > header { display: none; }
section[data-testid="stSidebar"] { display: none; }

/* ── HERO ─────────────────────────────────────────── */
.hero {
    background: linear-gradient(145deg, #060d07 0%, #0f2010 60%, #091509 100%);
    border-bottom: 1px solid var(--border);
    position: relative;
    overflow: hidden;
    display: flex;
    min-height: 260px;
}
.hero::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
    pointer-events: none; z-index: 0;
}
.hero-left {
    flex: 1; padding: 44px 48px 40px;
    position: relative; z-index: 1;
    border-right: 1px solid var(--border);
    display: flex; flex-direction: column; justify-content: center;
}
.hero-right {
    width: 52%; padding: 36px 44px;
    position: relative; z-index: 1;
    display: flex; flex-direction: column; justify-content: center; gap: 20px;
    background: linear-gradient(135deg, rgba(57,211,83,0.03) 0%, transparent 60%);
}
.hero-right::after {
    content: '';
    position: absolute; top: -60px; right: -60px;
    width: 320px; height: 320px;
    background: radial-gradient(circle, rgba(57,211,83,0.09) 0%, transparent 65%);
    border-radius: 50%; pointer-events: none;
}
.hero-tag {
    display: inline-flex; align-items: center; gap: 6px;
    background: rgba(57,211,83,0.1); border: 1px solid rgba(57,211,83,0.25);
    color: var(--green-bright); font-family: 'DM Sans', sans-serif;
    font-size: 10px; font-weight: 600; letter-spacing: 2.5px;
    text-transform: uppercase; padding: 4px 12px; border-radius: 20px;
    margin-bottom: 14px; width: fit-content;
}
.hero-title {
    font-family: 'Syne', sans-serif; font-size: 54px; font-weight: 800;
    line-height: 1.0; color: #ffffff; margin: 0 0 4px; letter-spacing: -2px;
}
.hero-title span { color: var(--green-bright); }
.hero-tagline {
    font-family: 'Syne', sans-serif; font-size: 11px; font-weight: 500;
    color: rgba(57,211,83,0.5); letter-spacing: 3px;
    text-transform: uppercase; margin-bottom: 14px;
}
.hero-subtitle {
    font-size: 14.5px; color: var(--text-muted);
    font-weight: 300; line-height: 1.65; max-width: 400px;
}
.hero-stats {
    display: flex; gap: 0; margin-top: 28px;
    border: 1px solid var(--border); border-radius: 12px;
    overflow: hidden; background: rgba(0,0,0,0.2);
}
.stat-item {
    flex: 1; padding: 12px 16px;
    border-right: 1px solid var(--border); text-align: center;
}
.stat-item:last-child { border-right: none; }
.stat-num {
    font-family: 'Syne', sans-serif; font-size: 22px; font-weight: 800;
    color: var(--green-bright); display: block; line-height: 1;
}
.stat-label {
    font-size: 9px; color: var(--text-muted);
    letter-spacing: 1.2px; text-transform: uppercase; margin-top: 3px; display: block;
}
.hero-feat-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
.hero-feat {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(57,211,83,0.12);
    border-radius: 12px; padding: 14px 16px;
    position: relative; overflow: hidden;
}
.hero-feat::before {
    content: ''; position: absolute; top: 0; left: 0;
    width: 3px; height: 100%; background: var(--green-bright); opacity: 0.5;
}
.hero-feat-icon  { font-size: 20px; margin-bottom: 6px; display: block; }
.hero-feat-title { font-family: 'Syne', sans-serif; font-size: 12px; font-weight: 700; color: #fff; margin-bottom: 3px; }
.hero-feat-desc  { font-size: 11px; color: var(--text-muted); line-height: 1.4; }
.hero-disease-strip { display: flex; gap: 8px; flex-wrap: wrap; align-items: center; }
.hero-disease-pill {
    background: rgba(57,211,83,0.06); border: 1px solid rgba(57,211,83,0.15);
    border-radius: 20px; font-size: 10.5px; color: var(--text-muted);
    padding: 3px 10px; white-space: nowrap;
}
.hero-section-mini-label {
    font-size: 9px; font-weight: 700; letter-spacing: 2px;
    text-transform: uppercase; color: rgba(57,211,83,0.4); margin-bottom: 8px;
}

/* ── MODEL CARDS ──────────────────────────────────── */
.model-card {
    background: var(--bg-card2); border: 1px solid var(--border);
    border-radius: 14px; padding: 20px 22px; margin-bottom: 16px;
    position: relative; transition: all 0.3s ease;
}
.model-card:hover  { border-color: rgba(57,211,83,0.35); box-shadow: 0 0 20px rgba(57,211,83,0.06); }
.model-card.winner { border-color: rgba(57,211,83,0.4); background: linear-gradient(135deg, rgba(57,211,83,0.04) 0%, var(--bg-card2) 100%); }
.model-badge {
    position: absolute; top: 14px; right: 14px;
    background: rgba(57,211,83,0.15); border: 1px solid rgba(57,211,83,0.3);
    color: var(--green-bright); font-size: 10px; font-weight: 600;
    letter-spacing: 1px; text-transform: uppercase; padding: 3px 9px; border-radius: 20px;
}
.model-name    { font-family: 'Syne', sans-serif; font-size: 16px; font-weight: 700; color: #fff; margin: 0 0 4px; }
.model-disease { font-size: 13px; color: var(--text-muted); margin: 0 0 14px; }
.model-disease span { color: var(--text-primary); font-weight: 500; }
.conf-bar-bg   { background: rgba(255,255,255,0.07); border-radius: 6px; height: 6px; overflow: hidden; margin-top: 6px; }
.conf-bar-fill { height: 100%; border-radius: 6px; background: linear-gradient(90deg, var(--green-mid), var(--green-bright)); }
.conf-label    { display: flex; justify-content: space-between; font-size: 11px; color: var(--text-muted); margin-bottom: 4px; }
.metrics-row   { display: flex; gap: 12px; margin-top: 14px; }
.metric-chip {
    background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08);
    border-radius: 8px; padding: 6px 12px; font-size: 11px;
    color: var(--text-muted); flex: 1; text-align: center;
}
.metric-chip b {
    display: block; font-family: 'Syne', sans-serif;
    font-size: 15px; font-weight: 700; color: var(--text-primary); margin-bottom: 1px;
}

/* ── DISEASE INFO ─────────────────────────────────── */
.disease-header {
    background: linear-gradient(135deg, rgba(57,211,83,0.06) 0%, rgba(57,211,83,0.02) 100%);
    border: 1px solid var(--border); border-radius: 16px;
    padding: 24px 28px; margin-bottom: 24px;
    display: flex; align-items: flex-start; gap: 18px;
}
.disease-emoji { font-size: 42px; line-height: 1; flex-shrink: 0; }
.disease-title { font-family: 'Syne', sans-serif; font-size: 24px; font-weight: 800; color: #fff; margin: 0 0 4px; letter-spacing: -0.5px; }
.disease-meta  { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 10px; }
.meta-tag {
    background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.1);
    border-radius: 20px; font-size: 11px; font-weight: 500;
    letter-spacing: 0.5px; padding: 3px 10px; color: var(--text-muted);
}
.severity-tag { border-radius: 20px; font-size: 11px; font-weight: 600; letter-spacing: 0.5px; padding: 3px 10px; }
.desc-text    { font-size: 14px; color: var(--text-muted); line-height: 1.6; margin-top: 8px; }
.info-section {
    background: var(--bg-card); border: 1px solid var(--border);
    border-radius: 12px; padding: 20px 22px; margin-bottom: 16px;
}
.info-section-title {
    font-family: 'Syne', sans-serif; font-size: 11px; font-weight: 700;
    letter-spacing: 2px; text-transform: uppercase; color: var(--text-muted); margin-bottom: 14px;
}
.info-item {
    display: flex; gap: 10px; align-items: flex-start;
    margin-bottom: 9px; font-size: 13.5px; color: var(--text-primary); line-height: 1.5;
}
.info-item:last-child { margin-bottom: 0; }
.info-bullet { width: 6px; height: 6px; background: var(--green-bright); border-radius: 50%; margin-top: 7px; flex-shrink: 0; }
.spread-tag {
    background: rgba(240,180,41,0.1); border: 1px solid rgba(240,180,41,0.2);
    border-radius: 8px; padding: 8px 14px; font-size: 13px;
    color: var(--accent-amber); display: flex; align-items: center; gap: 8px;
}

/* ── HEALTHY BANNER ───────────────────────────────── */
.healthy-banner {
    background: linear-gradient(135deg, rgba(39,174,96,0.12) 0%, rgba(39,174,96,0.05) 100%);
    border: 1.5px solid rgba(39,174,96,0.3); border-radius: 14px;
    padding: 28px 32px; text-align: center; margin-bottom: 24px;
}
.healthy-icon  { font-size: 48px; margin-bottom: 10px; }
.healthy-title { font-family: 'Syne', sans-serif; font-size: 22px; font-weight: 700; color: #27ae60; margin-bottom: 6px; }
.healthy-text  { font-size: 14px; color: var(--text-muted); line-height: 1.5; }

/* ── NO LEAF / BLUR WARNING ───────────────────────── */
.no-leaf-banner {
    background: rgba(224,82,82,0.07);
    border: 2px dashed rgba(224,82,82,0.35);
    border-radius: 16px; padding: 40px 32px;
    text-align: center; margin-top: 20px;
}
.no-leaf-icon  { font-size: 56px; margin-bottom: 16px; display: block; }
.no-leaf-title { font-family: 'Syne', sans-serif; font-size: 22px; font-weight: 700; color: #e05252; margin-bottom: 10px; }
.no-leaf-text  { font-size: 13.5px; color: var(--text-muted); line-height: 1.75; max-width: 360px; margin: 0 auto 22px; }
.no-leaf-tips  { display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; }
.no-leaf-tip {
    background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08);
    border-radius: 10px; padding: 10px 18px; font-size: 12px; color: var(--text-muted);
}

/* ── PLACEHOLDER ──────────────────────────────────── */
.placeholder-area {
    display: flex; flex-direction: column; align-items: center;
    justify-content: center; height: 100%; min-height: 400px; text-align: center;
}
.placeholder-icon  { font-size: 64px; margin-bottom: 20px; opacity: 0.4; }
.placeholder-title { font-family: 'Syne', sans-serif; font-size: 20px; font-weight: 700; color: var(--text-muted); margin-bottom: 8px; }
.placeholder-text  { font-size: 13px; color: var(--text-muted); opacity: 0.6; max-width: 280px; line-height: 1.6; }

/* ── SECTION LABEL ────────────────────────────────── */
.section-label {
    font-family: 'Syne', sans-serif; font-size: 12px; font-weight: 700;
    letter-spacing: 2px; text-transform: uppercase; color: var(--text-muted);
    margin-bottom: 16px; padding-bottom: 10px; border-bottom: 1px solid var(--border);
}

/* ── STREAMLIT OVERRIDES ──────────────────────────── */
[data-testid="stHorizontalBlock"] { gap: 0 !important; }
[data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:first-child {
    padding: 28px 24px 28px 36px !important;
    background: var(--bg-card); border-right: 1px solid var(--border);
}
[data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:last-child {
    padding: 28px 36px 28px 36px !important;
}
[data-testid="stFileUploader"] {
    background: rgba(57,211,83,0.03) !important;
    border: 1.5px dashed rgba(57,211,83,0.25) !important;
    border-radius: 12px !important; padding: 8px !important; transition: all 0.3s ease !important;
}
[data-testid="stFileUploader"]:hover {
    border-color: rgba(57,211,83,0.5) !important;
    background: rgba(57,211,83,0.06) !important;
}
[data-testid="stFileUploader"] label  { color: var(--text-muted) !important; }
[data-testid="stFileUploader"] button {
    background: rgba(57,211,83,0.1) !important; border: 1px solid rgba(57,211,83,0.3) !important;
    color: var(--green-bright) !important; border-radius: 8px !important;
}
.stImage { border-radius: 10px; overflow: hidden; }
.stImage img { border-radius: 10px; }
.stSpinner { color: var(--green-bright) !important; }
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--bg-dark); }
::-webkit-scrollbar-thumb { background: rgba(57,211,83,0.2); border-radius: 3px; }
</style>
"""
