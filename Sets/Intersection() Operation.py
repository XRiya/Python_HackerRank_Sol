
n = int(input())
english_subs = set(map(int, input().split()))
m = int(input())
french_subs = set(map(int, input().split()))

# Calculate the total number of students with both subscriptions
common_students = len(english_subs.intersection(french_subs))

# Print the result
print(common_students)
