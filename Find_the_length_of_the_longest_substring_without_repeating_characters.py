s = "abcabcbb"

max_length = 0
start = 0

last_seen = {}

for i in range(len(s)):
    char = s[i]

    if char in last_seen and last_seen[char] >= start:
        
        start = last_seen[char] + 1
        
        last_seen[char] = i
        
    
        
max_length = max(max_length, i - start + 1) 

print("Length of the longest substring without repeating characters :", max_length)       
        
