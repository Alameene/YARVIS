gfrom flask import Flask, render_template, request, jsonify
from gtts import gTTS
import os
import uuid
from pathlib import Path
import openai

# API setup
openai.api_key = os.environ.get("DEEPSEEK_API_KEY")
openai.api_base = "https://api.deepseek.com/v1"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/audio_responses'
Path(app.config['UPLOAD_FOLDER']).mkdir(parents=True, exist_ok=True)

def generate_response(message):
    try:
        response = openai.ChatCompletion.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are YARVIS, a helpful and intelligent assistant."},
                {"role": "user", "content": message}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return "Sorry, YARVIS couldn't respond. Try again later."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    response_text = generate_response(user_message)

    # Generate voice
    audio_filename = f"{uuid.uuid4().hex}.mp3"
    audio_path = os.path.join(app.config['UPLOAD_FOLDER'], audio_filename)
    gTTS(response_text).save(audio_path)

    return jsonify(reply=response_text, audio_url=f'/static/audio_responses/{audio_filename}')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

