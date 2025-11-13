R1 = 1000
R2 = 500
temp1 = 20
temp2 = 30
formula = f"({R2}-{R1})/({R1}*({tempB}-{tempA}))"
result = eval(formula)
coefficient = result*10**-3
print(formula)
print(f"{result} per oC")
print(f"{coefficient}*10^-3 per oC")
