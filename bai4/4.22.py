print("Phạm Tiến Lập")
print("245752021610071")
result = []
for num in range(1000, 3001):
    s = str(num)
    if all(int(ch) % 2 == 0 for ch in s):
        result.append(s)
print(','.join(result))
