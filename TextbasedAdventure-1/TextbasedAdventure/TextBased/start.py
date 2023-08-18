
import pygame
from pygame.locals import *
import sys
import pygame_gui


def show_text(text_to_show):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                Screen.fill("BLACK")
                new_text = pygame.font.SysFont("Bhanscrift", 100).render(
                    f"Hello, {text,to_show}", True, "black")
                new_text_rect = new_text.get_rect(center=(width/2, height/2))
            screen.blit(new_text, new_text_rect)

            clock.tick(60)
            pygame.display.update()


size = width, height = (800, 600)
clock = pygame.time.Clock()
MANAGER = pygame_gui.UIManager((width, height))

textBox = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.rect(
    (350, 550), (750, 50)), manager=MANAGER, object_id="#main_text_entry")

pygame.init()
running = True
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Dungeons")
screen.fill((0, 0, 0))
pygame.display.update()


def get_user_name():
    while running:
        UI_REFRESH_RATE = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame_gui.UI_TEXT_EFFECT_FINISHED and event.ui_object_id == "#main_text_Entry":
                show_text(event.text)
            running = False
            MANAGER.process_events(event)
            MANAGER.update(UI_REFRESH_RATE)
            MANAGER.draw_ui(screen)
            screen.fill((0, 0, 0))


pygame.display.update()

pygame.quit()
