n = input("Enter a number:\n")
print("Your entered number is")
j = 0
for digit in n:  # for collecting single digits
    i = int(digit)
    j = j + 1
    print(i, " ", end="")
print("\nNumber of digits in the given number is", j)
sum_ = 0
k = 0
while k < j:  # for summing
    sum_ = sum_ + int(n[k]) ** j
    k += 1
if int(n) == sum_:
    print("The number is an Armstrong Number")
else:
    print("The number is not an Armstrong Number")
