a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
i = 1
while(i<=a and i<= b):
  if(a%i == 0 and b%i == 0):
    gcd = i
  i += 1
print("GCD is:", gcd)

if(a>b):
    lcm=a
else:
    lcm=b
while(1):
    if(lcm%a==0 and lcm%b==0):
        print("LCM is:", lcm)
        break
    lcm=lcm+1