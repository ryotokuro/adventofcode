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
matching = []

for i in range(start, end):
    golden_pair = False  # check if a separated matching 2 pair exists
    ascending = True  # flag for ascending digit order
    matching = []  # tracks length of repeated sequence
    
    for j, k in zip(str(i), str(i)[1:]):  # iterates through the digits
        if k >= j:
            if k == j:
                matching.append(k)
            else:
                if len(matching) == 1:
                    golden_pair = True
                matching = []  # reset matching num that im keeping track of
        else:
            ascending = False
            break

    # part 2: if an exclusive pair of length 2 exists (golden pair)
    # then the pin is valid
    if len(matching) == 1:
        golden_pair = True
    if ascending and golden_pair:
        storage.append(i)
        valid += 1

print(valid)  # number of valid passwords
