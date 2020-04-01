# #문제1-1
stock_name = "키움증권"
stock_price = 3900
stock_percent = 3.8
print("주식이름 : %s, 가격 : %s원, 등락율 : %s" % (stock_name, stock_price, stock_percent))

#문제1-2
print("등락율 : %s %%" % stock_percent)
print("등락율 : %s %s" % (stock_percent, "%"))





# # 문제2-2 : 1x1, 1x2 ... 9x7, 9x8, 9x9 형식으로 구구단을 출력하시오.
# for i in range(1, 10):
#     for j in range(1, 10):
#         result = i * j
#         print("%s x %s = %s" % (i, j, result))


# #문제3-1 : {“키움증권“:5000, “카카오“:3000, “네이버”:2000} 에서 3개 증권사 가격의 총합을 출력해라!
# a_dict = {"키움증권" : 5000, "카카오" : 3000, "네이버" : 2000}
# a_plus = 0
# for val in a_dict.keys():
#     a_plus = a_plus + a_dict[val]     # a_plus += a_dict[val] 형태와 같다
#     print("종목 : %s, 가격: %s " % (val, a_dict[val]))
#     print("더한값 %s " % a_plus)
#
# print(a_plus)


#문제3-2 : 예수금이 111000원이 있다. 예수금을 가지고 문제3-1의 증권사에서 원하는 만큼 사라. 그리고 남은 금액을 출력해라.
# #단 ! for문과 if문을 모두 활용해라.
# a_dict = {"키움증권" : 5000, "카카오" : 3000, "네이버" : 2000, "애플" : 1010000}
# my_account = 111000
# for val in a_dict.keys(): # keys()를 사용하면 ["키움증권', '카카오', '네이버', '애플'] 처럼 key들만 가져온다.
#     if val == "키움증권":
#         my_account = my_account - a_dict[val] * 5         # 이런 형태!!  86000 = 111000 - 5000 * 5
                                                            # my_account -= a_dict[val] * 5 이 형태도 가능
#     elif val == "카카오":
#         my_account -= a_dict[val] * 2                     # 80000 = 86000 - 3000 * 2
#     elif val == "네이버":
#         my_account -= a_dict[val] * 5
#
# print("남은 금액 : %s " % my_account)

#문제3-3 : 키움증권의 가격이 매일 1000원씩 올랐다. 10000원이 되었을 경우 종목 하나를 더 주시하기로 했다.
# 키움증권이 10000원이 되었을 때 이베스트증권 5000원짜리도 dictionary에 추가해서 출력해라!
a_dict = {"키움증권" : 5000, "카카오" : 3000, "네이버" : 2000}
ee_bool = True
while ee_bool:
    a_dict['키움증권'] = a_dict['키움증권'] + 1000

    if a_dict['키움증권'] == 10000:
        a_dict.update({"이베스트증권" : 5000}) # {"키움증권" : 5000, "카카오" : 3000, "네이버" : 2000, '이베스트증권': 5000} 처럼 이베스트증권 업데이트됨
        break

print(a_dict)
