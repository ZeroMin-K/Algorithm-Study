str = input()
print(''.join([alpha.upper() if alpha.islower() else alpha.lower() for alpha in str]))