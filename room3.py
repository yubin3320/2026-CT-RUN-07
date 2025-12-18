import pygame
import sys
import time

pygame.init()

# -------------------------------
#  폰트 로드
# -------------------------------
font = pygame.font.Font("HCRBatang-Bold.ttf", 40)
font_small = pygame.font.Font("HCRBatang-Bold.ttf", 24)  # 작은 안내 텍스트용

# -------------------------------
#  배경 이미지 로드 + 리사이즈
#   [방 3 잠김], [방 3 열림], [바깥] 사용
# -------------------------------
orig_bg_closed = pygame.image.load("방 3 잠김.png")   # 기본 배경
orig_bg_open   = pygame.image.load("방 3 열림.jpg")   # 퀘스트 완료 후 배경
orig_outside   = pygame.image.load("바깥.png")        # 엔딩 배경

# 닫힌 배경을 기준으로 화면 크기 결정
TARGET_HEIGHT = 650
ratio = TARGET_HEIGHT / orig_bg_closed.get_height()
TARGET_WIDTH = int(orig_bg_closed.get_width() * ratio)

bg_closed = pygame.transform.scale(orig_bg_closed, (TARGET_WIDTH, TARGET_HEIGHT))
bg_open   = pygame.transform.scale(orig_bg_open,   (TARGET_WIDTH, TARGET_HEIGHT))
outside_bg = pygame.transform.scale(orig_outside, (TARGET_WIDTH, TARGET_HEIGHT))

WIDTH, HEIGHT = TARGET_WIDTH, TARGET_HEIGHT
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Room 3")

bg_closed = bg_closed.convert()
bg_open   = bg_open.convert()
outside_bg = outside_bg.convert()

# 현재 사용할 배경 (처음엔 잠김 상태)
current_bg = bg_closed

# -------------------------------
#  이미지 로드 (컵, 손전등, 인체모형, on 버튼)
# -------------------------------
empty_cup_img         = pygame.image.load("빈 컵.png").convert_alpha()          # [빈 컵]
hot_cup_img           = pygame.image.load("뜨신물컵.png").convert_alpha()       # [뜨신물컵]
flashlight_img        = pygame.image.load("손전등.png").convert_alpha()        # [손전등]

mannequin_img         = pygame.image.load("인체모형.png").convert_alpha()      # [인체모형]
mannequin_numbers_img = pygame.image.load("인체모형-숫자.png").convert_alpha()  # [인체모형-숫자]
mannequin_key_img     = pygame.image.load("인체모형 열쇠.png").convert_alpha()  # [인체모형 열쇠]

uv_button_img         = pygame.image.load("on.png").convert_alpha()            # [on 버튼]

# on 버튼 크기 및 위치 (화면 왼쪽 아래)
uv_btn_size = 70
uv_button_img = pygame.transform.scale(uv_button_img, (uv_btn_size, uv_btn_size))
uv_button_rect = uv_button_img.get_rect()
uv_button_rect.left = 20
uv_button_rect.bottom = HEIGHT - 20

# -------------------------------
#  클릭 영역들 (비율 기준)
# -------------------------------

# 정수기 클릭 영역 (오른쪽 부분)
water_dispenser_rect = pygame.Rect(
    int(WIDTH * 0.65),   # x
    int(HEIGHT * 0.25),  # y
    int(WIDTH * 0.20),   # width
    int(HEIGHT * 0.55)   # height
)

# 소파 클릭 영역
sofa_rect = pygame.Rect(
    int(WIDTH * 0.18),
    int(HEIGHT * 0.52),
    int(WIDTH * 0.55),
    int(HEIGHT * 0.32)
)

# 인체모형 클릭 영역 (조금 더 넓게 / 중앙 쪽으로)
mannequin_rect = pygame.Rect(
    int(WIDTH * 0.20),
    int(HEIGHT * 0.10),
    int(WIDTH * 0.30),
    int(HEIGHT * 0.80)
)

# ---------------- utility 함수 ----------------

def draw_text_center(text: str, y: int):
    """지정한 y 위치에 가운데 정렬 텍스트 출력"""
    render = font.render(text, True, (255, 255, 255))
    rect = render.get_rect(center=(WIDTH // 2, y))
    screen.blit(render, rect)


def draw_text_center_small(text: str, y: int):
    """작은 폰트로 중앙 정렬 텍스트 출력"""
    render = font_small.render(text, True, (200, 200, 200))
    rect = render.get_rect(center=(WIDTH // 2, y))
    screen.blit(render, rect)


def type_line_with_click(text: str):
    """
    배경(current_bg)을 깔고
    한 줄 텍스트를 타이핑 효과로 보여준 뒤
    클릭하면 종료하는 공통 연출.
    """
    clock = pygame.time.Clock()
    displayed = ""
    index = 0
    typing_done = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if not typing_done:
            if index < len(text):
                index += 1
                displayed = text[:index]
                pygame.time.wait(40)  # 타이핑 속도
            else:
                typing_done = True

        # 배경 및 텍스트 다시 그림
        screen.blit(current_bg, (0, 0))
        draw_text_center(displayed, HEIGHT - 120)

        if typing_done:
            draw_text_center_small("클릭하면 넘어갑니다", HEIGHT - 70)

        pygame.display.update()
        clock.tick(60)

        if typing_done:
            # 타이핑이 끝난 뒤에는 클릭을 기다린다
            clicked = False
            while not clicked:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        clicked = True
                        break

                # 클릭 대기 중에도 화면 유지
                screen.blit(current_bg, (0, 0))
                draw_text_center(displayed, HEIGHT - 120)
                draw_text_center_small("클릭하면 넘어갑니다", HEIGHT - 70)
                pygame.display.update()
                clock.tick(60)
            break


def get_scaled_cup(image: pygame.Surface):
    """
    정수기 크기를 기준으로 컵 이미지 스케일 & 위치 계산
    (정수기보다 조금 더 크게 보이도록 확대)
    """
    scale_factor = 1.1  # 정수기보다 조금 크게

    cup_width = int(water_dispenser_rect.width * scale_factor)
    cup_height = int(water_dispenser_rect.height * scale_factor)

    # 화면을 넘지 않도록 최대 크기 제한
    cup_width = min(cup_width, int(WIDTH * 0.6))
    cup_height = min(cup_height, int(HEIGHT * 0.6))

    scaled = pygame.transform.scale(image, (cup_width, cup_height))
    rect = scaled.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    return scaled, rect

# ---------------- 컵 / 소파 / 손전등 연출 ----------------

def show_empty_cup_first():
    """첫 정수기 클릭: 빈 컵 획득 연출 (3초)"""
    screen.blit(current_bg, (0, 0))

    empty_scaled, rect = get_scaled_cup(empty_cup_img)
    screen.blit(empty_scaled, rect)
    draw_text_center("빈 컵을 획득했다.", rect.bottom + 30)

    pygame.display.update()
    time.sleep(3)


def show_fill_cup_sequence():
    """
    두 번째 정수기 클릭:
    1) 빈 컵 1초
    2) 빈 컵 → 뜨신물컵 크로스 페이드
    3) 뜨신물컵 + '순서를 기억하시오' 5초
    """
    empty_scaled, rect = get_scaled_cup(empty_cup_img)
    hot_scaled, _ = get_scaled_cup(hot_cup_img)  # 크기는 같게

    # 1) 빈 컵 1초
    screen.blit(current_bg, (0, 0))
    screen.blit(empty_scaled, rect)
    pygame.display.update()
    time.sleep(1)

    # 2) 크로스 페이드 (약 0.6초)
    steps = 30
    for i in range(steps + 1):
        alpha_hot = int(255 * (i / steps))
        alpha_empty = 255 - alpha_hot

        empty_scaled.set_alpha(alpha_empty)
        hot_scaled.set_alpha(alpha_hot)

        screen.blit(current_bg, (0, 0))
        screen.blit(empty_scaled, rect)
        screen.blit(hot_scaled, rect)
        draw_text_center("순서를 기억하시오", rect.bottom + 30)

        pygame.display.update()
        pygame.time.wait(20)  # 20ms * 30 ≈ 0.6초

    # 3) 뜨신물컵 고정 + 텍스트 5초
    hot_scaled.set_alpha(255)
    screen.blit(current_bg, (0, 0))
    screen.blit(hot_scaled, rect)
    draw_text_center("순서를 기억하시오", rect.bottom + 30)
    pygame.display.update()
    time.sleep(5)


def show_sofa_dialog():
    """
    뜨신물컵 연출 이후에 나오는 소파 관련 텍스트 두 줄:
    1) '소파는 왜 있는 걸까?'
    2) '뭐가 있을지 모르니 클릭해보자.'
    각각 타이핑 효과 + 클릭으로 다음 문장
    """
    lines = [
        "소파는 왜 있는 걸까?",
        "뭐가 있을지 모르니 클릭해보자."
    ]
    for line in lines:
        type_line_with_click(line)


def show_flashlight():
    """
    소파 클릭 시: 손전등 이미지 +
    '손전등을 획득했다'를 타이핑 효과로 보여주고, 클릭 시 종료.
    """
    text = "손전등을 획득했다"

    clock = pygame.time.Clock()
    displayed = ""
    index = 0
    typing_done = False

    # 손전등 이미지 크기 조정
    max_w = int(WIDTH * 0.4)
    max_h = int(HEIGHT * 0.3)
    iw, ih = flashlight_img.get_size()
    ratio = min(max_w / iw, max_h / ih)
    fw, fh = int(iw * ratio), int(ih * ratio)

    flashlight_scaled = pygame.transform.scale(flashlight_img, (fw, fh))
    f_rect = flashlight_scaled.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))

    # 메인 타이핑 루프
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if not typing_done:
            if index < len(text):
                index += 1
                displayed = text[:index]
                pygame.time.wait(40)  # 타이핑 속도
            else:
                typing_done = True

        # 배경 + 손전등 + 텍스트
        screen.blit(current_bg, (0, 0))
        screen.blit(flashlight_scaled, f_rect)
        draw_text_center(displayed, f_rect.bottom + 40)

        if typing_done:
            draw_text_center_small("클릭하면 넘어갑니다", HEIGHT - 60)

        pygame.display.update()
        clock.tick(60)

        if typing_done:
            # 타이핑이 끝난 뒤 클릭 대기
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        waiting = False
                        return  # 정상 종료

                screen.blit(current_bg, (0, 0))
                screen.blit(flashlight_scaled, f_rect)
                draw_text_center(displayed, f_rect.bottom + 40)
                draw_text_center_small("클릭하면 넘어갑니다", HEIGHT - 60)
                pygame.display.update()
                clock.tick(60)


def show_post_flashlight_dialog():
    """손전등을 얻은 뒤 나오는 안내 텍스트 2줄"""
    type_line_with_click("손전등은 어디에 쓰는 걸까?")
    type_line_with_click("아직 관찰하지 않은 인체 모형을 클릭해보자")

# ---------------- 인체모형 퍼즐 텍스트 보조 ----------------

def show_on_button_hint_over_scene(mannequin_scaled, m_rect):
    """
    퍼즐 진입 직후, 일반 인체모형 + on 버튼이 보이는 상태에서
    '새로 생긴 on 버튼을 눌러보자' 텍스트를 한 번 보여준다.
    """
    clock = pygame.time.Clock()
    text = "새로 생긴 on 버튼을 눌러보자"
    displayed = ""
    index = 0
    typing_done = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if not typing_done:
            if index < len(text):
                index += 1
                displayed = text[:index]
                pygame.time.wait(40)
            else:
                typing_done = True

        # 퍼즐 장면 (일반 인체모형 + 버튼) 그리기
        screen.blit(current_bg, (0, 0))
        screen.blit(mannequin_scaled, m_rect)
        screen.blit(uv_button_img, uv_button_rect)

        draw_text_center(displayed, m_rect.bottom + 40)
        if typing_done:
            draw_text_center_small("클릭하면 넘어갑니다", HEIGHT - 60)

        pygame.display.update()
        clock.tick(60)

        if typing_done:
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        waiting = False
                        return

                screen.blit(current_bg, (0, 0))
                screen.blit(mannequin_scaled, m_rect)
                screen.blit(uv_button_img, uv_button_rect)
                draw_text_center(displayed, m_rect.bottom + 40)
                draw_text_center_small("클릭하면 넘어갑니다", HEIGHT - 60)
                pygame.display.update()
                clock.tick(60)


def show_numbers_text_over_scene(mannequin_numbers_scaled, m_rect):
    """
    on 버튼을 눌러 숫자가 보이게 된 직후,
    현재 퍼즐 화면(숫자 인체모형 + on 버튼) 위에
    '손전등이 켜져 모형에 써있는 숫자가 보인다' 텍스트를
    타이핑 효과로 한 번 보여주는 함수.
    """
    clock = pygame.time.Clock()
    text = "손전등이 켜져 모형에 써있는 숫자가 보인다"
    displayed = ""
    index = 0
    typing_done = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if not typing_done:
            if index < len(text):
                index += 1
                displayed = text[:index]
                pygame.time.wait(40)
            else:
                typing_done = True

        # 퍼즐 장면 다시 그림
        screen.blit(current_bg, (0, 0))
        screen.blit(mannequin_numbers_scaled, m_rect)
        screen.blit(uv_button_img, uv_button_rect)

        draw_text_center(displayed, m_rect.bottom + 40)
        if typing_done:
            draw_text_center_small("클릭하면 넘어갑니다", HEIGHT - 60)

        pygame.display.update()
        clock.tick(60)

        if typing_done:
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        waiting = False
                        return

                screen.blit(current_bg, (0, 0))
                screen.blit(mannequin_numbers_scaled, m_rect)
                screen.blit(uv_button_img, uv_button_rect)
                draw_text_center(displayed, m_rect.bottom + 40)
                draw_text_center_small("클릭하면 넘어갑니다", HEIGHT - 60)
                pygame.display.update()
                clock.tick(60)


def show_mannequin_key_scene(m_rect, mw, mh):
    """
    3-2-1-4 정답을 맞춘 뒤:
    인체모형 열쇠 이미지 + '열쇠를 발견했다' 텍스트를
    타이핑 효과로 보여주고, 클릭하면 종료.
    """
    clock = pygame.time.Clock()
    text = "열쇠를 발견했다"
    displayed = ""
    index = 0
    typing_done = False

    mannequin_key_scaled = pygame.transform.scale(mannequin_key_img, (mw, mh))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if not typing_done:
            if index < len(text):
                index += 1
                displayed = text[:index]
                pygame.time.wait(40)
            else:
                typing_done = True

        screen.blit(current_bg, (0, 0))
        screen.blit(mannequin_key_scaled, m_rect)
        draw_text_center(displayed, m_rect.bottom + 40)
        if typing_done:
            draw_text_center_small("클릭하면 넘어갑니다", HEIGHT - 60)

        pygame.display.update()
        clock.tick(60)

        if typing_done:
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        waiting = False
                        return

                screen.blit(current_bg, (0, 0))
                screen.blit(mannequin_key_scaled, m_rect)
                draw_text_center(displayed, m_rect.bottom + 40)
                draw_text_center_small("클릭하면 넘어갑니다", HEIGHT - 60)
                pygame.display.update()
                clock.tick(60)

# ---------------- 엔딩 ----------------

def show_ending():
    """
    방 3를 탈출한 뒤 바깥 배경을 보여주며
    엔딩 텍스트 5줄을 순서대로 보여주고,
    마지막 문장 뒤 클릭 시 게임 종료.
    """
    global current_bg
    current_bg = outside_bg

    lines = [
        "나는 끝내 기계가 되지 않았다.",
        "차갑던 시스템에서 벗어난 지금, 내 심장은 분명히...",
        "인간의 박동으로 뛰고 있다.",
        "그들은 나를 기계로 만들지 못했다.",
        "어둠을 지나 살아남은 나는... 여전히 인간이다."
    ]

    for line in lines:
        type_line_with_click(line)

    pygame.quit()
    sys.exit()

# ---------------- 인체모형 퍼즐 본체 ----------------

def get_clicked_number(mx, my, m_rect, mw, mh):
    """인체모형 숫자 이미지에서 클릭된 부분이 1/2/3/4 중 무엇인지 판정"""
    cx = m_rect.centerx
    top = m_rect.top

    # 대략적인 영역 설정 (이미지 비율 기준, 필요하면 조정)
    area_1 = pygame.Rect(cx - mw * 0.10, top + mh * 0.05, mw * 0.20, mh * 0.18)  # 머리(1)
    area_2 = pygame.Rect(cx - mw * 0.18, top + mh * 0.25, mw * 0.36, mh * 0.18)  # 가슴(2)
    area_3 = pygame.Rect(m_rect.left + mw * 0.02, top + mh * 0.45, mw * 0.20, mh * 0.22)  # 왼팔(3)
    area_4 = pygame.Rect(cx + mw * 0.05, top + mh * 0.55, mw * 0.25, mh * 0.30)  # 오른다리(4)

    if area_1.collidepoint(mx, my):
        return 1
    if area_2.collidepoint(mx, my):
        return 2
    if area_3.collidepoint(mx, my):
        return 3
    if area_4.collidepoint(mx, my):
        return 4
    return None


def run_mannequin_puzzle():
    """
    인체모형을 크게 보여주고,
    on 버튼을 누르면 숫자 모형으로 바뀌며
    3-2-1-4 순서로 클릭해야 성공하는 퍼즐.
    성공 시 열쇠 연출 후 엔딩으로 바로 이동한다.
    """
    global current_bg, room_cleared

    clock = pygame.time.Clock()

    # 인체모형(일반) / 숫자 이미지 크기 조정
    max_w = int(WIDTH * 0.5)
    max_h = int(HEIGHT * 0.8)
    iw, ih = mannequin_img.get_size()
    ratio = min(max_w / iw, max_h / ih)
    mw, mh = int(iw * ratio), int(ih * ratio)

    mannequin_normal_scaled = pygame.transform.scale(mannequin_img, (mw, mh))
    mannequin_numbers_scaled = pygame.transform.scale(mannequin_numbers_img, (mw, mh))

    m_rect = mannequin_normal_scaled.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))

    # 퍼즐 진입 직후: 일반 모형 + on 버튼 + 힌트 텍스트
    current_bg = bg_closed if not room_cleared else bg_open
    show_on_button_hint_over_scene(mannequin_normal_scaled, m_rect)

    numbers_visible = False
    sequence = []
    correct_sequence = [3, 2, 1, 4]

    running_puzzle = True
    while running_puzzle:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                # on 버튼 클릭 → 숫자 모형으로 전환
                if uv_button_rect.collidepoint(mx, my):
                    if not numbers_visible:
                        numbers_visible = True
                        show_numbers_text_over_scene(mannequin_numbers_scaled, m_rect)

                # 숫자가 보이는 상태에서만 숫자 클릭 처리
                elif numbers_visible and m_rect.collidepoint(mx, my):
                    num = get_clicked_number(mx, my, m_rect, mw, mh)
                    if num is not None:
                        seq_index = len(sequence)
                        if seq_index < len(correct_sequence) and num == correct_sequence[seq_index]:
                            sequence.append(num)
                            if len(sequence) == len(correct_sequence):
                                # 퍼즐 성공 → 열쇠 연출 후 방 열기 + 엔딩
                                show_mannequin_key_scene(m_rect, mw, mh)
                                room_cleared = True
                                show_ending()  # 엔딩에서 게임 종료
                        else:
                            # 틀리면 초기화
                            sequence = []

        # 퍼즐 화면 그리기
        current_bg = bg_open if room_cleared else bg_closed
        screen.blit(current_bg, (0, 0))

        if numbers_visible:
            screen.blit(mannequin_numbers_scaled, m_rect)
        else:
            screen.blit(mannequin_normal_scaled, m_rect)

        screen.blit(uv_button_img, uv_button_rect)

        pygame.display.update()
        clock.tick(60)

# ---------------- 메인 루프 ----------------

start_ticks = pygame.time.get_ticks()  # 시작 시각(ms)

cup_state = 0                 # 0: 없음, 1: 빈 컵 획득, 2: 뜨신물컵까지 완료
sofa_dialog_shown = False     # 소파 힌트 텍스트가 이미 나왔는지
flashlight_obtained = False   # 손전등을 이미 얻었는지
post_flashlight_dialog_shown = False  # 손전등 이후 대사(2줄)를 보여줬는지
room_cleared = False          # 퍼즐 완료 시 True

running = True
while running:
    # 방 상태에 따라 배경 선택
    current_bg = bg_open if room_cleared else bg_closed

    screen.blit(current_bg, (0, 0))

    elapsed = pygame.time.get_ticks() - start_ticks

    # 상태에 따른 화면 하단 안내 텍스트
    if cup_state == 0:
        if 1000 <= elapsed <= 4000:
            draw_text_center("정수기를 클릭하시오", HEIGHT - 80)
    elif cup_state == 1:
        draw_text_center("정수기를 다시 클릭하시오", HEIGHT - 80)

    # 손전등을 얻었다면 왼쪽 아래 on 버튼 표시 (메인 화면)
    if flashlight_obtained and not room_cleared:
        screen.blit(uv_button_img, uv_button_rect)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()

            # 정수기 클릭
            if water_dispenser_rect.collidepoint(mx, my):
                if cup_state == 0:
                    show_empty_cup_first()
                    cup_state = 1
                elif cup_state == 1:
                    show_fill_cup_sequence()
                    cup_state = 2
                    if not sofa_dialog_shown:
                        show_sofa_dialog()
                        sofa_dialog_shown = True

            # 소파 클릭
            elif sofa_rect.collidepoint(mx, my):
                if not flashlight_obtained:
                    show_flashlight()
                    flashlight_obtained = True
                    if not post_flashlight_dialog_shown:
                        show_post_flashlight_dialog()
                        post_flashlight_dialog_shown = True

            # 인체모형 클릭
            elif mannequin_rect.collidepoint(mx, my):
                if flashlight_obtained and not room_cleared:
                    run_mannequin_puzzle()
                elif not flashlight_obtained:
                    type_line_with_click("어두워서 그런지, 특별한 건 잘 보이지 않는다.")

pygame.quit()
sys.exit()
