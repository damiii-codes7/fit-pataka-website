import streamlit as st
import streamlit.components.v1 as components

# ─────────────────────────────────────────────────────────
# CONFIG — edit these to update the whole site
# ─────────────────────────────────────────────────────────
BRAND_NAME = "FIT PATAKA"
HERO_LINE_1 = "Building a body where"
HERO_LINE_2 = "strength, confidence & health are the norm."
FOLLOWERS = "34K+"
INSTAGRAM_URL = "https://www.instagram.com/fit.pataka/"
YOUTUBE_URL = "https://www.youtube.com/@FITPATAKA-ns95"  # update with her real channel URL
CALENDLY_URL = "https://calendly.com/fitpataka/consultation"  # replace with her real Calendly link
PAYMENT_LINK = "https://razorpay.me/@fitpataka"  # replace with her real payment link
WHATSAPP_NUMBER = "917338806821"  # replace with her number, no + or spaces

HERO_IMAGE = "https://images.unsplash.com/photo-1518611012118-696072aa579a?q=80&w=1600"
ABOUT_IMAGE = "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?q=80&w=900"

SERVICES = [
    {
        "title": "Weight Loss Coaching",
        "tag": "1:1 PROGRAM",
        "desc": "Personalized nutrition + training for sustainable fat loss, with weekly check-ins.",
        "price": "₹4,999 / month",
        "image": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?q=80&w=800",
    },
    {
        "title": "Weight Gain & Strength",
        "tag": "1:1 PROGRAM",
        "desc": "Structured plans for healthy weight gain and strength building, built for your body type.",
        "price": "₹4,999 / month",
        "image": "https://images.unsplash.com/photo-1517836357463-d25dfeac3438?q=80&w=800",
    },
    {
        "title": "Group Transformation",
        "tag": "8-WEEK PROGRAM",
        "desc": "Community coaching with live check-ins and a shared meal + workout framework.",
        "price": "₹2,499 / person",
        "image": "https://images.unsplash.com/photo-1518611012118-696072aa579a?q=80&w=800",
    },
    {
        "title": "Diet Plan Only",
        "tag": "SELF-GUIDED",
        "desc": "A custom macro-based diet plan without ongoing coaching — for those who already train.",
        "price": "₹1,499 one-time",
        "image": "https://images.unsplash.com/photo-1490645935967-10de6ba17061?q=80&w=800",
    },
]

TESTIMONIALS = [
    {"stat": "8", "unit": "kg lost", "quote": "Lost it in 3 months without crash dieting. Actually sustainable."},
    {"stat": "12", "unit": "kg gained", "quote": "First time gaining weight the healthy way instead of just eating junk."},
    {"stat": "16", "unit": "weeks", "quote": "The check-ins kept me accountable — best money I've spent on myself."},
]

YOUTUBE_VIDEO_IDS = [
    # Add real YouTube video IDs here (the part after v= in the URL)
    "dQw4w9WgXcQ",
]

# ─────────────────────────────────────────────────────────
# PAGE SETUP
# ─────────────────────────────────────────────────────────
st.set_page_config(
    page_title=BRAND_NAME,
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

        .stApp { background-color: #000000; }
        .block-container {padding-top: 2.5rem; padding-bottom: 4rem; max-width: 1180px;}

        /* ---- Hero ---- */
        .hero-wrap {
            text-align: center;
            padding: 2rem 0 1rem 0;
        }
        .hero-eyebrow {
            font-size: 0.8rem;
            letter-spacing: 3px;
            text-transform: uppercase;
            color: #FFFFFF66;
            font-weight: 600;
            margin-bottom: 14px;
        }
        .hero-title {
            font-size: clamp(2.4rem, 6vw, 4.4rem);
            font-weight: 700;
            line-height: 1.05;
            letter-spacing: -2px;
            background: linear-gradient(101deg, #FFF 0%, rgba(255,255,255,0.55) 100%);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 0 auto;
            max-width: 900px;
        }
        .hero-sub {
            color: #FFFFFF99;
            font-size: 1.05rem;
            font-weight: 300;
            max-width: 560px;
            margin: 22px auto 0 auto;
        }

        /* ---- Pill buttons ---- */
        .pill-btn {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 12px 26px;
            border-radius: 999px;
            border: 1px solid #FFFFFF3D;
            background: linear-gradient(180deg, #FFFFFF14 0%, #FFFFFF00 100%);
            backdrop-filter: blur(6px);
            color: #fff !important;
            font-size: 0.9rem;
            font-weight: 500;
            text-decoration: none !important;
            transition: border-color 0.2s ease;
        }
        .pill-btn:hover { border-color: #FFFFFF8A; }
        .pill-btn-solid {
            background: #FFFFFF;
            color: #000 !important;
            border: none;
            font-weight: 600;
        }
        .pill-row { display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; margin-top: 28px; }

        /* ---- Stats strip ---- */
        .stats-strip {
            display: flex;
            justify-content: center;
            gap: 60px;
            flex-wrap: wrap;
            margin: 56px 0 8px 0;
            padding: 28px 0;
            border-top: 1px solid #FFFFFF14;
            border-bottom: 1px solid #FFFFFF14;
        }
        .stat-num {
            font-size: 2.2rem;
            font-weight: 700;
            color: #fff;
            letter-spacing: -1px;
        }
        .stat-label {
            font-size: 0.78rem;
            color: #FFFFFF66;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            margin-top: 2px;
        }

        /* ---- Section headers ---- */
        .eyebrow {
            font-size: 0.78rem;
            letter-spacing: 3px;
            text-transform: uppercase;
            color: #FFFFFF66;
            font-weight: 600;
            margin-top: 70px;
            margin-bottom: 6px;
        }
        .section-title {
            font-size: clamp(1.8rem, 3.5vw, 2.6rem);
            font-weight: 600;
            letter-spacing: -1px;
            color: #FFFFFFCC;
            margin-bottom: 24px;
        }

        /* ---- Rounded image cards (ecosystem style) ---- */
        .img-card {
            position: relative;
            border-radius: 24px;
            overflow: hidden;
            border: 1px solid #343839;
            height: 380px;
            background-size: cover;
            background-position: center;
            display: flex;
            align-items: flex-end;
            padding: 24px;
        }
        .img-card::before {
            content: "";
            position: absolute; inset: 0;
            background: linear-gradient(180deg, rgba(0,0,0,0) 30%, rgba(0,0,0,0.85) 100%);
        }
        .img-card-content { position: relative; z-index: 2; width: 100%; }
        .img-card-tag {
            font-size: 0.68rem;
            letter-spacing: 2px;
            text-transform: uppercase;
            color: #FFFFFFB3;
            font-weight: 600;
            margin-bottom: 8px;
        }
        .img-card-title {
            font-size: 1.5rem;
            font-weight: 700;
            color: #fff;
            margin-bottom: 6px;
            letter-spacing: -0.5px;
        }
        .img-card-desc {
            font-size: 0.85rem;
            color: #FFFFFFCC;
            margin-bottom: 12px;
            line-height: 1.4;
        }
        .img-card-price {
            font-size: 0.95rem;
            font-weight: 700;
            color: #fff;
        }

        /* ---- Testimonial cards ---- */
        .test-card {
            border-radius: 20px;
            border: 1px solid #FFFFFF1A;
            background: #0A0A0A;
            padding: 26px;
            height: 100%;
        }
        .test-stat { font-size: 2.4rem; font-weight: 700; color: #fff; letter-spacing: -1px; }
        .test-unit { font-size: 0.95rem; color: #FFFFFF80; margin-left: 4px; }
        .test-quote { color: #FFFFFFB3; font-size: 0.92rem; margin-top: 14px; line-height: 1.5; }

        /* ---- About ---- */
        .about-img {
            border-radius: 24px;
            border: 1px solid #343839;
            overflow: hidden;
        }
        .about-text {
            color: #FFFFFFB3;
            font-size: 1rem;
            line-height: 1.7;
        }
        .about-text b { color: #fff; }

        /* ---- Footer ---- */
        .footer-wrap {
            margin-top: 90px;
            padding-top: 30px;
            border-top: 1px solid #FFFFFF14;
            text-align: center;
            color: #FFFFFF66;
            font-size: 0.85rem;
        }

        a { color: inherit; }
        iframe { border-radius: 20px; border: 1px solid #FFFFFF1A !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────────────────
# HERO
# ─────────────────────────────────────────────────────────
st.markdown(
    f"""
    <div class="hero-wrap">
        <div class="hero-eyebrow">{BRAND_NAME} · WOMEN'S FITNESS COACHING</div>
        <div class="hero-title">{HERO_LINE_1}<br>{HERO_LINE_2}</div>
        <div class="hero-sub">
            Personalized weight loss & weight gain coaching for women — real results,
            no crash diets, no guesswork.
        </div>
        <div class="pill-row">
            <a class="pill-btn pill-btn-solid" href="#book">Book a Free Consultation</a>
            <a class="pill-btn" href="{INSTAGRAM_URL}" target="_blank">📸 Instagram</a>
            <a class="pill-btn" href="{YOUTUBE_URL}" target="_blank">▶️ YouTube</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="img-card" style="height: 440px; background-image: url('{HERO_IMAGE}');">
        <div class="img-card-content">
            <div class="img-card-tag">WOMEN'S HEALTH · WEIGHT LOSS · WEIGHT GAIN</div>
            <div class="img-card-title" style="font-size: 1.9rem;">Real transformations, built to last</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────────────────
# STATS STRIP
# ─────────────────────────────────────────────────────────
st.markdown(
    f"""
    <div class="stats-strip">
        <div style="text-align:center;">
            <div class="stat-num">{FOLLOWERS}</div>
            <div class="stat-label">Instagram Community</div>
        </div>
        <div style="text-align:center;">
            <div class="stat-num">100%</div>
            <div class="stat-label">Focused on Women</div>
        </div>
        <div style="text-align:center;">
            <div class="stat-num">1:1</div>
            <div class="stat-label">Personalized Coaching</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────────────────
# ABOUT
# ─────────────────────────────────────────────────────────
st.markdown('<div class="eyebrow">THE COACH</div><div class="section-title">About Me</div>', unsafe_allow_html=True)
about_col1, about_col2 = st.columns([1, 1.4])
with about_col1:
    st.markdown(f'<div class="about-img"><img src="{ABOUT_IMAGE}" style="width:100%; display:block;"></div>', unsafe_allow_html=True)
with about_col2:
    st.markdown(
        """
        <div class="about-text">
        Hey, I'm the face behind <b>Fit Pataka</b> 👋 — I help women lose and gain weight
        the right way, without crash diets or unsustainable routines.
        <br><br>
        Over the last few years I've built a community of <b>34,000+ women</b> on Instagram
        who are learning that fitness isn't about punishment — it's about consistency,
        the right nutrition, and training that fits your life.
        <br><br>
        My focus is 100% on women's health: weight loss, healthy weight gain, and
        building habits that actually stick.
        </div>
        """,
        unsafe_allow_html=True,
    )

# ─────────────────────────────────────────────────────────
# VIDEOS
# ─────────────────────────────────────────────────────────
st.markdown('<div class="eyebrow">ON YOUTUBE</div><div class="section-title">Videos</div>', unsafe_allow_html=True)
if YOUTUBE_VIDEO_IDS:
    video_cols = st.columns(len(YOUTUBE_VIDEO_IDS))
    for col, vid in zip(video_cols, YOUTUBE_VIDEO_IDS):
        with col:
            st.video(f"https://www.youtube.com/watch?v={vid}")
st.markdown(f'<a class="pill-btn" href="{YOUTUBE_URL}" target="_blank">See more on YouTube →</a>', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────
# SERVICES
# ─────────────────────────────────────────────────────────
st.markdown('<div class="eyebrow">WORK WITH ME</div><div class="section-title">Services</div>', unsafe_allow_html=True)
service_cols = st.columns(2)
for i, service in enumerate(SERVICES):
    with service_cols[i % 2]:
        st.markdown(
            f"""
            <div class="img-card" style="background-image: url('{service['image']}'); margin-bottom: 24px;">
                <div class="img-card-content">
                    <div class="img-card-tag">{service['tag']}</div>
                    <div class="img-card-title">{service['title']}</div>
                    <div class="img-card-desc">{service['desc']}</div>
                    <div class="img-card-price">{service['price']}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown(
    f'<div style="text-align:center; margin-top: 10px;">'
    f'<a class="pill-btn pill-btn-solid" href="{PAYMENT_LINK}" target="_blank">💳 Pay & Book a Service</a>'
    f"</div>",
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────────────────
# TESTIMONIALS
# ─────────────────────────────────────────────────────────
st.markdown('<div class="eyebrow">RESULTS</div><div class="section-title">Client Testimonials</div>', unsafe_allow_html=True)
test_cols = st.columns(len(TESTIMONIALS))
for col, t in zip(test_cols, TESTIMONIALS):
    with col:
        st.markdown(
            f"""
            <div class="test-card">
                <span class="test-stat">{t['stat']}</span><span class="test-unit">{t['unit']}</span>
                <div class="test-quote">"{t['quote']}"</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ─────────────────────────────────────────────────────────
# MINI CONSULTATION BOOKING (Calendly embed)
# ─────────────────────────────────────────────────────────
st.markdown('<div id="book"></div>', unsafe_allow_html=True)
st.markdown('<div class="eyebrow">GET STARTED</div><div class="section-title">Book a Free Mini Consultation</div>', unsafe_allow_html=True)
st.markdown(
    '<div style="color:#FFFFFF99; margin-bottom: 18px;">Pick a slot below for a free 15-minute call to talk about your goals and whether we\'re a good fit to work together.</div>',
    unsafe_allow_html=True,
)
components.iframe(CALENDLY_URL, height=650, scrolling=True)

# ─────────────────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────────────────
st.markdown(
    f"""
    <div class="footer-wrap">
        <div class="pill-row" style="margin-bottom: 18px;">
            <a class="pill-btn" href="{INSTAGRAM_URL}" target="_blank">📸 Instagram</a>
            <a class="pill-btn" href="{YOUTUBE_URL}" target="_blank">▶️ YouTube</a>
            <a class="pill-btn" href="https://wa.me/{WHATSAPP_NUMBER}" target="_blank">💬 WhatsApp</a>
        </div>
        © {BRAND_NAME} — Website built with Streamlit.
    </div>
    """,
    unsafe_allow_html=True,
)
