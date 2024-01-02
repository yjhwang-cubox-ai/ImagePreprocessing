from PIL import Image
import cv2
import numpy as np

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
                cv2.rectangle(result,(x1,y1),(x,y),(0,0,0),-1)
            elif mode == "white":
                cv2.rectangle(result,(x1,y1),(x,y),(255,0,0),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        click = False;                                      # 마우스를 때면 상태 변경
        if mode == "black":
            cv2.rectangle(result,(x1,y1),(x,y),(0,0,0),-1)
        elif mode == "white":
            cv2.rectangle(result,(x1,y1),(x,y),(255,0,0),-1)

if __name__ == "__main__":
    
    img_size_ratio = 1
    dliate_iteration = 1
    
    img = cv2.imread("sample.jpg", cv2.IMREAD_COLOR)
    src = cv2.resize(img,  dsize=(1920,1200), interpolation=cv2.INTER_LINEAR)
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    
    v = cv2.inRange(v, 0, 0)
    temp = cv2.bitwise_and(hsv, hsv, mask = v)
    result = cv2.cvtColor(temp, cv2.COLOR_HSV2BGR)
    
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_rectangle, result)
    
    while True:
        cv2.imshow('origin', img)
        cv2.imshow('image', result)    # 화면을 보여준다.
        # cv2.imshow('dst', dst)
        k = cv2.waitKey(1) & 0xFF   # 키보드 입력값을 받고
        
        if k == 27:           
            
            result = cv2.cvtColor(result, cv2.COLOR_RGB2RGBA)
            img_ = Image.fromarray(result)
            # img_.show()
            
            for x in range(768):
                for y in range(512):
                    pixel = img_.getpixel((x,y))
                    r, g, b = pixel[:3]
                    if r < 10 and g <10 and b <10:
                        img_.putpixel((x, y), (r, g, b, 0))
                    else:
                        img_.putpixel((x, y), (r, g, b, 170))
                        
                        
            img_.save('mask_result/hologram_1.png')
            break
    
    cv2.destroyAllWindows()