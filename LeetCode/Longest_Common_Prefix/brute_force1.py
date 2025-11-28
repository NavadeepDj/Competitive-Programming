def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        minstr = strs[0]
        # m = len(minstr)
        for i in range(1, len(strs)):
            if len(minstr) > len(strs[i]):
                minstr = strs[i]

        m = len(minstr)
        print(minstr)
        if m == 0:
            return ""
        for i in range(m):
            for j in range(1, len(strs)):
                if strs[0][i] != strs[j][i]:
                    return lcp
            else:
                lcp += strs[0][i]
                print("lcp",lcp)
        return lcp
