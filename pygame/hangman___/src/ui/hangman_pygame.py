import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import random
import pygame
import sys

from hangman import Hangman, words_list

SHORT_SUCCESS_SOUND = "src/assets/short-success.mp3"
SUCCESS_SOUND = "src/assets/success.mp3"
FAILURE_SOUND = "src/assets/failure.mp3"
HANGMAN_IMAGE = "src/assets/hangman.jpg"
PAPER_IMAGE = "src/assets/paper.jpg"
FONT_PATH = "src/assets/QETonyFlores.ttf"
TEXT_COLOR = (0, 0, 0)
BG_COLOR = (255, 255, 255)
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 300

difficulty = "easy"  # easy, medium, hard


class ShakingSprite(pygame.sprite.Sprite):
    sprite_state_coordinates = {
        "0": {"sprite_column": 2, "sprite_row": 1},
        "1": {"sprite_column": 0, "sprite_row": 2},
        "2": {"sprite_column": 1, "sprite_row": 2},
        "3": {"sprite_column": 2, "sprite_row": 2},
        "4": {"sprite_column": 0, "sprite_row": 3},
        "5": {"sprite_column": 1, "sprite_row": 3},
        "6": {"sprite_column": 2, "sprite_row": 3},
    }
    sprite_width = 78
    sprite_height = 88

    def __init__(self, image, x, y, shake_amplitude=5, shake_duration=500):
        super().__init__()
        self.wrong_answers = 0
        self.original_image = image
        self.compute_image_rect()
        self.rect = self.image.get_rect(center=(x, y))
        self.shake_amplitude = shake_amplitude
        self.shake_duration = shake_duration
        self.shake_start_time = None
        self.original_center = self.rect.center

    @property
    def sprite_column(self):
        return self.sprite_state_coordinates[str(self.wrong_answers)]["sprite_column"]

    @property
    def sprite_row(self):
        return self.sprite_state_coordinates[str(self.wrong_answers)]["sprite_row"]

    def compute_image_rect(self):
        try:
            self.sprite_rect = (
                self.sprite_column * self.sprite_width,
                self.sprite_row * self.sprite_height,
                self.sprite_width,
                self.sprite_height,
            )
            self.image = self.original_image.subsurface(self.sprite_rect).copy()
            self.image = self.image.convert_alpha()

            # Set white pixels as transparent
            self.image.set_colorkey((255, 255, 255))
        except Exception:
            pass

    def update_sprite_rect(self, new_rect):
        self.sprite_rect = new_rect
        self.image = self.original_image.subsurface(self.sprite_rect).copy()

    def update(self):
        if self.shake_start_time is not None:
            elapsed_time = pygame.time.get_ticks() - self.shake_start_time
            if elapsed_time < self.shake_duration:
                # damping_factor is calculated as 1 - (elapsed_time / shake_duration),
                # which decreases from 1 to 0 over the duration of the shake.
                # The shake offsets are multiplied by the damping factor to reduce their amplitude over time.
                # The object's position is updated relative to its original center, ensuring it returns to the origin gradually.
                damping_factor = 1 - (elapsed_time / self.shake_duration)
                shake_offset_x = (
                    random.randint(-self.shake_amplitude, self.shake_amplitude)
                    * damping_factor
                )
                shake_offset_y = (
                    random.randint(-self.shake_amplitude, self.shake_amplitude)
                    * damping_factor
                )
                self.rect.centerx = self.original_center[0] + shake_offset_x
                self.rect.centery = self.original_center[1] + shake_offset_y
            else:
                self.shake_start_time = None
                self.rect.center = self.original_center
                self.compute_image_rect()

    def start_shake(self):
        self.compute_image_rect()
        self.shake_start_time = pygame.time.get_ticks()


class HangmanPygame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Hangman")
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

        self.FONT = pygame.font.Font(FONT_PATH, 24)
        self.base_font = pygame.font.Font(None, 32)

        self.input_rect = pygame.Rect(200, 200, 140, 32)

        self.color_base = pygame.Color("light blue")
        self.color_failure = pygame.Color("light coral")
        self.color = self.color_base

        image = pygame.image.load(HANGMAN_IMAGE)
        self.shaking_sprite = ShakingSprite(image, 230, 130, 2)
        self.all_sprites = pygame.sprite.Group(self.shaking_sprite)

        self.hangman = Hangman(words_list, difficulty)
        self.hangman.setup()
        print(
            "Difficulty:",
            self.hangman.difficulty,
            "Word length:",
            len(self.hangman.word),
            "Max tries:",
            self.hangman.max_tries,
            "Word:",
            self.hangman.word,
        )

    def play_sound(self, sound_path: str):
        # play sound
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play(0)

    def show_message(self, message):
        # show a message on the screen
        self.screen.blit(self.FONT.render(message, True, TEXT_COLOR), (20, 20))

    def print_letters(self):
        # show all alphabet letters (a to z) on the screen in 2 rows
        for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            x = self.screen.get_width() // 2 - 130 + (i % 13) * 20
            y = 240 + (i // 13) * 30
            # pygame.draw.rect(screen, (255, 255, 255), (x, y, 20, 20))
            self.screen.blit(self.FONT.render(letter, True, TEXT_COLOR), (x + 5, y - 5))
            # strike through the letter if it was already played
            if letter in self.hangman.letters:
                line_width = 4
                pygame.draw.line(
                    self.screen, (255, 0, 0), (x + 5, y), (x + 15, y + 15), line_width
                )
                pygame.draw.line(
                    self.screen, (255, 0, 0), (x + 5, y + 15), (x + 15, y), line_width
                )

    def reset(self):
        # reset the game
        self.color = self.color_base
        self.hangman.setup()
        self.start_time = pygame.time.get_ticks()
        print(
            "Difficulty:",
            self.hangman.difficulty,
            "Word length:",
            len(self.hangman.word),
            "Max tries:",
            self.hangman.max_tries,
            "Word:",
            self.hangman.word,
        )

    def run(self):
        self.start_time = pygame.time.get_ticks()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_rect.collidepoint(event.pos):
                        self.reset()

                if event.type == pygame.KEYDOWN:
                    # only allow letters
                    if not event.unicode.isalpha():
                        continue

                    char = str(event.unicode).upper()
                    message = self.hangman.play_letter(char)
                    if message:
                        print(message)
                        self.play_sound(FAILURE_SOUND)
                        self.color = self.color_failure
                        self.shaking_sprite.wrong_answers = self.hangman.wrong_answers
                        self.shaking_sprite.start_shake()
                    else:
                        self.play_sound(SHORT_SUCCESS_SOUND)
                        self.color = self.color_base

            self.screen.fill(BG_COLOR)
            # print image as background
            self.screen.blit(pygame.image.load(PAPER_IMAGE), (0, 0))

            text_surface = self.base_font.render(
                self.hangman.underlines, True, TEXT_COLOR
            )
            self.input_rect.w = text_surface.get_width() + 10
            # center the text horizontally on the screen
            self.input_rect.x = self.screen.get_width() // 2 - self.input_rect.w // 2

            self.screen.blit(
                text_surface, (self.input_rect.x + 5, self.input_rect.y + 5)
            )

            self.all_sprites.update()
            self.all_sprites.draw(self.screen)

            self.print_letters()

            if self.hangman.has_won():
                self.play_sound(SUCCESS_SOUND)
                self.show_message("Congratulations! You found the word.")
            elif self.hangman.has_attempts_left():
                time_since_enter = pygame.time.get_ticks() - self.start_time
                seconds_since_enter = time_since_enter // 1000
                message = f"Tries left: {self.hangman.tries_left}"
                self.show_message(message)
                message = "Seconds since enter: " + str(seconds_since_enter)
                seconds_since_enter != 0 and self.screen.blit(
                    self.FONT.render(message, True, TEXT_COLOR), (20, 40)
                )
            else:
                self.show_message(f"Game over! The word was: {self.hangman.word}")

            pygame.display.flip()

            self.clock.tick(60)
