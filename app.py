import streamlit as st
import streamlit.components.v1 as components

# ─────────────────────────────────────────────────────────
# CONFIG — edit these to update the whole site
# ─────────────────────────────────────────────────────────
BRAND_NAME = "FIT PATAKA"
HERO_LINE_1 = "Building a body where"
HERO_LINE_2 = "Strength, Confidence & Health are the norm."
FOLLOWERS = "35K+"
INSTAGRAM_URL = "https://www.instagram.com/fit.pataka/"
YOUTUBE_URL = "https://www.youtube.com/@fitpataka-ns95"
CALENDLY_URL = "https://calendly.com/fitpataka"  # her real Calendly link
PAYMENT_LINK = "https://razorpay.me/@sandhyabalaji"  # replace with her real payment link
WHATSAPP_NUMBER = "917338806821"

HERO_IMAGE = "https://raw.githubusercontent.com/damiii-codes7/fit-pataka-website/main/hero.jpg"
ABOUT_IMAGE = "https://raw.githubusercontent.com/damiii-codes7/fit-pataka-website/main/about.jpg"

SERVICES = [
    {
        "title": "Nutrition Only",
        "tag": "1 MONTH FROM",
        "desc": "Custom nutrition plan and macro guidance, no group classes or PT sessions.",
        "price": "₹5,000 / month",
    },
    {
        "title": "Fitness (Group Classes) Only",
        "tag": "1 MONTH FROM",
        "desc": "Live group fitness classes — no nutrition plan included.",
        "price": "₹4,000 / month",
    },
    {
        "title": "Nutrition + Fitness",
        "tag": "1 MONTH FROM",
        "desc": "Nutrition plan plus group fitness classes, the most popular combo.",
        "price": "₹8,000 / month",
    },
    {
        "title": "Personal Training Only",
        "tag": "1 MONTH FROM",
        "desc": "1:1 personal training sessions, no nutrition plan included.",
        "price": "₹10,000 / month",
    },
    {
        "title": "Personal Training + Nutrition",
        "tag": "1 MONTH FROM",
        "desc": "The full package — 1:1 training and a custom nutrition plan together.",
        "price": "₹15,000 / month",
    },
]

# Package pricing table — plan: {months: (price, savings)}
PACKAGE_PRICING = [
    {
        "name": "Nutrition Only",
        "1": ("₹5,000", None),
        "2": ("₹9,500", "save ₹500"),
        "3": ("₹13,500", "save ₹1,500"),
        "6": ("₹25,000", "save ₹5,000"),
    },
    {
        "name": "Fitness (Group Classes) Only",
        "1": ("₹4,000", None),
        "2": ("₹7,500", "save ₹500"),
        "3": ("₹10,500", "save ₹1,500"),
        "6": ("₹20,000", "save ₹4,000"),
    },
    {
        "name": "Nutrition + Fitness",
        "1": ("₹8,000", None),
        "2": ("₹15,000", "save ₹1,000"),
        "3": ("₹22,000", "save ₹2,000"),
        "6": ("₹42,000", "save ₹6,000"),
    },
    {
        "name": "Personal Training Only",
        "1": ("₹10,000", None),
        "2": ("₹18,500", "save ₹1,500"),
        "3": ("₹27,000", "save ₹3,000"),
        "6": ("₹52,000", "save ₹8,000"),
    },
    {
        "name": "Personal Training + Nutrition",
        "1": ("₹15,000", None),
        "2": ("₹28,000", "save ₹2,000"),
        "3": ("₹41,000", "save ₹4,000"),
        "6": ("₹78,000", "save ₹12,000"),
    },
]

# Add real YouTube video links here — thumbnails + embeds are pulled automatically
YOUTUBE_VIDEOS = [
    "https://youtu.be/Uw3py4sNgKY",
    "https://youtu.be/xO6vExuYEpg",
    "https://youtu.be/4rY6jifLF28",
]

# ─────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────
def get_youtube_id(url: str) -> str:
    if "watch?v=" in url:
        return url.split("watch?v=")[1].split("&")[0]
    if "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    return url

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
        html, body, [class*="css"] { font-family: Georgia, 'Times New Roman', serif; }

        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        .stApp { background-color: #D6182B; }
        .block-container {padding-top: 2.5rem; padding-bottom: 4rem; max-width: 1180px;}

        /* ---- Global center alignment ---- */
        .block-container, .about-text, .service-desc, .test-quote,
        .hero-sub, .section-title, .eyebrow, .white-card, table, th, td {
            text-align: center !important;
        }
        [data-testid="stVerticalBlock"], [data-testid="column"] { text-align: center; }
        [data-testid="stImage"] { display: flex; justify-content: center; }

        /* ---- Hero ---- */
        .hero-wrap { text-align: center; padding: 2rem 0 1rem 0; }
        .hero-eyebrow {
            font-size: 0.8rem; letter-spacing: 3px; text-transform: uppercase;
            color: #FFFFFFB3; font-weight: 600; margin-bottom: 14px;
        }
        .hero-title {
            font-size: clamp(2.4rem, 6vw, 4.4rem);
            font-weight: 700; line-height: 1.08; letter-spacing: -1px;
            color: #FFFFFF; margin: 0 auto; max-width: 900px;
        }
        .hero-sub {
            color: #FFFFFFDD; font-size: 1.05rem; font-weight: 300;
            max-width: 560px; margin: 22px auto 0 auto;
        }

        /* ---- Pill buttons ---- */
        .pill-btn {
            display: inline-flex; align-items: center; gap: 8px;
            padding: 12px 26px; border-radius: 999px;
            border: 1.5px solid #FFFFFF; background: transparent;
            color: #fff !important; font-size: 0.9rem; font-weight: 600;
            text-decoration: none !important; transition: all 0.2s ease;
        }
        .pill-btn:hover { background: #FFFFFF1A; }
        .pill-btn-solid { background: #FFFFFF; color: #D6182B !important; border: none; }
        .pill-row { display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; margin-top: 28px; }

        /* ---- Stats strip ---- */
        .stats-strip {
            display: flex; justify-content: center; gap: 60px; flex-wrap: wrap;
            margin: 56px 0 8px 0; padding: 28px 0;
            border-top: 1px solid #FFFFFF33; border-bottom: 1px solid #FFFFFF33;
        }
        .stat-num { font-size: 2.2rem; font-weight: 700; color: #fff; letter-spacing: -1px; }
        .stat-label { font-size: 0.78rem; color: #FFFFFFB3; text-transform: uppercase; letter-spacing: 1.5px; margin-top: 2px; }

        /* ---- Section headers ---- */
        .eyebrow {
            font-size: 0.78rem; letter-spacing: 3px; text-transform: uppercase;
            color: #FFFFFFB3; font-weight: 600; margin-top: 70px; margin-bottom: 6px;
        }
        .section-title {
            font-size: clamp(1.8rem, 3.5vw, 2.6rem); font-weight: 600;
            letter-spacing: -1px; color: #FFFFFF; margin-bottom: 24px;
        }

        /* ---- White cards (services, testimonials) ---- */
        .white-card {
            background: #FFFFFF; border-radius: 20px; padding: 24px;
            color: #1A1A1A;
        }
        .service-tag {
            font-size: 0.68rem; letter-spacing: 2px; text-transform: uppercase;
            color: #D6182B; font-weight: 700; margin-bottom: 8px;
        }
        .service-title { font-size: 1.35rem; font-weight: 700; color: #1A1A1A; margin-bottom: 6px; letter-spacing: -0.3px; }
        .service-desc { font-size: 0.88rem; color: #4A4A4A; margin-bottom: 14px; line-height: 1.45; }
        .service-price { font-size: 1rem; font-weight: 700; color: #D6182B; }

        .test-card { background: #FFFFFF; border-radius: 20px; padding: 26px; height: 100%; color: #1A1A1A; }
        .test-stat { font-size: 2.4rem; font-weight: 700; color: #D6182B; letter-spacing: -1px; }
        .test-unit { font-size: 0.95rem; color: #6A6A6A; margin-left: 4px; }
        .test-quote { color: #333333; font-size: 0.92rem; margin-top: 14px; line-height: 1.5; }

        /* ---- Photo cards (image-based) ---- */
        .img-card {
            position: relative; border-radius: 20px; overflow: hidden;
            height: 340px; background-size: cover; background-position: center;
            display: flex; align-items: flex-end; padding: 20px;
            border: 3px solid #FFFFFF;
        }
        .img-card::before {
            content: ""; position: absolute; inset: 0;
            background: linear-gradient(180deg, rgba(0,0,0,0) 40%, rgba(0,0,0,0.75) 100%);
        }
        .img-card-content { position: relative; z-index: 2; width: 100%; }
        .img-card-title { font-size: 1.2rem; font-weight: 700; color: #fff; }

        /* ---- YouTube thumbnails ---- */
        .yt-thumb-wrap {
            position: relative; border-radius: 16px; overflow: hidden;
            border: 3px solid #FFFFFF; display: block; text-decoration: none !important;
        }
        .yt-thumb-wrap img { width: 100%; display: block; }
        .yt-play-icon {
            position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
            width: 54px; height: 54px; border-radius: 50%;
            background: rgba(214, 24, 43, 0.9);
            display: flex; align-items: center; justify-content: center;
        }
        .yt-play-icon::after {
            content: ""; width: 0; height: 0;
            border-top: 10px solid transparent; border-bottom: 10px solid transparent;
            border-left: 16px solid #fff; margin-left: 4px;
        }

        /* ---- About ---- */
        .about-img { border-radius: 20px; overflow: hidden; border: 3px solid #FFFFFF; }
        .about-text { color: #FFFFFFEE; font-size: 1rem; line-height: 1.7; }
        .about-text b { color: #fff; }

        /* ---- Footer ---- */
        .footer-wrap {
            margin-top: 90px; padding-top: 30px; border-top: 1px solid #FFFFFF33;
            text-align: center; color: #FFFFFFB3; font-size: 0.85rem;
        }

        a { color: inherit; }
        iframe { border-radius: 16px; border: 3px solid #FFFFFF !important; }
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
            <a class="pill-btn pill-btn-solid" href="#book">Book a Consultation — ₹200/30min</a>
            <a class="pill-btn" href="{INSTAGRAM_URL}" target="_blank">Instagram</a>
            <a class="pill-btn" href="{YOUTUBE_URL}" target="_blank">YouTube</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="img-card" style="height: 420px; background-image: url('{HERO_IMAGE}');">
        <div class="img-card-content">
            <div class="img-card-title" style="font-size: 1.7rem;">Real transformations, built to last</div>
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
        Hey, I'm the face behind <b>Fit Pataka</b> 👋 — your girl-next-door fat loss coach.
        PCOS, bloating, belly fat — I fix the <i>why</i>, not just the weight. No starving here,
        food is love, not the enemy.
        <br><br>
        Over the last few years I've built a community of <b>34,000+ women</b> on Instagram and a
        Tamil-language YouTube channel — easy home workouts and nutrition tips, made simple for
        every woman, in the language you're most comfortable in.
        <br><br>
        This is a safe space for women done with crash diets and toxic fitness culture. Here,
        fitness is power, not punishment. Strength, not shrinking. Self-respect, not comparison.
        Busy, bloated, burnt out, or just beginning — you belong here.
        <br><br>
        My focus is 100% on women's health: weight loss, healthy weight gain, managing
        PCOS/thyroid/hormonal health, and building habits that actually stick — so you can feel
        confident in your own skin and stay strong at 60 and beyond.
        </div>
        """,
        unsafe_allow_html=True,
    )

# ─────────────────────────────────────────────────────────
# VIDEOS (thumbnail grid, click to open on YouTube)
# ─────────────────────────────────────────────────────────
st.markdown('<div class="eyebrow">ON YOUTUBE</div><div class="section-title">Videos</div>', unsafe_allow_html=True)
if YOUTUBE_VIDEOS:
    video_cols = st.columns(len(YOUTUBE_VIDEOS) if len(YOUTUBE_VIDEOS) <= 3 else 3)
    for i, video_url in enumerate(YOUTUBE_VIDEOS):
        vid = get_youtube_id(video_url)
        with video_cols[i % len(video_cols)]:
            st.markdown(
                f"""
                <a class="yt-thumb-wrap" href="{video_url}" target="_blank">
                    <img src="https://img.youtube.com/vi/{vid}/hqdefault.jpg">
                    <div class="yt-play-icon"></div>
                </a>
                """,
                unsafe_allow_html=True,
            )
st.markdown(f'<div style="margin-top:16px;"><a class="pill-btn" href="{YOUTUBE_URL}" target="_blank">See more on YouTube →</a></div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────
# SERVICES
# ─────────────────────────────────────────────────────────
st.markdown('<div class="eyebrow">WORKOUT WITH ME</div><div class="section-title">Services</div>', unsafe_allow_html=True)
def render_service_card(service):
    st.markdown(
        f"""
        <div class="white-card" style="margin-bottom: 20px;">
            <div class="service-tag">{service['tag']}</div>
            <div class="service-title">{service['title']}</div>
            <div class="service-desc">{service['desc']}</div>
            <div class="service-price">{service['price']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

pair_count = len(SERVICES) // 2
for row in range(pair_count):
    left, right = st.columns(2)
    with left:
        render_service_card(SERVICES[row * 2])
    with right:
        render_service_card(SERVICES[row * 2 + 1])

if len(SERVICES) % 2 == 1:
    _, center, _ = st.columns([1, 2, 1])
    with center:
        render_service_card(SERVICES[-1])

# ---- Package pricing table ----
st.markdown('<div class="eyebrow" style="margin-top:40px;">SAVE MORE</div><div class="section-title" style="font-size:1.6rem;">Package Pricing — the longer you commit, the more you save</div>', unsafe_allow_html=True)

table_rows = ""
for plan in PACKAGE_PRICING:
    cells = ""
    for month in ["1", "2", "3", "6"]:
        price, savings = plan[month]
        savings_html = f'<br><span style="color:#D6182B; font-size:0.72rem; font-weight:600;">{savings}</span>' if savings else ""
        cells += f'<td style="padding:14px 12px; text-align:center; color:#1A1A1A;">{price}{savings_html}</td>'
    table_rows += f'<tr style="border-bottom:1px solid #EEEEEE;"><td style="padding:14px 12px; font-weight:600; color:#1A1A1A;">{plan["name"]}</td>{cells}</tr>'

st.markdown(
    f"""
    <div class="white-card" style="padding: 8px; overflow-x:auto;">
        <table style="width:100%; border-collapse:collapse; font-size:0.85rem;">
            <thead>
                <tr style="background:#D6182B;">
                    <th style="padding:14px 12px; text-align:left; color:#fff; border-radius:12px 0 0 0;">PLAN</th>
                    <th style="padding:14px 12px; color:#fff;">1 MONTH</th>
                    <th style="padding:14px 12px; color:#fff;">2 MONTHS</th>
                    <th style="padding:14px 12px; color:#fff;">3 MONTHS</th>
                    <th style="padding:14px 12px; color:#fff; border-radius:0 12px 0 0;">6 MONTHS</th>
                </tr>
            </thead>
            <tbody>
                {table_rows}
            </tbody>
        </table>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f'<div style="text-align:center; margin-top: 24px;">'
    f'<a class="pill-btn pill-btn-solid" href="{PAYMENT_LINK}" target="_blank">Pay & Book a Plan</a>'
    f"</div>",
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────────────────
# MINI CONSULTATION BOOKING (Calendly embed)
# ─────────────────────────────────────────────────────────
st.markdown('<div id="book"></div>', unsafe_allow_html=True)
st.markdown('<div class="eyebrow">GET STARTED</div><div class="section-title">Book a Consultation</div>', unsafe_allow_html=True)
st.markdown(
'<div style="color:#FFFFFFDD; margin-bottom: 18px; text-align:center;">A 30-minute 1:1 call to talk through your goals — Pick a slot below.</div>',
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
            <a class="pill-btn" href="{INSTAGRAM_URL}" target="_blank">Instagram</a>
            <a class="pill-btn" href="{YOUTUBE_URL}" target="_blank">YouTube</a>
            <a class="pill-btn" href="https://wa.me/{WHATSAPP_NUMBER}" target="_blank">WhatsApp</a>
        </div>
        © {BRAND_NAME} — Built For Fitness and Nutrition with love and care.
    </div>
    """,
    unsafe_allow_html=True,
)
