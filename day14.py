class Car:  #클래스 정의
    pass

# a = 10
# if a < 100:
#     pass        #빨간 줄 안 뜨게 임시로 적어둘 땐 pass

#클래스 정의
class Car:
    def __init__(self, model, price):  #생성자를 정의하는 코드    #생성자는 호출 안해도 됨
        self.model = model          #model, price 속성이 있어야함을 정의한 것
        self.price = price
        print(f"모델 이름:{self.model} 가격:{self.price} 객체 생성!!")


    def __del__(self):   #프로그램 종료 시 자동 소멸되기 때문 => 소멸되고 있었지만 안 보였을 뿐
        print(f"{self.model} 의 객체가 소멸됨!!")  #눈에 보이는 것이 이 코드의 시점일 뿐

#self는 자기 자신을 의미, 즉 객체를 의미

    def drive(self, speed, distance):  #객체에 기능을 부여하는 코드
        print(f"{self.model}가 {speed}의 속도로 {distance}km 만큼 전진")


car1 = Car("avante", 2400)  #Car1 이라는 객체 생성
car1.is_n = "아님"  #car1 에만 해당하는 "멤버변수"추가    객체.속성 =
print(f"{car1.is_n}")

print(f"car1의 모델명: {car1.model}")
print(f"car1의 가격: {car1.price}")

car1.drive(80,1) #car1(객체) 이라고 객체를 특정해줬기 때문에 self 생략 가능
#Car.drive(car1, 80, 2) #Car(클래스)만 적으면 car1(객체)를 써줘야함
# -> self생략 불가능이므로 car1 이라고 객체를 특정해줌

print(isinstance(car1,Car))    #객체와 인스턴스가 클래스 내에 있는 게 맞는지
car2 = Car("santafe", 4000)  #Car2 이라는 객체 생성
car2.drive(50, 10)


#del car1   #코드의 중간에서 강제 소멸시킬 때, 그게 아니면 자동 소멸되고 있음

#RPG 게임 만들 때
#player 라는 객체-닉네임, 레벨, 경험치,  ->  생성자로 정의
#한 게임 끝나면 소멸되기 때문에 그 전에 저장해야 함 -> del 코드 부분에 저장하기 코드를 실행

#도서목록 대출 시스템
#도서목록 이라는 객체 - 저자, 장르, 작가   -> 생성자로 정의
#대출, 반납  ->  메소드(기능) 로 정의

#C- 포인터, 자바- 추상화, 파이썬- 클래스



class Player:
    def __init__(self, nickname, hp, gold=0, level=0):  #gold, level 디폴트 값 설정함 (디폴트값은 항상 마지막에)
        self.nickname = nickname
        self.hp = hp
        self.level = level
        self.gold = gold
        print(nickname, hp, gold, level)

    def __del__(self):
        print("저장중")
        print("저장되었습니다.")

    def change_nickname(self, new_nickname):
        self.nickname = new_nickname

    def del_player(self):
        print("케삭되었습니다.")


player1 = Player("yoon", 5000, 10000, 100)
player1.change_nickname("dong")    #닉네임 변경
print(player1.nickname)
# def func(name="홍길동"):
#     print(name)
#
# func()

# player1 = Player("yoon")  #디폴트값으로 나올 것


class Person:
    def __init__(self, age, email, name="홍길동"):
        self.name = name
        self.age = age
        self.email = email

    def introduce(self):
        print(f"이름은 {self.name}이고 나이는 {self.age}고 이메일은 {self.email}입니다")

person1 = Person(27, "dongyoon7212@naver.com", "이동윤")
person1.introduce()
person2 = Person(20, "example@gmail.com")
person2.introduce()
person2.address = "부산 진구"
print(person2.address)


class Computer:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        print(f"브랜드:{self.brand} 사이즈:{self.size} 객체 생성!!")


    def __del__(self):
        print(f"{self.brand} 의 객체가 소멸됨!!")


    def on(self, on, off):
        print(f"전원 켜기:{on} 전원 끄기:{off} ")

com1 = Computer("apple", 13)
com1.on()


