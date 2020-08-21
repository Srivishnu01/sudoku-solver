depend={}
for i in range(1,10):
  for j in range(1,10):
    a,b=((i-1)//3)*3,((j-1)//3)*3
    lt=[]
    for x in range(1,10):
      lt.extend(((x,j),(i,x)))
    for x in range(a+1,a+4):
     for y in range(b+1,b+4):
       lt.append((x,y))
    lt=set(lt)
    lt.discard((i,j))
    depend[(i,j)]=lt
class suduko:
    def __init__(self,game,notbuilt=True,z={}):
        self.arr=game
        self.zero=z
        if notbuilt:
         for i in range(9):
            for j in range(9):
                self.update(i,j)
         self.deleteOnes()
         if len(self.zero):
           print(self.solve())
    def update(self,i,j):
        if self.arr[i][j]==0:
                  a,b=(i//3)*3,(j//3)*3
                  self.zero[(i+1,j+1)]=set(range(1,10))-set(self.arr[i]+[self.arr[x][j] for x in range(9)]+[self.arr[a+x][b+y] for x in (0,1,2) for y in (0,1,2)])
    def deleteOnes(self):
        atleat=False
        szks=tuple(self.zero.keys())
        for tempKey in szks:
            temp=self.zero[tempKey]
            if len(temp)==1:
                i,j=tempKey
                k=tuple(temp)[0]
                self.arr[i-1][j-1]=k
                del self.zero[tempKey]
                atleat=True
                for key in set(self.zero.keys())&depend[tempKey]:
                    self.zero[key].discard(k)
                    if not len(self.zero[key]):
                      return True
        if atleat:
            if self.deleteOnes()==True:
              return True
    def solve(self):
      tst=tuple(self.zero.keys())[0]
      psb=tuple(self.zero[tst])
      for ni in psb:
        z={}
        for x in self.zero.keys():
          z[x]=set(list(self.zero[x])+[])
        i,j=tst
        ac=[x[:] for x in self.arr]
        ac[i-1][j-1]=ni
        del z[tst]
        flag=False
        for key in set(z.keys())&depend[tst]:
             z[key].discard(ni)
             if not len(z[key]):
               flag=True
               break
        if flag: continue
        s=suduko(ac, False, z)
        del ac
        del z
        if s.deleteOnes()==True:
          continue
        if not len(s.zero) or s.solve():
           self.arr=s.arr
           return True
      else:
        return False
    def __str__(self):
        ret="\n"
        for row in self.arr:
            for val in row:
                ret+=str(val)+" "
            ret+="\n"
        return ret
game=[[int(x) for x in list(input())] for i in range(9)]
print(suduko(game))

'''
950000800
000701000
200000000
037400000
000050900
000000000
000600003
000090040
000000017
'''
