p =float(input("p=enter principal : "))

r =float(input("r=enter rate : "))

t =float(input("t=enter time :"))

n =float(input("n= number of years : "))

SI =str(p * (1+r*t))
CI =str (p * (1+r/n) ** n*t)
print ("yusuf and sons limited")
print ("Simple Interest = " +SI)
print ("Compound Interest ="+CI)


