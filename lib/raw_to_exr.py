from unity_raw_to_exr import raw_to_exr
import os

path_to_raw = '/home/hernan/Documents/MLV_app/testRaw/M05-1826_.raw'


if __name__ == "__main__":
    if os.path.isfile(path_to_raw):
        raw_to_exr(path_to_raw)
    else:
        print("Path does not exist")