import cv2
import numpy as np

source = cv2.imread('data/images/sample.jpg')

scalingFactor = 1/255.0

# 0~255로 되어있는 이미지를 0~1사이의 실수로 정규화

source = source * scalingFactor

print(source)


# 반대로, 실수로 되어있는것을, 다시 0~255로 만드는 방법
# 즉, 다시 이미지 배열로 만드는 방법

source = source * 255

print(source)

# 위의 코드는 실수이므로 결과가 이미지 배열이 아니다.


#따라서 다시 이미지 배열로 만드렴녀 데이터 타입을 변경해줘야 한다.
#변경방법 2가지
#1. np.uint8(cource)
#2. source.astype('unit8')

source = source.astype('uint8')

print(source)