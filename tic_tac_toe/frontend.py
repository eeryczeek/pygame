from backend import TicTacToe
import pygame
import sys

pygame.init()

width, height = 300, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")

BLACK = (0, 0, 0)
PINK = (255, 128, 255)
PURPLE = (255, 64, 255)

font = pygame.font.Font(None, 100)
game_over_font = pygame.font.Font(None, 70)
small_font = pygame.font.Font(None, 50)

game = TicTacToe()

button_width, button_height = 220, 50
button_x = width // 2 - button_width // 2
button_y = height - 100

game_over = False


def reset_game():
    global game, game_over
    game = TicTacToe()
    game_over = False


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = pygame.mouse.get_pos()
            row = y // 100
            col = x // 100
            if game.board[row][col] == ' ':
                game.action((row, col))
                if game.check_win() or game.check_draw():
                    game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN and game_over:
            if button_x < event.pos[0] < button_x + button_width and button_y < event.pos[1] < button_y + button_height:
                reset_game()

    screen.fill(BLACK)

    for i in range(1, 3):
        pygame.draw.line(screen, PINK, (0, i * 100), (width, i * 100), 2)
        pygame.draw.line(screen, PINK, (i * 100, 0), (i * 100, height), 2)

    for i in range(3):
        for j in range(3):
            if game.board[i][j] == 'x':
                text = font.render('X', True, PURPLE)
                screen.blit(text, (j * 100 + 25, i * 100 + 20))
            elif game.board[i][j] == 'o':
                text = font.render('O', True, PURPLE)
                screen.blit(text, (j * 100 + 25, i * 100 + 20))

    if game_over:
        screen.fill(BLACK)

        game_over_text = game_over_font.render("Game Over", True, PINK)
        screen.blit(game_over_text, (width // 2 - 130, height - 260))

        if game.check_win():
            winner_info = game_over_font.render(
                f"{game.player.upper()} won!", True, PINK)
            screen.blit(winner_info, (width // 2 - 75, height - 180))

        if game.check_draw():
            draw_info = game_over_font.render(f"Draw!!", True, PINK)
            screen.blit(draw_info, (width // 2 - 60, height - 200))

        play_again_text = small_font.render("Play Again", True, BLACK)
        pygame.draw.rect(screen, PINK, (button_x, button_y,
                         button_width, button_height))
        screen.blit(play_again_text, (width // 2 - 90, button_y + 10))

    pygame.display.flip()

pygame.quit()
sys.exit()
