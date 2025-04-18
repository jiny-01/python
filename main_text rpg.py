import os.path

from package.models import Player
from package.utils import load_game
from package.utils import save_game
from package.game import shop
from package.constants import monsters
from package.game import battle


def main():
    print("턴제 RPG 게임")


## 새로 시작 / 불러오기 묻기?
    if os.path.exists("save.json"):    # 경로에 이 파일이 존재하면
        choice = input("1. 기존 캐릭터 불러오기\n 2. 새로 시작하기\n선택:")
        if choice == "1":
            player = load_game()     #저장 파일 불러오기
            if not Player:
                print("저장된 캐릭터가 없습니다.")
                return
        else:
            nickname = input("닉네임을 입력해 주세요: ")
            player = Player(nickname)
    else:
        nickname = input("닉네임을 입력해 주세요 : ")
        player = Player(nickname)

    while True:
        print("\n[메뉴]")
        print("1. 배틀")
        print("2. 상점")
        print("3. 내 아이템 확인")
        print("4. 내 정보 확인")
        print("5. 게임 종료")
        choice = input("선택 : ")

        if choice == "1":
            print("\n[배틀]")
            for idx, monster in enumerate(monsters):
                print(f"{idx + 1}. {monster.name} (HP: {monster.hp}, 공격력: {monster.attack}")
            m_choice = int(input("몬스터를 선택하세요:")) - 1
            if 0 <= m_choice < len(monsters):
                battle(player, monsters[m_choice])
            else:
                print("잘못된 입력입니다.")
        elif choice == "2":
            print("\n[상점]")
            shop(player)
        elif choice == "3":
            print("\n[내 아이템 확인]")
            if player.items:
                for item in player.items:
                    print(f"{item["name"]} (추가 공격력: {item["attack"]}, 추가 HP: {item["hp"]}, 추가 MP: {item["mp"]}, 추가 치명타 확률: {item["cri_luk"]}")
            else:
                print("보유한 아이템이 없습니다.")
        elif choice == "4":
            print("\n[내 정보 확인]")
            print(f"닉네임: {player.nickname}\n레벨: {player.level} ({player.exp})/{player.max_exp}\n공격력: {player.attack}\n치명타 확률: {player.cri_luk}\nHP: {player.hp}\nMP: {player.mp}\n골드: {player.gold})")
        elif choice == "5":
            print("\n[게임 종료]")
            save_game(player)
            break
        else:
            print("잘못된 입력입니다.")

#입력받아서 닉네임을 클래스의 객체로 생성


if __name__ == "__main__":         #파일이름(name) 이 main 에 있으면 main 에서만 실행되도록 함 -> 다른 파일이 실행됨을 방지
    main()

