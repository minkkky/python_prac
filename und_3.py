import pygame as pg
import random



# 색상 정의
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (178,34,34)
CFBLUE = (100,149,237)

pg.init() # 초기화
pg.mixer.init() # 효과음 초기화
screen = pg.display.set_mode((480, 640)) # 화면크기선언
pg.display.set_caption("UP & DOWN") # 창 이름

COLOR_INACTIVE = pg.Color(WHITE) # 비활성화 된 입력창 색상
COLOR_ACTIVE = pg.Color(BLUE) # 활성화 된 입력창 색상

FONT = pg.font.SysFont("나눔손글씨곰신체", 30, True, True)
wFONT = pg.font.SysFont("나눔손글씨곰신체", 70, True, True)

# 출력할 문자열
text_main1 = FONT.render("저는 어떤 숫자일까요?", True, WHITE)
text_main2 = FONT.render("1~100 사이의 숫자를 입력하고", True, WHITE)
text_main3 = FONT.render("엔터를 눌러주세요!", True, WHITE)
test_main4 = FONT.render("스페이스바를 눌러 다시 시작하기", True, BLACK)

text_up = FONT.render("UP! 정답보다 크네요.", True, RED)
text_down = FONT.render("DOWN! 정답보다 작네요.", True, RED)
text_redo = FONT.render("다시 입력하고 엔터!", True, RED)

text_win = wFONT.render("정답이에요!", True, BLUE)
text_lose = wFONT.render("실패했어요ㅠㅠ", True, RED)

# 효과음
bgm = pg.mixer.Sound( "./sound/bensound-jazzyfrenchy.mp3" )
bgm.play(-1) # bgm 자동재생

click_sound = pg.mixer.Sound( "./sound/Deny 1.mp3" )
X_sound = pg.mixer.Sound( "./sound/Hobbit Oh 5.mp3" )
error_sound = pg.mixer.Sound( "./sound/Robot blip Sound.mp3" )
clap_sound = pg.mixer.Sound( "./sound/Small Crowd Applause Sound.mp3" )

# 변수 정의
com = random.randint(1, 100)
user = -1
count = 0
result = -1

class InputBox:

    def __init__(self, x, y, w, h, text=''):
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
                click_sound.play() # 입력한 클릭시 SE
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE

        if event.type == pg.KEYDOWN:
            global user, com, count, result
            if self.active:
                if event.key == pg.K_RETURN: # 엔터로 입력
                    print(self.text)
                    user = self.text
                    self.text = ''
                    print('user: '+user)
                    print(result)

                    if int(user) > 100 or int(user) < 1:
                        print('다시 입력해주세요!')
                        result = 0
                        error_sound.play() # 범위밖 숫자 입력시 SE

                    else:
                        if int(user) > com:
                            print('정답보다 크네요')
                            result = 2
                            X_sound.play() # 오답시 SE

                        elif int(user) < com:
                            print('정답보다 작네요')
                            result = 3
                            X_sound.play() # 오답시 SE

                        else:
                            print('정답입니다.')
                            result = 1
                            clap_sound.play() # 정답시 SE

                elif event.key == pg.K_BACKSPACE: # 한글자씩 지우기
                    self.text = self.text[:-1]

                elif event.key == pg.K_SPACE: # 스페이스바로 재시작
                    init()


                elif event.key == pg.K_1: # 이하 숫자키만 입력 되게
                    self.text += event.unicode
                elif event.key == pg.K_2:
                    self.text += event.unicode
                elif event.key == pg.K_3:
                    self.text += event.unicode
                elif event.key == pg.K_4:
                    self.text += event.unicode
                elif event.key == pg.K_5:
                    self.text += event.unicode
                elif event.key == pg.K_6:
                    self.text += event.unicode
                elif event.key == pg.K_7:
                    self.text += event.unicode
                elif event.key == pg.K_8:
                    self.text += event.unicode
                elif event.key == pg.K_9:
                    self.text += event.unicode
                elif event.key == pg.K_0:
                    self.text += event.unicode
                # 그 외의 키들은 인식X

                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)

def intput(user): # 유저가 입력한 값을 띄워준다
    global screen
    font = pg.font.Font(None, 35)
    text = font.render('Input : ' + str(user), True, BLACK)
    screen.blit(text, (90, 350))

def result_msg(): # 결과 메시지를 띄워준다
    global screen, result, FONT, wFONT, text_up, text_down, text_redo, text_win

    if result == 1: # win
        screen.blit(text_win, (90, 450))

    if result == 2: # up
        screen.blit(text_up, (90, 400)) # 결과 메시지 출력 자리 확인용
        screen.blit(text_redo, (90, 450))

    if result == 3: # down
        screen.blit(text_down, (90, 400)) # 결과 메시지 출력 자리 확인용
        screen.blit(text_redo, (90, 450))

    if result == 0: # 다시 입력하세요
        screen.blit(text_redo, (90, 450))

def init(): # 재시작
    global com, user, result, count

    pg.init()
    com = random.randint(1, 100)
    user = -1
    count = 0
    result = -1

def main():
    clock = pg.time.Clock()
    input_box = InputBox(90, 280, 200, 35) # 입력창 설정
    input_boxes = [input_box]
    done = False

    global com, user

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()

        screen.fill(CFBLUE) # 배경화면
        for box in input_boxes:
            box.draw(screen)

        screen.blit(text_main1, (90, 100))  # 기본 메시지 출력
        screen.blit(text_main2, (90, 150))
        screen.blit(text_main3, (90, 200))
        screen.blit(test_main4, (80, 600))

        intput(user)
        result_msg()

        pg.display.flip()
        clock.tick(10)

if __name__ == '__main__':
    main()
    pg.quit()