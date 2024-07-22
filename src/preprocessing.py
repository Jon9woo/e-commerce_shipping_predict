import pandas as pd

# 데이터 로드
data = pd.read_csv('../data/shipping.csv')
print('데이터 로드 완료')

# 결측치 제거
data = data.dropna()
print('결측치 제거 완료')

# 종속변수명 변경
data = data.rename(columns={'Reached.on.Time_Y.N': 'Reached_on_Time_y_n'})
print('종속변수명 변경 완료')

# 데이터 저장
data.to_csv('../data/shipping_preprocessed.csv', index=False)
print('데이터 저장 완료')

