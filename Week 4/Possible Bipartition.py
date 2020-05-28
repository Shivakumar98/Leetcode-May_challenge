Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.

 

Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]

Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false

Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false

 

Note:

    1 <= N <= 2000
    0 <= dislikes.length <= 10000
    1 <= dislikes[i][j] <= N
    dislikes[i][0] < dislikes[i][1]
    There does not exist i != j for which dislikes[i] == dislikes[j].




class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        d={}
        for i in dislikes:
            if i[0] in d:
                d[i[0]].add(i[1])
            else:
                d[i[0]]=set([i[1]])
            if i[1] in d:
                d[i[1]].add(i[0])
            else:
                d[i[1]]=set([i[0]])
        print(d)
        
        seen={}
        
        for i in range(1,N+1):
            if i not in seen:
                seen[i]=0
                stack=[i]
                while stack:
                    a=stack.pop()
                    if a in d:
                        for b in d[a]:
                            if b in seen:
                                if seen[a]==seen[b]:
                                    return False
                            else:
                                seen[b]=(seen[a]+1)%2
                                stack.append(b)
        print(seen)
        
        return True
