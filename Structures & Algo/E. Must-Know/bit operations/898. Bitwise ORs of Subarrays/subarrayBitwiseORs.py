class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        o = set()
        for i in range(len(arr)):
            o.add(arr[i])
            for j in range(i - 1, -1, -1):
                if arr[j] == arr[j] | arr[i]: break
                arr[j] |= arr[i]
                o.add(arr[j])

        return len(o)
                

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        ors = set()

        for x in arr:
            ors = {o | x for o in ors}
            ors.add(x)
            ans |= ors

        return len(ans)         