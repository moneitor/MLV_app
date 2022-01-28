# %%
import os
import numpy as np
import imageio
import rawpy as raw
import matplotlib.pyplot as plt

imageio.plugins.freeimage.download()


path_to_dng = "./example_dng.dng"
path_to_exr = "./example_exr.exr"

def convert(dng, exr):
    name = os.path.splitext(os.path.basename(dng))[0]
    
    #original_img = imageio.imread(dng)  
    original = raw.imread(dng)
    original_img = original.postprocess(output_color=raw.ColorSpace.sRGB, 
                                        no_auto_bright=True, 
                                        gamma=(2.222,4.5)                                                                            
                                        )
    original_cast_32 = original_img.astype("float32")    
    original_cast_32 /= 255.0
    
    output_path = "./converted.exr"
    
    plt.imshow(original_cast_32)
    plt.show()
    
    #print("original min: {}, max: {}".format(np.min(original_cast_32), np.max(original_cast_32)))
    if os.path.isfile(output_path):
        os.remove(output_path)
    #imageio.imwrite(output_path, original_cast_32, "EXR-FI")



if __name__ == "__main__":

    if os.path.isfile(path_to_exr):
        convert(path_to_dng, path_to_exr)
        #imageio.show_formats()
