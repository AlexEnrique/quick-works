import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav  # read .wav file type
from scipy.signal import wiener      # wiener filter

# ========================================================
# numpy.fft.rfft:  Discrete Fourier transform of a
#                   real sequence.
# numpy.fft.ifft:  Return discrete inverse Fourier
#                   transform of real or complex sequence.
# ========================================================

def apply_filter(channels):
    filtered_channels = []
    for channel in channels:
        filtered_channels.append( wiener(channel) )

    return filtered_channels

def main():
    # $$ READING THE DATA $$
    print("Reading the .wav file...")
    fs, data = wav.read("11.wav") # WARNING: Change the file name
                                  # fs is the frequency rate.
                                  # data is a matrix in which each column is an
                                  # input channel. Each element in a column is
                                  # the sound amplitude at some specific time;
                                  # the associated time is in the same position
                                  # of the "time" array defined below.

    # Separating channels: channels[j] == jth channel
    channels = data.transpose()

    # $$ APPLYING WIENER FILTER $$
    print("Applying Wiener Filter to each channel... (It will take some time)")

    filtered_channels = wiener(channels)

    print("") # new line print
    # $$ FILTERED DATA TO AUDIO $$
    print("Creating filtered audio file...")

    data = np.array(filtered_channels).transpose()
    wav.write("new-11.wav", fs, data)

    # $$ ENDING main() $$
    print("Done!")
    print("A new .wav file was created in the current directory")


if __name__ == "__main__":
    main()
