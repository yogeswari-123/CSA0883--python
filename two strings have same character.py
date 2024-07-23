def count_matching_chars(s1, s2):
    count = 0
    for i in range(min(len(s1), len(s2))):
        if s1[i] == s2[i]:
            count += 1
    return count

S1 = "what"
S2 = "watch"

matches = count_matching_chars(S1, S2)
print("Number of matching characters in same index:", matches)
