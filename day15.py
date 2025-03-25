#상속

#부모클래스만들기
class Parent:
    def introduce(self):
        print("저는 부모입니다.")

#자식클래스 만들기
class Child(Parent):
    pass
    # def introduce(self):       #메소드 오버라이딩
    #     print("저는 자식입니다.")

child = Child()
child.introduce()


class Car:
    def __init__(self, model, price):  #객체 생성(속성)
        self.model = model
        self.price = price

    def drive(self):    #메소드 정의
        print(f"{self.model}가 앞으로 전진합니다.")

class ElecCar:
    pass
    def __init__(self, model, price, energy_efficiency):
        self.model = model
        self.price = price
        self.energy_efficiency = energy_efficiency

    def drive(self):
        print(f"{self.model}이 전기로 전진합니다.")


class ElecCar(Car):
    pass

    def __init__(self, model, price, energy_efficiency):
        #Car().__init__(self, model, price
        super().__init__(model, price)    # super 쓰면 self 필요없음
        self.energy_efficiency = energy_efficiency

    def drive(self):
        super().drive()       #부모클래스의 메소드를 그대로 호출             #오버라이딩
        print(f"{self.model}이 전기로 전진합니다.")


ev6 = ElecCar("ev6", "5000", "60kWh")
ev6.drive()


###다단계상속###
class GrandParent:
    def introduce(self):
        print("우리는 할머니 할아버지")


class Parent(GrandParent):
    def introduce(self):
        super().introduce()       #부모인 Grandparent  물려받아 오버라이딩
        print("우리는 엄마아빠")

class child(Parent):
    def study(self):
        super().introduce()       #부모인 Parent 의 introduce()
        print("우리는 자식")

child1 = Child()
child1.introduce()  #먼저 부모인 Parent 의 introduce, 그 후 Parent 코드에 있는 Grandparent의 코드로 가기 때문에
                    #순서대로 "우리는 엄마아빠", "우리는 할머니할아버지"가 출력되고 마지막에 "우리는 자식" 이 출력


###다중상속
class Father:
    def drive(self):
        print("운전을 잘함")

class Mother:
    def cook(self):
        print("운전을 잘함")

class Child(Father, Mother):   #2개의 클래스를 상속받음
    def study(self):
        print("공부를 잘함")


child1 = Child()
child1.drive()
child1.cook()
child1.study()


#======================================================================================
class Animal:
    def breathe(self):
        print("숨을 쉴 수 있어요")

class Swimmer:
    def swim(self):
        print("헤엄을 칠 수 있어요")

class Fish(Animal, Swimmer):
    pass

nimo = Fish()
nimo.breathe()
nimo.swim()


class GrandParent:
    def introduce(self):
        print("우리는 할머니 할아버지")

class Father(GrandParent):
    def doctor(self):
        print("나는 의사")

class Mother:
    def rich(self):
        print("나는 부자")

####==============여기까지가 다단계상속

class Child(Father, Mother):   #아이는 엄마, 아빠 다중상속
    pass
    def smart(self):
        print("나는 똑똑하다")

child = Child()
child.rich()
child.smart()
child.doctor()

class A:
    def introduce(self):
        print("나는 A")

class B:
    def introduce(self):
        print("나는 B")

class C:
    def introduce(self):
        print("나는 C")

# class D:
#     def introduce(self):
#         print("나는 D")

class Child(A, B, C):
    def introduce(self):
        print(Child.mro())   #MRO 순서 알고 싶을 때
        super().introduce()  #다중상속ㅇ의 경우 부모클래스가 다수일 경우   #MRO에 따라 첫번째 부모클래스 호출
        super(B, self).introduce()  #해당 클래스의 다음을 출력  ->  B 다음 클래스인 C 출력
        super(A, self).introduce()  #해당 클래스의 다음을 출력  ->  A 다음 클래스인 B 출력
        C.introduce(self)           #특정 클래스를 출력할 때 -> 잘 쓰진 않음
child = Child()
child.introduce()


##MRO (Method Resolution Order) 메소드 결정 순서 => 미리 부모 클래스들의 순서를 정해둔 것

#=====================================================================================
#예제 - 하이브리드 차 만들기

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand}의 {self.model}가 시동을 겁니다.")

    def stop(self):
        print(f"{self.bramd}의 {self.model}가 정지합니다.")

class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        # self.brand = brand
        # self.model = model
        super().__init__(brand, model)  #부모인 Car 의 메소드 상속받음
        self.battery_capacity = battery_capacity  #전기차의 속성 추가

    def charge(self):
        print(f"{self.brand}의 {self.model}가 배터리를 충전합니다.")

class GasolineCar(Car):
        def __init__(self, brand, model, fuel_tank_capacity):
            super().__init__(brand, model)  #부모인 Car 의 메소드 상속받음
            self.fuel_tank_capacity = fuel_tank_capacity  #가솔린차의 속성 추가

        def refuel(self):
            print(f"{self.brand}의 {self.model}가 연료를 주유합니다.")

#여기까지는 다단계속성(Car - Electric, Gasoline)


##다중속성
#문제점 생긴 부분(처음 코드)
class HybridCar(Car, ElectricCar, GasolineCar):
    def __init__(self, brand, model, battery_capacity, fuel_tank_capacity):
        print(HybridCar.mro())
        Car.__init__(self, brand, model)
        ElectricCar.__init__(self, battery_capacity)
        GasolineCar.__init__(self, fuel_tank_capacity)

        # super().__init__(brand, model, battery_capacity)  #이 init을 타고 Electric init으로 감 그러면 electric init  을 타고 Car 로 가야하는데 Gasoline 으로 가는 것이 문제
        # super(ElectricCar, self).__init__(brand, model, fuel_tank_capacity)

        #다른 방법 - 직접 집어넣기 - 나오긴 하지만 상속은 아님
        #class HybridCar(Car, ElectricCar, GasolineCar):
        # Car.__init__(self, brand, model)
        # ElectricCar.__init__(self, battery_capacity)
        # GasolineCar.__init__(self, fuel_tank_capacity)
    def switch_mode(self, mode):
        if mode == "electric":
            print(f"{self.brand}의 {self.model}가 전기모드로 전환됩니다.")
        elif mode == "gasoline":
            print(f"{self.brand}의 {self.model}가 내연기관모드로 전환됩니다.")
        else:
            print("잘못된 모드입니다.")


hybrid = HybridCar("hyundai", "sonata", "60kWh", "50L")
hybrid.switch_mode("electric")
hybrid.stop()
hybrid.start()
hybrid.charge()
hybrid.refuel()


##문제점






