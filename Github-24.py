#Github-24
scores = []
for i in range(10):
    score = float(input(f"請輸入第{i+1}個成績: "))
    scores.append(score)
min_score = min(scores)
max_score = max(scores)
temp_scores = scores.copy()
temp_scores.remove(min_score)
temp_scores.remove(max_score)
total = sum(temp_scores)
average = total / len(temp_scores)
print(f"去除最小值({min_score})與最大值({max_score})後的加總為: {total}")
print(f"去除最小值與最大值後的平均為: {average:.2f}")
