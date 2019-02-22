import sys
from noise import *

'''------------------------------------
LOGIC:
[1] load file
[2] reduce noise
[3] trim silence
[4] output file
------------------------------------'''

if __name__ == "__main__":
    instructions = '''
    - This script requires a text file passed via command line. That file must
    contains the paths to files which the filter will be applied, and the output
    path, where the filtered files will be saved.
    - For convention, the first line of the file must be the output directory
    path (ending with a '/').
    - To pass a text file, say file.txt, call the script as:
        'python3 main.py : file.txt'
    '''
    try:
        file = open(sys.argv[2], 'r') # sys.argv == [main.py, :, file.txt]
    except:
        print(instructions)

    # work on the files
    samples = file.readlines()
    output_directory = samples[0][:-1] # [:-1] remove the '\n' from the end
    samples.pop(0)

    for s in samples:
        # reading a file
        filepath = s[:-1] # [:-1] remove the '\n' from the end
        y, samplerate = read_file(filepath)

        # reducing noise using db power
        y_reduced_power = reduce_noise_power(y, samplerate)

        # trimming silences
        y_reduced_power, _ = trim_silence(y_reduced_power)
        # y_reduced_power = np.array(y_reduced_power.tolist())

        output_file(output_directory ,filepath, y_reduced_power, samplerate, '_filtered')
        print("Done for file " + filepath)
