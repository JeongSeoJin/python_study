from random import *

#일반유닛
class unit:
    def __init__(self, name, hp, speed): #__init__ = 생성자
        self.name = name #멤버 변수
        self.hp = hp 
        self.speed = speed
        print("{0} 유닛이 생성 되었습니다".format(name))
    
    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]".format(self.name, location, self.speed))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은{1}입니다".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

#공격유닛
class attack_unit(unit):#상속, 여기서 상속하려는 클래스를 정의해줌
    def __init__(self, name, hp, damage, speed):
        unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1}방향으로 적군을 공격 합니다. [공격력{2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은{1}입니다".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

#마린
class marine(attack_unit):
    def __init__(self):
        attack_unit.__init__(self, "마린", 40, 5, 1)

        #스팀팩 : 일정시간동안 이동 및 공격 속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. [hp 10 감소]".format(self.name))
        else:
            print("{0}체력이 부족하여 스팀팩을 사용하지 못합니다".format(self.name))

#탱크
class tank(attack_unit):
    #시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능, 이동은 불가
    seize_developed = False #시즈모드 개발여부

    def __init__(self):
        attack_unit.__init__(self, "탱크", 150, 35, 1)
        self.seize_mode = False

    def set_seize_mode(self):
        if tank.seize_developed == False:
            return

            #현재 시즈모드가 아닐때 ->시즈모드
        if self.seize_mode ==False:
            print("{0} : 시즈모드로 전환합니다". format(self.name))
            self.damage *=2
            self.seize_mode = True
        else:
            print("{0} : 시즈모드를 해제합니다". format(self.name))
            self.damage /=2
            self.seize_mode = False
        #현재 시즈모드일때 -> 시즈모드 해제

#드랍쉽 : 공중유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격
#다중상속 : 부모 클래스(클래스를 주는 클래스)를 2개 이상 받는 것 +자식클래스(클래스를 물려받는 클래스)

#날 수 있는 기능을 가진 클래스 (속도가 다른 유닛이 존재 = flying)speed)
class flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

#공중 공격 유닛 클래스
class flyableattackunit(attack_unit, flyable):
    def __init__(self, name, hp, damage, flying_speed):
        attack_unit.__init__(self, name, hp, damage, 0)#지상 스피드 0
        flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)  #연산자 오버로딩 : 유닛이 공중유닛일때는 fly함수, 지상유닛일때는 move함수를 만드는 것이 쥐찮으니, move라은 함수를 만듦

#레이스
class wraith(flyableattackunit):
    def __init__(self):
        flyableattackunit.__init__(self, "레이스",80, 20, 5)