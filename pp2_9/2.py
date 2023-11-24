import pygame
import os

class Music:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.playing = False
        self.tracks = ["/Users/batyr/OneDrive/Desktop/pp2_9/oceandrive.mp3",
                        "/Users/batyr/OneDrive/Desktop/pp2_9/starboy.mp3"]
        self.current_track = 0

    def play_pause(self):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(self.tracks[self.current_track])
            pygame.mixer.music.play()
            self.playing = True
        elif self.playing:
            pygame.mixer.music.pause()
            self.playing = False
        else:
            pygame.mixer.music.unpause()
            self.playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.playing = False

    def next(self):
        self.stop()
        self.current_track = (self.current_track + 1) % len(self.tracks)
        self.play_pause()

    def previous(self):
        self.stop()
        self.current_track = (self.current_track - 1) % len(self.tracks)
        self.play_pause()

    def keyboard(self):
        while True:
            key = input("Press a key (P: play/pause, S: stop, N: next, B: previous, Q: quit): ").upper()
            if key == "P":
                self.play_pause()
            elif key == "S":
                self.stop()
            elif key == "N":
                self.next()
            elif key == "B":
                self.previous()
            elif key == "Q":
                break
            else:
                print("Invalid key. Try again.")

if __name__ == "__main__":
    player = Music()
    player.keyboard()