print("========== 예제 2.1 ==========")
print("Hello world")


print("\n\n========== 예제 2.2 ==========")
print("Hello world")
#Hello world


print("\n\n========== 예제 2.3 ==========")
print("Hello world" + " Thank you")
#Hello world Thank you


print("\n\n========== 예제 2.4 ==========")
print(900629)
#900629


print("\n\n========== 예제 2.5 ==========")
print("%s 입니다." % "홍길동")
#홍길동 입니다.
print("%s 입니다." % "이순신")
#이순신 입니다.
print("%s원 입니다." % 5000)
#5000원 입니다.


print("\n\n========== 예제 2.6 ==========")
print("이름은 %s 이고 %s에 삽니다." % ("홍길동", "서울"))
#이름은 홍길동 이고 서울에 삽니다.


print("\n\n========== 예제 2.7 ==========")
#int 변수, 최대값 : 9223372036854775807
stock_price = 3900
print(stock_price)
stock_price = 4500
print(stock_price)
stock_price_type = type(stock_price) # <class 'int'>
print(stock_price_type)


print("\n\n========== 예제 2.8 ==========")
#float 변수
stock_percent = 3.8 # 3.8
print(stock_percent)
stock_percent_type = type(stock_percent) #<class 'float'>
print(stock_percent_type)


print("\n\n========== 예제 2.9 ==========")
#string 변수
stock_name = "홀딩스" # 홀딩스
print(stock_name)
stock_name_type = type(stock_name) #<class 'str'>
print(stock_name_type)
stock_name = "3900" # 3900
print(stock_name)
stock_name_type = type(stock_name) #<class 'str'>
print(stock_name_type)


print("\n\n========== 예제 2.10 ==========")
#bool 변수
stock_buy = False
print(stock_buy)
stock_buy_type = type(stock_buy) #<class 'bool'>
print(stock_buy_type)


print("\n\n========== 예제 2.11 ==========")
stock_price = 2000
stock_price2 = 2500
stock_result = stock_price + stock_price2
print(stock_result) # 4500


print("\n\n========== 예제 2.12 ==========")
stock_price = 2000
stock_price2 = 1000
stock_result= stock_price - stock_price2
print(stock_result) # 1000


print("\n\n========== 예제 2.13 ==========")
stock_price = 1000
stock_price2 = 1200
stock_result = stock_price * stock_price2
print(stock_result) # 1200000


print("\n\n========== 예제 2.14 ==========")
stock_price = 2000
stock_price2 = 2200
stock_result = stock_price / stock_price2
print(stock_result) # 0.9090909090909091
stock_result = stock_price // stock_price2
print(stock_result) # 0


print("\n\n========== 예제 2.15 ==========")
stock_price = 1000
stock_price2 = 900
stock_result = stock_price % stock_price2
print(stock_result) # 100
