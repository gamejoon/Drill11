from pico2d import load_image
import game_framework
import random

# width = 183 pixel, height = 167 pixel, 3cm per pixel

PIXEL_PER_MITER = (10.0 / 0.3)
RUN_SPEED_KMPH = 30.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_MITER)

TIME_PER_ACTION = 0.6
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAME_PER_ACTION = 14

class Bird:
    def __init__(self):
        self.x = random.randint(0, 1600)
        self.y = 400
        self.frame = 0
        self.face_dir = 1
        self.width = 183
        self.height = 167
        self.image = load_image("bird_animation.png")
    
    def update(self):
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.face_dir * RUN_SPEED_PPS * game_framework.frame_time
        if (self.face_dir == 1 and self.x + self.width // 2 > 1600) or (self.face_dir == -1 and self.x - self.width // 2 < 0):
            self.face_dir *= -1
    
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw((int(self.frame) % 5) * self.width, (int(self.frame) // 5) * self.height, self.width, self.height, self.x, self.y)
        else:
            self.image.clip_composite_draw((int(self.frame) % 5) * self.width, (int(self.frame) // 5) * self.height, self.width, self.height, 0, 'v', self.x, self.y, self.width, self.hight)