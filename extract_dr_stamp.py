from PIL import Image
import numpy as np
import cv2


click = False     # Mouse 클릭된 상태 (false = 클릭 x / true = 클릭 o) : 마우스 눌렀을때 true로, 뗏을때 false로
x1,y1 = -1,-1
mode = "black"

# Mouse Callback함수 : 파라미터는 고정됨.
def draw_rectangle(event, x, y, flags, param):
    global x1,y1, click, mode                                     # 전역변수 사용

    if event == cv2.EVENT_LBUTTONDOWN:                      # 마우스를 누른 상태
        click = True 
        x1, y1 = x,y
        print("사각형의 왼쪽위 설정 : (" + str(x1) + ", " + str(y1) + ")")
		
    elif event == cv2.EVENT_MOUSEMOVE:                      # 마우스 이동
        if click == True:         
            if mode == "black":
                cv2.rectangle(img_result,(x1,y1),(x,y),(0,0,0),-1)
            elif mode == "white":
                cv2.rectangle(img_result,(x1,y1),(x,y),(255,0,0),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        click = False;                                      # 마우스를 때면 상태 변경
        if mode == "black":
            cv2.rectangle(img_result,(x1,y1),(x,y),(0,0,0),-1)
        elif mode == "white":
            cv2.rectangle(img_result,(x1,y1),(x,y),(255,0,0),-1)


if __name__ == "__main__":
    
    img_color = cv2.imread('test/015_.jpg') # 이미지 파일을 컬러로 불러옴
    img_color = cv2.resize(img_color, dsize=(768,512), interpolation=cv2.INTER_LINEAR)
    height, width = img_color.shape[:2] # 이미지의 높이와 너비 불러옴, 가로 [0], 세로[1]

    # img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV) # cvtColor 함수를 이용하여 hsv 색공간으로 변환

    lower_red = (0, 0, 100) # hsv 이미지에서 바이너리 이미지로 생성 , 적당한 값 30
    upper_blue = (150, 150, 255)
    img_mask = cv2.inRange(img_color, lower_red, upper_blue) # 범위내의 픽셀들은 흰색, 나머지 검은색
    
    img_result = cv2.bitwise_and(img_color, img_color, mask = img_mask) 
    # 바이너리 이미지를 마스크로 사용하여 원본이미지에서 범위값에 해당하는 영상부분을 획득
    
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_rectangle, img_result)
    
    while True:
        cv2.imshow('origin', img_color)
        cv2.imshow('image', img_result)    # 화면을 보여준다.
        # cv2.imshow('dst', dst)
        k = cv2.waitKey(1) & 0xFF   # 키보드 입력값을 받고
        
        if k == 27:
            cv2.imwrite("test.png", img_result)
            print("finish")
            
            img = Image.open('test.png')
            img = img.convert("RGBA")
            datas = img.getdata()
            
            newData = []
            cutOff = 50
            
            for item in datas:
                if item[0] < cutOff and item[1] < cutOff and item[2] < cutOff:
                    newData.append((0,0,0,0))
                else:
                    newData.append(item)
            
            img.putdata(newData)
            img.save("mask_result/dr_template_stamp.png")
            
            template = Image.open('inpainting_template\img7_mask002.png').resize((768,512))
            
            combined = Image.alpha_composite(template.convert('RGBA'), img)
            combined = combined.convert('RGB')
            
            combined.save('combined____.png')
            
            
            
            
            
            
            
            break
            
            
            # result = cv2.cvtColor(img_result, cv2.COLOR_RGB2RGBA)
            # img_ = Image.fromarray(result)
            # # img_.show()
            
            # for x in range(768):
            #     for y in range(512):
            #         pixel = img_.getpixel((x,y))
            #         r, g, b = pixel[:3]
            #         if r == 0 and g == 0  and b == 0 :
            #             img_.putpixel((x, y), (r, g, b, 0))
            #         else:
            #             img_.putpixel((x, y), (r, g, b, 255))
                        
                        
            # img_.save('mask_result/dr_template_1.png')
            # break
    
    cv2.destroyAllWindows()
    
   