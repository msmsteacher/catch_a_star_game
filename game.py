import pygame
import math
from Mode import Mode
from Difficulty import Difficulty
from Menu import Menu
from Play import Play
from Setting import Setting
from Bye import Bye
from Ranking import Ranking
from Media import Media

'''
ゲームメインクラスです
'''
class STAR_GAME():
    def __init__(self):
        pygame.init() # pygame初期化
        pygame.display.set_mode((1200, 675), 0, 32) # 画面設定
        self.screen = pygame.display.get_surface()
        pygame.display.set_caption('catch a star game') # ウィンドウタイトル
        # 各ゲームモードのインスタンスの生成
        self.media = Media()
        self.menu = Menu(self.media)
        self.play = Play(self.media)
        self.setting = Setting(self.media)
        self.bye = Bye(self.media)
        self.ranking = Ranking(self.media)
        self.media.play_bgm(1)
        # 各モードへ分岐するための辞書型
        self.game_mode_list = {Mode.MENU:self.menu, Mode.PLAY:self.play, Mode.SETTING:self.setting, Mode.RANKING:self.ranking, Mode.BYE:self.bye}

    '''
    キャラクター表示に関する設定
    '''
    def chara_set(self, screen, difficulty, rect_player, anim_counter):
        # キャラクターがアニメーションするための操作
        anim_counter += 1
        if anim_counter == 360:
            anim_counter = 0
        player_num = round((math.sin(math.radians(anim_counter))+1)*1.5) # 正弦を使ってアニメーションを変化させる
        # 正弦に応じた画像を難易度設定に応じたサイズに変更して表示
        player = pygame.transform.rotozoom(self.media.player_anim[player_num], 0, 0.5*difficulty[Difficulty.SIZE])

        # 難易度によるキャラクター描画位置ズレ補正
        x, y = rect_player.topleft
        size = (25 * -(difficulty[Difficulty.SIZE] - 2))
        return player, x + size, y + size, anim_counter

    '''
    メインループ
    '''
    def main(self):
        rect_player = self.media.player_anim[0].get_rect()
        rect_player.center = (450, 220) # プレイヤー画像の初期位置
        difficulty = [2, 2, 2] # 難易度の初期化
        game_mode = Mode.MENU
        anim_counter = 0
        while True:
            self.screen.blit(self.media.bg[game_mode], self.media.bg[game_mode].get_rect()) # 背景の描画
            
            # 各ゲームモードへの分岐
            last_game_mode = game_mode
            mode = self.game_mode_list[game_mode]
            game_mode = mode.main(self.screen, difficulty, rect_player)

            # 次ゲームモードが変わるときに初期化を行う
            if last_game_mode == Mode.MENU and game_mode != Mode.MENU:
                self.game_mode_list[game_mode].__init__(self.media)

            # キャラクターの描画
            player, x, y, anim_counter = self.chara_set(self.screen, difficulty, rect_player, anim_counter)
            self.screen.blit(player, (x, y))

            pygame.display.update()


if __name__ == "__main__":
    game = STAR_GAME()
    game.main()