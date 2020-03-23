class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        lookup = [0 for x in range(len(s) + 1)]
        lookup[0:2] = [1,1]

        for i in range(2, len(s) + 1):
            # One step jump, this is because 0 MUST be a part of "10" or "20"
            if 0 < int(s[i - 1:i]):
                lookup[i] = lookup[i - 1]

            # Two step jump
            if 10 <= int(s[i - 2:i]) <= 26:
                lookup[i] += lookup[i - 2]

        print(lookup)
        return lookup[-1]

    # Bottoms up approach
    # Make a lookup, each lookup tile at i represents the # of ways to decode s[:i]
