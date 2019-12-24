import os
import time
from skimage import io
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC
from sklearn.utils import shuffle
import numpy as np


def get_average_colors(image_names, N):
    X = np.zeros((len(image_names), N * 3))

    for i in range(0, len(image_names)):
        #if i%50 == 0:
        #    print(i)
        RED_sum = 0
        GREEN_sum = 0
        BLUE_sum = 0
        q = 0
        image = io.imread(image_names[i])
        size = len(image)

        for j in range(0, N):
            for k in range((size // N) * j, (size // N) * (j + 1)):
                for img in image[k]:   # img[RED, GREEN, BLUE]
                    if img[0] > 30:
                        RED_sum += img[0] ** 2
                    if img[1] > 30:
                        GREEN_sum += img[1] ** 2
                    if img[2] > 30:
                        BLUE_sum += img[2] ** 2
                    q += 1

            X[i, j * 3] = RED_sum / q
            X[i, j * 3 + 1] = GREEN_sum / q
            X[i, j * 3 + 2] = BLUE_sum / q

            RED_sum = 0
            GREEN_sum = 0
            BLUE_sum = 0
            q = 0
    return X

iter_num = 1000
#data for traning
Lsc = os.listdir('./Landscapes')
Oth = os.listdir('./Other_images')
Lsc = ['./Landscapes/'+image  for image in Lsc]
Oth = ['./Other_images/'+image  for image in Oth]
Lsc_ans = np.ones(len(Lsc)) #arrays of answers: right - 1, wrong - 0
Oth_ans = np.zeros(len(Oth))
IMG = Lsc + Oth
ANS = np.concatenate((Lsc_ans,Oth_ans))
IMG, ANS = shuffle(IMG, ANS)

#making for test
LscT = os.listdir('./Landscapes_for_test')
OthT = os.listdir('./Other_images_for_test')
LscT = ['./Landscapes_for_test/'+image  for image in LscT]
OthT = ['./Other_images_for_test/'+image  for image in OthT]
TAR = np.ones(len(LscT)) # Right and Wrong test ANS
TAW = np.zeros(len(OthT))
test_img = LscT + OthT
test_ans = np.concatenate((TAR,TAW))

start_time = time.time()
X_train = get_average_colors(IMG, 4)
SVC = LinearSVC(max_iter=iter_num).fit(X_train, ANS)
X_test = get_average_colors(test_img, 4)
test_pred = SVC.predict(X_test)
print(test_ans)
print(test_pred)
print('Prediction accuracy is {}%'.format(accuracy_score(test_pred, test_ans) * 100))
print('Program execution time is: {}s'.format(time.time() - start_time))