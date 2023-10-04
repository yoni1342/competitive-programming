class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        k -= 1

        while k:
            nodes = self.countNodes(n, cur)
            if k >= nodes:
                cur += 1
                k -= nodes
            else:
                cur *= 10
                k -= 1

        return cur

    def countNodes(self, n, cur):
        total = 0

        nxt = cur + 1
        while cur <= n:
            total += min(n - cur + 1, nxt - cur)
            cur *= 10
            nxt *= 10

        return total