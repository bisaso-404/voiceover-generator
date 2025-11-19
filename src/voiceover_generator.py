import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import wave

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def save_wav(filename: str, pcm: bytes, channels=1, rate=24000, sample_width=2):
    """Save PCM bytes as a playable WAV file."""
    os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)
    print(f"WAV file saved: {filename}")

def generate_voice(text: str, output_path: str):
    """
    Generate TTS from text and save as WAV.
    """
    # Generate audio
    response = client.models.generate_content(
        model="gemini-2.5-flash-preview-tts",
        contents=text,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name="Kore")
                )
            ),
        )
    )

    # Extract raw PCM bytes
    pcm = response.candidates[0].content.parts[0].inline_data.data

    # Save as WAV
    save_wav(output_path, pcm)

    return output_path
