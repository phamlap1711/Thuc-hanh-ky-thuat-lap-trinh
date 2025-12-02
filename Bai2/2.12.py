print("Phạm Tiến Lập")
print("245752021610071")
a, b = 1, 2
total = 0
print(a, end=" ")
print(b, end=" ")
while a <= 4000000 - 1:
    if a % 2 == 0:
        total += a
    a, b = b, a + b
    print(a, end=" ")
print("\nTổng các số chẵn trong dãy là:", total)
