# Fit Pataka — Portfolio & Consultation Website

A single-page Streamlit site: intro, videos, services, testimonials, a Calendly
booking embed, and a payment link for consultations.

## 1. Before you deploy — edit these in `app.py`

At the top of the file, under `CONFIG`:

- `YOUTUBE_URL` — her real channel link
- `CALENDLY_URL` — her real Calendly booking page (see setup below)
- `PAYMENT_LINK` — her real payment link (see setup below)
- `WHATSAPP_NUMBER` — her WhatsApp number, digits only with country code (e.g. `919876543210`)
- `YOUTUBE_VIDEO_IDS` — list of real video IDs to embed (the part after `v=` in a YouTube URL)
- `SERVICES` — real service names, descriptions, prices
- `TESTIMONIALS` — real client quotes (get her permission first)
- `HERO_IMAGE` / `ABOUT_IMAGE` — swap the Unsplash placeholder URLs for her real photos
  (easiest: upload photos to the repo in an `/assets` folder and point to
  `"assets/hero.jpg"` instead of a URL)

## 2. Calendly

Already set — `CALENDLY_URL` points to her real page: `https://calendly.com/fitpataka`
It's a 30-minute consultation at ₹200, booked directly through Calendly (payment
is collected there if she's connected a payment method in Calendly, otherwise
via the site's separate `PAYMENT_LINK`).

## 3. Set up the payment link

Pick one depending on what she has access to:

- **Razorpay Payment Pages** (easiest in India, no code) — create a payment
  page at razorpay.me, copy the link into `PAYMENT_LINK`
- **Instamojo** — similar no-code payment link generator
- **UPI deep link** — for a simple "pay via UPI" button instead of a full
  gateway, use `upi://pay?pa=her-upi-id@bank&pn=FitPataka&cu=INR`

Either way, she'll need a bank account / KYC linked to actually receive funds
— that part happens on Razorpay/Instamojo's side, not in this code.

## 4. Push to GitHub (same flow as YK Legal)

```bash
git init
git add .
git commit -m "Initial Fit Pataka website"
git branch -M main
git remote add origin https://github.com/<your-username>/fit-pataka-website.git
git push -u origin main
```

## 5. Deploy on Streamlit Community Cloud

1. Go to share.streamlit.io and sign in with GitHub
2. Click "New app" → select the `fit-pataka-website` repo → branch `main` → file `app.py`
3. Deploy — you'll get a live URL like `fit-pataka.streamlit.app`
4. Put that link in her Instagram bio

## Running locally to preview changes first

```bash
pip install -r requirements.txt
streamlit run app.py
```
