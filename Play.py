import pygame
from pygame.locals import *
import time
import random
from Control import Control
from Mode import Mode
from Difficulty import Difficulty
from Star import Star
from Ranking import Ranking

# 規定値を定義
LIMIT_TIME = 20
X = 0
Y = 1

'''
Playクラス
    ゲーム画面を表示するクラス
'''
class Play():
    def __init__(self, media):
        self.start_time = time.time()
        self.star_list = [] # 降ってくる星用のリスト
        self.get_star = 0 # 取得した星の数
        self.titlefont = pygame.font.SysFont('inkfree', 80)
        self.comment = pygame.font.SysFont('inkfree', 40)
        self.title = self.titlefont.render("Play", True, (255,255,255))
        self.result = self.titlefont.render("Result", True, (255,255,255))
        self.control = Control()
        self.media = media
        self.ranking = Ranking(media)
        self.read_ranking = False # ランキングを読み込んだかどうか
        self.write_point = False # ランキングに書き込めるかどうか
        self.eng_chara = [['a','b','c','d','e','f','g','h','i','j','k','l','m',' '],
                          ['n','o','p','q','r','s','t','u','v','w','x','y','z','Back']]
        self.choose = [0, 0]
        self.your_name = ''


    def main(self, screen, difficulty, rect_player):
        # タイトルと設定情報の描画
        star_num = self.titlefont.render("Star:{0}".format(self.get_star), True, (255,255,255))
        lim_time = LIMIT_TIME - int((time.time() - self.start_time))
        time_num = self.titlefont.render("Time:{0}".format(lim_time), True, (255,255,255))
        screen.blit(self.title, (20,50))

        # 終了条件を満たしていたら
        if lim_time <= 0:
            screen.blit(self.result, (500,50))
            screen.blit(star_num, (500,150))
            # ランキング情報を1度だけ読み出し順位を確認する
            if self.read_ranking == False:
                self.write_point = self.ranking.read_ranking(self.get_star)
                self.read_ranking = True

            # ランキングで更新があったら名前を入力させる
            if self.write_point:
                screen.blit(self.titlefont.render("New Record!", True, (255,255,255)), (430, 250))
                # スクリーンキーボードを表示する
                for i, eng in enumerate(self.eng_chara):
                    for j, chara in enumerate(eng):
                        screen.blit(self.comment.render(chara, True, (255,255,255)), (350+j*40,400+i*40))
                screen.blit(self.comment.render("END", True, (255,255,255)), (350+220,400+2*40))
                screen.blit(self.comment.render(self.your_name, True, (255,255,255)), (350, 350)) # 名前を表示
                # 今自分が選択している位置を四角形で表示
                pygame.draw.rect(screen, (255,255,0), Rect(350+40*self.choose[X],410+40*self.choose[Y],30,30),2)
                self.input_name()
            else:
                screen.blit(self.titlefont.render("press enter!", True, (255,255,255)), (430, 250))
                # エンターを押したら終了するための処理
                con = self.control.control()
                if con == 'return':
                    rect_player.center = (450, 220)
                    self.media.kirakira.play()
                    self.media.play_bgm(1)
                    return Mode.MENU
        # まだ終了していなかったら(制限時間内なら)
        else:
            screen.blit(time_num, (900, 10))
            screen.blit(star_num, (900, 100))
            ran = random.randint(0, 100)
            # 生成した乱数が難易度の一定数以内なら星を生成する
            if ran <= (difficulty[Difficulty.STAR] - 1):
                self.star_list.append(Star(random.randint(100, 1100), 50))
            # 生成された星を描画する
            for i, star in enumerate(self.star_list):
                screen.blit(self.media.star, (star.x, star.y))
                star.y += 2 # 星を落とす
                # もしキャラクターと星が重なっていたら星を取得
                if star.hit(rect_player, 15*difficulty[Difficulty.SIZE]):
                    self.star_list.pop(i)
                    self.get_star += 1
                    self.media.hit.play()
                # 地面以下なら星を消滅
                elif self.star_list[i].y > 600:
                    self.star_list.pop(i) 

            # 横移動用コントロール
            con = self.control.control2()
            if con == 'left':
                if rect_player.centerx > 100:
                    rect_player.center = (rect_player.centerx - difficulty[Difficulty.SPEED], 550)
            elif con == 'right':
                if rect_player.centerx < 1100:
                    rect_player.center = (rect_player.centerx + difficulty[Difficulty.SPEED], 550)

        return Mode.PLAY

    def input_name(self):
        # コントロール操作
        con = self.control.control()
        if con == 'up':
            if self.choose[Y] > 0:
                self.choose[Y] -= 1
        elif con == 'down':
            if self.choose[Y] < 2:
                self.choose[Y] += 1
        elif con == 'left':
            if self.choose[X] > 0:
                self.choose[X] -= 1
        elif con == 'right':
            if self.choose[X] < 13:
                self.choose[X] += 1
        elif con == 'return':
            if self.choose[Y] == 2 and self.your_name != '': # Exitで名前有
                self.media.kirakira.play()
                # 新しいランキングを書き出す
                self.ranking.write_ranking(self.your_name)
                self.write_point = False
            elif self.choose[Y] == 2 and self.your_name == '': # Exitで名前無
                self.media.kirakira.play()
                self.write_point = False
            else:
                # enterした場所にある文字を名前として保存する
                for i in range(14):
                    for j in range(2):
                        if self.choose[Y] == j and self.choose[X] == i:
                            if self.choose[X] == 13 and self.choose[Y] == 1:
                                self.your_name = self.your_name[0:-1]
                            else:
                                self.your_name += self.eng_chara[j][i]
        # 一番下ならENDにする
        if self.choose[Y] == 2:
            self.choose[X] = 6