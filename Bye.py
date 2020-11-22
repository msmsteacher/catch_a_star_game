import pygame
import sys

'''
Byeクラス
    終了用画像を表示し3秒後に画面を閉じる
'''
class Bye():
    def __init__(self, media):
        self.title = pygame.font.SysFont('inkfree', 80).render("Thank you for playing!", True, (255,255,255))

    def main(self, screen, defficulty, rect_player):
        screen.blit(self.title, (20,50))
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()