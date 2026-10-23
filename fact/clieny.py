import Pyro4
uri=input("enter uri:")
obj=Pyro4.Proxy(uri)
print("factorial",obj.calculate(5))
print("Mode",obj.mode([1,2,3,1,1,1]))
