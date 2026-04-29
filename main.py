import cv2
import torch
import numpy as np
import time


# YOLOv5 모델 로드 (미리 클론된 yolov5 레포지토리 사용)
# 'yolov5s'는 작은 모델로 빠른 추론에 적합합니다.
# 'custom_yolov5s.yaml'로 훈련시킨 모델을 사용하려면 경로를 변경하세요.
model = torch.hub.load('./yolov5', 'yolov5s', pretrained=True, source='local')
model.eval() # 모델을 평가 모드로 설정

# 비디오 파일 경로 (예시: YOLOv5 레포지토리 내의 샘플 비디오)
# 또는 로컬 컴퓨터에서 웹캠을 사용하려면 cap = cv2.VideoCapture(0)으로 변경

cap = cv2.VideoCapture(0)

# 비디오 파일이 없거나 열 수 없는 경우 오류 메시지 출력
if not cap.isOpened():
    print("비디오 파일을 열 수 없습니다. 경로를 확인하거나 웹캠을 연결하세요.")
else:
    print("비디오 스트림이 성공적으로 열렸습니다.")

# 실시간 처리를 위한 설정
frame_skip = 1 # 모든 프레임을 처리하려면 1로 설정. 성능 향상을 위해 건너뛸 프레임 수
frame_count = 0

try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("비디오 스트림의 끝에 도달했거나 프레임을 읽을 수 없습니다.")
            break

        frame_count += 1
        if frame_count % frame_skip != 0:
            continue

        # BGR (OpenCV) -> RGB (YOLOv5)
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # 추론 수행
        results = model(img_rgb)

        # 결과를 프레임에 시각화 (results.render()는 YOLOv5가 제공하는 시각화 함수)
        # 결과를 NumPy 배열로 변환
        annotated_frame = results.render()[0] 
        
        # RGB -> BGR (OpenCV 표시를 위해)
        annotated_frame_bgr = cv2.cvtColor(annotated_frame, cv2.COLOR_RGB2BGR)

        # 실시간 비디오 화면 표시
        cv2.imshow('YOLOv5 Detection', annotated_frame_bgr)
        
        # 예시: 100프레임마다 이미지 저장
        if frame_count % 100 == 0:
            cv2.imwrite(f'./output_frame_{frame_count}.jpg', annotated_frame_bgr)
            print(f"프레임 {frame_count} 처리 및 저장 완료.")

        # `q` 키를 누르면 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
    print("비디오 스트림 처리 완료.")
