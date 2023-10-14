n = int(input())
s = set(map(int, input().split()))
num_commands = int(input())

# Process commands
for _ in range(num_commands):
    command = input().split()
    if command[0] == "pop":
        if s:
            s.pop()
    elif command[0] == "remove":
        x = int(command[1])
        s.discard(x)
    elif command[0] == "discard":
        x = int(command[1])
        s.discard(x)

# Print the sum of elements in the set
print(sum(s))
