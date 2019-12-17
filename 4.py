# FACTS ABOUT THE PASSWORD
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease;
# they only ever increase or stay the same (like 111123 or 135679). 

# Other than the range rule, the following are true:
# - 111111 meets these criteria (double 11, never decreases).
# - 223450 does not meet these criteria (decreasing pair of digits 50).
# - 123789 does not meet these criteria (no double).

# How many different passwords within the range given in your
# puzzle input meet these criteria?

# input: 138307-654504
start = 138307
end = 654504

# password is within range(start, end+1)
# two adjacent digits are the same
# left to right x+1 >= x
valid = 0
storage = []
for i in range(start, end+1):
    twin_digits = False  #check if at least a pair exists
    ascending = True
    for j, k in zip(str(i), str(i)[1:]):  # iterates through the digits
        #print(k, j, k>=j)
        if k >= j:
            if k == j:
                twin_digits = True
        else:
            ascending = False
            break
    #print()
    if ascending and twin_digits:
        storage.append(i)
        valid += 1

print(storage)
print(valid)
    
