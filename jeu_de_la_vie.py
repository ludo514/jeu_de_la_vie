import pygame
import random

WHITE = (255, 255, 255)
NOIR = (0, 0, 0)

class GameOfLife():
    def __init__(self,ligne,colonne,screen):
        self.ligne = ligne
        self.colonne = colonne
        self.screen = screen
        self.x = 0
        self.y = 0
        self.taille = 10
        self.map = self.setup()


    def setup(self):
        map = []
        for i in range(self.ligne+1):#double boucle pour crée une brique dans la class mur
            map.append([])
            for j in range(self.colonne+1):
                cellule = random.randint(0,1)
                map[i].append(cellule)

        return map


    def nouvelle_map(self):
        nouvelle_map = []
        for i in range(self.ligne+1):
            nouvelle_map.append([])
            for j in range(self.colonne+1):
                cellule = 0
                nouvelle_map[i].append(cellule)
        return nouvelle_map

    def get_cellule(self,i,j):
        if self.map[i][j] == 1:
            return 1
        else:
            return 0

    def count(self,i,j):
        compte = 0
        compte += self.get_cellule(i+1,j+1)
        compte += self.get_cellule(i-1,j-1)
        compte += self.get_cellule(i+1,j-1)
        compte += self.get_cellule(i-1,j+1)
        compte += self.get_cellule(i+1,j)
        compte += self.get_cellule(i-1,j)            
        compte += self.get_cellule(i,j+1)
        compte += self.get_cellule(i,j-1)

        if self.map[i][j] == 1:
            if compte < 2 or compte > 3:
                return 0
            if compte == 3 or compte == 2:
                return 1
        elif self.map[i][j] == 0:
            if compte == 3:
                return 1
        return self.map[i][j]


    def mise_a_jour(self):
        nouvelle_map = self.nouvelle_map()
        for i in range(self.ligne):
            for j in range(self.colonne):
                nouvelle_cellule = self.count(i,j)
                nouvelle_map[i][j] = nouvelle_cellule
        self.map = nouvelle_map

    def draw(self):
        self.x = 0
        self.y = 0
        self.taille = 10
        for i in range(self.ligne):
            for j in range(self.colonne):
                if self.map[i][j] == 1:
                    pygame.draw.rect(self.screen, NOIR, (self.x,self.y,self.taille,self.taille))
                    self.x = self.x + 11
                else:
                    pygame.draw.rect(self.screen, WHITE, (self.x,self.y,self.taille,self.taille))
                    self.x = self.x + 11
            self.y = self.y + 11
            self.x = 0


def main():
    if __name__ == "__main__":

        #constant taille ecran et vitesse de boucle
        LARGEUR = 640
        HAUTEUR = 640
        FPS = 10
        ligne = 50
        colonne = 50

        # couleur en rgb


        # initialisation de pygame et création de la fenêtre
        pygame.init()
        screen = pygame.display.set_mode((LARGEUR, HAUTEUR))

        pygame.display.set_caption("Game of life")#nom de la fenêtre
        clock = pygame.time.Clock()
        #police = pygame.font.SysFont("comicsansms", 30, 1)

        #création des objets
        game = GameOfLife(ligne,colonne,screen)
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
            game.mise_a_jour()
            screen.fill(NOIR)
            game.draw()

            # après avoir tout déssiner
            pygame.display.flip()

    pygame.quit()

main()