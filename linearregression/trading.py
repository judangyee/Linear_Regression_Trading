from pykiwoom.kiwoom import *
import pygame

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)
account_list = kiwoom.GetLoginInfo("ACCNO")
account = account_list[0]
df = kiwoom.block_request("opw00001",
                          계좌번호=account,
                          비밀번호="",
                          비밀번호입력매체구분="00",
                          조회구분=2,
                          output="예수금상세현황",
                          next=0)

#소리
buy_sound = pygame.mixer.Sound("linearregression/Buyorder.wav") # 매수 주문이 체결되었습니다
sell_order = pygame.mixer.Sound("linearregression/Sellorder.wav") # 매도 주문이 체결 되었습니다

# p: 종목코드 /q:수량
def BuyOrder(p, q): #매수 모듈
    accounts = kiwoom.GetLoginInfo("ACCNO")
    stock_account = accounts[0]
    kiwoom.SendOrder("시장가매수", "0101", stock_account, 1, p, q, 0, "03", "")
    return print(p, "매수주문이 체결되었습니다."), buy_sound.play()

def SellOrder(p, q): #매도 모듈
    accounts = kiwoom.GetLoginInfo("ACCNO")
    stock_account = accounts[0]
    kiwoom.SendOrder("시장가매도", "0101", stock_account, 2, p, q, 0, "03", "")
    return print(p, "매도 주문이 체결 되었습니다."), sell_order.play()

def soundtest():
    return buy_sound.play(), sell_order.play()

def deposit_resived(): #예수금 확인 모듈
    dr = int(df['예수금'][0])
    return dr