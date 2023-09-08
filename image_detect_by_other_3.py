import image_detect_model as model

import os
import cv2
import glob
from tqdm import tqdm
import dlib
import shutil

# image_dir_output_path = "D:/Deeplearning/crop_danbooru/30001-35000"
# image_dir_output_path = "./out_image"
#image_dir_output_path = "./"



#save_test = 0

haar_anime_face_cascade = cv2.CascadeClassifier("model/haar_anime_face_detect.xml")
lbp_anime_face_cascade = cv2.CascadeClassifier("model/lbp_anime_face_detect.xml")
hog_anime_face_detector = dlib.simple_object_detector("model/detector_face.svm")

def make_data_path(link_path):
    target_path_png = link_path + "/*.png"
    target_path_jpg = link_path + "/*.jpg"
    path_list = []
    for path in glob.glob(target_path_png):
        path_list.append(path)
    for path in glob.glob(target_path_jpg):
        path_list.append(path)
        
    return path_list

def detect_three_model(img):
    haar_detect = model.haar_anime_face_detect(img, haar_anime_face_cascade)
    lbp_detect = model.lbp_anime_face_detect(img, lbp_anime_face_cascade)
    hog_detect = model.hog_anime_face_detect(img, hog_anime_face_detector)
    return haar_detect + lbp_detect + hog_detect

def get_all_path(input_dir_path):
    image_path_list = []
    for i in range(2, 68):
        input_dir_path_all = input_dir_path + str(i)
        image_list = make_data_path(input_dir_path_all)

    
def main(input_dir, output_dir):
    # image_path = "D:/Deeplearning/scraip_danbooru/normal"
    # image_path = "./exa_image"

    for i in range(64, 69):
        input_dir_path = input_dir + str(i * 10000)
        # input_dir_path = input_dir
        output_dir_path = output_dir + str(i * 10000)
        if not os.path.isdir(output_dir_path):
            os.makedirs(output_dir_path)

        #63/68の途中までやってた
        print(f"{i:02d} / 69")
        image_list = make_data_path(input_dir_path)
        for path in tqdm(image_list):
            cv2img = cv2.imread(path)
            detect_result = detect_three_model(cv2img)
            if detect_result < 1:
                shutil.move(path, output_dir_path)



"""

    for i, path in enumerate(tqdm(image_list)):
        if i % 10000 == 0:
            dir_name = str(i)
            dir_name_all = image_dir_output_path + dir_name
            if not os.path.isdir(dir_name_all):
                os.makedirs(dir_name_all)
        cv2img = cv2.imread(path)
        # print(type(cv2img))
        # print("-------------")
        detect_result = detect_three_model(cv2img)
        # print(detect_result)
        if detect_result < 1:
            shutil.move(path, dir_name_all)
"""

if __name__ == '__main__':
    # get_final_image("./exa_image/6.png")
    input_dir = "D:/DeepLearning/crop_danbooru/upload/"
    output_dir = "D:/DeepLearning/danbooru-detect-error/"
    main(input_dir, output_dir)
    

