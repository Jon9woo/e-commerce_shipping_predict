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