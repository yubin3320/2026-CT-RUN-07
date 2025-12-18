import pygame
import sys
from PIL import Image

pygame.init()

show_elevator_msg = False
elevator_msg_time = 0
show_generator_msg = False
generator_msg_time = 0

highlight_alpha = 0
highlight_direction = 5

ROOM2_TO_MAP_CLICK = pygame.Rect(580, 700, 220, 120)

door_to_room3_rect = pygame.Rect(160, 500, 200, 120)




# --------------------------------------
#  전역 변수 — 레버/발전기/전선 퍼즐
# --------------------------------------
lever_obtained = False        # 레버 획득 여부
generator_unlocked = False    # 발전기 해결 여부

wire_progress = 0              # 전선 자르기 진행도
cut_wires = set()              # 잘린 전선 저장

# 클릭해야 하는 전선 실제 좌표
WIRE_POINTS = {
    "red": (647, 364),
    "yellow": (664, 381),
    "green": (684, 373),
    "blue": (704, 374),
}

WIRE_ORDER = ["yellow", "blue", "green", "red"]  # 정답 순서

highlight_alpha = 0
highlight_direction = 5

lever_auto_show = False
lever_show_start_time = 0

generator_key = False
generator_key_time = 0

# 버튼
skip_button_rect = pygame.Rect(900, 700, 200, 60)
BOX_OPEN_BACK_BTN = pygame.Rect(40, 40, 150, 50)


lever_obtained = False      # 레버(마스터키) 획득 여부
generator_unlocked = False  # 발전기 해결 여부




orig_bg_closed = pygame.image.load("방 3 잠김.png")   # 기본 배경
orig_bg_open   = pygame.image.load("방 3 열림.jpg")   # 퀘스트 완료 후 배경
orig_outside   = pygame.image.load("바깥.png")


# ▼▼▼ 레버 스킵 & 자동 표시 관련 변수 ▼▼▼
skip_button_rect = pygame.Rect(900, 700, 200, 60)

lever_auto_show = False
lever_show_start_time = 0

generator_key = False
generator_key_time = 0


pygame.mixer.music.load("bgm.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

CHAIR_BACK_BTN = pygame.Rect(40, 40, 150, 50)
BOX_OPEN_BACK_BTN = pygame.Rect(40, 40, 150, 50)

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("RUN:07")

clock = pygame.time.Clock()

door_to_room2_rect = pygame.Rect(448, 99, 5, 80)

key_obtained = False
current_screen = "INTRO_TEXT_1"
safe_unlock_start_time = 0
key_show_time = 0

map = pygame.transform.scale(pygame.image.load("map.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))

# ---------------------------------------------------------
# 파일 클릭 영역
# ---------------------------------------------------------
FOLDER_PLAN = pygame.Rect(180, 200, 150, 150)
FOLDER_TARGET = pygame.Rect(480, 200, 150, 150)
FOLDER_EMPTY1 = pygame.Rect(620, 200, 150, 150)
FOLDER_EMPTY2 = pygame.Rect(620, 420, 150, 150)

safe_rect = pygame.Rect(780, 260, 150, 150)
board_rect = pygame.Rect(600, 120, 300, 120)

FILE_CLOSE_BTN = pygame.Rect(1050, 50, 80, 40)
FILE_NEXT_BTN = pygame.Rect(900, 700, 200, 60)

typed_text = ""
typing_index = 0
typing_speed = 2

user_input = ""
error_message = ""

ANSWER_WORDS = {"분해", "패턴인식", "추상화", "알고리즘"}

cursor_visible = True
cursor_timer = 0

# ---------------------------------------------------------
# 비밀번호 확인
# ---------------------------------------------------------
def check_password(text):
    clean = text.replace(",", " ").strip()
    words = clean.split()
    return set(words) == ANSWER_WORDS

# ---------------------------------------------------------
# GIF 로드
# ---------------------------------------------------------
def load_gif_frames(path):
    img = Image.open(path)
    frames = []
    try:
        while True:
            frame = img.convert("RGBA")
            pg_frame = pygame.image.fromstring(frame.tobytes(), frame.size, frame.mode)
            pg_frame = pygame.transform.scale(pg_frame, (SCREEN_WIDTH, SCREEN_HEIGHT))
            frames.append(pg_frame)
            img.seek(img.tell() + 1)
    except EOFError:
        pass
    return frames

# ---------------------------------------------------------
# 색상 / 폰트
# ---------------------------------------------------------
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)

FONT_TITLE = pygame.font.Font("HCRBatang-Bold.ttf", 20)
FONT_BUTTON = pygame.font.Font("HCRBatang-Bold.ttf", 20)
FONT_TEXTBOX = pygame.font.Font("HCRBatang-Bold.ttf", 28)

# ---------------------------------------------------------
# 이미지 로드
# ---------------------------------------------------------
room2 = pygame.transform.scale(pygame.image.load("방 2 잠김.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
chair_zoom = pygame.transform.scale(pygame.image.load("의자 순서.png"), (600, 600))
box = pygame.transform.scale(pygame.image.load("상자.jpg"), (600, 600))
box_open = pygame.transform.scale(pygame.image.load("상자열림.jpg"), (600, 600))

GIF_FRAMES = load_gif_frames("bg1.gif")
GIF_INDEX = 0
GIF_DELAY = 7
GIF_COUNTER = 0

ELB_RECT = pygame.Rect(775, 137, 239, 237)
BOX_RECT = pygame.Rect(883, 428, 132, 134)
CHAIR_RECT = pygame.Rect(611, 325, 80, 151)
GENERATOR_RECT = pygame.Rect(208, 146, 278, 319)

# ---------------------------------------------------------
# BOX - 전선 퍼즐
# ---------------------------------------------------------
WIRE_ORDER = ["yellow", "blue", "green", "red"]
wire_progress = 0
cut_wires = set()

# 전선 자르는 '정확한' 클릭 포인트 (화면 좌표 기준)
# 4) 전선 클릭 포인트 (좌표계를 화면 기준으로 통일 → bx, by 제거)
WIRE_RECTS_LOCAL = {
    "red": pygame.Rect(647, 364, 10, 10),
    "yellow": pygame.Rect(664, 381, 10, 10),
    "green": pygame.Rect(684, 373, 10, 10),
    "blue": pygame.Rect(704, 374, 10, 10),
}

lever_obtained = False

lever_img = pygame.transform.scale(
    pygame.image.load("레버.png"), (300, 300)
)

# ---------------------------------------------------------
# INTRO 이미지들
# ---------------------------------------------------------
INTRO_IMAGES = [
    pygame.transform.scale(pygame.image.load("만화1.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)),
    pygame.transform.scale(pygame.image.load("만화2.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)),
    pygame.transform.scale(pygame.image.load("방 1 배경.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)),
    pygame.transform.scale(pygame.image.load("방 1 잠김.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)),
    pygame.transform.scale(pygame.image.load("비번해결.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)),
    pygame.transform.scale(pygame.image.load("파일.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)),
    pygame.transform.scale(pygame.image.load("만화6.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)),
    pygame.transform.scale(pygame.image.load("만화7-FB.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)),
]

POPUP_IMAGE = pygame.transform.scale(pygame.image.load("쪽지.png"), (600, 400))
PC_BG = pygame.transform.scale(pygame.image.load("컴퓨터배경.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))

file1 = pygame.transform.scale(pygame.image.load("file.jpg"), (SCREEN_WIDTH, SCREEN_HEIGHT))
file2 = pygame.transform.scale(pygame.image.load("file2.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))

safe_rect = pygame.Rect(738, 330, 136, 169)
board_rect = pygame.Rect(610, 126, 252, 144)

SAFE_CODE = [1, 2, 1, 1]
safe_input = [0, 0, 0, 0]

door_rect = pygame.Rect(95, 242, 101, 265)

SAFE_UP = []
SAFE_DOWN = []

room1 = pygame.transform.scale(pygame.image.load("방 1 잠김.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
safe = pygame.transform.scale(pygame.image.load("금고.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
board = pygame.transform.scale(pygame.image.load("board.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))

key = pygame.transform.scale(pygame.image.load("열쇠.png"), (180, 120))

# ---------------------------------------------------------
# INTRO 텍스트들 (대사 포함)
# ---------------------------------------------------------

INTRO1_LINES = [
    "눈을 뜨자 연구실처럼 보이는 곳에 있다.\n'여기는 어디지...?'",
    "주변을 둘러봐도 익숙한 건 없는 것 같다...",
    "밖으로 나가고자 문을 찾았다."
]

INTRO2_LINES = [
    "문 손잡이를 돌려보자\n'철커덕'하는 소리가 났고,\n문이 잠겨있음을 깨달았다.",
    "열쇠를 찾기 위해,\n지금 있는 방을 뒤져보기로 했다.",
    "'여긴 대체 누구의 방일까?\n그리고 왜 내가 여기에 갇혀있는 것일까?'"
]

INTRO3_LINES = [
    "내가 처음에 앉아있던 책상의 오른쪽 서랍을 열어보았다.",
    "해석이 필요해 보이는 쪽지가 한 장 들어있다."
]

INTRO4_LINES = [
    "'이 쪽지는 어디에 쓰이는 것일까?'",
    "다른 것들도 살펴보자."
]

INTRO5_LINES = [
    "컴퓨터 잠금이 풀렸다.",
    "컴퓨터 화면을 살펴보니, 2개의 파일이 있다."
]

INTRO6_LINES = [
    "첫 번째 파일을 클릭하니,\n화면에 빼곡히 적힌 문서가 나타났다.",
    "파일의 내용은 '인간의 신체 기능을 디지털화하여\n기계적 개체로 전환하는 장기 프로젝트•••'",
    "한 마디로,'사람을 컴퓨터로 만드는 인체 시험' 계획서이다."
]

INTRO7_LINES = [
    "두 번째 파일을 클릭하니,\n낯선 사람들의 얼굴과 인적사항이 적혀있다.",
    "이 사람들의 공통점은 단 하나-실험체들이라는 것."
]

# ---------------------------------------------------------
# 클릭 영역
# ---------------------------------------------------------
DRAWER_AREA = pygame.Rect(488, 342, 49, 32)
COMPUTER_AREA = pygame.Rect(300, 200, 180, 120)

intro_index = 0
game_started = False

# -----------------------------
# 2. 맵 & 플레이어(문 밖) 세팅
# -----------------------------
TILE_SIZE = 64

try:
    MAP_IMAGE = pygame.image.load('map.png').convert_alpha()
    MAP_IMAGE = pygame.transform.scale(MAP_IMAGE, (SCREEN_WIDTH, SCREEN_HEIGHT))
except pygame.error as e:
    print(f"맵 이미지 로드 오류: map.png 파일을 확인하세요. {e}")
    MAP_IMAGE = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    MAP_IMAGE.fill((50, 50, 50, 255))

MAP_RECT = MAP_IMAGE.get_rect()
MAP_RECT.topleft = (0, 0)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.animations = {
            'idle_front': [self._load_image('학생 정면 걷기 1.png')],

            'walk_front': [self._load_image('학생 정면 걷기 1.png'),
                           self._load_image('학생 정면 걷기 2.png')],
            'walk_back': [self._load_image('학생 후면 걷기 1.png'),
                          self._load_image('학생 후면 걷기 2.png')],
            'walk_left': [self._load_image('학생 왼쪽 측면 걷기 1.png'),
                          self._load_image('학생 왼쪽 측면 걷기 2.png')],
            'walk_right': [self._load_image('학생 오른쪽 측면 걷기 1.png'),
                           self._load_image('학생 오른쪽 측면 걷기 2.png')]
        }

        self.state = 'idle_front'
        self.current_images = self.animations[self.state]
        self.animation_index = 0
        self.image = self.current_images[self.animation_index]

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.speed = 4
        self.frame_counter = 0
        self.animation_speed = 0.15

    def _load_image(self, file_name):
        try:
            img = pygame.image.load(file_name).convert_alpha()
            return pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        except:
            temp = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)
            temp.fill((255, 0, 0, 150))
            return temp

    # 충돌 체크 (투명 + 테두리만 막기, 검은문은 통과 가능)
    def check_collision(self, next_rect):
        px = next_rect.centerx
        py = next_rect.bottom - 2

        local_x = int(px - MAP_RECT.x)
        local_y = int(py - MAP_RECT.y)

        # 화면 밖은 벽
        if local_x < 0 or local_x >= MAP_IMAGE.get_width():
            return True
        if local_y < 0 or local_y >= MAP_IMAGE.get_height():
            return True

        pixel = MAP_IMAGE.get_at((local_x, local_y))

        # 테두리 벽 막기
        if local_x <= 3 or local_x >= MAP_IMAGE.get_width() - 3:
            return True
        if local_y <= 3 or local_y >= MAP_IMAGE.get_height() - 3:
            return True

        # 투명(바깥 영역)은 막기
        if pixel.a == 0:
            return True

        return False

    def update(self):
        keys = pygame.key.get_pressed()
        new_x, new_y = self.rect.x, self.rect.y
        moving = False

        if keys[pygame.K_LEFT]:
            new_x -= self.speed
            self.state = 'walk_left'
            moving = True
        elif keys[pygame.K_RIGHT]:
            new_x += self.speed
            self.state = 'walk_right'
            moving = True

        if keys[pygame.K_UP]:
            new_y -= self.speed
            self.state = 'walk_back'
            moving = True
        elif keys[pygame.K_DOWN]:
            new_y += self.speed
            self.state = 'walk_front'
            moving = True

        new_rect_x = self.rect.copy()
        new_rect_x.x = new_x
        if not self.check_collision(new_rect_x):
            self.rect.x = new_x

        new_rect_y = self.rect.copy()
        new_rect_y.y = new_y
        if not self.check_collision(new_rect_y):
            self.rect.y = new_y

        if not moving:
            if self.state.startswith("walk"):
                self.state = "idle_front"

        self.current_images = self.animations.get(self.state, self.animations["idle_front"])

        if moving:
            self.frame_counter += self.animation_speed
            if self.frame_counter >= len(self.current_images):
                self.frame_counter = 0
            self.animation_index = int(self.frame_counter)
        else:
            self.animation_index = 0

        self.image = self.current_images[self.animation_index]


# Player 생성 (문 밖 맵 시작 위치)
player = Player(1000, 100)
player_group = pygame.sprite.Group(player)

# -----------------------------
# 타자기 효과
# ---------------------------------------------------------
def update_typing(text):
    global typed_text, typing_index, typing_speed
    if typing_index < len(text):
        if pygame.time.get_ticks() % typing_speed == 0:
            typing_index += 1
        typed_text = text[:typing_index]
    return typed_text


def draw_textbox_typing(full_text, x, y, w, h):
    pygame.draw.rect(SCREEN, WHITE, (x, y, w, h))
    pygame.draw.rect(SCREEN, BLACK, (x, y, w, h), 3)

    typing_out = update_typing(full_text)
    lines = typing_out.split("\n")

    lh = FONT_TEXTBOX.size("가")[1] + 8
    oy = y + 20

    for i, line in enumerate(lines):
        txt = FONT_TEXTBOX.render(line, True, BLACK)
        SCREEN.blit(txt, (x + 20, oy + i * lh))



# ---------------------------------------------------------
# 화면 그리기  (mx, my 추가됨! ← 오류 해결 핵심)
# ---------------------------------------------------------
def draw_scene(mx, my):
    global GIF_INDEX, GIF_COUNTER, cursor_visible, cursor_timer
    global CLOSE_BTN, BOARD_BACK_BTN, SAFE_UP, SAFE_DOWN
    global SAFE_CONFIRM_BTN, SAFE_BACK_BTN
    global key_obtained, safe_unlock_start_time
    global wire_progress, cut_wires
    global current_screen
    global generator_key, generator_key_time, key_obtained
    global show_elevator_msg, elevator_msg_time
    global show_generator_msg, generator_msg_time

    SCREEN.fill((0, 0, 0))

    # --- GIF 배경 ---
    if current_screen.startswith("INTRO") :
        SCREEN.blit(GIF_FRAMES[GIF_INDEX], (0, 0))
        GIF_COUNTER += 1
        if GIF_COUNTER >= GIF_DELAY:
            GIF_COUNTER = 0
            GIF_INDEX = (GIF_INDEX + 1) % len(GIF_FRAMES)

    # 시작 화면
    if not game_started:
        text = FONT_TITLE.render("아무 곳이나 클릭해서 시작", True, WHITE)
        SCREEN.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, SCREEN_HEIGHT - 80))
        return

    # -----------------------------
    # INTRO
    # -----------------------------
    if current_screen.startswith("INTRO_TEXT_"):
        idx = int(current_screen[-1]) - 1
        SCREEN.blit(INTRO_IMAGES[idx], (0, 0))

        intro_sets = [INTRO1_LINES, INTRO2_LINES, INTRO3_LINES, INTRO4_LINES]
        draw_textbox_typing(intro_sets[idx][intro_index], 150, 550, 900, 150)



    # -----------------------------
    # ROOM_SCREEN (서랍 안내)
    # -----------------------------
    elif current_screen == "ROOM_SCREEN":
        SCREEN.blit(INTRO_IMAGES[3], (0, 0))
        txt = FONT_TEXTBOX.render("서랍을 클릭해보세요.", True, WHITE)
        SCREEN.blit(txt, (50, 50))



    # -----------------------------
    # ROOM_SCREEN_2 (컴퓨터 안내)
    # -----------------------------
    elif current_screen == "ROOM_SCREEN_2":
        SCREEN.blit(INTRO_IMAGES[3], (0, 0))
        txt = FONT_TEXTBOX.render("컴퓨터를 클릭해보자...", True, WHITE)
        SCREEN.blit(txt, (50, 50))



    # -----------------------------
    # DRAWER POPUP
    # -----------------------------
    elif current_screen == "DRAWER_POPUP":
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        SCREEN.blit(overlay, (0, 0))

        px = SCREEN_WIDTH//2 - 300
        py = SCREEN_HEIGHT//2 - 200
        SCREEN.blit(POPUP_IMAGE, (px, py))

        close_text = FONT_TEXTBOX.render("닫기", True, WHITE)
        SCREEN.blit(close_text, (px + 520, py + 350))

        CLOSE_BTN = pygame.Rect(px + 500, py + 330, 120, 50)



    # -----------------------------
    # PC SCREEN
    # -----------------------------
    elif current_screen == "PC_SCREEN":
        SCREEN.blit(PC_BG, (0, 0))

        title = FONT_TEXTBOX.render("비밀번호를 입력하세요", True, BLACK)
        SCREEN.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 300))

        pygame.draw.rect(SCREEN, BLACK, (350, 380, 500, 70), 3)

        cursor_timer += 1
        if cursor_timer >= 30:
            cursor_visible = not cursor_visible
            cursor_timer = 0

        display = user_input + ("|" if cursor_visible else "")
        txt = FONT_TEXTBOX.render(display, True, BLACK)
        SCREEN.blit(txt, (360, 395))

        if error_message:
            err = FONT_TEXTBOX.render(error_message, True, (200, 0, 0))
            SCREEN.blit(err, (SCREEN_WIDTH//2 - err.get_width()//2, 480))



    # -----------------------------
    # COMIC5
    # -----------------------------
    elif current_screen == "COMIC5_SCENE":
        SCREEN.blit(INTRO_IMAGES[4], (0, 0))
        draw_textbox_typing(INTRO5_LINES[intro_index], 250, 550, 700, 150)



    # -----------------------------
    # PC 파일 목록
    # -----------------------------
    elif current_screen == "PC_FILE_SCREEN":
        SCREEN.blit(INTRO_IMAGES[5], (0, 0))

        pygame.draw.rect(SCREEN, (40, 100, 220), FILE_NEXT_BTN, border_radius=10)
        next_txt = FONT_TEXTBOX.render("다음으로", True, WHITE)
        SCREEN.blit(next_txt, (FILE_NEXT_BTN.x + 35, FILE_NEXT_BTN.y + 15))



    # -----------------------------
    # 폴더 화면들
    # -----------------------------
    elif current_screen == "PLAN_SCREEN":
        SCREEN.blit(file1, (0, 0))
        pygame.draw.rect(SCREEN, (200, 0, 0), FILE_CLOSE_BTN)
        SCREEN.blit(FONT_TEXTBOX.render("X", True, WHITE), (FILE_CLOSE_BTN.x + 25, FILE_CLOSE_BTN.y + 5))

    elif current_screen == "TARGET_SCREEN":
        SCREEN.blit(file2, (0, 0))
        pygame.draw.rect(SCREEN, (200, 0, 0), FILE_CLOSE_BTN)
        SCREEN.blit(FONT_TEXTBOX.render("X", True, WHITE), (FILE_CLOSE_BTN.x + 25, FILE_CLOSE_BTN.y + 5))

    elif current_screen == "EMPTY_FILE1_SCREEN":
        SCREEN.fill((255, 255, 240))
        txt = FONT_TEXTBOX.render("아무 내용이 없는 빈 파일입니다.", True, BLACK)
        SCREEN.blit(txt, (100, 100))
        pygame.draw.rect(SCREEN, (200, 0, 0), FILE_CLOSE_BTN)
        SCREEN.blit(FONT_TEXTBOX.render("X", True, WHITE), (FILE_CLOSE_BTN.x + 25, FILE_CLOSE_BTN.y + 5))

    elif current_screen == "EMPTY_FILE2_SCREEN":
        SCREEN.fill((240, 255, 240))
        txt = FONT_TEXTBOX.render("아무 내용이 없는 빈 파일입니다.", True, BLACK)
        SCREEN.blit(txt, (100, 100))
        pygame.draw.rect(SCREEN, (200, 0, 0), FILE_CLOSE_BTN)
        SCREEN.blit(FONT_TEXTBOX.render("X", True, WHITE), (FILE_CLOSE_BTN.x + 25, FILE_CLOSE_BTN.y + 5))



    # -----------------------------
    # NEXT STORY
    # -----------------------------
    elif current_screen == "NEXT_STORY":
        SCREEN.blit(INTRO_IMAGES[6], (0, 0))
        draw_textbox_typing(INTRO6_LINES[intro_index], 250, 550, 700, 150)

    elif current_screen == "NEXT1_STORY":
        SCREEN.blit(INTRO_IMAGES[7], (0, 0))
        draw_textbox_typing(INTRO7_LINES[intro_index], 250, 550, 700, 150)



    # -----------------------------
    # ROOM 1 화면 (금고/칠판/문)
    # -----------------------------
    elif current_screen == "ROOM_SCREEN1":
        SCREEN.blit(room1, (0, 0))
        txt = FONT_BUTTON.render("단서를 찾아서 이 방을 탈출하자!", True, GRAY)
        SCREEN.blit(txt, (40, 40))



    # -----------------------------
    # 칠판 화면
    # -----------------------------
    elif current_screen == "BOARD_SCREEN":
        SCREEN.blit(board, (0, 0))

        BOARD_BACK_BTN = pygame.Rect(40, 40, 150, 50)
        back_txt = FONT_BUTTON.render("← 뒤로가기", True, GRAY)
        SCREEN.blit(back_txt, (BOARD_BACK_BTN.x + 5, BOARD_BACK_BTN.y))

        red = (255, 50, 50)
        expr = FONT_TEXTBOX.render("print(300x4+50/10+6)", True, red)
        SCREEN.blit(expr, (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 50))


    # -----------------------------

    # SAFE LOCK SCREEN (금고)

    # -----------------------------

    elif current_screen == "SAFE_LOCK_SCREEN":

        SCREEN.blit(safe, (0, 0))

        title = FONT_TEXTBOX.render("금고가 잠겨 있습니다.", True, WHITE)

        SCREEN.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 80))

        sub = FONT_BUTTON.render("번호를 맞혀 금고를 여세요.", True, GRAY)

        SCREEN.blit(sub, (SCREEN_WIDTH // 2 - sub.get_width() // 2, 130))

        # 버튼 리스트 초기화

        SAFE_UP.clear()

        SAFE_DOWN.clear()

        start_x = 300

        y_up = 250

        y_num = 320

        y_down = 390

        # 4칸 금고 UI 그리기

        for i in range(4):
            x = start_x + i * 150

            # ▲ 버튼

            up_rect = pygame.Rect(x, y_up, 80, 50)

            pygame.draw.rect(SCREEN, (100, 100, 255), up_rect)

            SCREEN.blit(FONT_BUTTON.render("▲", True, WHITE), (x + 25, y_up + 5))

            SAFE_UP.append(up_rect)

            # 숫자

            num = FONT_TEXTBOX.render(str(safe_input[i]), True, WHITE)

            SCREEN.blit(num, (x + 30, y_num))

            # ▼ 버튼

            down_rect = pygame.Rect(x, y_down, 80, 50)

            pygame.draw.rect(SCREEN, (100, 100, 255), down_rect)

            SCREEN.blit(FONT_BUTTON.render("▼", True, WHITE), (x + 25, y_down + 5))

            SAFE_DOWN.append(down_rect)

        # 확인 버튼

        SAFE_CONFIRM_BTN = pygame.Rect(500, 500, 200, 70)

        pygame.draw.rect(SCREEN, (0, 180, 0), SAFE_CONFIRM_BTN)

        SCREEN.blit(FONT_TEXTBOX.render("확인", True, WHITE), (560, 520))

        # 뒤로가기 버튼

        SAFE_BACK_BTN = pygame.Rect(40, 40, 140, 50)

        pygame.draw.rect(SCREEN, (80, 80, 80), SAFE_BACK_BTN)

        SCREEN.blit(FONT_BUTTON.render("← 뒤로", True, WHITE),

                    (SAFE_BACK_BTN.x + 25, SAFE_BACK_BTN.y + 10))

        # 오류 메시지

        if error_message:
            err = FONT_TEXTBOX.render(error_message, True, (255, 80, 80))

            SCREEN.blit(err, (SCREEN_WIDTH // 2 - err.get_width() // 2, 600))




    # -----------------------------
    # 금고 열림 화면
    # -----------------------------
    elif current_screen == "SAFE_UNLOCK_SCREEN":
        SCREEN.blit(safe, (0, 0))
        msg = FONT_TEXTBOX.render("금고가 열렸다!", True, WHITE)
        SCREEN.blit(msg, (SCREEN_WIDTH // 2 - msg.get_width() // 2, 250))

        SCREEN.blit(key, (
            SCREEN_WIDTH // 2 - key.get_width() // 2,
            SCREEN_HEIGHT // 2 - key.get_height() // 2 + 40
        ))

        # ★ 3초 후 자동 종료
        if pygame.time.get_ticks() - safe_unlock_start_time >= 3000:
            current_screen = "ROOM_SCREEN1"


    # -----------------------------
    # MAP SCREEN
    # -----------------------------
    elif current_screen == "MAP_SCREEN":
        SCREEN.blit(map, MAP_RECT.topleft)
        player_group.draw(SCREEN)



    # -----------------------------
    # 방 2 화면
    # -----------------------------
    elif current_screen == "ROOM2":
        SCREEN.blit(room2, (0, 0))

        # 엘리베이터 메시지 (2초 유지)
        if show_elevator_msg:
            SCREEN.blit(FONT_TEXTBOX.render("이건 작동하지 않는건가..?", True, WHITE),
                        (SCREEN_WIDTH // 2 - 200, 80))

            if pygame.time.get_ticks() - elevator_msg_time > 2000:
                show_elevator_msg = False

        # 발전기 메시지 (2초 유지)
        if show_generator_msg:
            SCREEN.blit(FONT_TEXTBOX.render("작동하지 않는다.", True, WHITE),
                        (SCREEN_WIDTH // 2 - 150, 130))

            if pygame.time.get_ticks() - generator_msg_time > 2000:
                show_generator_msg = False

        if generator_key:
            # 열쇠 이미지 화면 중앙에 표시
            SCREEN.blit(
                key,
                (
                    SCREEN_WIDTH // 2 - key.get_width() // 2,
                    SCREEN_HEIGHT // 2 - key.get_height() // 2
                )
            )

            # 1.5초(1500ms) 지나면 자동으로 MAP_SCREEN으로 이동
            if pygame.time.get_ticks() - generator_key_time > 2000:


                generator_key = False  # 열쇠 표시 끄고
                current_screen = "MAP_SCREEN"  # 맵 화면으로 전환

            # 사라짐




    # -----------------------------
    # BOX2 화면
    # -----------------------------
    elif current_screen == "BOX2":
        SCREEN.blit(box,
                    (SCREEN_WIDTH//2 - box.get_width()//2,
                     SCREEN_HEIGHT//2 - box.get_height()//2))



    # -----------------------------
    # BOX_OPEN 화면 (핵심 수정 완료!)
    # -----------------------------
    # -----------------------------
    # BOX_OPEN 화면
    # -----------------------------
    elif current_screen == "BOX_OPEN":

        # 박스 위치
        bx = SCREEN_WIDTH // 2 - box_open.get_width() // 2
        by = SCREEN_HEIGHT // 2 - box_open.get_height() // 2

        SCREEN.blit(box_open, (bx, by))

        # 점점 반짝임
        global highlight_alpha, highlight_direction
        highlight_alpha += highlight_direction
        if highlight_alpha >= 180 or highlight_alpha <= 40:
            highlight_direction *= -1

        # 현재 자를 전선
        target_wire = WIRE_ORDER[wire_progress] if wire_progress < 4 else None

        # 전선 점 위치 = 그대로 화면 좌표
        for wire_name, (wx, wy) in WIRE_POINTS.items():

            # 반짝임(현재 잘라야 할 전선만)
            if wire_name == target_wire:
                glow = pygame.Surface((40, 40), pygame.SRCALPHA)
                glow.fill((255, 255, 0, highlight_alpha))
                SCREEN.blit(glow, (wx - 20, wy - 20))

            # 이미 잘린 전선 X 표시
            if wire_name in cut_wires:
                pygame.draw.line(SCREEN, (0, 0, 0), (wx - 10, wy - 10), (wx + 10, wy + 10), 3)
                pygame.draw.line(SCREEN, (0, 0, 0), (wx + 10, wy - 10), (wx - 10, wy + 10), 3)

        # 레버 표시 (레버 획득 전)
        if (wire_progress >= 4 or lever_auto_show) and not lever_obtained:
            SCREEN.blit(
                lever_img,
                (
                    SCREEN_WIDTH // 2 - lever_img.get_width() // 2,
                    SCREEN_HEIGHT // 2 - lever_img.get_height() // 2
                )
            )

        # 건너뛰기 버튼
        pygame.draw.rect(SCREEN, (60, 60, 60), skip_button_rect, border_radius=10)
        txt = FONT_BUTTON.render("건너뛰기", True, WHITE)
        SCREEN.blit(txt, (skip_button_rect.x + 40, skip_button_rect.y + 10))

        # 뒤로가기 버튼
        pygame.draw.rect(SCREEN, (50, 50, 50), BOX_OPEN_BACK_BTN)
        SCREEN.blit(FONT_BUTTON.render("← 뒤로", True, WHITE),
                    (BOX_OPEN_BACK_BTN.x + 20, BOX_OPEN_BACK_BTN.y + 10))

        # (레버 나오게 하는 코드 / 뒤로가기 텍스트 등은 그 아래에 계속 두면 됨)




    # -----------------------------
    # CHAIR_ZOOM
    # -----------------------------
    elif current_screen == "CHAIR_ZOOM":
        SCREEN.blit(chair_zoom,
                    (SCREEN_WIDTH//2 - chair_zoom.get_width()//2,
                     SCREEN_HEIGHT//2 - chair_zoom.get_height()//2))

        SCREEN.blit(FONT_BUTTON.render("← 뒤로가기", True, WHITE),
                    (CHAIR_BACK_BTN.x, CHAIR_BACK_BTN.y))

    elif current_screen == "ROOM3":
        SCREEN.blit(orig_bg_closed, (0, 0))
        # 필요하면 대사 or 안내문 추가 가능

    # -----------------------------
    # INTRO / STORY 안내 문구
    # -----------------------------
    if current_screen.startswith("INTRO_TEXT") or current_screen == "COMIC5_SCENE":
        tip = FONT_BUTTON.render("클릭해서 계속...", True, GRAY)
        SCREEN.blit(tip, (SCREEN_WIDTH//2 - 80, SCREEN_HEIGHT - 40))

    # ---------------------------------------------------------
    # 게임 루프
    # ---------------------------------------------------------
# ---------------------------------------------------------
# 게임 루프
# ---------------------------------------------------------
def game_loop():
    global game_started, current_screen
    global intro_index, typing_index, typed_text
    global user_input, error_message
    global key_obtained, safe_unlock_start_time
    global show_elevator_msg, elevator_msg_time
    global show_generator_msg, generator_msg_time
    global wire_progress, cut_wires
    global SAFE_CONFIRM_BTN, SAFE_BACK_BTN, SAFE_UP, SAFE_DOWN
    global generator_key
    global generator_key_time
    global generator_unlocked
    global lever_obtained
    global lever_auto_show
    global highlight_alpha, highlight_direction

    running = True

    # 클릭이 없을 때도 draw_scene이 안전하게 동작하도록 기본 좌표 설정
    mx, my = -1, -1

    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            # -----------------------------------
            # PC 화면 키보드 입력
            # -----------------------------------
            if current_screen == "PC_SCREEN":
                if event.type == pygame.TEXTINPUT:
                    user_input += event.text

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]

                    elif event.key == pygame.K_RETURN:
                        if check_password(user_input):
                            current_screen = "COMIC5_SCENE"
                            intro_index = 0
                            typing_index = 0
                            error_message = ""
                        else:
                            error_message = "비밀번호를 잘못 입력하셨습니다."

                        user_input = ""

            # -----------------------------------
            # 마우스 클릭 처리
            # -----------------------------------
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                print("클릭 좌표:", mx, my)

                if not game_started:
                    game_started = True
                    continue

                # --------------- INTRO 진행 ---------------
                if current_screen.startswith("INTRO_TEXT_"):
                    idx = int(current_screen[-1]) - 1
                    lines = [INTRO1_LINES, INTRO2_LINES, INTRO3_LINES, INTRO4_LINES][idx]

                    # 타자기 효과 다 안 끝났으면 스킵
                    if typing_index < len(lines[intro_index]):
                        typing_index = len(lines[intro_index])
                    else:
                        intro_index += 1

                        # 다음 섹션으로 이동
                        if intro_index >= len(lines):
                            next_map = {
                                "INTRO_TEXT_1": "INTRO_TEXT_2",
                                "INTRO_TEXT_2": "INTRO_TEXT_3",
                                "INTRO_TEXT_3": "ROOM_SCREEN",
                                "INTRO_TEXT_4": "ROOM_SCREEN_2",
                            }

                            current_screen = next_map[current_screen]
                            intro_index = 0

                        typing_index = 0


                # ---------- 비번 성공 후 만화5 ----------
                elif current_screen == "COMIC5_SCENE":
                    if typing_index < len(INTRO5_LINES[intro_index]):
                        typing_index = len(INTRO5_LINES[intro_index])
                    else:
                        intro_index += 1
                        if intro_index >= len(INTRO5_LINES):
                            current_screen = "PC_FILE_SCREEN"
                            intro_index = 0
                            typing_index = 0
                        else:
                            typing_index = 0


                # ---------- 서랍 화면 ----------
                elif current_screen == "ROOM_SCREEN":
                    if DRAWER_AREA.collidepoint((mx, my)):
                        current_screen = "DRAWER_POPUP"

                elif current_screen == "DRAWER_POPUP":
                    if CLOSE_BTN.collidepoint((mx, my)):
                        current_screen = "INTRO_TEXT_4"
                        intro_index = 0
                        typing_index = 0


                # ---------- 컴퓨터 클릭 ----------
                elif current_screen == "ROOM_SCREEN_2":
                    if COMPUTER_AREA.collidepoint((mx, my)):
                        current_screen = "PC_SCREEN"


                # ---------- 파일 목록 ----------
                elif current_screen == "PC_FILE_SCREEN":
                    if FOLDER_PLAN.collidepoint((mx, my)):
                        current_screen = "PLAN_SCREEN"
                    elif FOLDER_TARGET.collidepoint((mx, my)):
                        current_screen = "TARGET_SCREEN"
                    elif FOLDER_EMPTY1.collidepoint((mx, my)):
                        current_screen = "EMPTY_FILE1_SCREEN"
                    elif FOLDER_EMPTY2.collidepoint((mx, my)):
                        current_screen = "EMPTY_FILE2_SCREEN"
                    elif FILE_NEXT_BTN.collidepoint((mx, my)):
                        current_screen = "NEXT_STORY"


                # ---------- 폴더 닫기 ----------
                elif current_screen in ["PLAN_SCREEN", "TARGET_SCREEN",
                                        "EMPTY_FILE1_SCREEN", "EMPTY_FILE2_SCREEN"]:
                    if FILE_CLOSE_BTN.collidepoint((mx, my)):
                        current_screen = "PC_FILE_SCREEN"


                # ---------- NEXT STORY ----------
                elif current_screen == "NEXT_STORY":
                    if typing_index < len(INTRO6_LINES[intro_index]):
                        typing_index = len(INTRO6_LINES[intro_index])
                    else:
                        intro_index += 1
                        if intro_index >= len(INTRO6_LINES):
                            current_screen = "NEXT1_STORY"
                            intro_index = 0
                        typing_index = 0


                elif current_screen == "NEXT1_STORY":
                    if typing_index < len(INTRO7_LINES[intro_index]):
                        typing_index = len(INTRO7_LINES[intro_index])
                    else:
                        intro_index += 1
                        if intro_index >= len(INTRO7_LINES):
                            current_screen = "ROOM_SCREEN1"
                            intro_index = 0
                        typing_index = 0


                # ---------- 방1: 금고/칠판/문 ----------
                elif current_screen == "ROOM_SCREEN1":
                    if safe_rect.collidepoint((mx, my)):
                        current_screen = "SAFE_LOCK_SCREEN"

                    elif board_rect.collidepoint((mx, my)):
                        current_screen = "BOARD_SCREEN"

                    elif door_rect.collidepoint((mx, my)):
                        if key_obtained:
                            current_screen = "MAP_SCREEN"
                        else:
                            print("문이 잠겨 있습니다.")


                # ---------- 금고 잠금 화면 ----------
                elif current_screen == "SAFE_LOCK_SCREEN":

                    if SAFE_BACK_BTN.collidepoint((mx, my)):
                        current_screen = "ROOM_SCREEN1"
                        error_message = ""

                    # 숫자 증가
                    for i, rect in enumerate(SAFE_UP):
                        if rect.collidepoint((mx, my)):
                            safe_input[i] = (safe_input[i] + 1) % 10

                    # 숫자 감소
                    for i, rect in enumerate(SAFE_DOWN):
                        if rect.collidepoint((mx, my)):
                            safe_input[i] = (safe_input[i] - 1) % 10

                    # 확인 버튼
                    if SAFE_CONFIRM_BTN.collidepoint((mx, my)):
                        if safe_input == SAFE_CODE:
                            key_obtained = True
                            safe_unlock_start_time = pygame.time.get_ticks()
                            current_screen = "SAFE_UNLOCK_SCREEN"
                            error_message = ""



                # ---------- 칠판 화면 ----------
                elif current_screen == "BOARD_SCREEN":
                    if BOARD_BACK_BTN.collidepoint((mx, my)):
                        current_screen = "ROOM_SCREEN1"


                # ---------------------------------------------------
                # 방2: 엘리베이터 / 발전기 / 의자 / 박스
                # ---------------------------------------------------
                elif current_screen == "ROOM2":

                    # ⭐⭐⭐ ROOM2 → MAP 먼저 검사 (가장 위에 둬야 함)
                    if ROOM2_TO_MAP_CLICK.collidepoint((mx, my)):
                        print("ROOM2 → MAP_SCREEN 이동!")
                        current_screen = "MAP_SCREEN"
                        continue

                    # 엘리베이터
                    if ELB_RECT.collidepoint((mx, my)):
                        show_elevator_msg = True
                        elevator_msg_time = pygame.time.get_ticks()

                    # 발전기
                    elif GENERATOR_RECT.collidepoint((mx, my)):
                        if lever_obtained and not generator_unlocked:
                            print("발전기 해결 → 열쇠 획득!")
                            generator_unlocked = True
                            generator_key = True
                            generator_key_time = pygame.time.get_ticks()
                            key_obtained = True
                        else:
                            show_generator_msg = True
                            generator_msg_time = pygame.time.get_ticks()

                    elif CHAIR_RECT.collidepoint((mx, my)):
                        current_screen = "CHAIR_ZOOM"

                    elif BOX_RECT.collidepoint((mx, my)):
                        current_screen = "BOX2"



                # ---------- BOX2 → BOX_OPEN ----------
                elif current_screen == "BOX2":
                    current_screen = "BOX_OPEN"


                # ---------------------------------------------------
                # BOX_OPEN 전선 클릭 처리 (핵심!)
                # ---------------------------------------------------
                # BOX_OPEN 클릭 처리
                elif current_screen == "BOX_OPEN":

                    # 뒤로가기
                    if BOX_OPEN_BACK_BTN.collidepoint((mx, my)):
                        current_screen = "ROOM2"
                        continue

                    # 건너뛰기
                    if skip_button_rect.collidepoint((mx, my)):
                        lever_auto_show = True
                        lever_show_start_time = pygame.time.get_ticks()
                        wire_progress = len(WIRE_ORDER)
                        continue

                    # 레버가 화면에 있고 아직 획득 전이면 → 클릭 감지
                    if (wire_progress >= 4 or lever_auto_show) and not lever_obtained:

                        lever_rect = pygame.Rect(
                            SCREEN_WIDTH // 2 - lever_img.get_width() // 2,
                            SCREEN_HEIGHT // 2 - lever_img.get_height() // 2,
                            lever_img.get_width(),
                            lever_img.get_height()
                        )

                        if lever_rect.collidepoint((mx, my)):
                            print("레버 획득!!")
                            lever_obtained = True
                            current_screen = "ROOM2"
                            continue

                    # 레버가 아직 없으면 → 전선 클릭 처리
                    if wire_progress < 4:

                        target_wire = WIRE_ORDER[wire_progress]

                        for wire_name, (wx, wy) in WIRE_POINTS.items():
                            rect = pygame.Rect(wx - 15, wy - 15, 30, 30)

                            if rect.collidepoint((mx, my)):

                                if wire_name == target_wire:
                                    cut_wires.add(wire_name)
                                    wire_progress += 1
                                    print("정답 전선:", wire_name)

                                else:
                                    print("오답! 다시 시작")
                                    cut_wires.clear()
                                    wire_progress = 0

                                break





                # ---------- 의자 확대 ----------
                elif current_screen == "CHAIR_ZOOM":
                    if CHAIR_BACK_BTN.collidepoint((mx, my)):
                        current_screen = "ROOM2"

        # ---------------------------------------------------
        # 맵 이동 업데이트
        # ---------------------------------------------------
        if current_screen == "MAP_SCREEN":
            player_group.update()

        # ---------------------------------------------------
        # 화면 그리기 (mx, my 전달!!)
        # ---------------------------------------------------
        draw_scene(mx, my)
        pygame.display.flip()
        clock.tick(60)

        # -------------------------------
        # MAP 화면 클릭 → ROOM3 이동
        # -------------------------------
        # ----------------------------------------
        # ROOM2 → MAP 이동 (클릭 기반) ← 가장 먼저!
        # ----------------------------------------


        # ---------------------------------------------------
        # MAP → ROOM2 이동
        # ---------------------------------------------------
        # MAP → ROOM2 이동 (발전기 애니메이션 중이 아닐 때만)
        # ---------------------------------------------------
        # MAP 영역에서 ROOM 이동 먼저 체크!
        # ---------------------------------------------------
        if current_screen == "MAP_SCREEN" and not generator_key:
            px = player.rect.centerx
            py = player.rect.centery
            print("플레이어 위치:", px, py)

            # MAP → ROOM2
            if door_to_room2_rect.colliderect(player.rect):
                print("MAP → ROOM2 이동!")
                current_screen = "ROOM2"

            # MAP → ROOM3
        if door_to_room3_rect.collidepoint(mx, my):
            print("MAP → ROOM3 이동 (클릭)!!")
            current_screen = "ROOM3"
            continue



    pygame.quit()
    sys.exit()



# ---------------------------------------------------------
# 실행
# ---------------------------------------------------------
if __name__ == "__main__":
    game_loop()




