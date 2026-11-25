class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
      l=len(nums)
      hashes=[0]*(l+1)
      base=max(nums)+1
      mod=10**9+7
      power=[1]*(l+1)
      for i, num in enumerate(nums):
        hashes[i+1]=(hashes[i]*base+num)%mod
        power[i+1]=(power[i]*base)%mod
      left,right=1,l
      while left<=right:
        mid=(left+right)//2
        freq=defaultdict(int)
        found=False
        for i in range(l-mid+1):
          h=(hashes[i+mid]-(hashes[i]*power[mid]))%mod
          freq[h]+=1
        for key in freq:
          if freq[key]==1:
            found=True
            break
        if found:
          right=mid-1
        else:
          left=mid+1
      return left