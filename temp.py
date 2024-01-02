import cv2

def on_mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"마우스 클릭 위치: x={x}, y={y}")

def get_mouse_click_coordinates(image_path):
    # 이미지 읽기
    img = cv2.imread(image_path)

    # 윈도우 생성 및 마우스 콜백 함수 등록
    cv2.namedWindow("Image")
    cv2.setMouseCallback("Image", on_mouse_click)

    while True:
        # 이미지 보여주기
        cv2.imshow("Image", img)

        # 'q' 키를 누르면 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 윈도우 종료
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = "sample.jpg"  # 이미지 파일 경로를 적절히 변경하세요
    get_mouse_click_coordinates(image_path)