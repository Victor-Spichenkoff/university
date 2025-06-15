import pygame.image

from code.Const import WIN_WIDTH, COLOR_YELLOW, COLOR_ORANGE, MENU_OPTIONS, COLOR_WHITE
from code.helpers import check_events


class Menu:
    def __init__(self, window):
        self.window = window
        self.surface = pygame.image.load("./assets/MenuBg.png").convert_alpha()
        self.rect = self.surface.get_rect(left=0, top=0)  # rect -> retângulo

    def run(self):
        menu_option = 0
        pygame.mixer_music.load("./assets/Menu.mp3")
        # TODO: DESCOMENTAR PARA MÚSICA
        pygame.mixer_music.play(-1)  # toca; -1 -> infinito

        while True:
            # desenhar. (origem, destino)
            self.window.blit(source=self.surface, dest=self.rect)
            # TEXTO:
            self.menu_text(50, "Mountain", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))
            for i in range(len(MENU_OPTIONS)):
                if i == menu_option:
                    self.menu_text(30, MENU_OPTIONS[i], COLOR_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(30, MENU_OPTIONS[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()  # atualiza a tela

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  #FECHO
                    pygame.quit()
                    quit() # acabar com o pygame (init)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # seta para baixo
                        menu_option += 1
                        if menu_option == len(MENU_OPTIONS):
                            menu_option = 0
                    if event.key == pygame.K_UP:  # seta para cima
                        menu_option -= 1
                        if menu_option == -1:
                            menu_option = len(MENU_OPTIONS) - 1

                    if event.key == pygame.K_RETURN: # enter
                        return MENU_OPTIONS[menu_option] # return -> acaba com o menu




    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()  # é imagem
        text_rect = text_surf.get_rect(center=text_center_pos)  # cria retângulo
        self.window.blit(source=text_surf, dest=text_rect)  # renderiza
