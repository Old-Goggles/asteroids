import pygame

def display_score(screen, score, multiplier, consecutive_hits, font_name=None, font_size=36):
    font = pygame.font.SysFont(font_name, font_size)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    multiplier_text = font.render(f"Multiplier: {multiplier}x", True, (255, 255, 255))
    streak_text = font.render(f"Streak: {consecutive_hits}", True, (255, 255, 255))
    
    screen.blit(score_text, (20, 20))
    screen.blit(multiplier_text, (20, 60))
    screen.blit(streak_text, (20, 100))