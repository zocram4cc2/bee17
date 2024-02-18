import os

# Get which file we're joining and specify the base path
base_dir = '../data/'
bin = int(input("Binary file: "))
if(bin == 0):
    base_dir += 'match/'
elif(bin == 1):
    base_dir += 'player/'
elif(bin == 2):
    base_dir += 'team/'

# specify the directories
data_dir = base_dir + 'raw'
reconst_dir = base_dir + 'reconst'
output_dir = base_dir + 'output'

# create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# get the list of files
files = os.listdir(data_dir)

for f in files:
    data_file = os.path.join(data_dir, f)
    reconst_file = os.path.join(reconst_dir, f)
    output_file = os.path.join(output_dir, f)
    
    # check if corresponding file exists in reconst directory
    if os.path.isfile(data_file) and os.path.isfile(reconst_file):
        with open(data_file, 'r') as d, open(reconst_file, 'r') as r, open(output_file, 'w') as o:
            data_lines = d.readlines()
            reconst_lines = r.readlines()

            # iterate over each line
            for data_line, reconst_line in zip(data_lines, reconst_lines):
                # write combined line to output file
                o.write(f'{data_line.strip()} //{reconst_line}')

print("Files have been processed and written to the 'output' directory.")
