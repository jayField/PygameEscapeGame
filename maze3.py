# maze ver3
# 현재 원 복제 해결
# 클래스 정리 + color 함수 정리
# 조건 개선
import pygame

# import time
# pygame.display.update() 꼭 넣어라!!!!!!!!!!!!!#

"""
    initializing pygame
                        """

# 개선 가능성 : game board 내에서 아래 코드들을 구현하고
# 클래스로 객체 생성함으로써, 실행하는 것을 목표로 해보자
# =========> 개선 완료!!!!!!!!!! 20.01.04(16:04)

# set screen size
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

pygame.init()

# set screen of game
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

"""
    All of classes
    Game, Map, User
                    """


# Game : Set basic functions
# color, set rectangle size, position, draw rectangle

class Game:

    def __init__(self):
        pass


    # choose color you want // map,user,gameboard
    # 로직 수정해야됨, parameter가 들어오면 해당 파라미터에 맞는 color가 return
    # 색변경 성공(정회) 19.01.07
    def color(self, c):

        color_list = ["RED", "GREEN", "BLUE", "PURPLE", "BLACK", "GRAY", "WHITE"]
        return_color_list = []

        # return color
        # 개선 : 비효율적임
        for i in color_list:
            if (i == c and c == "RED"):
                RED = 255, 0, 0
                return RED

            elif (i == c and c == "GREEN"):
                GREEN = 0, 255, 0  # Green: R   0, G 255, B   0
                return GREEN

            elif (i == c and c == "BLUE"):
                BLUE = 0, 0, 255  # Blue:  R   0, G   0, B 255
                return BLUE

            elif (i == c and c == "PURPLE"):
                PURPLE = 127, 0, 127  # Purple: R 127, G   0, B 127
                return PURPLE

            elif (i == c and c == "BLACK"):
                BLACK = 0, 0, 0  # Black: R   0, G   0, B   0
                return BLACK

            elif (i == c and c == "GRAY"):
                GRAY = 127, 127, 127  # Gray:  R 127, G 127, B 127
                return GRAY

            elif (i == c and c == "WHITE"):
                WHITE = 255, 255, 255  # White: R 255, G 255, B 255
                return WHITE



    # set x.point, y.point // map, user
    def set_point(self, x, y):
        xPoint = x
        yPoint = y

        return xPoint, yPoint

    # 개선할 점 : 나중에 이 함수로 screen 그리는 함수로 구현해보자
    def rec_size(self, w, h):
        SCREEN_WIDTH = w
        SCREEN_HEIGHT = h

        return SCREEN_WIDTH, SCREEN_HEIGHT

    # draw rectangle
    def drawing_rec(self, s, c, x, y, w, h):
        rect = pygame.Rect((x, y), (w, h))
        pygame.draw.rect(s, c, rect)
        # pygame.display.update()  # screen update // 보류


# Map : set the map of game
# make background of game
# make block squares
# set quit point

class Map(Game):

    # Game Size
    def __init__(self, width, height):
        self.width = width
        self.height = height

    """
    def rec_size(self,w,h):
        SCREEN_WIDTH = w
        SCREEN_HEIGHT = h

        return SCREEN_WIDTH, SCREEN_HEIGHT
    """

    # Drawing Game board, overriding
    def drawing_rec(self, s, c, x, y, w, h):
        rect = pygame.Rect((x, y), (w, h))
        pygame.draw.rect(s, c, rect, 5)

    # set x,y point
    def set_point(self, x, y):
        xPoint = x
        yPoint = y

        return xPoint, yPoint

    # drawing_map
    # 개선 : background랑 square 함수 나누기
    def drawing_map(self, screen):

        BLACK = 0, 0, 0
        background = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.draw.rect(screen, BLACK, background)

        red = 255, 0, 0
        ####### ERROR###################### WHY ERROR###############
        # 해결 => Map 객체 선언을 init 밖에다가 해야한다 왜?????? 이유 알아보기. 20.01.04(16:00)

        # set one of rectangle in map
        map_rec_width, map_rec_height = self.width, self.height

        """
            개선 : 함수로 구현해보자
            screen size
            700 X 700

            100 x 5 씩 5개
            x,y 좌표 100~501
                            """
        for a in range(100, 501, 100):
            for b in range(100, 501, 100):
                # set of x,y point in map
                map_x_point, map_y_point = a, b
                # rect = pygame.Rect((x, y), (w, h))
                rect = pygame.Rect((map_x_point, map_y_point), (map_rec_width, map_rec_height))
                # draw map
                pygame.draw.rect(screen, red, rect, 3)

    # 벽을 만드는 조건, 나중에 개선하자


# User : set the unit of user(round stuff)
# make user moving condition

class User(Game):

    # r = radius of user unit p = position of user
    def __init__(self, r, position):
        self.radius = r
        # self.position = p // 나중에 포지션짤꺼
        self.position = position

    # s= screen, c = color x,y = x,y point r = radius
    # 왜 int로 강제형변환 해야하지?
    """
    def draw_block(screen, color, position):
        #position 위치에 color 색깔의 블록을 그린다
        block = pygame.Rect((position[1] * BLOCK_SIZE, position[0] * BLOCK_SIZE),
                            (BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, color, block)
    """

    # drawing user unit for circle

    def drawing_cir(self, s, c):
        pygame.draw.circle(s, c, (self.position), self.radius)

    # 방향키 움직이는 조건


# Game Board : set game board and all of rules
# set game board and all of rules
# put on map
# 아마 사라질 클래스, 일단 보류

class GameBoard(Game):
    color = ()

    # Map 그리기용 폭, 높이
    map_rec_width = 0
    map_rec_height = 0

    # Map x,y 좌표
    map_x_point = 0
    map_y_point = 0

    def __init__(self, w, h):
        """
            중요한 질문
            왜 init에 Map 객체를 선언해서 사용이 안될까?
                                                """
        # parameter : row and column
        # self.mapped = Map(5,5)

        self.SCREEN_WIDTH = w
        self.SCREEN_HEIGHT = h

    # set Game Board Size(Width, height)
    # w = width h = height
    """
    def set_gameBoard(self,w,h):
        self.width = w
        self.height = h

        return self.width,self.height
    """


"""                     
    initialize pygame
    일단 보류
                        """
# gameboard 실행
# game_board = GameBoard(SCREEN_WIDTH, SCREEN_HEIGHT)


"""
    Main statement
                   """
# Main : make objec of unit and map


if __name__ == "__main__":

    # set unit position[x, y]
    user_block_position = [150, 150]

    # para1 = radius of unit , para2 = user position
    user = User(50, user_block_position)

    # 고정 코드, 실행코드
    while True:
        events = pygame.event.get()  # ❶ 발생한 이벤트 목록을 읽어들인다
        for event in events:  # ❷ 이벤트 목록을 순회하며 각 이벤트를 처리한다
            if event.type == pygame.QUIT:  # ❸ 종료 이벤트가 발생한 경우
                exit()  # ❹ 게임을 종료한다
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    user_block_position[1] -= 100
                if event.key == pygame.K_DOWN:
                    user_block_position[1] += 100
                if event.key == pygame.K_LEFT:
                    user_block_position[0] -= 100
                if event.key == pygame.K_RIGHT:
                    user_block_position[0] += 100

        # para1 = radius, para2 = block_position
        # user = User(50, user_block_position)

        # user_block_position = user.set_point(block_position) # 지정
        # 사실 set_point로 객체 지정해도 되지만, 복잡해짐 단순하게 ㄱ ㄱ

        # para1 : width of square para2: height of square
        # 개선 : 어차피 정사각형이니 하나로 해보자
        mapping = Map(100, 100)

        # drawing back ground and squares
        # 개선 함수 따로 만들기
        mapping.drawing_map(screen)

        # 수정해야할 code // color 함수 실행
        PURPLE = 127, 0, 127

        # drawing unit of user
        # para1: screen para2 : color
        #user.drawing_cir(screen,PURPLE)

        # 왜 RED만 될까????????? 20.01.06 15:55

        user.drawing_cir(screen, user.color("GREEN"))
        #print(user.color("BLUE"))

        # dispay and update
        pygame.display.update()

    pygame.display.flip()

############### 20.1.5 10:34 현재 problem #########################
"""
1. 원이 복제 된다
2. color 함수 해결 
"""

############### 20.1.5.15:45 ################
"""
원복제 해결, map클래스 따로, user class따로 사용해야할듯
"""
