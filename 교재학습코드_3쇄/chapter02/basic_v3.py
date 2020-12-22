
print("\n\n========== 예제 2.25 ==========")
a_list = ("키움", "카카오", "대신")
for val in a_list:
    print(val)


print("\n\n========== 예제 2.26 ==========")
a_list = ["키움", "카카오", "네이버"]
for val in a_list:
    print(val)


print("\n\n========== 예제 2.27 ==========")
a_list = ["키움", "카카오", "네이버"]
a_list.append("대신증권")
for val in a_list:
    print(val)


print("\n\n========== 예제 2.28 ==========")
print(a_list[0])


print("\n\n========== 예제 2.29 ==========")
a_list = ["키움", "카카오", "네이버"] #list
print(a_list)
a_list[2] = "다음" #수정하기
print(a_list)
del a_list[1] #삭제하기
print(a_list)


print("\n\n========== 예제 2.30 ==========")
a_list = ["키움", "카카오", "네이버"]
for idx, val in enumerate(a_list):
    print("인덱스: %s, 값: %s" % (idx, val))


print("\n\n========== 예제 2.31 ==========")
a_dict = {"키움증권":1300, "카카오증권":1500, "네이버증권":1000}
print(a_dict.get("키움증권")) # 1300
print(a_dict['키움증권']) # 1300


print("\n\n========== 예제 2.32 ==========")
for key in a_dict.keys():
    print(a_dict.get(key))


print("\n\n========== 예제 2.33 ==========")
for key, value in a_dict.items(): #key와 value 값 모두 가져옴
    print("키값 : %s , value값 : %s" % (key, value))


print("\n\n========== 예제 2.34 ==========")
a_dict = {"키움증권":1300, "카카오증권":1500, "네이버증권":1000}
a_dict["다음증권"] = 2500
print(a_dict)


print("\n\n========== 예제 2.35 ==========")
a_dict = {"키움증권":1300, "카카오증권":1500, "네이버증권":1000}
a_dict.update({"다음증권":2500})
print(a_dict)


print("\n\n========== 예제 2.36 ==========")
a_dict = {"키움증권":1300, "카카오증권":1500, "네이버증권":1000}
a_dict["다음증권"] = 2500
a_dict["애플"] = 152000
a_dict["삼성"] = 221500
a_dict["LG"] = 25800
print(a_dict)


print("\n\n========== 예제 2.37 ==========")
a_dict = {"키움증권":1300, "카카오증권":1500, "네이버증권":1000}
a_dict.update({"다음증권":2000, "애플":152000, "삼성":221500, "LG":25800})
print(a_dict)
