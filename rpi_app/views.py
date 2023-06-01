import cv2
import picamera
from django.http import StreamingHttpResponse
from django.views.decorators import gzip

# VideoCapture 클래스를 사용하여 카메라로부터 영상을 캡처하는 제너레이터 함수
def video_stream():
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.framerate = 30

        # OpenCV VideoCapture를 사용하기 위해 카메라 영상 설정
        camera.start_preview()
        time.sleep(2)  # 카메라 초기화 시간

        # VideoCapture 객체 생성
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            raise RuntimeError("Could not open camera")

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # 프레임 처리 (예: 이미지 필터링, 객체 검출 등)

            # 프레임을 JPEG 형식으로 인코딩하여 바이트 스트림으로 변환
            _, img_encoded = cv2.imencode('.jpg', frame)

            # 바이트 스트림을 스트리밍 응답에 전달
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + img_encoded.tobytes() + b'\r\n')

        # 리소스 해제
        cap.release()

@gzip.gzip_page
def live_stream(request):
    # 스트리밍 응답 생성
    response = StreamingHttpResponse(video_stream(), content_type='multipart/x-mixed-replace; boundary=frame')
    return response





