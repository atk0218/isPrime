class Prime:
    def __init__(self,num):
        self.num = num

    def isPrime(self):
        if self.num < 2:
            return False
        for i in range(2,self.num):
            if self.num % i * i == 0:
                return True
        return False

prime = Prime(17)
if not prime.isPrime():
    print("Prime")
else:
    print("Not Prime")
