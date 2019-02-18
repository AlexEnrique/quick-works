'''------------------------------------
LOGIC:
[1] load file
[2] reduce noise
[3] trim silence
[4] output file
------------------------------------'''

if __name__ == "__main__":
    numfiles = 16
    samples  = [str(n)+'.wav' for n in range(1, numfiles + 1)]

    for s in samples:
        # reading a file
        filename = s
        y, sr = read_file(filename)

        # reducing noise using db power
        y_reduced_power = reduce_noise_power(y, sr)

        # trimming silences
        y_reduced_power, time_trimmed = trim_silence(y_reduced_power)

        output_directory = '03_flight_reduced/'
        output_file(output_directory ,filename, y_reduced_power, sr, '_filtered')

        print("Done for file " + s)
