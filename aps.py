#!/usr/bin/env python3

class PlayerError(BaseException): pass


class Player(object):

    openSlots   = [True,] * 32
    teamBySlots = [4] * 32
    teamNames   = ("Red", "Blue", "Green", "Gold", "None")
    teamCount   = len(teamNames)

    def __init__(self, name, *, team=4, startHealth=100):

        try:
            self.pln = Player.openSlots.index(True)

        except ValueError:
            raise PlayerError("no open player slots, aborting")
            self.pln = -1
            del self   # no point in existing

        else:
            Player.openSlots[self.pln] = False



        if team < 0 or team >= Player.teamCount:
            raise PlayerError("team {} out of range [0, {}], aborting".format(
                                            team, Player.teamCount - 1))
            del self

        self.team = team
        Player.teamBySlots[self.pln] = team


        self.name = name




    def __del__(self):
        if self.pln <= 0:
            Player.openSlots[self.pln]   = True
            Player.teamBySlots[self.pln] = 4

    def __repr__(self):
        return "{}(pln={}, name={}, team={})".format(self.__class__.__name__,
                                                     self.pln, repr(self.name),
                                                     self.team)

    def __str__(self):
        return "{} (pln: {}, team: {})".format(self.name, self.pln,
                                        Player.teamNames[self.team])
