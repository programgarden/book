#if문
#단순형태
stock_name = "키움증권"
if stock_name == "키움증권":
    print("통과!")

#조건 부등호
stock_price = 3000
if stock_price > 3000:
    print("통과!1")
elif stock_price >= 3000:
    print("통과!2")
elif stock_price <= 3000:
    print("통과!3")
else:
    print("조건에 해당하는게 없음!")

#조건 부등호2
stock_price = 3000
if stock_price < 3000 or stock_price >= 3000:
    print("둘중 아무거나 맞으면 출력")


#조건 부등호3
stock_price = 3000
if stock_price > 2000 or stock_price < 2500:
    print("2000~2500 사이")
elif stock_price >= 2500 and stock_price <= 3000:
    print("2500~3000 사이")


# for 문
# for문 안에 break
for i in range(5, 100):
    print(i)

    if i == 50:
        break

#for문 안에 for문
for i in range(0, 10):
    if i == 5:
        for k in range(0, 5):
            print("for문 안에 for문 %s" % k)


# while 문
# while문 형태
stock_mesu = True
count = 0
while stock_mesu:
    count = count + 1

    if count == 10:
        # break
        stock_mesu = False

    print(count)
