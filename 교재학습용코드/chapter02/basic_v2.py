print("========== 예제 2.16 ==========")
stock_name = "키움증권"
if stock_name == "키움증권":
    print("통과!")


print("\n\n========== 예제 2.17 ==========")
stock_price = 3000
if stock_price > 3000:
    print("통과!1")
elif stock_price >= 3000:
    print("통과!2")
elif stock_price <= 3000:
    print("통과!3")
else:
    print("조건에 해당하는 게 없음!")


print("\n\n========== 예제 2.18 ==========")
stock_price = 3000
if stock_price < 3000 or stock_price >= 3000:
    print("둘 중 아무거나 맞으면 출력")

print("\n\n========== 예제 2.19 ==========")
stock_price = 3000
if stock_price > 2000 or stock_price < 2500:
    print("2000~2500 사이")
elif stock_price >= 2500 and stock_price <= 3000:
    print("2500~3000 사이")

stock_price = 3000
if stock_price > 2000 and stock_price <= 3000:
    print("2001~3000 사이")
elif stock_price > 3000 and stock_price <= 4000:
    print("3001~4000 사이")


print("\n\n========== 예제 2.20 ==========")
for i in range(5, 100):
    print(i)


print("\n\n========== 예제 2.21 ==========")
for i in range(5, 100):
    print(i)

    if i == 50:
        break

print("\n\n========== 예제 2.22 ==========")
for i in range(0, 10):
    for k in range(0, 5):
        print("for 문 안에 for 문 %s" % k)


print("\n\n========== 예제 2.23 ==========")
stock_buy = True
count = 0
while stock_buy:
    count = count + 1

    if count == 10:
        break

    print(count)


print("\n\n========== 예제 2.24 ==========")
stock_buy = True
count = 0
while stock_buy:
    count = count + 1

    if count == 10:
        # break
        stock_buy = False

    print(count)
