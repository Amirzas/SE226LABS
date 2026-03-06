n = int(input("Lütfen 3 ile 9 arasında bir sayı girin: "))

while n < 3 or n > 9:
    n = int(input("Lütfen 3 ile 9 arasında bir sayı girin: "))

k = 1
direction = 1

while k > 0:
    i = 1
    while i <= k:
        print(i, end="")
        i += 1

    print()

    if k == n:
        direction = -1

    k += direction