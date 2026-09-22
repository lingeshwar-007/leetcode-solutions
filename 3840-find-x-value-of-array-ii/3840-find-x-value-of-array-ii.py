class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n=len(nums)
        nums=[x%k for x in nums]
        tree_prod=[1]*(4*n)
        tree_cnt=[[0]*k for _ in range(4*n)]
        def build(node,l,r):
            if l==r:
                tree_prod[node]=nums[l]
                tree_cnt[node][nums[l]]=1
                return
            mid=(l+r)//2
            build(2*node,l,mid)
            build(2*node+1,mid+1,r)
            p1,c1=tree_prod[2*node],tree_cnt[2*node]
            p2,c2=tree_prod[2*node+1],tree_cnt[2*node+1]
            tree_prod[node]=(p1*p2)%k
            tree_cnt[node]=c1[:]
            for r_val in range(k):
                tree_cnt[node][(p1*r_val)%k]+=c2[r_val]
        def update(node,l,r,idx,val):
            if l==r:
                tree_prod[node]=val
                tree_cnt[node]=[0]*k
                tree_cnt[node][val]=1
                return
            mid=(l+r)//2
            if idx<=mid:
                update(2*node,l,mid,idx,val)
            else:
                update(2*node+1,mid+1,r,idx,val)
            p1,c1=tree_prod[2*node],tree_cnt[2*node]
            p2,c2=tree_prod[2*node+1],tree_cnt[2*node+1]
            tree_prod[node]=(p1*p2)%k
            tree_cnt[node]=c1[:]
            for r_val in range(k):
                tree_cnt[node][(p1*r_val)%k]+=c2[r_val]
        def query(node,l,r,ql,qr):
            if ql<=l and r<=qr:
                return tree_prod[node],tree_cnt[node]
            mid=(l+r)//2
            if qr<=mid:
                return query(2*node,l,mid,ql,qr)
            if ql>mid:
                return query(2*node+1,mid+1,r,ql,qr)
            p1,c1=query(2*node,l,mid,ql,qr)
            p2,c2=query(2*node+1,mid+1,r,ql,qr)
            res_p=(p1*p2)%k
            res_c=c1[:]
            for r_val in range(k):
                res_c[(p1*r_val)%k]+=c2[r_val]
            return res_p,res_c
        build(1,0,n-1)
        ans=[]
        for idx,val,start,xi in queries:
            val_mod=val%k
            update(1,0,n-1,idx,val_mod)
            _,cnt=query(1,0,n-1,start,n-1)
            ans.append(cnt[xi])
        return ans