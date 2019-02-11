import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav  # read .wav file type
from scipy.signal import wiener      # wiener filter

# ============================================
# rfft:  Discrete Fourier transform of a
#       real sequence.
# ifft:  Return discrete inverse Fourier
#       transform of real or complex sequence.
# ============================================

def main():
    # $$ READING THE DATA $$
    print("Reading the .wav file...")
    fs, data = wav.read("1.wav") # WARNING: Change the file name
                                  # fs is the frequency rate.
                                  # data is a matrix in which each column is an
                                  # input channel. Each element in a column is
                                  # the sound amplitude at some specific time;
                                  # the associated time is in the same position
                                  # of the "time" array defined below.

    print("Separating channels...")
    channels = [] # to separate each channel of the data matrix
    for i in range(len(data[0])):   # len(data[i]) is the number of channels
        channels.append(data[:, i]) # get colum 'i' of data; channel 'i'

    # $$ APPLYING WIENER FILTER $$
    print("Applying Wiener Filter to each channel...")

    filtered_channels = []
    for channel in channels:
        filtered_channels.append( wiener( np.fft.rfft(channel) ) )


    # $$ PLOTING THE NEW DATA
    print("Ploting filtered channels...")

    time = np.arange(len(data)) / fs # time array contains each sample time
                                     # time[-1] == duration

    for i in range(len(filtered_channels)):
        plt.subplot(8, 1, i+1) # the index must be 1 <= index <= 8, not 0
        plt.plot(time, np.abs( np.fft.ifft( filtered_channels[i] ) ))
        plt.grid()
        plt.ylabel('Ch. ' + str(i+1))

    plt.xlabel('time (s)')
    plt.show()

    # $$ ENDING main() $$
    print("Done!")


if __name__ == "__main__":
    main()
