import glob
import os
import shutil
from tqdm import tqdm
import sys

def make_data_path(link_path):
    target_path_png = link_path + "/*.png"
    path_list = []
    for path in glob.glob(target_path_png):
        path_list.append(path)
        
    return path_list

def main(image_path, raw_our_dir_path):
    image_list = make_data_path(image_path)
    """
    fine_out_dir_path = ""
    i = 0
    fine_out_dir_path = str(30000)
    our_dir_path = os.path.join(raw_our_dir_path, fine_out_dir_path)
    if not os.path.isdir(our_dir_path):
        os.makedirs(our_dir_path)
    """
    for image in tqdm(image_list):
        """
        if i % 10000 == 0:
            fine_out_dir_path = str(i)
            our_dir_path = os.path.join(raw_our_dir_path, fine_out_dir_path)
            if not os.path.isdir(our_dir_path):
                os.makedirs(our_dir_path)
        """
        if os.path.isfile(image):
            # shutil.move(image, our_dir_path)
            shutil.move(image, raw_our_dir_path)
        del image
        
        # i += 1

if __name__ == '__main__':
    in_dir = "/mnt/f/deeplearning_upload_data/20211125"
    # out_dir = "/mnt/d/DeepLearning/crop_danbooru/upload/all-E"
    out_dir = "/mnt/f/deeplearning_upload_data/ALL"

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)
    main(in_dir, out_dir)
