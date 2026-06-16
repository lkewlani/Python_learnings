import pygame
import random
import sys
from words import word_list

# ── initialise ────────────────────────────────────────────────────────────────
pygame.init()

# ── constants ─────────────────────────────────────────────────────────────────
WIDTH, HEIGHT = 900, 600
FPS = 60
MAX_WRONG = 6

# colours
BG_COLOR        = (15,  20,  40)   # dark navy
GALLOWS_COLOR   = (200, 180, 140)  # warm wood
ROPE_COLOR      = (180, 160, 120)
BODY_COLOR      = (230, 100,  80)  # coral red for the man
BODY_OUTLINE    = (255, 140, 110)
LETTER_COLOR    = (255, 255, 255)
CORRECT_COLOR   = (80,  200, 120)  # green
WRONG_COLOR     = (220,  70,  70)  # red
GUESSED_COLOR   = (130, 130, 160)
BUTTON_COLOR    = (40,   50,  80)
BUTTON_HOVER    = (60,   80, 130)
BUTTON_BORDER   = (100, 120, 200)
TITLE_COLOR     = (180, 200, 255)
HINT_COLOR      = (200, 200, 100)
WIN_COLOR       = (80,  220, 120)
LOSE_COLOR      = (220,  70,  70)
SHADOW_COLOR    = (0,    0,   0, 100)

# fonts
FONT_BIG    = pygame.font.SysFont("consolas", 48, bold=True)
FONT_MED    = pygame.font.SysFont("consolas", 32, bold=True)
FONT_SMALL  = pygame.font.SysFont("consolas", 22)
FONT_TINY   = pygame.font.SysFont("consolas", 18)
FONT_TITLE  = pygame.font.SysFont("consolas", 56, bold=True)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman  –  Upgraded Edition")
clock = pygame.time.Clock()


# ── drawing helpers ───────────────────────────────────────────────────────────

def draw_gradient_bg():
    """Dark navy → slightly lighter at the bottom."""
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        r = int(15 + ratio * 10)
        g = int(20 + ratio * 15)
        b = int(40 + ratio * 30)
        pygame.draw.line(screen, (r, g, b), (0, y), (WIDTH, y))


def draw_gallows():
    """Draw the wooden gallows structure."""
    lw = 6   # line width
    # base
    pygame.draw.line(screen, GALLOWS_COLOR, (60, 500), (260, 500), lw)
    # vertical pole
    pygame.draw.line(screen, GALLOWS_COLOR, (120, 500), (120, 100), lw)
    # horizontal beam
    pygame.draw.line(screen, GALLOWS_COLOR, (120, 100), (280, 100), lw)
    # brace
    pygame.draw.line(screen, GALLOWS_COLOR, (120, 150), (170, 100), lw)
    # rope
    pygame.draw.line(screen, ROPE_COLOR, (280, 100), (280, 145), 4)


def draw_hangman(wrong: int):
    """Draw parts of the hangman depending on how many wrong guesses."""
    cx = 280  # center x

    if wrong >= 1:   # head
        pygame.draw.circle(screen, BODY_COLOR,   (cx, 168), 22, 0)
        pygame.draw.circle(screen, BODY_OUTLINE, (cx, 168), 22, 3)
        # eyes
        eye_color = (50, 20, 20) if wrong < MAX_WRONG else (255, 255, 255)
        pygame.draw.circle(screen, eye_color, (cx - 8, 164), 4)
        pygame.draw.circle(screen, eye_color, (cx + 8, 164), 4)
        # mouth – sad when alive, X when dead
        if wrong < MAX_WRONG:
            pygame.draw.arc(screen, (50, 20, 20),
                            pygame.Rect(cx - 10, 170, 20, 12), 3.14, 0, 3)
        else:
            pygame.draw.line(screen, (50, 20, 20), (cx-8, 172), (cx+8, 180), 3)
            pygame.draw.line(screen, (50, 20, 20), (cx+8, 172), (cx-8, 180), 3)

    if wrong >= 2:   # body
        pygame.draw.line(screen, BODY_COLOR, (cx, 190), (cx, 320), 6)

    if wrong >= 3:   # left arm
        pygame.draw.line(screen, BODY_COLOR, (cx, 220), (cx - 50, 270), 5)

    if wrong >= 4:   # right arm
        pygame.draw.line(screen, BODY_COLOR, (cx, 220), (cx + 50, 270), 5)

    if wrong >= 5:   # left leg
        pygame.draw.line(screen, BODY_COLOR, (cx, 320), (cx - 45, 390), 5)

    if wrong >= 6:   # right leg
        pygame.draw.line(screen, BODY_COLOR, (cx, 320), (cx + 45, 390), 5)


def draw_word(word: str, guessed: set):
    """Draw the word with revealed letters and blanks."""
    total_w = len(word) * 48
    start_x = WIDTH // 2 - total_w // 2 + 20
    y = 430

    for i, letter in enumerate(word):
        x = start_x + i * 48
        if letter in guessed:
            surf = FONT_MED.render(letter.upper(), True, CORRECT_COLOR)
            screen.blit(surf, (x - surf.get_width() // 2, y - 26))
        # underline always shown
        line_color = CORRECT_COLOR if letter in guessed else LETTER_COLOR
        pygame.draw.line(screen, line_color, (x - 16, y + 4), (x + 16, y + 4), 3)


def draw_alphabet(guessed: set, word: str):
    """Draw the A–Z keyboard with colour coding."""
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cols, rows = 13, 2
    btn_w, btn_h = 46, 38
    pad = 6
    total_w = cols * (btn_w + pad) - pad
    start_x = WIDTH // 2 - total_w // 2 + 230
    start_y = 490

    for idx, ch in enumerate(letters):
        col = idx % cols
        row = idx // cols
        x = start_x + col * (btn_w + pad)
        y = start_y + row * (btn_h + pad)
        rect = pygame.Rect(x, y, btn_w, btn_h)

        lower = ch.lower()
        if lower in guessed:
            color = CORRECT_COLOR if lower in word else WRONG_COLOR
            border = color
            text_color = (20, 20, 20)
        else:
            color = BUTTON_COLOR
            border = BUTTON_BORDER
            text_color = LETTER_COLOR

        pygame.draw.rect(screen, color, rect, border_radius=6)
        pygame.draw.rect(screen, border, rect, 2, border_radius=6)
        surf = FONT_TINY.render(ch, True, text_color)
        screen.blit(surf, surf.get_rect(center=rect.center))


def draw_lives(wrong: int):
    """Hearts or X's to show remaining lives."""
    max_lives = MAX_WRONG
    remaining = max_lives - wrong
    x_start = 480
    y = 30
    heart = "♥"
    for i in range(max_lives):
        color = (220, 60, 80) if i < remaining else (80, 40, 50)
        surf = FONT_MED.render(heart, True, color)
        screen.blit(surf, (x_start + i * 38, y))


def draw_title():
    surf = FONT_TITLE.render("HANGMAN", True, TITLE_COLOR)
    # subtle shadow
    shadow = FONT_TITLE.render("HANGMAN", True, (0, 0, 0))
    screen.blit(shadow, (WIDTH // 2 - surf.get_width() // 2 + 3, 13))
    screen.blit(surf,   (WIDTH // 2 - surf.get_width() // 2,     10))


def draw_panel_bg(rect: pygame.Rect, alpha=180):
    """Semi-transparent dark panel."""
    surf = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
    surf.fill((20, 25, 50, alpha))
    screen.blit(surf, (rect.x, rect.y))
    pygame.draw.rect(screen, BUTTON_BORDER, rect, 2, border_radius=12)


def draw_wrong_letters(guessed: set, word: str):
    """List letters guessed wrong on the right panel."""
    wrong_letters = [ch.upper() for ch in guessed if ch not in word]
    panel = pygame.Rect(700, 90, 180, 220)
    draw_panel_bg(panel)
    label = FONT_TINY.render("Wrong guesses:", True, WRONG_COLOR)
    screen.blit(label, (panel.x + 10, panel.y + 8))

    per_row = 5
    for i, ch in enumerate(wrong_letters):
        col = i % per_row
        row = i // per_row
        x = panel.x + 14 + col * 32
        y = panel.y + 36 + row * 36
        surf = FONT_SMALL.render(ch, True, WRONG_COLOR)
        screen.blit(surf, (x, y))


def draw_overlay_message(text: str, sub: str, color):
    """Full screen semi-transparent overlay for win / lose."""
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))
    screen.blit(overlay, (0, 0))

    big = FONT_BIG.render(text, True, color)
    screen.blit(big, big.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 60)))

    small = FONT_MED.render(sub, True, LETTER_COLOR)
    screen.blit(small, small.get_rect(center=(WIDTH // 2, HEIGHT // 2)))

    hint = FONT_SMALL.render("Press  R  to play again   |   ESC  to quit", True, HINT_COLOR)
    screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60)))


# ── game state ────────────────────────────────────────────────────────────────

def new_game():
    word = random.choice(word_list)
    return {
        "word":    word,
        "guessed": set(),
        "wrong":   0,
        "state":   "playing",   # "playing" | "won" | "lost"
    }


# ── main loop ─────────────────────────────────────────────────────────────────

def main():
    game = new_game()

    while True:
        clock.tick(FPS)

        # ── events ────────────────────────────────────────────────────────────
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_r:
                    game = new_game()

                if game["state"] == "playing":
                    # accept a-z key presses
                    if pygame.K_a <= event.key <= pygame.K_z:
                        ch = chr(event.key)
                        if ch not in game["guessed"]:
                            game["guessed"].add(ch)
                            if ch not in game["word"]:
                                game["wrong"] += 1

                        # check win / lose
                        if all(c in game["guessed"] for c in game["word"]):
                            game["state"] = "won"
                        elif game["wrong"] >= MAX_WRONG:
                            game["state"] = "lost"

        # ── draw ──────────────────────────────────────────────────────────────
        draw_gradient_bg()
        draw_title()

        draw_gallows()
        draw_hangman(game["wrong"])

        draw_lives(game["wrong"])
        draw_wrong_letters(game["guessed"], game["word"])

        draw_word(game["word"], game["guessed"])
        draw_alphabet(game["guessed"], game["word"])

        # status text
        lives_left = MAX_WRONG - game["wrong"]
        status = FONT_TINY.render(
            f"Lives remaining: {lives_left}   |   Press a letter key to guess   |   R = new game",
            True, HINT_COLOR
        )
        screen.blit(status, status.get_rect(center=(WIDTH // 2, 82)))

        # overlay on win / lose
        if game["state"] == "won":
            draw_overlay_message(
                "🎉  YOU WIN!",
                f'The word was: {game["word"].upper()}',
                WIN_COLOR
            )
        elif game["state"] == "lost":
            draw_overlay_message(
                "💀  GAME OVER",
                f'The word was: {game["word"].upper()}',
                LOSE_COLOR
            )

        pygame.display.flip()


if __name__ == "__main__":
    main()
