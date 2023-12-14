def Price_Cal(tp, meanX):
    lp = []
    for i in range(1,11): #주문 가격 설정
        k = tp - meanX*i
        lp.append(k)

