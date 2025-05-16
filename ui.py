import pygame

def display_score(screen, score, multiplier, consecutive_hits, font_name=None, font_size=36):
    font = pygame.font.SysFont(font_name, font_size)
    # Neon pink RGB: (255, 20, 147)
    combined_text = font.render(f"Score: {score} | Combo: {consecutive_hits} | x{multiplier}", True, (255, 20, 147))
    screen.blit(combined_text, (20, 20))
