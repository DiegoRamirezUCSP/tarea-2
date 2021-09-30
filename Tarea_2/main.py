
import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, BLACK, WHITE, CLARO, RED ,OSCURO
from checkers.game import Game
from checkers.minmax import minimax,get_all_moves

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    
    inputsito='rojo'
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    game.turn=RED
    #profundidad_arbol=input('¿Profundidad del arbol?')
    profundidad_arbol=2;
    while run:
        clock.tick(FPS)
        
        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), int(profundidad_arbol), WHITE, game)
            game.ai_move(new_board)
            if(len(get_all_moves(game.get_board(),WHITE,game))==0):
                game.get_board().white_left=0

        if game.turn == RED:
            if(len(get_all_moves(game.get_board(),RED,game))==0):
                game.get_board().red_left=0

        if game.winner() != None:
            color=game.winner()
            if color==WHITE:
                print('¡Ganador blanco!')
            else:
                print('¡Ganador rojo!')

            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
        game.update()
    
    pygame.quit()

main()
