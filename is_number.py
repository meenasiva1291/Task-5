#Approach 1:
x = ['123']
check = lambda x: x[0] >= 0
if check(x):
    print(f"Given {x} string is a number")

#Approach 2:
is_digit = lambda s:s.replace('.','',1).isdigit() if isinstance(s, str) else False
print(is_digit("122"))
print(is_digit('meena'))
print(is_digit('12.99'))