class circularstack:
  def __init__(self):
    self.cs=[]
    self.limit=int(input("enter limit"))
    self.top=None
  def isfull(self):
    if len(self.cs) == self.limit:
      return True
    else:
      return False
  def isempty(self):
    if len(self.cs)== 0:
      return True
    else:
      return False
  def display(self):
    if self.isempty():
      print("circular stack underflow")
    else:
      for i in self.cs:
        print(i,end= " ")
      print()
  def push(self,ele):
    if self.isfull() :
      print("circular stack overflow")
    else:
      if self.top==None:
        self.top=0
      else:
        self.top=(self.top+1)%self.limit
      self.cs.append(ele)
  def pop(self):
    if self.isempty():
      print("circular stack underflow")
    else:
      print(self.cs.pop())
      if self.top == self.limit:
        self.top = 0
      else:
        self.top=(self.top+1)%self.limit
  def peek(self):
    if self.isempty():
      print("circular stack underflow")
    else:
      print(self.cs[-1])
cs=circularstack()
while True:
  print("1.Push,2.Pop,3.peek")
  print("4.display 5.exit")
  ch=int(input("enter your choice"))
  if ch==1:
    ele=int(input("enter element"))
    cs.push(ele)
  elif ch==2:
    cs.pop()
  elif ch==3:
   cs.peek()
  elif ch==4:
   cs.display()
  elif ch==5:
    break
  else:
    print("invalid choice try again")
