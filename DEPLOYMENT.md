# EvaCRATE Deployment Guide

## Option 1: Full Stack on Render (Recommended for Quick Setup)

### Backend on Render:

1. Go to [https://render.com](https://render.com) and sign up with GitHub
2. Click **New +** → **Web Service**
3. Connect your GitHub repo `Amna-Sarfaraz/EvaCRATE`
4. Fill in:
   - **Name:** `evacrate-backend`
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Click **Create Web Service**
6. Wait for deployment (2-3 minutes)
7. Copy the deployed URL (e.g., `https://evacrate-backend.onrender.com`)

---

## Option 2: GitHub Pages (Frontend) + Render (Backend)

### Step 1: Deploy Backend

Follow the Render steps above.

### Step 2: Create GitHub Pages Branch

```bash
cd c:\Users\HP\Downloads\EvaCRATE_local

# Create a new branch for GitHub Pages
git checkout --orphan gh-pages

# Remove all files from this branch
git rm -rf .

# Copy the index.html to root and update API URL
# (See instructions below)

git add index.html
git commit -m "GitHub Pages deployment"
git push origin gh-pages
```

### Step 3: Enable GitHub Pages

1. Go to GitHub repo settings
2. Scroll to **Pages** section
3. Select **Source:** `gh-pages` branch
4. Click **Save**
5. Your site will be live at: `https://amna-sarfaraz.github.io/EvaCRATE/`

---

## Option 3: Vercel (Fast & Free - Best for Production)

1. Go to [https://vercel.com](https://vercel.com)
2. Import your GitHub repo
3. Framework: **Python** (Flask)
4. Deploy 
5. Get your live URL instantly

---

## Quick Local Testing Before Deployment

```bash
# 1. Install production dependencies
pip install -r requirements.txt

# 2. Run locally
python app.py

# 3. Test in browser
http://localhost:5000
```

---

## Environment Variables for Production

If using Render, add these in the Environment variables section:
- `FLASK_ENV`: `production`
- `PYTHON_VERSION`: `3.11`

---

## Next Steps

1. Choose deployment option above
2. Push latest code: `git add . && git commit -m "Deploy" && git push`
3. Test in browser
4. Share your live link!

---

## Troubleshooting

**Cold start takes long?**
- Normal on free tier. Upgrade to paid for instant response.

**API calls failing?**
- Check CORS is enabled in app.py ✓
- Verify backend URL is correct in HTML

**Model not loading?**
- Ensure `crop_model.pkl` is committed to repo
- Check file size (large files may timeout on deploy)

