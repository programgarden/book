print("\n\n========== 문제 3 ==========")
kakao_price = 1000
kiwoom_price = 500

for i in range(0, 3):
    kakao_price += 500
    kiwoom_price += 1000

if kakao_price > kiwoom_price:
    print("카카오가 더 높다")
elif kakao_price < kiwoom_price:
    print("키움이 더 높다")
elif kakao_price == kiwoom_price:
    print("키움과 카카오가 같다")


print("\n\n========== 문제 4 ==========")
for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        print("%s x %s = %s" % (i, j, result))

