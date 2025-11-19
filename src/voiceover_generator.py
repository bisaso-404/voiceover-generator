import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

def generate_voice(text, output_path):
    """Generate MP3 voice using Gemini 2.0 Flash TTS."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    model = genai.GenerativeModel(
        'gemini-2.0-flash-exp',
        generation_config={
            "response_modalities": ["AUDIO"],
        }
    )
    
    response = model.generate_content(text)
    
    # Extract and save audio
    audio_data = response.candidates[0].content.parts[0].inline_data.data
    with open(output_path, 'wb') as f:
        f.write(audio_data)
    
    return output_path