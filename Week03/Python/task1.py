print("9 dan büyük bir sayı giriniz")
x=int(input())
step=0
while x>9:
 temp=x
 toplam=0
 while temp>0:
     kalan=temp%10
     toplam +=kalan
     temp //=10
 x=toplam
 step+=1
print("Final value:", x)
print("Total steps:", step)