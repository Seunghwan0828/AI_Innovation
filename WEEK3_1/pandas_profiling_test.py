import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport

df_titanic = pd.read_csv("train.csv")
profile = ProfileReport(df_titanic, title="타이타닉 데이터셋 분석 결과", explorative=True)
profile.to_file("titanic_result.html")