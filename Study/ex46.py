#마린: 공격유닛, 군인, 총을 쏠 수 있음
name = "마린"
hp = 40
damage = 5

print("{0}유닛이 생성 되었습니다.".format(name))
print("체력 : {0}, 공격력{1}\n".format(hp, damage))

#탱크 공격유닛, 탱크, 포를 쏠 수 있음 일반모드/ 시즌모드
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0}유닛이 생성 되었습니다.".format(tank_name))
print("체력 : {0}, 공격력{1}\n".format(tank_hp, tank_damage))

def attack(name, location, damage):
    print("{0} : {1}방향으로 적군을 공격합니다. [공격력{2}]".format(\
        name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print("{0}유닛이 생성 되었습니다.".format(tank2_name))
print("체력 : {0}, 공격력{1}\n".format(tank2_hp, tank2_damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank_name, "1시", tank2_damage)   #여기서 수십개의 유닛이 생성되는데 계속 만들 수는 없으니까 이때 사용 되는게 class