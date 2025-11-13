metal = 3.92
R = 50
temp = 20
temp_change = 650
formula = f"{R}*(1+{metal}*10**-3*({temp_change}-{temp}))"
result = eval(formula)
print(formula)
print(f"{R}*(1+{metal}*10**-3*{temp_change-temp})")
print(f"{R}*({1+metal*10**-3*(temp_change-temp)})")
print(f"{result} Ω")
