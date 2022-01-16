import subprocess
import os

import constants as c


mlv_path = c.MLV

def run_mlv(input_files, output_path, starting_frame, end_frame, mode):
    """ Uses the mlv_dump command line tool from magic Lantern to 
    convert mlv videos into a DNG sequence"""    
    
    for input_file in input_files:
        file_name = os.path.splitext(os.path.basename(input_file))[0]
        
        full_output_path_dng = os.path.join(output_path, file_name + "_OUT")              
        
        if not os.path.exists(full_output_path_dng):
            os.makedirs(full_output_path_dng)            

        cmd_dng = mlv_path     
        cmd_dng += ' --dng -b 10 -o '
        cmd_dng += os.path.join(full_output_path_dng, file_name + "_dng." )       
        cmd_dng += ' -v -f {}-{} '.format(str(starting_frame), str(end_frame))
        cmd_dng += input_file             
        
        cmd_raw = mlv_path
        cmd_raw += ' -r -o '
        cmd_raw += os.path.join(full_output_path_dng, file_name + "_.raw" ) 
        cmd_raw += ' -v -f {}-{} '.format(str(starting_frame), str(end_frame))
        cmd_raw += ' '
        cmd_raw += input_file        
        
        if mode == 0:
            subprocess.run(cmd_dng, shell=True)
        if mode == 1:
            subprocess.run(cmd_raw, shell=True)
        
       
    
if __name__ == "__main__":
    mlv_file = os.path.expanduser("~/Documents/MLV_app/testVideos/M05-1826.MLV")
    output_path = os.path.expanduser("~/Documents/MLV_app/testVideosOutput/")
    
    if os.path.isfile(mlv_file):
        run_mlv(mlv_file, output_path, 1, 30, 0)
        