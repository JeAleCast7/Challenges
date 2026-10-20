import pygame
pygame.init()

# SETTINGS
SIZE = 600
CELL = SIZE // 3
screen = pygame.display.set_mode((SIZE, SIZE + 60))
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

RED, BLUE, GREEN = (220, 60, 60), (70, 130, 230), (80, 200, 120)

WINS = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def center(i):
    """Pixel position of the center of cell i."""
    return i % 3 * CELL + CELL // 2, i // 3 * CELL + CELL // 2


def new_game():
    """Returns a fresh state: board, current player, winning line, game over."""
    return [""] * 9, "X", None, False


board, player, line, over = new_game()

# MAIN LOOP
running = True
while running:

    # 1) EVENTS
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

        elif e.type == pygame.KEYDOWN and e.key == pygame.K_r:
            board, player, line, over = new_game()

        elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            if over:
                board, player, line, over = new_game()
            elif e.pos[1] < SIZE:
                i = e.pos[1] // CELL * 3 + e.pos[0] // CELL
                if board[i] == "":
                    board[i] = player
                    
                    line = next((c for c in WINS if board[c[0]] and board[c[0]] == board[c[1]] == board[c[2]]), None)
                    over = bool(line) or "" not in board
                    if not over:
                        player = "O" if player == "X" else "X"

    # 2) DRAWING
    screen.fill("black")

    for i in (1, 2):                                        
        pygame.draw.line(screen, "white", (i * CELL, 0), (i * CELL, SIZE), 4)
        pygame.draw.line(screen, "white", (0, i * CELL), (SIZE, i * CELL), 4)

    for i, mark in enumerate(board):
        x, y = center(i)
        if mark == "X":
            pygame.draw.line(screen, RED, (x - 60, y - 60), (x + 60, y + 60), 12)
            pygame.draw.line(screen, RED, (x - 60, y + 60), (x + 60, y - 60), 12)
        elif mark == "O":
            pygame.draw.circle(screen, BLUE, (x, y), 60, 12)

    if line:
        pygame.draw.line(screen, GREEN, center(line[0]), center(line[2]), 10)

# Status bar
    if line:
        msg = f"{board[line[0]]} wins! Click or press R to restart"
    elif over:
        msg = "Draw! Click or press R to restart"
    else:
        msg = f"Turn: {player}"
    pygame.draw.rect(screen, (60, 60, 60), (0, SIZE, SIZE, 60))
    text = font.render(msg, True, "white")
    screen.blit(text, text.get_rect(center=(SIZE // 2, SIZE + 30)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()