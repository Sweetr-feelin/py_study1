def content(s1, s2):
    cur = 0
    i = 0
    while cur != len(s1):
        if s1[cur] != s2[i]:
            i = 0
        elif s1[cur] == s2[i] and i == len(s2) - 1:
            return True
        elif s1[cur] == s2[i]:
            i += 1
        cur += 1
    return False
