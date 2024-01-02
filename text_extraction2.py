from PIL import Image
import numpy as np
import cv2


click = False     # Mouse 클릭된 상태 (false = 클릭 x / true = 클릭 o) : 마우스 눌렀을때 true로, 뗏을때 false로
x1,y1 = -1,-1
mode = "white"

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
                cv2.rectangle(binary_img,(x1,y1),(x,y),(0,0,0),-1)
            elif mode == "white":
                cv2.rectangle(binary_img,(x1,y1),(x,y),(255,0,0),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        click = False;                                      # 마우스를 때면 상태 변경
        if mode == "black":
            cv2.rectangle(binary_img,(x1,y1),(x,y),(0,0,0),-1)
        elif mode == "white":
            cv2.rectangle(binary_img,(x1,y1),(x,y),(255,0,0),-1)


if __name__ == "__main__":
    
    img = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)
    
    _, binary_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
    
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_rectangle, binary_img)
    
    while True:
        cv2.imshow('origin', binary_img)
        cv2.imshow('image', binary_img)    # 화면을 보여준다.
        # cv2.imshow('dst', dst)
        k = cv2.waitKey(1) & 0xFF   # 키보드 입력값을 받고
        
        if k == 27:
            binary_pil_img = Image.fromarray(binary_img)

            img = binary_pil_img.convert("RGBA")
            
            data = img.getdata()

            # 새로운 픽셀 데이터 생성
            new_data = []
            for item in data:
                # 검은색 부분은 그대로 유지하고, 나머지는 투명하게
                if item[:3] == (0, 0, 0):
                    new_data.append(item)
                else:
                    new_data.append((0, 0, 0, 0))

            # 이미지에 새로운 데이터 적용
            img.putdata(new_data)
            img.save("output.png", "PNG")
            
            break
    
    cv2.destroyAllWindows()
    
   