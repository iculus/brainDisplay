# Generate a 440 Hz square waveform in Pygame by building an array of samples and play
# it for 5 seconds.  Change the hard-coded 440 to another value to generate a different
# pitch.
#
# Run with the following command:
#   python pygame-play-tone.py

from array import array
from time import sleep, time

import pygame

class Note(pygame.mixer.Sound):

    def __init__(self, frequency, volume=.01):
        self.frequency = frequency
        pygame.mixer.Sound.__init__(self, self.build_samples())
        self.set_volume(volume)

    def build_samples(self):
        period = int(round(pygame.mixer.get_init()[0] / self.frequency))
        samples = array("h", [0] * period)
        amplitude = 2 ** (abs(pygame.mixer.get_init()[1]) - 1) - 1
        for time in xrange(period):
            if time < period / 2:
                samples[time] = amplitude
            else:
                samples[time] = -amplitude
        return samples

if __name__ == "__main__":
    pygame.mixer.pre_init(44100, -16, 1, 1024)
    pygame.init()
    startTime = time()
    currentTime = startTime
    while currentTime - startTime <= 1:
	n1
	currentTime = time()
	print 'a', currentTime
    while currentTime - startTime > 1 and currentTime - startTime <= 2:
        Note(440).play(-1)
	currentTime = time()
	print 'b', currentTime

