# Linear_Regression_Trading
## 1. Theory
Linear regression is a modeling technique that estimates the relationship between one or more causes and results and is mainly used in various fields such as financial market forecasting and product sales forecasting. 
The creator wanted to apply this to trading.The stock price showed an upward movement, fluctuating up and down based on the regression 
line. Based on this, we created a trading strategy based on the fact that stock prices fluctuate based on the regression line. 

선형회귀란 한 개 이상의 원인과 결과 간의 관계를 추정하는 모델링 기법으로 주로 금융 시장 예측, 제품의 판매량 예측 등 다양한 분야에서 사용된다. 제작자는 이를 트레이딩에 접목해보고자 했다.
주가가 회귀선을 기준으로 위아래로 변동하며 상승하는 움직임을 보였다. 이를 바탕으로 주가가 회귀선을 기준으로 변동한다는 사실을 기반한 트레이딩 전략을 만들었다.

참고한 사이트: [https://direction-f.tistory.com/8]

---
## 2.Trading Algorithm
1. 주가 입력 받음 (Import data with FinanacedataReader)
2. 주가를 회귀 분석 (LinearRegression Analysis with code)
3. 주가의 상태를 회귀선을 하향돌파, 또는 상향돌파하는지 탐색 (Keep watching stock chart and regression line 's state)
4. 만약 하향돌파한다면 매수준비(하향, 상향 관찰은 이전과의 기울기로 판단)(If stock chart's dicipline is smaller than 0 and cross the regression Line we have to prepare for buying)
5. 거미줄 매매를 위해 매수선의 매수단위 계산(매수단위는 회귀선과 주가간의 변동폭의 절댓값의 평균을 10으로 나눠 계산)

(Divide the average of the absolute value of the fluctuation between the regression line and the stock price by 10 to determine the purchase unit and place a purchase order.)

6. 다시 만나는 지점에서 매도 (Sell all order when stock line cross the regression line again)

---

## 3.Things to keep in mind
In this Program I use only stock price of close price. 
You can try with anothe price.
If you want to change the source of the data like yfinance, quantlib etc.
Please make sure date and closing price(or another data) are on the same row
If you make better model or have a  question about this program contact with my insatgram on my profile 
If you have a problem with pykiwoom api. I can't give you a help because I don't have any author to solve the api problem.
So if you have a problem with api use another that you can use

---

## You have to see before using this program!!!
***Caution***
API about stock(In this Program pykiwoom api) support only ***32bit*** python. So if you use 64bit python this program 
may not work

---

Using Data
The Data of Samsung(stockCode: 005930) 2018/01/01 ~ 2023/12/15 (from FinanceDatareader)
Trading With Kiwoom Securities

Python 3.12.0    ***(32bit)*** 

financedatareader 0.9.66

matplotlib 3.8.2

numpy 1.26.2

ploty 5.18.0

pygame2.5.2

scikit-learn 1.3.2

scipy 1.11.4
