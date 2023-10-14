# Enter your code here. Read input from STDIN. Print output to STDOUT
# Input
n, m = map(int, input().split())
arr = list(map(int, input().split()))
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

# Initialize happiness
happiness = 0

# Calculate happiness
for num in arr:
    if num in set_a:
        happiness += 1
    elif num in set_b:
        happiness -= 1

# Print the final happiness
print(happiness)
