#
# License: See LICENSE.md file
# GitHub: https://github.com/Baekalfen/PyBoy
#
"""
This class gives access to the raw audio buffer.
"""


class Sound:
    def __init__(self, mb):
        self.mb = mb

    def raw_sound_queue_pop(self):
        if len(self.mb.sound.audioqueue):
            return self.mb.sound.audioqueue.pop()
        return None
