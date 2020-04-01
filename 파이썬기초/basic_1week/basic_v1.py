#-------- 내용 출력하기, (%s:문자열 %d:정수 %f:부동소수점)

print("Hello world")
#Hello world

print("Hello world" + " Thank you")
#Hello world Thank you

print(900629)
#900629

print("%s 입니다." % "홍길동")
#홍길동 입니다.

print("이름은 %s 이고 %s에 삽니다." % ("홍길동", "서울"))
#이름은 홍길동 이고 서울에 삽니다.


# -------- 변수 만들어 보기

#int 변수, 최대값 : 9223372036854775807
stock_price = 3900
print(stock_price)
stock_price = 4500
print(stock_price)
stock_price = type(stock_price) # <class 'int'>
print(stock_price)

#float 변수
stock_percent = 3.8
print(stock_percent)
stock_percent = type(stock_percent) #<class 'float'>
print(stock_percent)

#string 변수
stock_name = "홀딩스"
print(stock_name)
stock_name = type(stock_name) #<class 'str'>
print(stock_name)

stock_name = "3900" # 3900
print(stock_name)
stock_name_type = type(stock_name) #<class 'str'>
print(stock_name_type)


#bool 변수
stock_buy = False
print(stock_buy)
stock_buy_type = type(stock_buy) #<class 'bool'>
print(stock_buy_type)


#--------- 변수들 덧셈/뺄셈 등.. 해보기
#int 더하기
stock_price = 2000
stock_price2 = 2500
stock_plus = stock_price + stock_price2
print(stock_plus)

#int 빼기
stock_price = 2000
stock_price2 = 1000
stock_plus = stock_price - stock_price2
print(stock_plus)

#int 곱하기
stock_price = 1000
stock_price2 = 1200
stock_plus = stock_price * stock_price2
print(stock_plus)

#int 나누기
stock_price = 2000
stock_price2 = 2200
stock_plus = stock_price / stock_price2
print(stock_plus)
stock_plus = stock_price // stock_price2
print(stock_plus)

#int 나눈 나머지 값
stock_price = 1000
stock_price2 = 900
stock_plus = stock_price % stock_price2
print(stock_plus)
