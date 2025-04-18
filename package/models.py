##플레이어 클래스


class Player:
    def __init__(self, nickname, level=1, gold=0, attack=10, exp=0, max_exp=100, hp=100, max_hp=100, mp=50, max_mp=50, cri_luk=0, skills=None, items=None):
        self.nickname = nickname
        self.level = level
        self.gold = gold
        self.attack = attack
        self.exp = exp          #경험치
        self.max_exp = max_exp
        self.hp = hp            #체력
        self.max_hp = max_hp
        self.mp = mp            #스킬 사용 시 소모되는 것 mp
        self.max_mp = max_mp
        self.cri_luk = cri_luk  #치명타 확률
        self.skills = skills if skills else [         #항상 skills 는 none 이기 때문에 바로 else 탐
            {"name": "달팽이 세마리", "mp_cost": 10, "damage_multiple": 1.2},
            {"name": "달팽이 네마리", "mp_cost": 18, "damage_multiple": 1.5},
            {"name": "달팽이 다섯마리", "mp_cost": 23, "damage_multiple": 1.8}
        ]
        self.items = items if items else []  # 불러올 때 item 이 있으면 쓰고 없으면 비게 둠

    def to_dict(self):
        return self.__dict__ #클래스(인스턴스)의 내부 상태를 딕셔너리로 변환


#제이슨 파일
    @classmethod
    def from_dict(cls, data):       #cls: 플레이어 클래스  ->  언패킹하여 플레이어 클래스에 데이터를 넣어줌
        return cls(**data)

#아이템 적용해서 올라가는 메소드
    def apply_item(self, item):
        self.attack += item["attack"]
        self.max_hp += item["hp"]
        self.max_mp += item["mp"]
        self.cri_luk += item["cri_luk"]
        print(f"<{item["name"]}> \n공격력 +{item["attack"]} => {self.attack}\n 최대 HP +{item["hp"]} => {self.max_hp}\n최대 MP +{item["mp"]} => {self.max_mp}\n추가 치명타 확률 +{item["cri_luk"]}% => {self.cri_luk}%")
        print(f"남은 골드: {self.gold}")

#플레이어 레벨업 메소드
#1) 레벨업 가능한 상황인지 확인하는 메소드
    def gain_exp(self, amount):         #amount: 얻은 경험치의 양  즉, amount = exp_reward
        self.exp += amount
        if self.exp >= self.max_exp:
            print("레벨업이 가능합니다")
            left_amount = amount - self.max_exp  #얻은 경험치가 내 맥스 경험치보다 클 때 남은 것을 left_amount(레벨업하고 남은 경험치)로 정의
            self.level_up(left_amount)           #레벨업 시 left_amount 를 레벨업 진행 메소드에서 그대로 가져감
            #레벨업 진행


# 2) 레벨업이 수행되는 메소드 - 능력치 향상
    def level_up(self, amount):
#여기서 amount 는 위에서의 left_amount 가 들어올 것, 즉 amount=left_amount(레벨업하고 남은 경험치)
        self.level += 1
        self.attack += 5
        self.max_hp += 10
        self.max_mp += 10
        self.hp = self.max_hp
        self.mp = self.max_mp
        self.exp = 0
        self.exp += amount                       #이월된 경험치만큼 추가
        self.max_exp = int(self.max_exp * 1.5)
        print(f"레벨 업! {self.level} 레벨이 되었습니다! 공격력 + 5, 최대 HP + 10, 최대 MP + 10")

    def mp_recovery(self, mp):   #1라운드 끝날 때 마다 mp가 5씩 증가 -> mp 에 받음
        self.mp = min(self.max_mp, self.mp + mp)    #이미 max이면 mp 추가할 필요가 없기 때문 ->  min(a, b): a, b 중 작은 것 채택
        print(f"현재 MP: {self.mp}")


#플레이어 죽었을 때
    def player_dead(self):
        self.items = []





"""
원래 알던 method 는 
instance method :  우리가 기본적으로 알고 있는 메소드
static method : 클래스 내에 유틸성 메소드, 즉 인스턴스나 클래스의 속성에 접근할 수 없음
class method: 인스턴스를 생성하지 않고 클래스에 직접적으로 접근함
첫 번째 인자로 해당 클래스(기본값) 두번째 인자 데이터로 넣어서 딕셔너리 언패킹

"""


##몬스터 클래스

class Monster:
    def __init__(self, name, max_hp, attack, exp_reward, gold_reward):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp                 #초기화할 때 hp => max_hp
        self.attack = attack
        self.exp_reward = exp_reward     #얼마나 exp 를 얻을 수 있는지
        self.gold_reward = gold_reward   #얼마나 돈 얻는지




