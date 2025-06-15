#Github-14
numbers = []
print("請輸入 10 個整數(限1~10)↓")
for i in range(10):
    num = int(input("請輸入第 " + str(i + 1) + " 個整數："))
    numbers.append(num)
min_value = min(numbers)
print("最小值為：", min_value)