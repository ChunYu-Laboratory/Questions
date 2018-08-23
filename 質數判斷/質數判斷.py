print('<< 質數判斷程式 >>',end='\n\n')
while True:
    n = input('請輸入大於 1 之正整數：')
    if n.isdigit():
        n = int(n)
        if n > 1:
            break
        else:
            print('輸入格式錯誤',end='\n\n')
    else:
        print('輸入格式錯誤',end='\n\n')
print()
factor = []
for x in range(1, n+1):
    if x*x > n:
        break
    if n % x == 0:
        factor.append([x,n//x])
if factor == [[1,n]]:
    print(n, 'is a prime number')
else:
    print(n,'with the following positive factors：',end='\n\n')
    print(factor)
print()
print('-----Finished-----')
