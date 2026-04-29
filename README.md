# YOLOv5 실시간 객체 탐지

YOLOv5를 활용한 실시간 비디오 객체 탐지 프로젝트입니다. 웹캠이나 비디오 파일에서 실시간으로 객체를 탐지하고 시각화합니다.

## 📋 프로젝트 개요

- **모델**: YOLOv5 (소형 모델 - yolov5s)
- **프레임워크**: PyTorch
- **비디오 처리**: OpenCV
- **실시간 처리**: 웹캠 또는 비디오 파일 지원
- **성능 최적화**: 프레임 스킵 옵션 지원

## 🚀 설치 방법
### 1. 필수 
vscode를 열고    
main.py 파일을 확인    
터미널을 열고    
```bash
conda create -n yolo python=3.13.12
conda activate yolo
```

### 2. YOLOv5 저장소 클론 (필수)

```bash
git clone https://github.com/ultralytics/yolov5.git
```
이렇게 되면 작업 폴더 아래에 yolov5가 새로 생깁니다. 

### 3. YOLOv5 의존성 설치

vscode에서 터머널을 열고 
```bash
pip install -r yolov5/requirements.txt
```

## 💻 사용 방법

### 1. 웹캠을 이용한 실시간 탐지

```bash
python main.py
```

기본 설정에서 웹캠(카메라 0번)을 사용하여 실시간 객체 탐지를 시작합니다.

### 2. 비디오 파일 사용

`main.py`의 다음 부분을 수정하세요:

```python
# 수정 전
cap = cv2.VideoCapture(0)

# 수정 후 (비디오 파일 경로로 변경)
cap = cv2.VideoCapture('your_video.mp4')
```

## 🎛️ 주요 설정 옵션

| 옵션 | 설명 | 기본값 |
|------|------|--------|
| `frame_skip` | 처리할 프레임 간격 (1: 모든 프레임, 5: 5프레임마다) | 1 |
| 모델 | YOLOv5 모델 크기 (n, s, m, l, x) | yolov5s |

성능 최적화를 위해 `frame_skip` 값을 증가시킬 수 있습니다:

```python
frame_skip = 3  # 3프레임마다 처리 (성능 향상)
```

## 🎮 실행 중 단축키

- **`q` 키**: 프로그램 종료

## 📊 출력 결과

- 실시간 비디오 윈도우에서 탐지된 객체 표시
- 100프레임마다 결과 이미지를 `output_frame_*.jpg`로 저장
<img width="1644" height="1040" alt="image" src="https://github.com/user-attachments/assets/32c2585b-7033-4522-b1a8-08cd25f457e7" />


## 📁 프로젝트 구조

```
20260429Yolo/
├── main.py              # 메인 실행 파일
├── README.md            # 프로젝트 설명
└── yolov5/              # YOLOv5 저장소
    ├── detect.py        # 탐지 스크립트
    ├── train.py         # 훈련 스크립트
    ├── models/          # 모델 정의
    ├── data/            # 데이터셋
    └── utils/           # 유틸리티
```

## 🎯 기능

✅ **실시간 객체 탐지** - 웹캠/비디오에서 실시간 탐지  
✅ **자동 시각화** - 탐지된 객체에 박스 및 라벨 표시  
✅ **결과 저장** - 정기적으로 처리된 프레임 저장  
✅ **성능 최적화** - 프레임 스킵을 통한 성능 조절  
✅ **유연한 모델 선택** - 다양한 크기의 YOLOv5 모델 지원

## 🔧 트러블슈팅

### 웹캠이 인식되지 않음
```python
# 다른 카메라 번호 시도
cap = cv2.VideoCapture(1)  # 또는 2, 3 등
```

### 모델 로드 실패
YOLOv5 저장소가 정확한 위치에 있는지 확인하세요:
```bash
ls yolov5/models/yolov5s.yaml
```

### 성능 저하
- `frame_skip` 값을 증가시키세요
- 더 작은 모델 사용 (yolov5n)

## 📚 참고 자료

- [YOLOv5 공식 저장소](https://github.com/ultralytics/yolov5)
- [OpenCV 문서](https://docs.opencv.org/)
- [PyTorch 공식 사이트](https://pytorch.org/)

## 📝 라이선스

이 프로젝트는 YOLOv5의 라이선스를 따릅니다.

---

**작성일**: 2026-04-29  
**마지막 수정**: 2026-04-29
