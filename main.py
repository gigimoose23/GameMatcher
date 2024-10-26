import pygame,sys
pygame.init()
WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
nameFont = pygame.font.SysFont("Times New Roman", 20)
gameImagesNames = ["candycrush.jpg", "ludo.png", "subwaysurfers.png", "templerun.png"]
gameImages = {}
for imgName in gameImagesNames:
    gameImages[imgName] = pygame.image.load("images/" + imgName)
candyTextRect = pygame.Rect(0, 0, 140, 25)
ludoTextRect = pygame.Rect(0, 100, 140, 25)
subwaySurfersTextRect = pygame.Rect(0, 200, 140, 25)
templeRunTextRect = pygame.Rect(0, 300, 140, 25)

candyRect = pygame.Rect(410, 0, 90, 90)
ludoRect = pygame.Rect(410, 100, 90, 90)
subwaySurfersRect = pygame.Rect(410, 200, 90, 90)
templeRunRect = pygame.Rect(410, 300, 90, 90)

def draw():
    
    screen.blit(gameImages["candycrush.jpg"], (410,0))
    screen.blit(gameImages["ludo.png"], (410,100))
    screen.blit(gameImages["subwaysurfers.png"], (410,200))
    screen.blit(gameImages["templerun.png"], (410,300))
    screen.blit(nameFont.render("Subway Surfers", True, (255,255,255)), (0,0))
    screen.blit(nameFont.render("Temple Run", True, (255,255,255)), (0,100))
    screen.blit(nameFont.render("Ludo", True, (255,255,255)), (0,200))
    screen.blit(nameFont.render("Candy Crush", True, (255,255,255)), (0,300))


firstCirclePos = None
secondCirclePos = None
alreadyClickedPlaces = []
textRecs = [subwaySurfersTextRect, templeRunTextRect, candyTextRect, ludoTextRect]
isFirstButtonINIT = False
while True:

    pygame.display.flip()
    draw()
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            print("got exit request")
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            if subwaySurfersRect.collidepoint(pygame.mouse.get_pos()) or templeRunRect.collidepoint(pygame.mouse.get_pos()) or candyRect.collidepoint(pygame.mouse.get_pos()) or ludoRect.collidepoint(pygame.mouse.get_pos()):
                if isFirstButtonINIT:

                    isFirstButtonINIT = False
                    secondCirclePos = pygame.mouse.get_pos()
                    pygame.draw.circle(screen, (255,255,255), pygame.mouse.get_pos(), 5)
                    pygame.draw.line(screen, (255,255,255), firstCirclePos, secondCirclePos)

        if event.type == pygame.MOUSEBUTTONDOWN:
            for textRec in textRecs:
                if textRec.collidepoint(pygame.mouse.get_pos()):
                    
        
                    if not textRec in alreadyClickedPlaces:
                        alreadyClickedPlaces.append(textRec)
                        firstCirclePos = pygame.mouse.get_pos()
                        isFirstButtonINIT = True

                        pygame.draw.circle(screen, (255,255,255), pygame.mouse.get_pos(), 5)
            
                
                
          

