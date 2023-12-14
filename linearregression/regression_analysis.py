import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import datetime
import pykiwoom
import FinanceDataReader as fdr
import statistics
import math

order_no = "123456789"
a = 0 #매수 상태
lp = [] #거미줄 가격 리스트

# Data Manager
df = fdr.DataReader('005930', '2018' )
df.insert(0, 'Date', df.index)
df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
df['Date'] = df['Date'].astype(str)
df['Date'] = df['Date'].str.replace('-', '')
df['Date'] = df['Date'].astype(int)
data = df['Date'].values.tolist()
close = df['Close'].values.tolist()  
tp = df['Close'].iloc[-1] # Today Price 
tmp = df['Close'].iloc[-2] # Prev Price 

result_x = [ ] # X값 이차원으로 변경
for item in data:
    result_x.append([item])

result_y = [ ] # Y값 이차원으로 배열
for item in close:
    result_y.append([item])

x = [[datetime.datetime(int(str(dnt[0])[0:4]), int(str(dnt[0])[4:6]), int(str(dnt[0])[6:8])).timestamp()] for dnt in result_x] #정수를 시간데이터로 변환
y = result_y

model = LinearRegression() # 모델 생성
model.fit(x, y) # 모델 학습
coef = model.coef_# 회귀계수 출력
intercept = model.intercept_ # 절편 출력 
y_pred = model.predict(x) # 예측 값
lY = y_pred[-1] #예측 값의 가장 최신값
comparison_index = y_pred - y #비교 지수
lci = lY -  tp # 비교 지수의 가장 최근 값
ncm = abs(comparison_index)
nncm = ncm.ravel()
avg = sum(nncm)/len(nncm) # 평균
meanX = math.floor(avg/10) #Buying Unit

for i in range(1,11): #주문 가격 설정
    k = tp - meanX*i
    lp.append(k)

if tmp < lY[0] <= tp: #주가가 회귀선 돌파
    print("매수대기")
    
elif tp < lY[0] <= tmp:
    print("매도")
else:
    print("관망")