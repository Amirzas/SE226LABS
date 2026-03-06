print("lütfen 10 ile 100 arasında bir sayı girin")
num=int(input())
fizz_count = 0
buzz_count = 0
fizzbuzz_count = 0

while num<10 or num>100:
    print(" geçersiz sayı,lütfen 10 ile 100 arasında bir sayı girin")
    num = int(input())
x=1
while x<=num:
        if x%7==0:
            x=x+1
            continue
        if x%3==0 and x%5==0:
            print("FizzBuzz")
            fizzbuzz_count += 1


        elif x%3==0:
            print("Fizz")
            fizz_count += 1

        elif x%5==0:
            print("Buzz")
            buzz_count += 1

        else:
            print(x)
        x=x+1
print("--- Summary ---")
print("Fizz count :", fizz_count)
print("Buzz count :", buzz_count)
print("FizzBuzz count:", fizzbuzz_count)