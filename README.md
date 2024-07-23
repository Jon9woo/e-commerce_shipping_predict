# E-Commerce 배송 데이터 예측 프로젝트

## 프로젝트 개요
이 프로젝트는 국제 전자 상거래 회사의 고객 데이터베이스를 분석하여 제품 배송이 제시간에 이루어지는지 예측하는 머신러닝 모델을 개발하는 것을 목표로 합니다. 이 회사는 전자 제품을 판매하며, 고객 수요를 충족시키기 위해 제품 배송의 시간 준수 여부를 예측하고자 합니다. 프로젝트는 AutoML 도구인 PyCaret과 실험 추적 도구인 MLflow를 사용하여 진행됩니다.

## 데이터셋 정보
- **이름**: E-Commerce Shipping Data
- **목적**: 제품 배송이 제시간에 이루어지는지 여부 예측
- **출처**: [Kaggle E-Commerce Shipping Data](https://www.kaggle.com/datasets)

## 사용 기술
- **언어**: Python
- **AutoML**: PyCaret
- **실험 추적**: MLflow
- **웹 프레임워크**: FastAPI (모델 배포를 위한 선택사항)

## 프로젝트 구조
.   
├── data   
│ ├── Train.csv   
│ └── archive.zip   
├── notebook   
│ ├── 01-dataEDA.ipynb   
│ ├── 02-modelSearch.ipynb   
│ ├── 03-hyperparameterTuning.ipynb   
│ └── logs.log   
└── src   
├── preprocessing.py   
└── init.py   


## 프로젝트 진행
1. 데이터 EDA
    - 데이터 불러오기
    - 데이터 탐색
    - 데이터 시각화
2. 데이터 전처리(preprocessing)
    - 결측치 처리
    - 이상치 처리
    - 데이터 분할
3. 피쳐 엔지니어링(feature engineering)
    - 데이터 범주화(One-hot Encoding, Label Encoding)
    - 데이터 스케일링(StandardScaler, MinMaxScaler)
4. 모델 검색(model search)
    - PyCaret을 사용한 AutoML
    - 모델 성능 비교
    - 최적 모델 선택
    ```python
    from pycaret.classification import *
    setup(data, target='target')
    compare_models()
    ```
5. 하이퍼파라미터 튜닝(hyperparameter tuning)
    - GridSearchCV, RandomizedSearchCV
6. 모델 성능 평가 및 비교
    - Confusion Matrix
    - ROC Curve
7. 모델 해석(Feature Importance, SHAP)
8. 모델 저장 및 배포

