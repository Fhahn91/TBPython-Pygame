##
#   Program that imports the Pygame module to have an image of a dog and cat
#   bounce around the frame.
#

# Importing Pygame Module
import pygame
import animals

def main():

    # Intilizing Pygame modules
    pygame.init()

    # Defining the colors.
    red = (255, 0, 0)
    black = (0, 0, 0)
    blue = (51, 51, 255)
    keylime = (204, 255, 102)

    # Defining the screen size, setting the display, and naming display.
    output_display = [1000, 600]
    screen = pygame.display.set_mode(output_display)
    pygame.display.set_caption("Cat Chase")

    all_sprites_list = pygame.sprite.Group()

    # Setting variables that will bounce and importing images into them ; Converts image
    # pixels to include alpha channels.
    cat = pygame.image.load(
        'C:\\Users\HP-Laptop\\Documents\\Python\\Bouncing Animals\\Pygame-Bounce-master\\GypGyp.png').convert_alpha()
    dog = pygame.image.load(
        'C:\\Users\\HP-Laptop\\Documents\\Python\\Bouncing Animals\\Pygame-Bounce-master\\PupPup.png').convert_alpha()
    bckgrnd = pygame.image.load(
        'C:\\Users\\HP-Laptop\\Documents\\Python\\Bouncing Animals'
        '\\Pygame-Bounce-master\\dvdsnvle_ste_prk.jpg').convert_alpha()

    # Defining event
    Bounce = False

    # Setting clock variable
    clock = pygame.time.Clock()

    # Defining positions
    red_pos_x = 0
    red_pos_y = 0
    key_pos_x = 90
    key_pos_y = 30
    cat_pos_x = 20
    cat_pos_y = 20
    dog_pos_x = 186
    dog_pos_y = 186

    # Defining speed and direction
    vel_x = 15
    vel_y = 10
    vel1_x = 55
    vel1_y = 10
    vel2_x = 20
    vel2_y = 15
    vel3_x = 23
    vel3_y = 12

    # Grouping all animal sprites into one container using the pygame sprite group class.
    animal_sprites = pygame.sprite.Group()

    # Creating a container for non-player animal character.
    NPC = animals.Kitty(cat)

    # Adding non-player character to animal sprite container.
    animal_sprites.add(NPC)

    # Creating a container for the player character.
    player = animals.Puppy(dog, dog_pos_x, dog_pos_y)
    animal_sprites.add(player)

    # Adding player character to animal sprite container.
    animal_sprites.add(player)

    # Unused group that shows functionality of pygames sprite system.
    sprites_roster = pygame.sprite.Group()
    sprites_roster.add(animal_sprites)

    # Intializing event with while loop.
    while Bounce == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Bounce = True

        # Setting pos to store the X & Y positions of the mouse and setting the cursor visibility to false.
        pos = pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)
        # Creating displaying and setting background to black.
        screen.blit(bckgrnd, [0, 0])

        # Drawing the images on the screen and setting their position.
        NPC.rect.x = cat_pos_x
        NPC.rect.y = cat_pos_y
        player.rect.x = pos[0]
        player.rect.y = pos[1]
        sprites_roster.draw(screen)

        pygame.draw.circle(screen, keylime, (key_pos_x, key_pos_y), 20, 0)
        pygame.draw.circle(screen, red, (red_pos_x, red_pos_y), 20, 0)

        # Using the addition assignment operator to update positions.
        cat_pos_x += vel_x
        cat_pos_y += vel_y
        dog_pos_x += vel1_x
        dog_pos_y += vel1_y
        key_pos_x += vel2_x
        key_pos_y += vel2_y
        red_pos_x += vel3_x
        red_pos_y += vel3_y

        # Using 'if' loop and 'or' operator to invert the speed and
        # direction of the images when they reach the display bounds.

        if cat_pos_y > 500 or cat_pos_y < 0:
            vel_y = vel_y * -1
        if cat_pos_x > 900 or cat_pos_x < 20:
            vel_x = vel_x * -1

        if dog_pos_y > 500 or dog_pos_y < 0:
            vel1_y = vel1_y * -1
        if dog_pos_x > 900 or dog_pos_x < 20:
            vel1_x = vel1_x * -1

        if key_pos_y > 500 or key_pos_y < 0:
            vel2_y = vel2_y * -1
        if key_pos_x > 900 or key_pos_x < 20:
            vel2_x = vel2_x * -1

        if red_pos_y > 500 or red_pos_y < 0:
            vel3_y = vel3_y * -1
        if red_pos_x > 900 or red_pos_x < 20:
            vel3_x = vel3_x * -1
        # Using clock to set frames per second.
        clock.tick(35)

        # Updating the contents of the entire display.
        pygame.display.flip()

    # Unintializing display module.
    pygame.quit()

    return

main()