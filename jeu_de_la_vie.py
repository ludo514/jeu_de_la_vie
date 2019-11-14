import pygame
import time

class Map(pygame.sprite.Sprite):
    #constructeur
    def __init__(self, hauteur, largeur, screen):
        pygame.sprite.Sprite.__init__(self)
        self.hauteur = hauteur
        self.largeur = largeur
        self.image = pygame.Surface((self.largeur, self.hauteur))
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.screen = screen
        self.map = []
        self.ligne = self.largeur
        self.colonne = self.hauteur
        self.i = 0
        self.j = 0

        for i in range(self.ligne+1):#double boucle pour crée une brique dans la class mur
            self.map.append([])
            for j in range(self.colonne+1):
                self.cellule = [pygame.Rect(self.x, self.y, 15, 15),0]
                self.map[i].append(self.cellule)
                self.x = self.x + 16
            self.y = self.y + 16
            self.x = 0
    
    def update(self):
        self.mettre_cellule()
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_SPACE]:
            self.verif() 

    def draw(self):
        for i in range(self.ligne):
            for j in range(self.colonne):
                if self.map[i][j][1] == 1:
                    pygame.draw.rect(self.screen, NOIR, self.map[i][j][0])
                else:
                    pygame.draw.rect(self.screen, WHITE, self.map[i][j][0])
    
    def mettre_cellule(self):
        for i in range(self.ligne):
            for j in range(self.colonne):
                if pygame.mouse.get_pressed()[0] and self.map[i][j][0].collidepoint(pygame.mouse.get_pos()):
                    self.map[i][j][1] = 1
    
    def count(self,array,i,j):
        compte = 0
        #|
        #| 1
        #|  #
        if array[i+1][j+1][1] == 1:
            compte += 1
        #|#
        #| 1
        #|  
        if array[i-1][j-1][1] == 1:
            compte += 1
        #|
        #| 1
        #|# 
        if array[i+1][j-1][1] == 1:
            compte += 1
        #|  #
        #| 1
        #|  
        if array[i-1][j+1][1] == 1:
            compte += 1
        #|  
        #| 1
        #| # 
        if array[i+1][j][1] == 1:
            compte += 1
        #| # 
        #| 1
        #|  
        if array[i-1][j][1] == 1:
            compte += 1
        #|  
        #| 1#
        #|  
        if array[i][j+1][1] == 1:
            compte += 1
        #|  
        #|#1
        #|  
        if array[i][j-1][1] == 1:
            compte += 1

        return compte

    
    def verif(self):
        for i in range(self.ligne):
            for j in range(self.colonne):
                if self.map[i][j][1] == 0 and self.count(self.map,i,j) == 3 or self.map[i][j][1] == 1 and (self.count(self.map,i,j) == 3 or self.count(self.map,i,j) == 2):
                    self.map[i][j][1] = 1
                if self.map[i][j][1] == 1 and (self.count(self.map,i,j) > 3 or self.count(self.map,i,j) < 2):
                    self.map[i][j][1] = 0

if __name__ == "__main__":

    #constant taille ecran et vitesse de boucle
    LARGEUR = 640
    HAUTEUR = 480
    FPS = 60

    # couleur en rgb
    WHITE = (255, 255, 255)
    NOIR = (0, 0, 0)

    # initialisation de pygame et création de la fenêtre
    pygame.init()
    screen = pygame.display.set_mode((LARGEUR, HAUTEUR))

    pygame.display.set_caption("Game of life")#nom de la fenêtre
    clock = pygame.time.Clock()
    #police = pygame.font.SysFont("comicsansms", 30, 1)

    #création des objets

    map = Map(HAUTEUR, LARGEUR, screen)

    #ajout des sprite à la liste


    # Boucle de jeu
    launched = True

    while launched:

        # vitesse de boucle (FPS)
        clock.tick(FPS)

        # récupération d'un event
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                launched = False

        
        #Update
        map.update()
        #Draw / rendue

        screen.fill(NOIR)
        map.draw()

        # après avoir tout déssiner
        pygame.display.flip()

pygame.quit()