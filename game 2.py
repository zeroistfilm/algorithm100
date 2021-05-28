
class Charcter(object):
    def __init__(self, name, hp, power):
        self.hp  = 1000
        self.name = name
        self.power = power

    def isAlive(self):
        return self.hp>0

    def getAttacked(self, damage):
        if self.isAlive():
            self.hp = self.hp-damage if self.hp>=damage else 0
        else:
            print(f"{self.name}은 이미 죽었습니다.")

    def attack(self, other_characther):
        if self.isAlive():
            other_characther.getAttacked(self.power)

    def __str__(self):
        return f"{self.name} 님의 hp는 {self.hp}만큼 남았습니다."

character1 = Charcter("타키탸키26", 100, 50)
character2 = Charcter("파이리12", 500, 70)


character1.attack(character2)
character2.attack(character1)
character2.attack(character1)
character2.attack(character1)

print(character1)
print(character2)