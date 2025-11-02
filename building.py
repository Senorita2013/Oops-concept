#activty 1
import pygame

pygame.init()

screen = pygame.display.set_mode((400,300))
done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.flip()

#activity 2
import pygame

pygame.init()
SCREEN_WIDTH,SCREEN_HEIGHT = 500,500

display_surface = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))
pygame.display.set_caption('Adding image and backround image')

backround_image = pygame.transform.scale(
    pygame.image.load('download-11.jpg').convert(),
    (SCREEN_WIDTH,SCREEN_HEIGHT))

penguin_image = pygame.transform.scale(
    pygame.image.load('cartoony-penguin-studio.jpg').convert_alpha(),(200,300))
penguin_rect = penguin_image.get_rect(center=(SCREEN_WIDTH//2,
                                              SCREEN_HEIGHT//2-30))

text = pygame.font.Font(None,36).render('Hello World',True,
                                        pygame.Color('black'))
text_rect = text. get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2+110))


def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.blit(backround_image,(0,0))
        display_surface.blit(penguin_image,penguin_rect)
        display_surface.blit(text,text_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__== '__main__':
    game_loop()