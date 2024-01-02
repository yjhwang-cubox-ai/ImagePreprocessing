from PIL import Image
import os
from tqdm import tqdm

# 투명도 그라디언트 적용 - 오른쪽 아래에서 대각선
def light_grad1(img, width, height, threshold):
    for y in range(height):
        alpha1 = int((y / height) * 255)  # 투명도 계산 (0 ~ 255 범위)
        for x in range(width):
            alpha = int((alpha1 + int(x/width * 255))/2)
            
            if alpha > threshold:
                alpha = threshold
        
            pixel = img.getpixel((x, y))
            r, g, b = pixel[:3]  # 픽셀의 RGB 값 가져오기
            img.putpixel((x, y), (r, g, b, alpha))  # 픽셀의 투명도 설정
    img.save("gradient/gradient1.png")
    return img

# 투명도 그라디언트 적용 - 왼쪽 아래에서 대각선
def light_grad2(img, width, height, threshold):
    for y in range(height):
        alpha1 = int((y / height) * 255)  # 투명도 계산 (0 ~ 255 범위)
        for x in range(width):
            alpha = int((alpha1 + int(255 - x/width * 255))/2)
            
            if alpha > threshold:
                alpha = threshold                
                
            pixel = img.getpixel((x, y))
            r, g, b = pixel[:3]  # 픽셀의 RGB 값 가져오기
            img.putpixel((x, y), (r, g, b, alpha))  # 픽셀의 투명도 설정
    img.save("gradient/gradient2.png")
    return img

# 투명도 그라디언트 적용 - 오른쪽위에서 대각선
def light_grad3(img, width, height, threshold):
    for x in range(width):
        alpha1 = int((x / width) * 255)  # 투명도 계산 (0 ~ 255 범위)
        for y in range(height):
            alpha = int((alpha1 + int(255 - y/height * 255))/2)
            
            if alpha > threshold:
                alpha = threshold
                
                
            pixel = img.getpixel((x, y))
            r, g, b = pixel[:3]  # 픽셀의 RGB 값 가져오기
            img.putpixel((x, y), (r, g, b, alpha))  # 픽셀의 투명도 설정
    img.save("gradient/gradient3.png")
    return img

# 투명도 그라디언트 적용 - 왼쪽위에서 대각선
def light_grad4(img, width, height, threshold):
    for x in range(width):
        alpha1 = int(255 - (x / width) * 255)  # 투명도 계산 (0 ~ 255 범위)
        for y in range(height):
            alpha = int((alpha1 + int(255 - y/height * 255))/2)
            
            if alpha > threshold:
                alpha = threshold                
                
            pixel = img.getpixel((x, y))
            r, g, b = pixel[:3]  # 픽셀의 RGB 값 가져오기
            img.putpixel((x, y), (r, g, b, alpha))  # 픽셀의 투명도 설정
    img.save("gradient/gradient4.png")  
    return img

# 투명도 그라디언트 적용 - 왼쪽이 진함
def light_grad5(img, width, height, threshold):
    for x in range(width):
        alpha = int(255 - (x / width) * 255)  # 투명도 계산 (0 ~ 255 범위)
        
        if alpha > threshold:
                alpha = threshold
        
        for y in range(height):
            pixel = img.getpixel((x, y))
            r, g, b = pixel[:3]  # 픽셀의 RGB 값 가져오기
            img.putpixel((x, y), (r, g, b, alpha))  # 픽셀의 투명도 설정
    img.save("gradient/gradient5.png")
    return img

# # 투명도 그라디언트 적용 - 오른쪽이 진함
def light_grad6(img, width, height, threshold):
    for x in range(width):
        alpha = int(255 - (x / width) * 255)  # 투명도 계산 (0 ~ 255 범위)
        
        if alpha > threshold:
                alpha = threshold
        
        for y in range(height):
            pixel = img.getpixel((x, y))
            r, g, b = pixel[:3]  # 픽셀의 RGB 값 가져오기
            img.putpixel((x, y), (r, g, b, alpha))  # 픽셀의 투명도 설정
    img.save("gradient/gradient6.png")     
    return img

# # 투명도 그라디언트 적용 - 위에서 아래로
def light_grad7(img, width, height, threshold):
    for y in range(height):
        alpha = int(255 - (y / height) * 255)  # 투명도 계산 (0 ~ 255 범위)
        
        if alpha > threshold:
                alpha = threshold
                
                
        for x in range(width):
            pixel = img.getpixel((x, y))
            r, g, b = pixel[:3]  # 픽셀의 RGB 값 가져오기
            img.putpixel((x, y), (r, g, b, alpha))  # 픽셀의 투명도 설정
    img.save("gradient/gradient7.png")         
    return img

# 투명도 그라디언트 적용 - 아래에서 위로
def light_grad8(img, width, height, threshold):
    for y in range(height):
        alpha = int((y / height) * 255)  # 투명도 계산 (0 ~ 255 범위)
        
        if alpha > threshold:
                alpha = threshold
                
                
        for x in range(width):
            pixel = img.getpixel((x, y))
            r, g, b = pixel[:3]  # 픽셀의 RGB 값 가져오기
            img.putpixel((x, y), (r, g, b, alpha))  # 픽셀의 투명도 설정
    img.save("gradient/gradient8.png")        
    return img


def main():
    # 이미지 파일 경로
    image_path = "output.png"
    output_path = "gradient"
    img_width = 960
    img_height = 600
    
    max_thres = 170

    # 이미지 불러오기
    # image = Image.open(image_path).convert("RGBA")
    image = Image.new("RGBA", (img_width, img_height), "black")
    # 이미지 크기 가져오기
    # width, height = image.size
    light_grad1(image, img_width, img_height, max_thres)
    light_grad2(image, img_width, img_height, max_thres)
    light_grad3(image, img_width, img_height, max_thres)
    light_grad4(image, img_width, img_height, max_thres)
    light_grad5(image, img_width, img_height, max_thres)
    light_grad6(image, img_width, img_height, max_thres)
    light_grad7(image, img_width, img_height, max_thres)
    light_grad8(image, img_width, img_height, max_thres)
    
    # for idx, img in enumerate(light_images):
    #     img_name = f"gradient{idx}.png"
    #     img_ = light_images[idx]
    #     img_.save(os.path.join(output_path, img_name))
    #     print(f"{img_name} 이 저장됨")
        
if __name__ == "__main__":
    main()