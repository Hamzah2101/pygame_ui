import pygame
import main_menu
import time
import constants
pygame.init()

print("BGM: 'Blue Space v0_95.mp3' by FoxSynergy on opengameart.org ")
print("Background: 'City Background Repetitive 3' by Alucard on opengameart.org ")
print("Button sfx: 'vgmenuselect' by Fupi on opengameart.org ")

#pygame.mixer.music.load('Blue Space v0_95.mp3')
#pygame.mixer.music.load('Blue Space v0_96.wav')
pygame.mixer.music.load('Blue Space v0_8 (32 kbps).mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

main_menu.main(0)

##### quit #####
pygame.mixer.Channel(1).play(constants.button_sfx)
time.sleep(0.25)
print("The program has been terminated.")
pygame.quit()
quit()
