import pygame 
from random import randint

pygame.init()

''' game window '''
size = (500, 500)
window = pygame.display.set_mode(size) 
back_color = (200, 200, 200)
window.fill(back_color)

timer = pygame.time.Clock()

''' variables '''
BLACK = (0,0,0)
LIGHT_BLUE = (200,200,255)

''' class '''
class TextArea():
    def __init__(self, x=0, y=0, width=10, height=10, color=None): 
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def set_text(self, text, fsize=12, text_color=BLACK):
        self.text = text
        self.image = pygame.font.Font(None, fsize)
        self.complete_text = self.image.render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        pygame.draw.rect(window, self.fill_color, self.rect)
        window.blit( self.complete_text, ( self.rect.x + shift_x, self.rect.y + shift_y) )

''' creating objects '''
question_card = TextArea(x=120, y=100, width=290, height=70, color=LIGHT_BLUE)
question_card.set_text(text='What is your course?', fsize=30)

answer_card = TextArea(x=120, y=240, width=290, height=70, color=LIGHT_BLUE)
answer_card.set_text(text='Python Course', fsize=30)

question_card.draw(10,10)
answer_card.draw(10,10)

''' game loop'''
while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_q:

                num = randint(1,3)
                if num == 1:
                     question_card.set_text('What do you study at Algorithmics?', 25)
                if num == 2:
                    question_card.set_text('What language is spoken in France?', 25)
                if num == 3:
                    question_card.set_text('What grows on an apple tree?', 35)   

                question_card.draw(10, 10)

            if event.key == pygame.K_a:
                num = randint(1,3)
                if num == 1:
                    answer_card.set_text('Python', 35)
                if num == 2:
                    answer_card.set_text('French', 35)
                if num == 3:
                    answer_card.set_text('Apples', 35)

                answer_card.draw(10, 10)

    pygame.display.update()
    timer.tick(40) 
