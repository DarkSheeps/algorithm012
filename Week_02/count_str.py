import collections
def isAnagram(s: str, t: str) -> bool:
    # print(collections.Counter(s))
    # return collections.Counter(s) == collections.Counter(t)
    if len(s) == len(t):
        set_fir_str = set(s)
        if set_fir_str == set(t):
            for i in set_fir_str:
                if s.count(i) != t.count(i):
                    return False
            return True
        return False
    else:
        return False

if __name__ == '__main__':
    print(isAnagram(s = "a", t = "b"))