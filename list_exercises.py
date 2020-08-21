numbers = []
for i in range(5):
    numbers.append(int(input("Number:")))

print(numbers[0])
print(numbers[len(numbers)-1])
print(min(numbers))
print(max(numbers))
print(float(sum(numbers)/len(numbers)))
