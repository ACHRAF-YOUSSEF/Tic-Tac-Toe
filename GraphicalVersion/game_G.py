import pygame

pygame.init()
screen = pygame.display.set_mode((700, 700))
SQ = 700//3

board = [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
]

def draw_text(screen, txt, x, y, police, color):
    txt_font = pygame.font.Font(None, police)
    txt = txt_font.render(txt, True, color)
    txt_rect = txt.get_rect()
    txt_rect.center =  (x, y)
    screen.blit(txt, txt_rect)

def iswin(user, board):
    if check_row(user, board): 
        return True
    
    if check_col(user, board): 
        return True
    
    if check_diag(user, board): 
        return True
    
    return False

def check_row(user, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row = False
                break
        
        if complete_row: return True
    
    return False 

def check_col(user, board):
    for col in range(3):
        complete_col = True
        for row in range(3):
            if board[row][col] != user:
                complete_col = False
                break
        
        if complete_col: return True
    
    return False

def check_diag(user, board):
    if board[0][0] == user and board[1][1] == user and board[2][2] == user: 
        return True
    
    elif board[0][2] == user and board[1][1] == user and board[2][0] == user: 
        return True
    else: 
        return False

def redrawScreen(screen):
    global board
    
    for row in range(len(board)):
        for col in range(len(board)):
            pygame.draw.rect(screen, (255, 255, 255), (row * SQ, col * SQ, SQ, SQ), 1)
            txt = "X" if board[row][col] == 1 else "O" if board[row][col] == 2 else "-"
            if txt != "-":
                if txt == "X":
                    draw_text(screen, txt, row * SQ + 120, col * SQ + 130, 400, (255, 0, 0))
                    
                else:
                    draw_text(screen, txt, row * SQ + 120, col * SQ + 130, 400, (0, 255, 0))

def current_user(user):
    if user: 
        return 1
    
    else: 
        return 2

def istaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != 0:
        print("This position is already taken.")
        return True
    
    else: 
        return False

def addToBoard(coords, board, active_user):
    row = coords[0]
    col = coords[1]
    board[row][col] = active_user

turns = 0
user = True
while True:
    screen.fill((0, 0, 0))
    redrawScreen(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        
        pos = pygame.mouse.get_pos()
        row , col = pos[0]//SQ, pos[1]//SQ
        coords = (row, col)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not istaken(coords, board):
                addToBoard(coords, board, current_user(user))
                turns += 1
                user = not user
    
    active_user = current_user(not user)
    txt = "X" if active_user == 1 else "O" if active_user == 2 else "-"
    if iswin(active_user, board):
        draw_text(screen, f"{txt} wins!", 700//2, 700//2, 280, (255, 255, 0))
        
    elif turns >= 9:
        draw_text(screen, "tie", 700//2, 700//2, 250, (255, 255, 0))  
    
    pygame.display.update()
