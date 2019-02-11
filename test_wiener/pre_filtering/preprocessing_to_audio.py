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

    filtered_channels = []
    count = 1
    for channel in channels:
        filtered_channels.append( wiener( np.fft.rfft(channel) ) )
        print("Done for channel %d/8!" % count)
        count += 1

    print("") # new line print
    # $$ PLOTING THE NEW DATA
    print("Creating filtered audio file...")

    for i in range(len(filtered_channels)):
        filtered_channels[i] = np.abs( np.fft.ifft( filtered_channels[i] ) )

    filtered_channels = np.array(filtered_channels)
    data = filtered_channels.transpose()
    print(data)
    print(len(data))
    print(len(data[0]))
    print(data[0])
    print(data[1])
    wav.write("new-11.wav", fs, data)

    # $$ ENDING main() $$
    print("Done!")
    print("A new .wav file was created in the current directory")


if __name__ == "__main__":
    main()
