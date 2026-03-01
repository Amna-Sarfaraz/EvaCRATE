# EvaCRATE — Local App

## Folder Structure
```
EvaCRATE_local/
├── app.py                  ← Flask server
├── crop_model.pkl          ← YOUR MODEL HERE (copy from Colab/training)
├── requirements.txt
├── README.md
└── templates/
    └── index.html          ← Farmer UI
```

## Setup & Run

### Step 1 — Copy your trained model
Copy `crop_model.pkl` into this folder (same folder as app.py).

### Step 2 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3 — Run the app
```bash
python app.py
```

### Step 4 — Open in browser
```
http://localhost:5000
```

## That's it.

- The app loads your `crop_model.pkl` directly
- Select crop + set days stored + click Detect
- Model predicts days to rot → shows Green/Yellow/Brown/Red
- Download or share the report

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `crop_model.pkl not found` | Copy the .pkl file into the same folder as app.py |
| `ModuleNotFoundError: flask` | Run `pip install flask` |
| `sklearn version mismatch` | Train and run with the same Python/sklearn version |
| Port 5000 in use | Change port in app.py: `app.run(port=5001)` |
