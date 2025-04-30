from pydub import AudioSegment
import speech_recognition as sr
import os


def transcribe_audio(audio_route):
    # Convertimos MP3 a WAV
    os.makedirs("temp", exist_ok=True)
    audio = AudioSegment.from_file(audio_route)
    audio.export("temp/temporal.wav", format="wav")

    recognizer = sr.Recognizer()
    with sr.AudioFile("temp/temporal.wav") as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data, language="es-ES")
        return text
    except sr.UnknownValueError:
        return "No se entendió el audio."
    except sr.RequestError as e:
        return f"Error de conexión: {e}"

def save_transcription(text, base_name="transcription", base_route="output"):
    os.makedirs("output", exist_ok=True)
    save_route = f"{base_route}/{base_name}.txt"
    with open(save_route, "w", encoding="utf-8") as file:
        file.write(text)
    print(f"\n✅ Transcripción guardada en: {save_route}")

if __name__ == "__main__":
    audio_route = "audio/audio.mp3"
    result = transcribe_audio(audio_route)
    print("\nTranscripción:\n", result)
    save_transcription(result)
