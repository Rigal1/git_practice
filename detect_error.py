import cv2
import glob
from tqdm import tqdm
import shutil



def make_data_path(link_path):
    target_path_png = link_path + "/*.png"
    path_list = []
    for path in glob.glob(target_path_png):
        path_list.append(path)
        
    return path_list

def load_link(load_path):
    load_link_text = ""
    with open(load_path) as f:
        load_link_text = f.read()
    link_list = load_link_text.split(",")
    return link_list

def save_link(image_list, save_path):
    image_link_list = image_list
    with open(save_path, mode = "w") as f:
        for link in image_link_list:
            if link == image_link_list[0]:
                f.write(link)
            else:
                f.write("," + link)

# path = "D:/DeepLearning/scraip_danbooru/20211021/20211021231314.png"
path = "D:/DeepLearning/scraip_danbooru/20211021/normal"
# image_path = make_data_path(path)
# delete_path = []

# for path in tqdm(image_path):
#     img = cv2.imread(path)
#     if img is None:
#         delete_path.append(path)

delete_path = load_link("delete.csv")
for path in delete_path:
    shutil.move(path, "./image_delete")

print(len(delete_path))

# save_link(delete_path, "delete.csv")




