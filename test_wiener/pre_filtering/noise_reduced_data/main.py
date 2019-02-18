'''------------------------------------
LOGIC:
[1] load file
[2] reduce noise
[3] trim silence
[4] output file
------------------------------------'''

if __name__ == "__main__":
    file_samples_names = input()
    file = open(file_samples_names, 'r')

    '''
    - file_samples_names must be a file containing the name of files to
    filter separed in each line (to use readlines()).
    - For convention, the first line of the file must be the output_directory
    path.
    '''
    samples = file.readlines()
    output_directory = samples[0]
    samples.pop(0)

    for s in samples:
        # reading a file
        filename = s
        y, sr = read_file(filename)

        # reducing noise using db power
        y_reduced_power = reduce_noise_power(y, sr)

        # trimming silences
        y_reduced_power, time_trimmed = trim_silence(y_reduced_power)

        output_file(output_directory ,filename, y_reduced_power, sr, '_filtered')
        print("Done for file " + s)
