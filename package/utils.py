import os.path
import json

from package.models import Player

def load_game():
    if os.path.exists("save.json"):
        with open("./save.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return Player.from_dict(data)     #Player 클래스에서 from_dict 메소드 가져옴, 데이터를 넣어줌
    return None

def save_game(player):
    with open("./save.json", "w", encoding="utf-8") as file:
        json.dump(player.to_dict(), file, indent=4, ensure_ascii=False)
    print("게임이 저장되었습니다.")


