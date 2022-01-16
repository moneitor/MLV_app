# This tool converts DNG to EXR using the next command line tools
#~ dcraw (http://www.guillermoluijk.com/tutorial/dcraw/index_en.htm)
#~ imagemagick (https://www.lifewire.com/convert-linux-command-unix-command-4097060)

# install dcraw by
#    sudo apt-get update -y
#    sudo apt-get install -y dcraw

# install imagemagick by
#    sudo apt install imagemagick


import os
import subprocess


dng_file = '/home/hernan/Documents/DNG_TO_EXR/sample_images/exampleDNG_0001.dng'
folder_input = '/home/hernan/Documents/MLV_app/testVideos/M05-1826_OUT'
folder_output = '/home/hernan/Documents/MLV_app/testVideos/M05-1826_OUT/exampleDNG'


def return_dng_files(folder):
    folders = os.listdir(folder)
    
    return folders


def dng_to_exr(dng_path, output_folder):
    if os.path.isdir(output_folder):
        print ("Folder already exists.")
    else:
        os.makedirs(output_folder)
    
    if os.path.isfile(dng_path):
    
        file_name = os.path.splitext(os.path.basename(dng_path))[0] + ".exr"
        
        cmd = 'dcraw -c -w -H 0 -o 1 -4'
        cmd += ' {} '.format(dng_path)
        cmd += '| convert - -depth 16 {}'.format(os.path.join(output_folder, file_name))      
        

        subprocess.run(cmd, shell=True)    
        

def convert_all_dngs_to_exr(folder_input, folder_output):
    folders = return_dng_files(folder_input)
    for folder in folders:
        full_path = os.path.join(folder_input, folder)
        if os.path.isfile(full_path):
            print(full_path)
            dng_to_exr(full_path, folder_output)
            print("outputed file")
    
    
if __name__ == "__main__":
    convert_all_dngs_to_exr(folder_input, folder_output)
    #dng_to_exr(dng_file, folder_output)