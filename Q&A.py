import pygame 

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

''' game loop'''
while True:
    question_card.draw(10,10)
    answer_card.draw(10,10)

    timer.tick(40) 

    pygame.display.update()
