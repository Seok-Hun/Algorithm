X = int(input())

output = 0
DP = 1

while DP!=X:
    if DP*5<=X:
        DP*=5
    elif DP*3<=X:
        DP*=3
    elif DP*2<=X:
        DP*=2
    else:
        DP+=1
    output += 1

print(int(output))