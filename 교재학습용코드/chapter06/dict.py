print("\n\n========== 예제 6.4 ==========")
sample_dict = {"1":"테스트1", "2":"테스트2", "3":"테스트3"}

a_test = sample_dict
a_test["1"] = "변경하기"

print("할당 %s" % a_test)
print("원본 %s" % sample_dict)


print("\n\n========== 예제 6.5 ==========")
sample_dict = {"1":"테스트1", "2":"테스트2", "3":"테스트3"}

a_test = sample_dict.copy()
a_test["1"] = "변경하기"

print("할당 %s" % a_test)
print("원본 %s" % sample_dict)
