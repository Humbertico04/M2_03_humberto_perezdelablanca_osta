A=int(input("Dime un número int: "))
print(str(A).rjust(len(str(A))+5, '0'))

print("\n")

B=float(input("Dime un número float: "))
print('{:.3f}'.format(B).zfill(9))