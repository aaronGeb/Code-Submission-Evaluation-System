n = input()
 
max_count = 1
current_count = 1
 
for i in range(1, len(n)):
    if n[i] == n[i - 1]:
        current_count += 1
        max_count = max(max_count, current_count)
    else:
        current_count = 1
 
print(max_count)