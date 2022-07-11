A,B = input().split()

def replace(To,From):
    return lambda number : number.replace(To,From)
to6 = replace('5','6')
to5 = replace('6','5')

def sum(func):
    return lambda A,B : int(func(A)) + int(func(B))

# 5 to 6 is Maximum, 6 to 5 is Minimum
print(sum(to5)(A,B) , sum(to6)(A,B))