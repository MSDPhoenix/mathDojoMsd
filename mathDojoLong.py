class MathDojo:
    def __init__(self):
        self.result = 0
        print(f"result = {self.result}")
    def add(self,num,*nums):
        self.result = self.result + num
        print(f"adding {num}")
        for i in nums:
            self.result = self.result + i
            print(f"adding {i}")
        print(f"result = {self.result}")
        return self
    def subtract(self,num,*nums):
        self.result = self.result - num
        print(f"subtracting {num}")
        for i in nums:
            self.result = self.result - i
            print(f"subtracting {i}")
        print(f"result = {self.result}")
        return self
md = MathDojo()

print(md.add(2).result)
print(md.add(2,3).result)
print(md.add(2,3,5).result)

print(md.subtract(2).result)
print(md.subtract(2,3).result)
print(md.subtract(2,3,5).result)

x = md.add(2).add(2,5,1).subtract(3,2).result
print("x =",x)

