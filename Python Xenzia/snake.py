import pygame, os, sys
import random
from pygame.locals import *

pygame.init()

fpsClock = pygame.time.Clock()

surface = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Python Xenzia')
font = pygame.font.Font(None, 32)


class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class GameData(object):
    def __init__(self):
        self.lives = 3
        self.isDead = False
        self.blocks = []
        self.tick = 250
        self.speed = 250
        self.level = 1
        self.berrycount = 0
        self.segments = 1  # Changes with levels
        self.frame = 0

        bx = random.randint(1, 38)
        by = random.randint(1, 28)

        self.berry = Position(bx, by)
        self.blocks.append(Position(20, 15))
        self.blocks.append(Position(19, 15))
        self.direction = 0  # 0 = right, 1 = left, 2 = up, 3 = down


def lose_life(gamedata):
    gamedata.lives -= 1
    gamedata.direction = 0
    gamedata.blocks[:] = []
    gamedata.blocks.append(Position(20, 15))
    gamedata.blocks.append(Position(19, 15))


def position_berry(gamedata):
    bx = random.randint(1, 38)
    by = random.randint(1, 28)
    found = True

    while found:
        found = False
        for b in gamedata.blocks:
            if b.x == bx and b.y == by:
                found = True
        if found:
            bx = random.randint(1, 38)
            by = random.randint(1, 28)
    gamedata.berry = Position(bx, by)


def load_map_file(fileName):
    f = open(fileName, 'r')
    content = f.readlines()
    f.close()
    return content


def head_hit_body(gamedata):
    head = gamedata.blocks[0]
    for b in gamedata.blocks:
        if b != head:
            if b.x == head.x and b.y == head.y:
                return True
    return False


def head_hit_wall(map, gamedata):
    row = 0

    for line in map:
        col = 0
        for char in line:
            if char == '1':
                if gamedata.blocks[0].x == col and gamedata.blocks[0].y == row:
                    return True

            col += 1

        row += 1
    return False


def draw_data(surface, gamedata):
    text = f"Lives = {gamedata.lives}, Level = {gamedata.level}"
    info = font.render(text, 0, (255, 255, 255))
    textpos = info.get_rect(centerx=surface.get_width() / 2, top=32)
    surface.blit(info, textpos)


def draw_game_over(surface, gamedata):
    text1 = font.render("Game Over", 1, (255, 255, 255))
    text2 = font.render("Press Space to play or close the window.", 0, (255, 255, 255))
    text3 = font.render("Use the arrow keys to navigate.", 0, (255, 255, 255))

    cx = surface.get_width() / 2
    cy = surface.get_height() / 2
    textpos1 = text1.get_rect(centerx=cx - 30, top=cy - 48)
    textpos2 = text1.get_rect(centerx=cx - 170, top=cy-15)
    textpos3 = text1.get_rect(centerx=cx - 120, top=cy+15)
    if gamedata.lives !=3:
        surface.blit(text1, textpos1)
    surface.blit(text2, textpos2)
    surface.blit(text3, textpos3)


def draw_walls(surface, img, map):
    row = 0
    for line in map:
        col = 0
        for char in line:
            if char == '1':
                imgRect = img.get_rect()
                imgRect.left = col * 16
                imgRect.top = row * 16
                surface.blit(img, imgRect)
            col += 1
        row += 1


def draw_snake(surface, img, gamedata):
    first = True
    for b in gamedata.blocks:
        dest = (b.x * 16, b.y * 16, 16, 16)
        if first:
            first = False
            src = (((gamedata.direction * 2) + gamedata.frame) * 16, 0, 16, 16)
        else:
            src = (8 * 16, 0, 16, 16)
        surface.blit(img, dest, src)


def update_game(gamedata, gameTime):
    gamedata.tick -= gameTime
    head = gamedata.blocks[0]

    if gamedata.tick < 0:
        gamedata.tick += gamedata.speed
        gamedata.frame += 1
        gamedata.frame %= 2
        if gamedata.direction == 0:
            move = (1, 0)
        elif gamedata.direction == 1:
            move = (-1, 0)
        elif gamedata.direction == 2:
            move = (0, -1)
        else:
            move = (0, 1)

        newpos = Position(head.x + move[0], head.y + move[1])
        first = True
        for b in gamedata.blocks:
            temp = Position(b.x, b.y)
            b.x = newpos.x
            b.y = newpos.y
            newpos = Position(temp.x, temp.y)

        # Movement
        keys = pygame.key.get_pressed()

        if (keys[K_RIGHT] or keys[K_PAGEDOWN]) and gamedata.direction != 1:
            gamedata.direction = 0
        elif (keys[K_LEFT] or keys[K_DELETE]) and gamedata.direction != 0:
            gamedata.direction = 1
        elif (keys[K_UP] or keys[K_HOME]) and gamedata.direction != 3:
            gamedata.direction = 2
        elif (keys[K_DOWN] or keys[K_END]) and gamedata.direction != 2:
            gamedata.direction = 3

        # berry location

        if head.x == gamedata.berry.x and head.y == gamedata.berry.y:
            lastIdx = len(gamedata.blocks) - 1
            for i in range(gamedata.segments):
                blockX = gamedata.blocks[lastIdx].x
                blockY = gamedata.blocks[lastIdx].y
                gamedata.blocks.append(Position(blockX, blockY))
            bx = random.randint(1, 38)
            by = random.randint(1, 28)
            gamedata.berry = Position(bx, by)
            gamedata.berrycount += 1

            if gamedata.berrycount == 10:
                gamedata.berrycount = 0
                gamedata.speed -= 25
                gamedata.level += 1
                gamedata.segments *= 2
                if gamedata.segments > 64:
                    gamedata.segments = 64
                if gamedata.speed < 100:
                    gamedata.speed = 100


def load_images():
    wall = pygame.image.load('Snake/wall.png')
    raspberry = pygame.image.load('Snake/berry.png')
    snake = pygame.image.load('Snake/snake.png')

    return {'wall': wall, 'berry': raspberry, 'snake': snake}


images = load_images()
images['berry'].set_colorkey((255, 0, 255))

snakemap = load_map_file('Snake/map.txt')
data = GameData()
quitGame = False
isPlaying = False

while not quitGame:

    if isPlaying:
        x = random.randint(1, 38)
        y = random.randint(1, 28)

        rrect = images['berry'].get_rect()
        rrect.left = data.berry.x * 16
        rrect.top = data.berry.y * 16

        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
        # Do update stuff here
        update_game(data, fpsClock.get_time())
        crashed = head_hit_wall(snakemap, data) or head_hit_body(data)
        if crashed:
            lose_life(data)
            position_berry(data)
        isPlaying = data.lives > 0
        if isPlaying:
            surface.fill((0, 0, 0))
            # Do drawing stuff here
            draw_walls(surface, images['wall'], snakemap)
            surface.blit(images['berry'], rrect)
            draw_snake(surface, images['snake'], data)
            draw_data(surface, data)
    else:
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type is QUIT:
                pygame.quit()
                sys.exit()

        if keys[K_SPACE]:
            isPlaying = True
            data = None
            data = GameData()
        draw_game_over(surface,data)

    pygame.display.update()
    fpsClock.tick(30)