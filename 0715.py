# #Unit 클래스 정의하시오.
# #생성자: hp,damage
# #메소드: 2개의 멤버변수 출력

class Unit:
    def __init__(self,name,hp,damage):
        self.hp = hp
        self.damage = damage
        self.name = name

    def printAll(self):
        print('체력: {0} 이고, 데미지 {1} 입니다. '.format(self.hp, self.damage))



marin = Unit('마린',50,5)
marin.printAll()

marin2 = Unit('마린2', 40, 10)
marin2.printAll()
#공중유닛(클로킹)
wraith1=Unit("레이스", 80, 5)
wraith2=Unit("레이스", 88, 5)
wraith2.clocking=True
if wraith2.clocking == True:
    print('{0}유닛이 {1}클로킹이 설정 되었습니다.'.format(wraith2.name, wraith2.clocking))

#공격 유닛 클래스를 정의하시오.
#클래스 이름: AttackUnit
#메소드: attack(self, location),damaged(self, damage): hp가 0이하이면 유닛은 파되되었습니다. 추력
class Attack_Unit(Unit):
    def __inint__(self,hp,name,damage):
        Unit.__init__(self,name,hp)
        
        self.damage=damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {}, 공격력{} \n ".format(Unit.hp, self.damage))
    
    def attack(self, location):
        print("{0} 유닛이 {1}로 공격 합니다.".format(Unit.name,location))

    def damaged(self, damage):
        Unit.hp -= damage
        print("{0}: 현재 체력은 {1} 입니다.".format(Unit.name, Unit.hp))
        if Unit.hp <= 0:
            print("{}유닛이 파괴되었습니다.".format(Unit.name))

class Flyable:
    def __init__(self,speed):
        self.speed = speed
        #print("{0} 유닛이 생성되었습니다.".format(Unit.name))
        print("속도 {} \n",format(self.speed))
    
    def fly(self,name,location):
        print('{} 방향으로 {} 날아갑니다. [속도: {}]'.format(name, location, self.speed))

#다중 상속 클래스 정의
class FlyableAttackUnit(Attack_Unit, Flyable):
    def __init__(self,name,hp,damage,flyspeed):
        Attack_Unit.__init__(self,name,hp,damage)
        Flyable.__init__(self, flyspeed)

valkyrie = FlyableAttackUnit('발키리',80,16,40)
valkyrie.fly(valkyrie.name,'3시')
   
#파이어벳: 공격유닛, 화염방사기, hp:50, damage: 16

# firebat = Attack_Unit(50, '파이어벳', 16)
# firebat.attack("5시")
# firebat.damaged(25)
# firebat.damaged(25)



##상속


# class Parent:
#     def __init__(self):
#         self.value="테스트"
#         print("Parent 클래스의 __init()__메소드가 호출되었습니다.")
#     def test(self):
#         print("Parent 클래스의 test() 메소드입니다.")

# #자식 클래스를 선언합니다.
# class Child(Parent):
#     def __init__(self):
#         Parent.__init__(self)
#         print("Child 클래스의 __init()__ 메소드가 호출되었습니다.")


# child=Child()


# class Parent:
#     def __init__(self):
#         self.value='테스트'
#         print('부모 클래스의 __init()__메소드가 호출되었습니다.')

#     def test(self):
#         print("부모 클래스의 test()메소드가 호출되었습니댜.")

# #상속
# class Child(Parent):
#     def __init__(self):
#         Parent.__init__(self)
#         print('부모 클래스의 test() 메소드가 호출되었습니다.')
    
# child = Child()
# child.test()
# print(child.value)


#다중상속
