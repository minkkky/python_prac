import random
import pygame

## 함수

class InputBox:
	global width,height

	def __init__(self, x, y, width, height, text=''):
		self.rect = pg.Rect(x, y, w, h)
		self.color = COLOR_INACTIVE
		self.text = text
		self.txt_surface = FONT.render(text, True, self.color)
		self.active = False

	def handle_event(self, event):
		if event.type == pg.MOUSEBUTTONDOWN:
			# If the user clicked on the input_box rect.
			if self.rect.collidepoint(event.pos):
				# Toggle the active variable.
				self.active = not self.active
			else:
				self.active = False
			# Change the current color of the input box.
			self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
		if event.type == pg.KEYDOWN:
			if self.active:
				if event.key == pg.K_RETURN:
					print(self.text)
					self.text = ''
				elif event.key == pg.K_BACKSPACE:
					self.text = self.text[:-1]
				else:
					self.text += event.unicode
				# Re-render the text.
				self.txt_surface = FONT.render(self.text, True, self.color)

	def update(self):
		# Resize the box if the text is too long.
		width = max(200, self.txt_surface.get_width() + 10)
		self.rect.w = width

	def draw(self, screen):
		# Blit the text.
		screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
		# Blit the rect.
		pg.draw.rect(screen, self.color, self.rect, 2)

def eventProcess():
	global isActive

	for event in pygame.event.get(): # 입력받은 값을 이벤트에 저장

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE: # ESC 눌러서 종료
				isActive = False
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

## 변수 선언 및 초기화
width = 740
height = 740
isActive = True

com = random.randint(1,100)
count = 0

disValue = 0
stoValue = 0
opPre = 0

clock = pygame.time.Clock()

## pygame init
pygame.init() # 초기화 (반드시 필요)
screen = pygame.display.set_mode((width,height)) #화면 크기 선언
pygame.display.set_caption("UP & DOWN") # 창 이름

## 이미지 가져오기
one = pygame.image.load("./img/1.png")
two = pygame.image.load("./img/2.png")
three = pygame.image.load("./img/3.png")
four = pygame.image.load("./img/4.png")
five = pygame.image.load("./img/5.png")
six = pygame.image.load("./img/6.png")
seven = pygame.image.load("./img/7.png")
eight = pygame.image.load("./img/8.png")
nine = pygame.image.load("./img/9.png")
zero = pygame.image.load("./img/0.png")
back = pygame.image.load("./img/back.png")
ok = pygame.image.load("./img/OK.png")

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

# 출력할 문자열
text_main1 = font.render("저는 어떤 숫자일까요?", True, BLACK)
text_main2 = font.render("1~100 사이의 숫자를 입력하고 OK 버튼을 눌러주세요!", True, BLACK)
text_main3 = font.render("ESC를 누르면 창을 닫을 수 있어요!", True, BLACK)

text_up = font.render("UP! 제 숫자보다 작아요.", True, ORANGE)
text_down = font.render("DOWN! 제 숫자보다 커요.", True, ORANGE)
text_redo = font.render("다시 입력해보세요!", True, ORANGE)

text_win = font.render("정답이에요!", True, BLUE)
text_lose = font.render("실패했어요ㅠㅠ", True, RED)

## LOOP
while(isActive):
	screen.fill(WHITE) # 배경화면
	screen.blit(text_main1, (100, 100)) # 기본 메시지 출력
	screen.blit(text_main2, (100, 150))
	screen.blit(text_main3, (100, 650))
	screen.blit(one, (100, 450)) # 버튼 첫줄 시작
	screen.blit(two, (190, 450))
	screen.blit(three, (280, 450))
	screen.blit(four, (370, 450))
	screen.blit(five, (460, 450))
	screen.blit(back, (550, 450))
	screen.blit(six, (100, 540)) # 버튼 둘째줄 시작
	screen.blit(seven, (190, 540))
	screen.blit(eight, (280, 540))
	screen.blit(nine, (370, 540))
	screen.blit(zero, (460, 540))
	screen.blit(ok, (550, 540))

	eventProcess()
	handle_event()

	pygame.display.flip()
	clock.tick(10)

if __name__ == '__main__':
    main()
    pg.quit()