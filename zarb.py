print("***************************")
n = int(input("Please Enter n: "))
m = int(input("Please Enter m: "))
print("***************************")
# ساخت جدول ضرب
for i in range(1, n+1):
    for j in range(1, m+1):
        print(i*j, end='\t')
    print()
print("***************************")
