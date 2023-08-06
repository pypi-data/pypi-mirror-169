import pygame

pygame.init()

class Text:
    def __init__(self, surface, **args):
        
        Texts.append(self)
        
        self.x, self.y = 0, 0
        self.width, self.height = 100, 100

        self.surface = surface
        self.renderSurface = pygame.Surface((self.width, self.height))
        
        self.color = (150, 150, 150)   # цвет фона
        self.pressedColor = (80, 80, 80)   # цвет кнопки когда она нажата
        self.textColor = (255, 255, 255)   # цвет текста

        self.oldMousePos = (0, 0)
        self.lastY = 0

        self.text = ''
        self.textPos = 0

        self.StartTime = 30
        self.time = 30
        self.direct = -1

        self.eding = True

        self.fontSize = 70   # размер шрифта
        self.fontPath = None
        self.font = pygame.font.Font(self.fontPath, self.fontSize)

        self.mode = 0

        self.render = True

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        for arg in args:
            get = str(arg)

            if get == 'x':
                self.x = args[get]
            if get == 'y':
                self.y = args[get]
                
            if get == 'width':
                self.width = args[get]
            if get == 'height':
                self.height = args[get]

            if get == 'color':
                self.color = args[get]

            if get == 'fontSize':
                self.fontSize = args[get]
            if get == 'textColor':
                self.textColor = args[get]
            
            if get == 'font':
                self.fontPath = args[arg]

        self.font = pygame.font.Font(self.fontPath, self.fontSize)
        self.renderSurface = pygame.Surface((self.width, self.height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def Press(self, key):
        if self.render and self.mode == 1 and self.eding:
            keys = pygame.key.get_pressed()

            if not keys[pygame.K_BACKSPACE] and not keys[pygame.K_KP_ENTER] and key != '\r' and self.mode == 1:
                self.text += key

            elif not keys[pygame.K_BACKSPACE] and keys[pygame.K_KP_ENTER] or key == '\r' and self.mode == 1:
                self.text += '\n'

                if self.lastY + self.textPos + self.fontSize // 1.5 > self.rect.height:
                    self.textPos -= self.fontSize // 1.5
            
            elif keys[pygame.K_BACKSPACE] and self.mode == 1 and self.text != '':
                self.text = self.text[:-1]
                if self.text != '' and self.text[-1] == '\n': self.text = self.text[:-1]
    
    def Scroll(self):
        self.oldMousePos = pygame.mouse.get_pos()
    
    def update(self):

        if self.render:

            if self.mode == 1:
                if self.direct == -1:
                    self.time -= 1
                    if self.time <= 0: self.direct = 1
                else:
                    self.time += 1
                    if self.time >= self.StartTime: self.direct = -1

            b1, b2, b3 = pygame.mouse.get_pressed()
            mx, my = pygame.mouse.get_pos()

            if b1 and self.rect.collidepoint(mx, my):
                newMousePos = pygame.mouse.get_pos()    

                if self.textPos + (newMousePos[1] - self.oldMousePos[1]) < 0:
                    self.textPos += (newMousePos[1] - self.oldMousePos[1])

            if b1 and self.rect.collidepoint(mx, my):
                self.mode = 1
            elif b1 and not self.rect.collidepoint(mx, my):
                self.mode = 0

            self.draw()
    
    def draw(self):
        if self.mode == 1 and self.renderSurface.get_width() != self.rect.width or self.renderSurface.get_height() != self.rect.height:
            self.renderSurface = pygame.Surface((self.rect.width, self.rect.height))
            self.text = self.text.replace('\n', '')

        self.renderSurface.fill(self.color)

        if self.mode == 1:
            while 1:
                get = self.text.split('\n')
                last = self.font.render(get[-1], 1, self.textColor)

                rect = pygame.Rect(10 + last.get_width(), 0, last.get_width(), last.get_height())
                if rect.x > self.rect.width:
                    self.text = self.text[0:-1] + '\n' + self.text[-1]

                    if self.lastY + self.textPos > self.rect.height:
                        self.textPos -= self.fontSize // 1.5

                    break
                break

        get = self.text.split('\n')

        y = 10

        for obj in get:

            tx = self.font.render(obj, 1, self.textColor)
            self.renderSurface.blit(tx, (10, y + self.textPos))

            y += self.fontSize // 1.5
        
        self.lastY = y
        
        if self.mode == 1 and self.direct == -1:
            pygame.draw.rect(self.renderSurface, (0, 150, 255), (10 + tx.get_width() + 5, (y - self.fontSize // 1.5) + self.textPos, self.fontSize // 8, self.fontSize // 1.5))

        self.surface.blit(self.renderSurface, (self.rect.x, self.rect.y))

Texts = []