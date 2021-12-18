class statistics():
    def __init__(self,numbers=[]):
        self.numbers=numbers
        self.f1=False
        self.f2=False
        self.f3=False
        self.f4=False
    def display_all(self):
        for self.i in self.numbers:
            print(self.i,"",end="")
        print()
    def new(self,numb):
        self.numbers.append(numb)
        self.f1=False
        self.f2=False
        self.f3=False
        self.f4=False
    def maxx(self):
        self.maxx=self.numbers[0]
        for self.i in self.numbers:
            if self.i>self.maxx: self.maxx=self.i
        self.f1=True
    def minn(self):
        self.minn=self.numbers[0]
        for self.i in self.numbers:
            if self.i<self.minn: self.minn=self.i
        self.f2=True
    def mean(self):
        self.s=0 
        for self.i in self.numbers:
            self.s+=self.i
        self.mean=self.s/len(self.numbers)
        self.f3=True
    def median(self):
        if len(self.numbers)%2==1: self.median=self.numbers[len(self.numbers)//2]
        else: self.median=(self.numbers[len(self.numbers)//2-1]+self.numbers[len(self.numbers)//2])/2
        self.f4=True
    def display_cal(self):
        if self.f1: print(f"maximum: {self.maxx}")
        else: print("maximum not determined")
        if self.f2: print(f"minimum: {self.minn}")
        else: print("minimum not determined")
        if self.f3: print(f"arithmetic mean: {self.mean}")
        else: print("arithmetic mean not determined")
        if self.f4: print(f"median: {self.median}")
        else: print("median not determined")

#numbers!=None and  if type(numbers) is list: else: self.numbers=[]
x=[12, 37, 6, 9, 17]
q=statistics(x)
q.new(64)
q.display_all()
q.minn()
q.maxx()
q.median()
q.mean()
q.display_cal()
q.new(24)
q.display_cal()
