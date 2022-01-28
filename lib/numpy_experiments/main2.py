import os
import numpy as np
import imageio
import rawpy as raw
import matplotlib.pyplot as plt
import cv2 as cv
import OpenEXR

imageio.plugins.freeimage.download()


path_to_dng = "./exampleDNG_0001.dng"
path_to_exr = "./CONVERTED_exr.exr"

def convert(dng, exr):
    os.environ["OPENCV_IO_ENABLE_OPENEXR"]="1"
    
    name = os.path.splitext(os.path.basename(dng))[0]
    
    original = raw.imread(dng)
    img = original.postprocess(output_color=raw.ColorSpace.sRGB, 
                               no_auto_bright=True,
                               use_auto_wb=False,
                               gamma=(1,4.5))  
    
    img = img[:,:,::-1]                                                                     
   
    
       
       
    original_cast_32 = np.float32(img)
    original_cast_32 /= 255.0
    
    print (img.shape)
    
    output_path = "./converted.exr"
    
    #plt.imshow(img)
    #plt.show()
    
    #print("original min: {}, max: {}".format(np.min(original_cast_32), np.max(original_cast_32)))
    if os.path.isfile(output_path):
        os.remove(output_path)
    cv.imwrite(output_path, original_cast_32,[cv.IMWRITE_EXR_TYPE, cv.IMWRITE_EXR_TYPE_HALF])
    #imageio.imwrite(output_path, original_cast_32, "EXR-FI")



if __name__ == "__main__":

    if os.path.isfile(path_to_dng):
        convert(path_to_dng, path_to_exr)
        #imageio.show_formats()
