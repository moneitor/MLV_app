import os
import numpy as np
import imageio
import rawpy as raw
import matplotlib.pyplot as plt
import cv2 as cv
import OpenEXR
import array
from process_raw import DngFile

imageio.plugins.freeimage.download()


path_to_dng = "./example_dng.dng"
path_to_exr = "./example_exr.exr"

def convert(dng, exr):
    os.environ["OPENCV_IO_ENABLE_OPENEXR"]="1"
    
    name = os.path.splitext(os.path.basename(dng))[0]
    
    
    original = DngFile.read(dng)
    img = original.postprocess(no_auto_bright=True, gamma=(1,4.5))  
      
    #img = img[:,:,::-1] 
    
    original_cast_32 = np.float32(img)
    original_cast_32 = original_cast_32/255.0
    
    arR = original_cast_32[:,:,0].astype(np.float32).tobytes()
    arG = original_cast_32[:,:,1].astype(np.float32).tobytes()
    arB = original_cast_32[:,:,2].astype(np.float32).tobytes()
    
 
    output_path = "./convertedCV2.exr" 

       
    if os.path.isfile(output_path):
        os.remove(output_path)        
    
    #exr = OpenEXR.OutputFile("fromOPENEXR.exr", OpenEXR.Header(img.shape[1],img.shape[0]))
    #exr.writePixels({'R': arR, 'G': arG, 'G': arB})
    #exr.close()
    
    cv.imwrite(output_path, original_cast_32)
    




if __name__ == "__main__":

    if os.path.isfile(path_to_exr):
        convert(path_to_dng, path_to_exr)
        #imageio.show_formats()
