# EvaCRATE Portable Dashboard

This folder contains a **standalone HTML version** of the EvaCRATE dashboard that automatically detects your environment and connects to the correct backend API.

## ✨ Key Features

- **Smart API Detection**: Automatically uses localhost for local testing, Render for production
- **No Build Process**: Single HTML file — just open and go
- **GitHub Pages Compatible**: Works perfectly when hosted on GitHub Pages + Render backend
- **Fully Functional**: All features from main dashboard included

## 🚀 How to Use

### Local Development
1. Keep Flask backend running: `python app.py`
2. Open `index.html` in browser
3. Dashboard automatically connects to `http://localhost:5000`

### GitHub Pages + Render Deployment

#### Step 1: Deploy Flask Backend to Render
```bash
# Go to https://render.com
# Sign in with GitHub
# Create new Web Service
# Select EvaCRATE GitHub repo
# Use render.yaml for configuration
# Wait 2-3 minutes for deployment
# Note your backend URL (e.g., https://evacrate-backend.onrender.com)
```

#### Step 2: Update API URL (if not using onrender.com)
If your Render URL is different, edit line 238 in `index.html`:
```javascript
return 'https://your-backend-url.onrender.com'; // Replace with your URL
```

#### Step 3: Deploy to GitHub Pages
```bash
# Create gh-pages branch
git checkout -b gh-pages

# Commit this docs folder content
git add -A
git commit -m 'Add portable dashboard for GitHub Pages'

# Force push to gh-pages
git push -u origin gh-pages --force
```

#### Step 4: Enable GitHub Pages
- Go to GitHub repo Settings > Pages
- Select `gh-pages` branch as source
- Your dashboard is live at: `https://username.github.io/EvaCRATE/`

## 🔧 API URL Resolution

The dashboard uses this logic to detect the backend:

```javascript
if (localhost or 127.0.0.1)
  → Use http://localhost:5000
else
  → Use https://evacrate-backend.onrender.com
```

**You don't need to change anything** — it auto-detects!

## 📊 Testing

1. **Local Test**
   - Run: `python app.py`
   - Open: `local/index.html`
   - Should see "Connected to EvaCRATE backend"

2. **Production Test**
   - Visit: `https://username.github.io/EvaCRATE/docs/`
   - Should connect to Render backend
   - Full crop risk detection available

## 🐛 Troubleshooting

### "Cannot connect to backend" Error
- **Locally**: Ensure Flask is running on port 5000
- **GitHub Pages**: Verify Render deployment completed and backend is live
- **CORS**: Flask app has CORS enabled — should work from any origin

### Buttons Don't Work
- Check browser console (F12 → Console)
- Verify API_BASE URL is correct
- Ensure JSON requests are valid

### Render URL Change
1. Open `index.html` in text editor
2. Find line 238: `return 'https://evacrate-backend.onrender.com';`
3. Replace with your new Render URL
4. Save and redeploy to GitHub Pages

## 📱 Mobile Testing

Works great on mobile! The responsive design adapts to all screen sizes.

## 🎯 Quick Links

- **Main Dashboard**: [Main index.html](../templates/index.html)
- **Flask Backend**: [app.py](../app.py)
- **Deployment Guide**: [DEPLOYMENT.md](../DEPLOYMENT.md)
- **Requirements**: [requirements.txt](../requirements.txt)

---

**Created for EvaCRATE Smart Crop Storage Monitor**
