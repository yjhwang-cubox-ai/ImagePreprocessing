from PIL import Image

def binarize_image(input_path, threshold=128):
    # 이미지 열기
    img = Image.open(input_path)

    # 이미지를 그레이스케일로 변환
    img = img.convert("L")

    # 이진화
    img = img.point(lambda p: p > threshold and 255)

    return img

def make_transparent(input_path, output_path):
    # 이미지 열기
    # img = Image.open(input_path)
    img = binarize_image(input_path)
    img.show()

    # 이미지를 RGBA 모드로 변환
    img = img.convert("RGBA")

    # 픽셀 데이터 가져오기
    data = img.getdata()

    # 새로운 픽셀 데이터 생성
    new_data = []
    for item in data:
        # 검은색 부분은 투명하게, 나머지는 그대로 유지
        if item[:3] == (0, 0, 0):
            new_data.append(item)            
        else:
            new_data.append((0, 0, 0, 0))

    # 이미지에 새로운 데이터 적용
    img.putdata(new_data)

    # 이미지 저장
    img.save(output_path, "PNG")

if __name__ == "__main__":
    input_image_path = "sample.jpg"
    output_image_path = "output_image.png"

    make_transparent(input_image_path, output_image_path)