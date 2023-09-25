import pyaudio
import wave

# Set parameters for the audio stream
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100  # Sample rate (samples per second)
CHUNK = 1024  # Size of each audio chunk (frames per buffer)
RECORD_SECONDS =   5# Duration of recording in seconds
OUTPUT_FILENAME = "recorded_audio.wav"  # Name of the output file

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open an audio stream
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("Recording...")

frames = []
# Record audio in chunks and save it to frames
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Finished recording")

# Close the audio stream
stream.stop_stream()
stream.close()
audio.terminate()

# Save the recorded audio to a WAV file
with wave.open(OUTPUT_FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))

print(f"Audio saved to {OUTPUT_FILENAME}")
