#type coversion
x = 10
y = 3.09
z = "10"
print(type(x))
print(type(y))
print(type(z))
#result = x+z
#conversion
result = x+int(z)
print (result)
result2 = str(x)+z
print(result2)
#string to float
result3 = float (z)+y
print(result3)