import subprocess
import os

import constants as c

mlv_path = c.MLV

def run_mlv(input_files, output_path, starting_frame, end_frame):
    """ Uses the mlv_dump command line tool from magic Lantern to 
    convert mlv videos into a DNG sequence"""
    
    file_name = os.path.splitext(os.path.basename(input_files))[0]
    
    full_output_path = os.path.join(output_path, file_name)
    
    if not os.path.exists(full_output_path):
        os.makedirs(full_output_path)
    
    
    cmd = mlv_path
    cmd += ' --dng -o '
    cmd += os.path.join(full_output_path, file_name + "_." )
    cmd += ' -v -f {}-{} '.format(str(starting_frame), str(end_frame))
    cmd += input_files 
    
    subprocess.run(cmd, shell=True)
    
    
    

if __name__ == "__main__":
    mlv_file = os.path.expanduser("~/Documents/MLV_app/testVideos/M05-1826.MLV")
    output_path = os.path.expanduser("~/Documents/MLV_app/testVideosOutput/")
    
    if os.path.isfile(mlv_file):
        run_mlv(mlv_file, output_path, 1, 30)
        