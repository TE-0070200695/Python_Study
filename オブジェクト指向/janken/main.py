import random
from hands import rock_aa,paper_aa,scissors_aa

hands = {0:'グー',1:'チョキ',2:'パー'}
hands_aa = {0:rock_aa,1:scissors_aa,2:paper_aa}
win = 0
lose = 0

def judge(user,cpu):
    if user==cpu:
        return 'あいこ',False
    elif any([
        user == 0 and cpu == 1,
        user == 1 and cpu == 2,
        user == 2 and cpu == 0
    ]):
        global win 
        win +=1
        return '勝ち',True
    # elif user == 0 and cpu == 1:
    #     return '勝ち'
    # elif user == 1 and cpu == 2:
    #     return '勝ち'
    # elif user == 2 and cpu == 0:
    #     return '勝ち'
    else:
        global lose
        lose +=1
        return '負け',True

def choice_hand():
    while True:
        #手を選択
        user_hand = input(f'じゃんけん！{str(hands)}:')
        try:
            user_hand = int(user_hand)
            if user_hand not in hands:
                raise ValueError
            if user_hand > 2:
                raise ValueError
            return user_hand
            
        except ValueError:
            print(f'{list(hands)}のいずれかを入力してください')

def play_game():
    while True:
        is_game_decided = False
        while not is_game_decided:
            #手を選択
            user_hand = choice_hand()

            #コンピュータの手を決定
            cpu_hand = random.choice(list(hands))

            #手を表示
            print('あなた',hands_aa[user_hand])
            print('コンピュータ',hands_aa[cpu_hand])

            #勝敗を判定
            result,is_game_decided = judge(user_hand,cpu_hand)
            print(f"\n{result}\n")

         #もう一度遊ぶか確認
        is_replay = input('再選する場合は何か入力してエンターキーを押してください:')
        if not is_replay:
            print(f'あなたの成績は{win}勝 {lose}敗でした。')            
            print('またね')
            break

if __name__ == '__main__':
    play_game()