from PIL import Image
import cv2
import numpy as np




img = cv2.imread("test/00014.jpeg", cv2.IMREAD_COLOR)
src = cv2.resize(img,  dsize=(768,512), interpolation=cv2.INTER_LINEAR)
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

cv2.imshow("h", h)
cv2.imshow("s", s)
cv2.imshow("v", v)
cv2.waitKey()

# img_ = Image.fromarray(src)
# for x in range(768):
#     for y in range(512):
#         pixel = img_.getpixel((x,y))
#         r, g, b = pixel[:3]
#         if r < 100 and g <100 and b <100:
#             img_.putpixel((x, y), (r, g, b))
#         else:
#             img_.putpixel((x, y), (r+50, g+50, b+50))

# img_.show()

# import numpy as np
# from PIL import Image

# def process_image_np(image_path, output_path):
#     # 이미지를 NumPy 배열로 변환
#     image = np.array(Image.open(image_path))

#     # 각 픽셀에 대해 조건을 확인하고 처리
#     condition = (image[:, :, 0] > 10) | (image[:, :, 1] > 10) | (image[:, :, 2] > 10)
#     image[condition] += 50

#     # 255를 초과하는 값들을 255로 설정
#     image = np.clip(image, 0, 255)

#     # NumPy 배열을 이미지로 변환
#     processed_image = Image.fromarray(np.uint8(image))

#     # 처리된 이미지 저장
#     processed_image.save(output_path)

# # 이미지 파일 경로 지정
# input_image_path = 'test/00000.jpeg'
# output_image_path = 'output_image.jpg'

# # 이미지 처리 함수 호출
# process_image_np(input_image_path, output_image_path)

from PIL import Image

def process_image(image_path, output_path):
    # 이미지 열기
    image = Image.open(image_path)

    # 이미지의 너비와 높이 가져오기
    width, height = image.size

    # 각 픽셀에 대해 조건을 확인하고 처리
    for x in range(width):
        for y in range(height):
            # 각 픽셀의 RGB 값 가져오기
            r, g, b = image.getpixel((x, y))

            # 조건 확인 후 처리
            if r <= 50 and g <= 50 and b <= 50:
                pass  # 아무 처리도 하지 않음
            else:
                # RGB 값 각각에 100 더하기
                r += 70
                g += 70
                b += 70

                # 255를 초과하는 값들을 255로 설정
                r = min(r, 255)
                g = min(g, 255)
                b = min(b, 255)

                # 이미지에 적용
                image.putpixel((x, y), (r, g, b))

    # 처리된 이미지 저장
    image.save(output_path)

# 이미지 파일 경로 지정
input_image_path = 'test/00014.jpeg'
output_image_path = 'output_image.jpg'

# 이미지 처리 함수 호출
process_image(input_image_path, output_image_path)