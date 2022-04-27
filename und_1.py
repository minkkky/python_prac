import random, pygame
import tkinter as tk

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
x,y = (480,640)
screen = pygame.display.set_mode((x,y))
pygame.display.set_caption("Click")

# 화면 타이틀 설정
pygame.display.set_caption("UP & DOWN") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("./img/background.png")

# FPS
clock = pygame.time.Clock()

# 폰트 설정
font = pygame.font.SysFont("나눔손글씨곰신체", 30, True, True)

RED = (255,0,0)
ORANGE = (255,153,51)
YELLOW = (255,255,0)
GREEN = (0,255,0)
SEAGREEN = 	(60,179,113)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
VIOLET = (204,153,255)
PINK = (255,153,153)

# 변수 선언
com = random.randint(0,9) # 숫자 랜덤으로 뽑아오기
count = 0 # 도전횟수
value = 0
user = 0

# 출력할 문자열
text_main1 = font.render("저는 어떤 숫자일까요?", True, WHITE)
text_main2 = font.render("0~000 사이의 숫자를 입력하고", True, WHITE)
text_main3 = font.render("스페이스바를 눌러주세요!", True, ORANGE)

text_up = font.render("UP! 제 숫자보다 작아요.", True, ORANGE)
text_down = font.render("DOWN! 제 숫자보다 커요.", True, ORANGE)
text_redo = font.render("다시 입력하고 스페이스바를 눌러주세요!", True, ORANGE)

text_win = font.render("정답이에요!", True, BLUE)
text_lose = font.render("실패했어요ㅠㅠ", True, RED)



# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:

	for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
		if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
			running = False  # 게임이 진행중이 아님

		if event.type == pygame.KEYDOWN: # 키보드로 값을 입력받음
			if event.key == pygame.K_1:
				print('1')
				value += 1
			elif event.key == pygame.K_2:
				print("2")
				value += 2
			elif event.key == pygame.K_3:
				print("3")
				value += 3
			elif event.key == pygame.K_4:
				print("4")
				value += 4
			elif event.key == pygame.K_5:
				print("5")
				value += 5
			elif event.key == pygame.K_6:
				print("6")
				value += 6
			elif event.key == pygame.K_7:
				print("7")
				value += 7
			elif event.key == pygame.K_8:
				print("8")
				value += 8
			elif event.key == pygame.K_9:
				print("9")
				value += 9
			elif event.key == pygame.K_0:
				print("0")
				value += 0

			if event.key == pygame.K_SPACE:
				user += value
				print("user: "+str(user))
				value = 0
				user = 0


	# 게임 화면 그리기

	screen.blit(background, (0, 0))

	screen.blit(text_main1, (80, 100))
	screen.blit(text_main2, (80, 145))
	screen.blit(text_main3, (80, 190))

	text_user = font.render("Input: " + str(user), True, BLACK)
	screen.blit(text_user, (80, 300))

	dt = clock.tick(10)  # 게임화면의 초당 프레임 수를 설정
	pygame.display.update()  # 게임 화면을 다시 그리기


pygame.quit() # pygame 종료