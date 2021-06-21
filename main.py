import pygame
pygame.font.init()
screen = pygame.display.set_mode((500,600))
x, y, val, dif = 0, 0, 0, 500/9
grid = [[7,8,0,4,0,0,1,2,0], [6, 0,0,0,7,5,0,0,9], [0,0,0,6,0,1,0,7,8], [0,0,7,0,4,0,2,6,0],[0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5], [0,7,0,3,0,0,0,1,2], [1,2,0,0,0,7,4,0,0], [0,4,9,2,0,6,0,0,7]]
def cord(pos):
    global x, y
    x, y = pos[0]//dif, pos[1]//dif
def box():
    for i in range(2):
        pygame.draw.line(screen,(255,0,0),(x*dif-3,(y+i)*dif),(x*dif+dif+3,(y+i)*dif),7)
        pygame.draw.line(screen,(255,0,0),((x+i)*dif,y*dif),((x+i)*dif,y*dif+dif),7)
def draw():
    for i in range (9):
        for j in range(9):
            if grid[i][j]!=0:
                pygame.draw.rect(screen,(140,100,250),(i*dif,j*dif,dif+1,dif+1))
                screen.blit(pygame.font.SysFont("comicsans",40).render(str(grid[i][j]),1,(0,0,0)),(i*dif+15,j*dif+15))
        for i in range(10):
            if i%3 == 0: thick = 7
            else: thick = 1
            pygame.draw.line(screen,(0,0,0),(0,i*dif),(500,i*dif),thick)
            pygame.draw.line(screen,(0,0,0),(i*dif,0),(i*dif,500),thick)
def draw_val(val):
    screen.blit(pygame.font.SysFont("comicsans",40).render(str(val),1,(0,0,0)),(x*dif+15,y*dif+15))
def error1():
    screen.blit(pygame.font.SysFont("comicsans",40).render("you are wrong",1,(0,0,0)),(20,570))
def valid(m,i,j,val):
    for it in range(9):
        if m[i][it] == val:return False
        if m[it][i] == val:return False
    it,jt = i//3, j//3
    for i in range(it*3,it*3+3):
        for j in range(jt*3, jt*3+3):
            if m[i][j] == val:return False
    return True
def solve(grid,i,j):
    while grid[i][j]!=0:
        if i<8: i+=1
        elif i==8 and j<8: i,j=0, j+1
        elif i==8 and j==8:return True
    pygame.event.pump()
    for it in range(1,10):
        if valid(grid,i,j,it)==True:
            grid[i][j] = it
            global x, y
            x, y = i, j
            draw()
            box()
            pygame.display.update()
            pygame.time.delay(20)
            if solve(grid,i,j)==1:return True
            else:grid[i][j] = 0
            draw()
            box()
            pygame.display.update()
            pygame.time.delay(50)
    return False
def setDefault():
    screen.blit(pygame.font.SysFont("comicsans",20).render("press D to reset to default",1,(0,0,0)),(20,520))
def result():
    screen.blit(pygame.font.SysFont("comicsans", 40).render("you won, press d to play again", 1, (0, 0, 0)), (20, 570))
run, flag1, flag2, rs, error = True,0,0,0,0
while run:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:run=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1,pos = 1, pygame.mouse.get_pos()
            cord(pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1: val = 1
            if event.key == pygame.K_2: val = 2
            if event.key == pygame.K_3: val = 3
            if event.key == pygame.K_4: val = 4
            if event.key == pygame.K_5: val = 5
            if event.key == pygame.K_6: val = 6
            if event.key == pygame.K_7: val = 7
            if event.key == pygame.K_8: val = 8
            if event.key == pygame.K_9: val = 9
            if event.key == pygame.K_d: rs, error,flag2,grid = 0,0,0, [[7,8,0,4,0,0,1,2,0],[6,0,0,0,7,5,0,0,9],[0,0,0,6,0,1,0,7,8],
            [0,0,7,0,4,0,2,6,0],[0,0,1,0,5,0,9,3,0],[9,0,4,0,6,0,0,0,5],[0,7,0,3,0,0,0,1,2],[1,2,0,0,0,7,4,0,0],[0,4,9,2,0,6,0,0,7]]
    if flag2 == 1:
        if solve(grid,0,0) == False: error=1
        else: rs, flag2 = 1, 0
    if val!=0:
        draw_val(val)
        if valid(grid,int(x),int(y),val) == True: grid[int(x)][int(y)],flag1=val, 0
        else: grid[int(x)][int(y)]=0
        val=0
    if error == 1:error1()
    if rs == 1: result()
    draw()
    if flag1==1:box()
    setDefault()
    pygame.display.update()
pygame.quit()

