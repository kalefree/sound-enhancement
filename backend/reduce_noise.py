import librosa
import noisereduce as nr
from speechbrain.pretrained import SpectralMaskEnhancement


data_path  = "../../sounds/"
# Load audio file using Librosa
audio, rate = librosa.load('meditation-session-annaloes-geerling.wav', sr=None)

# Noise reduction using noisereduce
reduced_noise_audio = nr.reduce_noise(y=audio, sr=rate)

# Use a pre-trained AI model for further enhancement, e.g., SpectralMaskEnhancement
enhancer = SpectralMaskEnhancement.from_hparams(source="speechbrain/mtl-mimic-voicebank", savedir="tmpdir")
enhanced_audio = enhancer.enhance_batch(reduced_noise_audio, rate)

# Save enhanced audio
librosa.output.write_wav('enhanced_audio.wav', enhanced_audio, rate)
