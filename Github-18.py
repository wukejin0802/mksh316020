#Github-18
def compute(a, b):
    return a ** b
a = int(input("請輸入整數 a："))
b = int(input("請輸入整數 b："))
result = compute(a, b)
print(f"{a} 的 {b} 次方為：{result}")