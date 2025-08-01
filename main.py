import math
import pygame
import colorsys
import numpy as np

def main():
    WIDTH = 1280
    HEIGHT = 720
    frame = 0

    pygame.init()
    pygame.display.set_caption("Background Visuals")
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        sine_wave(WIDTH, HEIGHT, frame, screen)

        pygame.display.flip()
        frame += 1
        clock.tick(60)

    pygame.quit()

def sine_wave(WIDTH, HEIGHT, frame, screen):
    for y in range(HEIGHT):
        # Frequency of the waves
        frequency = 0.05
        amplitude = 20
        speed = 0.01
        wave = math.sin((y * frequency) + frame * speed)
        x_offset = int(wave * amplitude)

        hue = ((y / HEIGHT) + (frame * 0.9)) % 1.0
        # Using colorsys to convert HSV to RGB
        rgb = colorsys.hsv_to_rgb(hue, 1, 1)

        # Scale RGB values to 0-150 range for visibility
        # Setting to *150 for low lighting
        color = tuple(int(c * 150) for c in rgb)

        # // 2 to get the middle of the screen
        start_x = WIDTH // 2 
        end_x = WIDTH // 2 + 1
        pygame.draw.line(screen, color, (start_x, y), (end_x, y), 2)

if __name__ == "__main__":
    main()