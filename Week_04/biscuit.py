class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not len(g) or not len(s) or s[-1]<g[0]:
            return 0
        g.sort()
        s.sort()
        g_index = s_index = 0
        while g_index < len(g) and s_index < len(s):
            if s[s_index] >= g[g_index]:
                g_index += 1
            s_index += 1
        return g_index
