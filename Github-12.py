#Github-12
n = int(input("請輸入一個正整數 n："))
if n < 0:
    print("請輸入正整數。")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial =factorial*i
    print(f"{n}! = {factorial}")