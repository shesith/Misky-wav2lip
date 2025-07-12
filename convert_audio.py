import librosa
import soundfile as sf

input_audio_path = "inputs/Misky_voice.mp3"
output_audio_path = "inputs/input_audio.wav"

audio, sr = librosa.load(input_audio_path, sr=None)
sf.write(output_audio_path, audio, sr, format='wav')

print("✅ Audio convertido a WAV correctamente")
