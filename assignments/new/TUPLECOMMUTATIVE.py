# Assignment
# 1. Prove that tuple concatenation is not commutative: t1 + t2 != t2 + t1
# 2. Prove that tuple repetition is commutative       : t1 * 3 == 3 * t1


t1 = (10, 20)
t2 = (40, 50)

# Tuple concatenation 
print(f"{t1 + t2       =}")  # Output:  10, 20, 40, 50
print(f"{t2 + t1       =}")  # Output:  40, 50, 10, 20

# Tuple repetition
print(f"{t1 * 3        =}")  # Output: 10, 20, 10, 20, 10, 20
print(f"{3 * t1        =}")  # Output: 10, 20, 10, 20, 10, 20