number=int(input("請輸入一個要轉換成二進位的數字;"))
binary=list()
while number > 1:
    binary.append(str(number %2))
    number //=2
binary.append(str(number))
print("".join(reversed(binary)))