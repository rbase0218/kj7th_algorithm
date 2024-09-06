score = int(input())

if score < 60: print('F')
elif score > 59 and score < 70: print('D')
elif score > 69 and score < 80: print('C')
elif score > 79 and score < 90: print('B')
else: print('A')