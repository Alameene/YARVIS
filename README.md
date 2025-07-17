# Y.A.R.V.I.S. – Your Autonomous Recognizer and Virtual Intelligent System

This is a voice-enabled AI chatbot powered by DeepSeek, Flask, and gTTS.

## Features
- Uses DeepSeek Chat API (free)
- Speaks responses using gTTS
- Ready to deploy on Render

## How to Deploy

1. Upload to GitHub
2. Go to [https://render.com](https://render.com) → Create New Web Service
3. Connect your GitHub repo
4. Set Environment Variable:
   - `DEEPSEEK_API_KEY = your_deepseek_api_key`
5. Set:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`

The app will be live in a few minutes!

---
Created by **AIMEES WD**
