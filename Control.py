import pygame
from pygame.locals import *
import sys
''''
Controlクラス
    キーボード入力に応じた処理を返すクラス
'''
class Control():
    def __init__(self):
        pass
    ''''
    キーボード入力を受け付け、命令を返すメソッド
    キーが押されたタイミングで判断する
    @return : 操作
    '''
    def control(self):
        for event in pygame.event.get():
            # 閉じるボタンが押されたとき
            if event.type == QUIT:          
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # キーを押したとき
                # ESCキーならスクリプトを終了
                if event.key == K_ESCAPE:
                    sys.exit()
                elif event.key == K_LEFT:
                    return 'left'
                elif event.key == K_RIGHT:
                    return 'right'
                elif event.key == K_UP:
                    return 'up'
                elif event.key == K_DOWN:
                    return 'down'
                elif event.key == K_RETURN:
                    return 'return'

        return None

    '''
    キーボード入力を受け付け、命令を返すメソッド
    キーが押されている間ずっと認識する
    @return : 操作
    '''
    def control2(self):
        for event in pygame.event.get():
            if event.type == QUIT:          
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()

        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_LEFT]:
            return 'left'
        elif pressed_key[K_RIGHT]:
            return 'right'
        elif pressed_key[K_UP]:
            return 'up'
        elif pressed_key[K_DOWN]:
            return 'down'
        elif pressed_key[K_RETURN]:
            return 'return'

        return None