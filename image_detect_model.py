import cv2

def haar_anime_face_detect(img, face_cascade):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 图片灰度化
    img_gray = cv2.equalizeHist(img_gray)  # 直方图均衡化
    faces = face_cascade.detectMultiScale(img_gray)  # 多尺度检测
    return len(faces)

def lbp_anime_face_detect(img, face_cascade):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 图片灰度化
    img_gray = cv2.equalizeHist(img_gray)  # 直方图均衡化
    faces = face_cascade.detectMultiScale(img_gray)  # 多尺度检测
    return len(faces)

def hog_anime_face_detect(img, face_detector):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 图片灰度化
    img_gray = cv2.equalizeHist(img_gray)  # 直方图均衡化
    faces = face_detector(img_gray)
    return len(faces)