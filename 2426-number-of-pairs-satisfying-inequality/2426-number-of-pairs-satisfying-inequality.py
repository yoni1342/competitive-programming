class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        count = 0
        
        def mergesort(l,r,arr):
            if l==r:
                return [arr[l]]

            mid = (l + r)//2

            lh = mergesort(l,mid, arr)
            rh = mergesort(mid+1, r,arr)
            
            return merge(lh, rh)
        
        def merge(a,b):
            nonlocal count

            
            ptr = 0
            for i in a:
                while ptr<len(b) and i-diff > b[ptr]:
                    ptr+=1
                
                count += len(b)-ptr
            
            p1, p2 = 0, 0
            
            res = []
            while p1<len(a) and p2<len(b):
                if a[p1] < b[p2]:
                    res.append(a[p1])
                    p1 += 1
                else:
                    res.append(b[p2])
                    p2 += 1
            
            if p1 < len(a):
                res.extend(a[p1:])
            if p2 < len(b):
                res.extend(b[p2:])
            
            return res
            
        a = [ x[0]-x[1] for x in zip(nums1, nums2)]
        mergesort(0,len(a)-1, a)
        return count