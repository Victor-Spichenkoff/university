import pygame.image

from code.Cont import WIN_WIDTH, WIN_HEIGHT, COLOR_ORANGE, MENU_OPTIONS, COLOR_WHITE
from code.helpers import check_events


class Menu:
    def __init__(self, window):
        self.window = window
        self.surface = pygame.image.load("./assets/MenuBg.png")
        self.rect = self.surface.get_rect(left=0, top=0)  # rect -> retângulo

    def run(self):
        pygame.mixer_music.load("./assets/Menu.mp3")
        # TODO: DESCOMENTAR PARA MÚSICA
        # pygame.mixer_music.play(-1)  # toca; -1 -> infinito

        while True:
            # desenhar. (origem, destino)
            self.window.blit(source=self.surface, dest=self.rect)
            # TEXTO:
            self.menu_text(50, "Mountain", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))
            for i in range(len(MENU_OPTIONS)):
                self.menu_text(30, MENU_OPTIONS[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))


            pygame.display.flip()  # atualiza a tela
            check_events()  # inclui

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()  # é imagem
        text_rect = text_surf.get_rect(center=text_center_pos)  # cria retângulo
        self.window.blit(source=text_surf, dest=text_rect)  # renderiza
