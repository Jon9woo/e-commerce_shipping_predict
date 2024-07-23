# preprocessing.py

import pandas as pd

def load_data(filepath):
    """Load the data from a CSV file."""
    data = pd.read_csv(filepath)
    print('데이터 로드 완료')
    return data

def remove_missing_values(data):
    """Remove rows with missing values."""
    data = data.dropna()
    print('결측치 제거 완료')
    return data

def rename_columns(data):
    """Rename columns for consistency."""
    data = data.rename(columns={'Reached.on.Time_Y.N': 'Reached_on_Time_y_n'})
    print('종속변수명 변경 완료')
    return data

def get_numerical_categorical_columns():
    """Get lists of numerical and categorical columns."""
    numerical = ['Customer_care_calls', 'Cost_of_the_Product', 'Prior_purchases', 'Discount_offered', 'Weight_in_gms']
    categorical = ['Warehouse_block', 'Mode_of_Shipment', 'Customer_rating', 'Product_importance', 'Gender']
    return numerical, categorical

def dummy_encode_categorical_columns(data, categorical_columns):
    """Dummy encode the categorical columns."""
    data = pd.get_dummies(data, columns=categorical_columns)
    print('범주형 변수 더미화 완료')
    return data

def save_data(data, filepath):
    """Save the preprocessed data to a CSV file."""
    data.to_csv(filepath, index=False)
    print('데이터 저장 완료')

def preprocess_data(input_filepath, output_filepath):
    """Complete preprocessing pipeline."""
    data = load_data(input_filepath)
    data = remove_missing_values(data)
    data = rename_columns(data)
    save_data(data, output_filepath)

def dummy_encoding(input_filepath, output_filepath):
    data = pd.read_csv(input_filepath)
    numerical_columns, categorical_columns = get_numerical_categorical_columns()
    data = dummy_encode_categorical_columns(data, categorical_columns)
    save_data(data, output_filepath)

# 실행 예제
if __name__ == "__main__":
    # 데이터 전처리만 실행
    preprocess_data('../data/shipping.csv', '../data/shipping_preprocessed.csv')
    # 전처리된 데이터 더미화 실행
    dummy_encoding('../data/shipping_preprocessed.csv', '../data/shipping_dummy_encoded.csv')

