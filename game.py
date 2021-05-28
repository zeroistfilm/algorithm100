from abc import *

class character(metaclass=ABCMeta):
    def __init__(self, name, health_point, striking_power, defensive_power):
        self.name = name
        self.health_point = health_point
        self.striking_power = striking_power
        self.defensive_power = defensive_power

    def getInfo(self):
        print(self.name, self.health_point, self.striking_power, self.defensive_power)



    @abstractmethod
    def Attack(self, other):
        pass

    @abstractmethod
    def Receive(self,striking_point ):
        pass


class Warrior(character):
    def Attack(self, other):
        print("칼로 찌른다!", self.striking_power)
        other.Receive(self.striking_power)

    def Receive(self, striking_point):
        self.health_point -=striking_point
        if self.health_point<0:
            self.health_point = 0
            print("죽음")

    def __str__(self):
        return f"{self.name}의 상태 : {self.health_point} "

class Elf(character):

    def __init__(self, name, health_point=100, striking_power=3, defensive_power=3):
        super().__init__(name, health_point, striking_power, defensive_power)
        self.manteau=0

    def Attack(self, other):
        print("마법을 쓴다!", self.striking_power)
        other.Receive(self)


    def Receive(self, striking_point):
        print(f"{self.name} {striking_point} 공격받음!")

        if self.manteau>1:
            if self.manteau - striking_point<0:
                striking_point -=self.manteau
                self.manteau=0
            else:
                striking_point -= self.manteau

        self.health_point -=striking_point
        if self.health_point<0:
            self.health_point=0
            print("죽음")



    def WearManteau(self):
        self.manteau+=1
        print(f"망토를 입음{self.manteau}")

    def __str__(self):
        return f"{self.name}의 상태 : {self.health_point} | {self.manteau}"


player1 = Warrior('a',100, 20,10)
player2 = Elf('b',100, 15,15)


player1.Attack(player2)
print(player2)
for i in range(10):
    player2.WearManteau()

player1.Attack(player2)
print(player2)


player1.Attack(player2)
player1.Attack(player2)
player1.Attack(player2)
player1.Attack(player2)
print(player2)
