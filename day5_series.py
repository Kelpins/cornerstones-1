n = int(input("positive value for n: "))
sequence = []
for i in range(1,n+1):
    sequence.append(1 / i**3)
print(sequence)
print(sum(sequence))