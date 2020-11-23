from random import *

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f"{name} 유닛이 생성 되었습니다!")
    
    def move(self, location):
        print(f"{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]")
    
    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")


# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격 합니다. [공격력 {self.damage}]")

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "Marine", 40 ,1, 5)
    
    def stim_pack(self):
        if self.hp > 10:
            self.hp -= 10
            print(f"{self.name} : 스팀팩 사용. (HP 10 감소)")
        else:
            print(f"{self.name} : 스팀팩 사용 불가!! 체력이 부족합니다.")

class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "Tank", 150, 1, 35)
        self.seize_mode=False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        if self.seize_mode == False:
            print(f"{self.name} : 시즈모드로 전환합니다.")
            self.damage *= 2
            self.seize_mode = True
        else:
            print(f"{self.name} : 시즈모드로 해제합니다.")
            self.damage /= 2
            self.seize_mode = False

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print(f"{name} : {location} 방향으로 날아갑니다. [속도 {self.flying_speed}]")

class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "Wraith", 80, 20, 5)
        self.cloacked = False
    
    def clocking(self):
        self.cloacked != self.cloacked
        if self.cloacked:
            print("Clocking enabled!!")
        else:
            print("Clocking disabled!!")


def game_start():
    print("[Notice] New game started")

def game_over():
    print("[Notice] Game ended.")

# firebat1 = AttackUnit("firebat", 50, 5, 16)
# firebat1.attack("5'")
# firebat1.damaged(25)

# battlecruiser = FlyableAttackUnit("Battlecruiser", 500, 25, 3)

# battlecruiser.move("9'")


# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)
        self.location = location



game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()
w2 = Wraith()

attack_units = []

attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)
attack_units.append(w2)

for unit in attack_units:
    unit.move("1'")

Tank.seize_developed=True
print("[Notice] Seize_mode developed!!")

supply_depot = BuildingUnit("Supply_depot", 500, "7'")

for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stim_pack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

for unit in attack_units:
    unit.attack("1'")

for unit in attack_units:
    unit.damaged(randint(5, 20))

game_over()