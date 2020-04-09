print("\n\n========== 문제 5 ==========")
a_dict = {"키움증권" : 5000, "카카오" : 3000, "네이버" : 2000}
a_plus = 0
for val in a_dict.keys():
    a_plus = a_plus + a_dict[val] # a_plus += a_dict[val] 형태와 같다
    print("종목 : %s, 가격: %s " % (val, a_dict[val]))
    print("더한값 %s " % a_plus)


print("\n\n========== 문제 6 ==========")
a_dict = {"키움증권": 5000, "카카오": 3000, "네이버": 2000}
my_account = 111000
for val in a_dict.keys():
    if val == "키움증권":
        my_account = my_account - a_dict[val] * 5
    elif val == "카카오":
        my_account -= a_dict[val] * 2
    elif val == "네이버":
        my_account -= a_dict[val] * 5

print("남은 금액 : %s " % my_account)


print("\n\n========== 문제 7 ==========")
a_dict = {"키움증권" : 5000, "카카오" : 3000, "네이버" : 2000}
ee_bool = True
while ee_bool:
    a_dict['키움증권'] = a_dict['키움증권'] + 1000

    if a_dict['키움증권'] == 10000:
        a_dict.update({"이베스트증권" : 5000})
        break

print(a_dict)
