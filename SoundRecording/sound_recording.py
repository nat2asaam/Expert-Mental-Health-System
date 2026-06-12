import sounddevice as sd
from scipy.io import wavfile
def record_sound():
    fps = 44100  # Sample rate
    seconds = 5  # Duration
    print("Recording...")
    # Records raw audio data as a NumPy array
    my_recording = sd.rec(int(seconds * fps), samplerate=fps, channels=2)
    sd.wait()  # Wait until the recording is finished
    print("Done!")
    # Save as WAV file
    wavfile.write('output.wav', fps, my_recording)
