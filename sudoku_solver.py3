def oneToNine(l):
    for i in range(1,10):
       if i not in l:
           return False
    else:
        return True
class suduko:
    def __init__(self,game):
        self.arr=game
        self.zero={}
        for i in range(9):
            for j in range(9):
                self.update(i,j)
    def update(self,i,j):
        if self.arr[i][j]==0:
                   self.zero[(i,j)]=list(range(1,10))
                   a,b=(i//3)*3,(j//3)*3
                   for k in self.arr[i]+[self.arr[x][j] for x in range(9)]+[self.arr[a+x][b+y] for x in (0,1,2) for y in (0,1,2)]:
                       if k in self.zero[(i,j)]:
                           self.zero[(i,j)].remove(k)
    def updateAll(self,i,j):
        for ii in range(9):
            for jj in range(9):
                if ii==i or jj==j or (i//3==ii//3 and j//3==jj//3):
                    self.update(ii,jj)
    def solve(self):
        temp=self.zero.keys()
        for key in temp:
            i,j=key
            posy=self.zero[key]
            self.zero.pop(key)
            for p in posy:
                self.arr[i][j]=p
                self.updateAll(i,j)
                if self.isSolved() or self.solve():
                    return True
            self.zero[key]=posy
            self.arr[i][j]=0
            self.updateAll(i,j)
        else:
            return False
    def isSolved(self):
        g=self.arr
        for i in range(9):
            if not oneToNine(g[i]) or not oneToNine([g[x][i] for x in range(9)]):
                return False
        for i in range(0,9,3):
            for j in range(0,9,3):
                if not oneToNine([g[i+x][j+y] for x in (0,1,2) for y in (0,1,2)]):
                    return False
        return True
    def __str__(self):
        ret="\n"
        for row in self.arr:
            for val in row:
                ret+=str(val)+" "
            ret+="\n"
        return ret
game=[[int(x) for x in input().split()] for i in range(9)]
s=suduko(game)
print(s.solve(),s)
input()

'''1 2 3 4 5 6 7 8 9
4 5 6 7 8 9 1 2 3
7 8 9 1 2 3 4 5 6
2 3 1 5 6 4 8 9 7
5 6 4 8 9 7 2 3 1
8 9 7 2 3 1 5 6 4
3 1 2 6 4 5 9 7 8
6 4 5 9 7 8 3 1 2
9 7 8 3 1 2 6 4 5
'''
