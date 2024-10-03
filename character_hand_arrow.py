from pico2d import *
import random

# fill here

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

def handle_events():
    global running
    global x, y

    # fill here

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def random_hand():
    global hx, hy
    if hx == x and hy == y:
        hx, hy = random.randrange(TUK_WIDTH),random.randrange(TUK_HEIGHT)

def follow_arrow(hx, hy):
    global x, y
    if x != hx and y != hy:
        for i in range(0, 100 +1, 1):
            t = i/100
            x = (1-t) * x + t * hx
            y = (1-t) * y + t * hy
            break
        pass

running = True
frame = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
hx, hy = random.randrange(TUK_WIDTH), random.randrange(TUK_HEIGHT)
hide_cursor()


while running:
    clear_canvas()

    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    arrow.draw(hx, hy)
    update_canvas()
    random_hand()
    follow_arrow(hx, hy)
    handle_events()
    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()




