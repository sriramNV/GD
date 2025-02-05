import pygame as pg

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sound/'
        self.npc_attack = pg.mixer.Sound(self.path + 'npc_attack.wav')
        self.npc_death = pg.mixer.Sound(self.path + 'npc_death.wav')
        self.npc_pain = pg.mixer.Sound(self.path + 'npc_pain.wav')
        self.player_pain = pg.mixer.Sound(self.path + 'player_pain.wav')
        self.shotgun = pg.mixer.Sound(self.path + 'shotgun.wav')
        self.theme = pg.mixer.Sound(self.path + 'theme.mp3')
        pg.mixer.music.set_volume(0.3)
