import cv2
import numpy as np
from numpy.core.records import array

#1차원 배열 만들기
arr = np.array([5,10,15])

print(arr)
print(arr.shape)

print(arr[0])
arr[1] = 50
print(arr)

#2차원 배열 만들기

array_2d = np.array([5,6,1,2,9,10])

array_2d = array_2d.reshape(3,2)
print(array_2d)

#2차원 배열읠 데이터 억세스
#2행 1열의 데이터를 억세스!
print( array_2d[1, 1])

# 이미지 파일을 칼라(BGR)로 읽어오는 방법
img = cv2.imread('data/images/smaple.jpg')

print(img)
print(img.shape)
print(img.ndim)
#이미지 파일을 그레이스케일ㄹ로 읽어오는 방법
img2 = cv2.imread('data/images/sample.jpg',0)

print(img2)
print(img2.shape)
print(img2.ndim)