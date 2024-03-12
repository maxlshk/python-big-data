import pytest
import pandas as pd
from app.io.input import read_from_file_with_pandas


def test_read_from_file_with_pandas_exists():
    df = read_from_file_with_pandas("test_data.csv")
    assert df is not None


def test_read_from_file_with_pandas_content():
    data = {'Name': ['John', 'Anna'], 'Age': [28, 22]}
    df_expected = pd.DataFrame(data)
    df_expected.to_csv("test_data.csv", index=False)
    df = read_from_file_with_pandas("test_data.csv")
    pd.testing.assert_frame_equal(df, df_expected)


def test_read_from_file_with_pandas_no_file():
    with pytest.raises(FileNotFoundError):
        read_from_file_with_pandas("non_existent_file.csv")
