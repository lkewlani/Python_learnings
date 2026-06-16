haystack = "leetcode"
needle = "leet"

for i in range(len(haystack) - len(needle) + 1):
    if haystack[i:i + len(needle)] == needle:
        print(i)
        break
else:
    print(-1)