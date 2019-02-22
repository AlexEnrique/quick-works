import soundfile
import librosa
from pysndfx import AudioEffectsChain
import numpy as np
import math
import python_speech_features
import scipy as sp
from scipy import signal

from scipy.io import wavfile as wav

# http://python-speech-features.readthedocs.io/en/latest/
# https://github.com/jameslyons/python_speech_features
# http://practicalcryptography.com/miscellaneous/machine-learning/guide-mel-frequency-cepstral-coefficients-mfccs/#deltas-and-delta-deltas


# http://dsp.stackexchange.com/search?q=noise+reduction/

'''------------------------------------
FILE READER:
    receives filename,
    returns audio time series (y) and sampling rate of y (sr)
------------------------------------'''
def read_file(filepath):
    # getting sampling rate (int) and audio time series of the 8 channels
    data, samplerate = soundfile.read(filepath)

    # separing the channels
    channels = []
    for i in range(len(data.transpose())): #data.transpose()[i] == channel i (base 0)
        file = 'temp/'+str(i)+'.wav'

        soundfile.write(file, data.transpose()[i], samplerate)
        channel, _ = librosa.core.load(file)
        channels.append(channel.tolist())

    channels = np.array(channels)
    return channels, samplerate

'''------------------------------------
NOISE REDUCTION USING POWER:
    receives an audio matrix,
    returns the matrix after gain reduction on noise
------------------------------------'''
def reduce_noise_power(channels, sr):
    y_clean = []
    for channel in channels:
        y = np.array(channel.tolist(), dtype='float32')
        cent = librosa.feature.spectral_centroid(y=y, sr=sr)

        threshold_h = round(np.median(cent))*1.5
        threshold_l = round(np.median(cent))*0.1

        less_noise = AudioEffectsChain().lowshelf(gain=-30.0, frequency=threshold_l, slope=0.8).highshelf(gain=-12.0, frequency=threshold_h, slope=0.5)
        y_clean.append(less_noise(y).tolist()) # tolist() to remove the 'dtype'

    return np.array(y_clean)


def deepcopy(bigger):
    aux = [[] for i in range(len(bigger))]
    i = 0
    for arr in bigger:
        for e in arr:
            aux[i].append(e)
        i += 1

    return np.array(aux, dtype='float32')

'''------------------------------------
SILENCE TRIMMER:
    receives an audio matrix,
    returns an audio matrix with less silence and the amout of time that was trimmed
------------------------------------'''
def trim_silence(channels):
    aux = []
    for y in channels:
        y_trimmed, _ = librosa.effects.trim(y, top_db=20, frame_length=2, hop_length=500)
        trimmed_length = librosa.get_duration(y) - librosa.get_duration(y_trimmed)
        aux.append(y_trimmed)

    trimmed = deepcopy(aux)
    return trimmed, trimmed_length

'''------------------------------------
OUTPUT GENERATOR:
    receives a destination path, file name, audio matrix, and sample rate,
    generates a wav file based on input
------------------------------------'''
def output_file(destination, filepath, y_reduced, samplerate, ext=""):
    # extract the file name from the file path
    pos = -1
    for i in range(len(filepath)):
        if filepath[i] == '/': pos = i

    filename = filepath[pos:] if pos != -1 else filepath

    destination = destination + filename[:-4] + ext + '.wav'
    soundfile.write(destination, y_reduced.transpose(), samplerate)
    # print(np.array(y_reduced.transpose().tolist()))

    # librosa.output.write_wav(destination, y, sr)
    # wav.write(destination, samplerate, data)
