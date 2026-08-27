class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        arr = defaultdict(list)
        squ= defaultdict(list)
        for i in range(9):
            print("hello")
            s=set()
            for j in range(9):
                val=board[i][j]
                if val.isdigit():
                    i1= i//3
                    j1=j//3
                    sq=str(i1)+str(j1)
                    if val in squ[sq]:
                        return False
                    squ[sq].append(val)
                    if val in arr[str(j)]:
                        return False
                    arr[str(j)].append(val)
                    if val in s:
                        return False
                
                    s.add(val)
            print(s)
            print(arr)
            print(squ)
        return True