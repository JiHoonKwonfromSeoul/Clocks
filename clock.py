import pygame
import sys
import numpy as np
import math
import os
from datetime import datetime

# 게임 윈도우 크기
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 900

# 색 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (34, 139, 34)
BLUE = (0, 0, 255)
SKYBLUE=(135,206,235)
DEEPBROWN=(101,67,33)

# Pygame 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("20171829Kwon_Clock")

# 윈도우 생성
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 게임 화면 업데이트 속도
clock = pygame.time.Clock()

# assets 경로 설정
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')

#이미지 로드

# 게임 종료 전까지 반복
done = False

#함수:로테이션과 이동, 함수변경

def Rmat(degree):
    radian = np.deg2rad(degree)
    c = np.cos(radian)
    s = np.sin(radian)
    R = np.array( [[ c, -s, 0], [s, c, 0], [0, 0, 1] ] )
    return R

def Tmat(a,b):
    H = np.eye(3)
    H[0,2] = a
    H[1,2] = b
    return H

def print_text(text, position):
    font=pygame.font.SysFont('arial',40,True,False)
    surface=font.render(text,True,(0,0,0))
    screen.blit(surface,position)

def convert_degrees(R,theta):
    y=math.cos(2*math.pi*theta/360)*R
    x=math.sin(2*math.pi*theta/360)*R
    return x+450-15,-(y-450)-15


# 폰트 선택(폰트, 크기, 두껍게, 기울기)
font = pygame.font.SysFont('arial', 20, True, True)

# 게임 반복 구간
while not done:
# 이벤트 반복 구간
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # 윈도우 화면 채우기
    current_time=datetime.now()
    second=current_time.second
    minute=current_time.minute
    hour=current_time.hour

    screen.fill(WHITE)
    pygame.draw.circle(screen,SKYBLUE,(450,450),450)
    pygame.draw.circle(screen,BLACK,(450,450),450,4)

    print_text("20171829Kwon_Clock", (300,200))
    for number in range(1,13):
        print_text(str(number),convert_degrees(350,number*30))

    #분
    R=300
    theta=(minute+second/60)*(360/60)
    pygame.draw.line(screen,BLACK,(450,450),convert_degrees(R,theta),6)
    #초
    R=300
    theta=second*(360/60)
    pygame.draw.line(screen,RED,(450,450),convert_degrees(R,theta),4)
    #시
    R=150
    theta=(hour+minute/60+second/3600)*(360/12)
    pygame.draw.line(screen,BLACK,(450,450),convert_degrees(R,theta),8)
    # 화면 업데이트
    pygame.display.flip()
    clock.tick(60)



# 게임 종료
pygame.quit()
