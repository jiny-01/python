##상점 리스트

from package.constants import shop_items
import random
import time


##기본 공격 수행 메소드 - 치명타가 적용되는지 / 기본 공격인지
def basic_atk(player):
    if random.randint(1, 100) <= player.cri_luk:      #player 확률 20일 때 random이 player 보다 작을 확률 (1~20) => 20% 와 같다고 볼 수있음
        damage = player.attack * 2
        print("치명타!!!")
    else:
        damage = player.attack
    print(f"{player.nickname}의 기본공격!!, {damage}전달!")
    return damage


##기본 공격 외 스킬 공격 실행 메소드
def skill_attack(player):
    print("사용가능한 스킬")
    for idx, skill in enumerate(player.skills):
        print(f"{idx + 1}. {skill["name"]} (MP소모:{skill["mp_cost"]}, 데미지 배수:{skill["damage_multiple"]}")  #스킬 사용시 출력할 정보
    skill_choice = int(input("사용할 스킬을 선택해주세요:")) - 1

    if 0 <= skill_choice < len(player.skills):                       #
        skill = player.skills[skill_choice]
        if player.mp >= skill["mp_cost"]:                              #플레이어의 mp 가 스킬 사용 시 소모될 mp 보다 클 때 사용가능
            player.mp -= skill["mp_cost"]
            damage = int(player.attack * skill["damage_multiple"])     #데미지 깎이는 것을 보기 쉽게 정수형으로 나타내기 위함
            print(f"{player.nickname}가 {skill["name"]}을 시전하였습니다. {damage} 데미지!")
            return damage
        else:
            print("MP가 부족합니다. 기본 공격을 수행합니다.")
            return basic_atk(player)
    else:
        print("잘못된 입력입니다. 기본 공격을 수행합니다.")
        return basic_atk(player)





#플레이어 턴일 때 공격 선택하는 메소드
def player_turn(player):
    print("행동을 선택하세요")
    print("1. 기본 공격")
    print("2. 스킬 사용")
    action = input("선택:")

    if action == "1":
        return basic_atk(player)         #basic_atk 에서 리턴한 데미지를 battle 까지 가져가야하기 때문
    elif action == "2":
        return skill_attack(player)
    else:
        print("잘못된 입력입니다. 기본 공격을 수행합니다.")
        return basic_atk(player)


#본격 배틀 실행하는 메소드
def battle(player, monster):
    print(f"{player.nickname} vs {monster.name}")
    while player.hp > 0 and monster.hp > 0:     #둘 다 살아있어야만 배틀 가능하기 때문
        print(f"[{player.nickname} HP: {player.hp}, MP: {player.mp}] vs [{monster.name}, HP: {monster.hp}]")

        #플레이어 턴
        damage = player_turn(player)
        monster.hp -= damage
        time.sleep(2)

#몬스터 처치하는 부분
        if monster.hp <= 0:                                 #몬스터의 체력이 0이하일 때 = 몬스터 처치완료
            print(f"{monster.name}을 처치했습니다.")
            exp_reward_multiple = random.uniform(0.9, 1.1)  #0.9~1.1 사이에서 랜덤으로 하나
            gold_reward_multiple = random.uniform(0.9, 1.1)
            exp_reward = int(monster.exp_reward * exp_reward_multiple)  #몬스터의 보상리워드에 랜덤계수 곱한 것
            gold_reward = int(monster.gold_reward * gold_reward_multiple)
            player.gain_exp(exp_reward)    #레벨업 가능 여부 확인 메소드의 amount에 exp_reward가 들어가는 것
            player.gold += gold_reward     #플레이어의 gold 에 보상 gold 를 더해줌
            print(f"경험치-{exp_reward}, 골드-{gold_reward} 획득!")

#몬스터 & 플레이어 데이터의 초기화
            monster.hp = monster.max_hp
            player.hp = player.max_hp
            player.mp = player.max_mp
            break


##몬스터 안 죽었을 때 몬스터 턴
        player.hp -= monster.attack
        print(f"{monster.name}의 반격! {monster.attack} 데미지 받음!")
        time.sleep(2)

        mp_recovery_amount = 5                  #1라운드 끝날 때마다 5mp 씩 회복
        player.mp_recovery(mp_recovery_amount)

##플레이어가 죽었을 때
        if player.mp <= 0:
            print("패배했습니다. 게임 오버")
            player.player_dead()
            player.hp = player.max_hp        #hp, mp 기본상태로 초기화
            player.mp = player.max_mp
            break




##상점에서 아이템 구매하는 메소드
def shop(player):
    print("\n[상점]")
    print(f"\n보유골드: {player.gold}")
    for idx, item in enumerate(shop_items):    #idx: 아이템의 인덱스 & 아이템 같이 빼옴 -> enumerate 사용
        print(f"{idx + 1}. {item["name"]} (추가 공격력: {item["attack"]}, 추가 HP: {item["hp"]}, 추가 MP: {item["mp"]} 추가 치명타 확률: {item["cri_luk"]}, 가격: {item["price"]})")
    choice = int(input("구매할 아이템 번호를 입력해주세요(취소: 0):"))-1
    if 0 <= choice < len(shop_items):
        item = shop_items[choice]
        if player.gold >= item["price"]:
            player.gold -= item["price"]
            player.items.append(item)
            player.apply_item(item)
            print(f"{item["name"]}을/를 구매했습니다!")
        else:
            print("골드가 부족합니다.")
    elif choice == -1:   #0을 원하지만 choice 에 -1 을 선언했기 때문에 -1
        print("구매를 취소했습니다.")
    else:
        print("잘못된 입력입니다.")

