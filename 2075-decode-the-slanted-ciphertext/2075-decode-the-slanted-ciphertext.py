class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        # Time and Space: O(n) & O(n)
        N = len(encodedText)
        cols = N // rows 

        code = [[None] * cols for _ in range(rows)]
        for i, c in enumerate(encodedText):
            code[i // cols][i % cols] = c
        
        ans = []
        for i in range(cols):
            for x in range(rows):
                if i + x < cols:
                    ans.append(code[x][i+x])
        return "".join(ans).rstrip()