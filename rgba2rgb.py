import cv2
import glob
from tqdm import tqdm

input_path = "D:/DeepLearning/crop_danbooru/dataset-20210927-old"
output_path = "D:/DeepLearning/crop_danbooru/dataset-20210927"

def make_data_path(link_path):
    target_path_png = link_path + "/*.png"
    target_path_jpg = link_path + "/*.jpg"
    path_list = []
    for path in glob.glob(target_path_png):
        path_list.append(path)
    # for path in glob.glob(target_path_jpg):
        # path_list.append(path)
        
    return path_list

path_list = make_data_path(input_path)
for i, path in enumerate(tqdm(path_list)):
    img = cv2.imread(path)
    cv2.imwrite(f"{output_path}/{i:06d}.png", img)