import pygame
import random
from time import sleep

BLACK = (0, 0, 0)  # 검은색
WHITE = (255, 255, 255)  # 흰색
RED = (255, 0, 0)  # 빨강
pad_width = 480  # 게임 패드 넓이
pad_height = 640  # 게임 패드 높이
fighter_width = 0.3  # 전투기 넓이
fighter_height = 0.3  # 전투기 높이
enemy_width = 26  # 적 전투기 넓이
enemy_height = 20  # 적 전투기 높이


# Score 적립
def drawScore(count):
    global gamepad

    font = pygame.font.SysFont(None, 20)
    text = font.render('Kill Point : ' + str(count), True, WHITE)
    gamepad.blit(text, (0, 0))


# 놓친 전투기 카운트
def drawpassed(count):
    global gamepad

    font = pygame.font.SysFont(None, 20)
    text = font.render('Enemy Passed : ' + str(count), True, WHITE)
    gamepad.blit(text, (360, 0))


def dispMessage(text):
    global gamepad

    textfont = pygame.font.Font(None, 80)
    text = textfont.render(text, True, RED)
    textpos = text.get_rect()
    textpos.center = (pad_width / 2, pad_height / 2)
    gamepad.blit(text, textpos)
    pygame.display.update()
    sleep(2)
    runGame()


# 화면 구성
def initGame():
    global gamepad, clock, fighter, enemy, bullet

    pygame.init()  # 라이브러리 초기화
    gamepad = pygame.display.set_mode((pad_width, pad_height))  # 가로,세로
    pygame.display.set_caption("슈팅게임")  # 타이틀 지정
    fighter = pygame.image.load('c://_imgs/icon1.gif')  # 전투기 이미지 불러오기
    enemy = pygame.image.load('c://_imgs/icon2.gif')  # 적 전투기 이미지 불러오기
    bullet = pygame.image.load('c://_imgs/icon3.gif')  # 미사일 이미지 불러오기
    clock = pygame.time.Clock()


def drawObject(obj, x, y):  # 전투기를 화면에 표시
    global gamepad
    gamepad.blit(obj, (x, y))


# 메인 게임 부분
def runGame():
    global gamepad, clock, fighter, enemy, bullet, isShot
    isShot = False
    Score = 0
    enemypassed = 0
    bullet_xy = []  # 미사일 리스트 생성

    # 전투기 초기 좌표 설정
    x = pad_width * 0.45
    y = pad_height * 0.9
    x_change = 0  # 전투기 움직임 위치 초기화
    y_change = 0  # 전투기 움직임 위치 초기화

    # 적의 초기 좌표 설정
    enemy_x = random.randrange(0, pad_width - enemy_width)
    enemy_y = 0
    enemy_speed = 5

    ongame = False
    while not ongame:
        for event in pygame.event.get():  # x 키를 누르면 종료한다.
            if event.type == pygame.QUIT:
                ongame = True

            if event.type == pygame.KEYDOWN:  # 이벤트 타입이 키를 누른것인가
                if event.key == pygame.K_LEFT:  # 왼쪽 키인가
                    x_change -= 5  # 왼쪽으로 5만큼
                elif event.key == pygame.K_RIGHT:  # 오른쪽 키인가
                    x_change += 5  # 오른쪽으로 5만큼
                elif event.key == pygame.K_UP:
                    y_change -= 5
                elif event.key == pygame.K_DOWN:
                    y_change += 5
                elif event.key == pygame.K_SPACE:  # 미사일 스페이스바 구현
                    if len(bullet_xy) < 3:
                        bullet_x = x + (fighter_width / 2)
                        bullet_y = y - fighter_height
                        bullet_xy.append([bullet_x, bullet_y])  # 미사일 누적
            if event.type == pygame.KEYUP:
                x_change = 0
                y_change = 0

        gamepad.fill(BLACK)  # 배경 검은색으로 지정
        x += x_change
        y += y_change
        if x < 0:  # 전투기가 왼쪽 너머까지 가지 못하게 한다.
            x = 0
        elif x > pad_width - fighter_width:  # 전투기가 오른쪽 너머로 가지 못하게 한다.
            x = pad_width - fighter_width
        if y < 0:  # 전투기가 위쪽 너머로 가지 못하게 한다.
            y = 0
        elif y > pad_height - fighter_height:  # 전투기가 아랫쪽 너머로 가지 못하게 한다.
            y = pad_height - fighter_height
        if y < enemy_y + enemy_height:
            if (enemy_x > x and enemy_x < x + fighter_width) or (
                    enemy_x + enemy_width > x and enemy_x + enemy_width < x + fighter_width):
                dispMessage('Crashed')
        drawObject(fighter, x, y)  # 전투기 구현

        if len(bullet_xy) != 0:
            for i, bxy in enumerate(bullet_xy):
                bxy[1] -= 10  # 미사일의 y 좌표 값을 줄여서 위로 올라가는 효과
                bullet_xy[i][1] = bxy[1]  # 추가적으로 y 좌표 값을 줄인다.

                # 미사일로 적을 격추 했을 때
                if bxy[1] < enemy_y:
                    if bxy[0] > enemy_x and bxy[0] < enemy_x + enemy_width:
                        bullet_xy.remove(bxy)
                        isShot = True
                        Score += 100

                if bxy[1] <= 0:  # 미사일의 y 좌표 값이 0보다 작아지면 삭제한다.
                    try:
                        bullet_xy.remove(bxy)
                    except:
                        pass
        if len(bullet_xy) != 0:
            for bx, by in bullet_xy:
                drawObject(bullet, bx, by)

        drawScore(Score)

        enemy_y += enemy_speed
        if enemy_y > pad_height:
            enemy_y = 0
            enemy_x = random.randrange(0, pad_width - enemy_width)
            enemypassed += 1

        if enemypassed == 2:
            dispMessage('Game Over')

        drawpassed(enemypassed)

        # 격추시 미사일 삭제
        if isShot:
            enemy_x = random.randrange(0, pad_width - enemy_width)
            enemy_y = 0
            isShot = False

        drawObject(enemy, enemy_x, enemy_y)  # 적 전투기 구현

        pygame.display.update()
        clock.tick(30)  # fps 30으로 지정z

    pygame.quit()


initGame()
runGame()