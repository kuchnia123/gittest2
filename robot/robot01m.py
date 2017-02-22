#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rg


class Robot:

    def czy_puste(poz):
        if ('normal' in rg.loc_types(poz)) and not ('obstacle' in rg.loc_types(poz)):
            if game.robots.get(poz) == None:
                return True
        return False

    def wrogowie_obok23(self, game):
        lista = []
        for poz, robot in game.robots.iteritems():
            if robot.player_id != self.player_id:
                if rg.dist(poz, self.location) == 2 or rg.dist(poz, self.location) == 3:
                    lista.append(poz)
        return lista

    def czy_wejscie(self, poz):
        if 'spawn' in rg.loc_types(poz):
            return True
        return False


    def czy_wrog(self, poz, game):
        if game.robots.get(poz) != None:
            if game.robots[poz].player_id != self.player_id:
                return True
        return False ['attack', poz]

    def wrogowie(self, game):
        wrogowie_obok = [] #pusta lista
        for poz, robot in game.robots.iteritems():
            for poz in rg.locs_around(self.location):
                if self.czy_wrog(poz, game) and poz not in wrogowie_obok:
                    wrogowie_obok.append(poz)
        return wrogowie_obok;

    def bezpieczne(self):
        lista = []
        for poz in rg.locs_around(self.location):
            if self.czy_puste(game, poz):
                lista.append(poz)
        return lista


    def act(self, game):

        print game.robots

        bezpieczne = self.bezpieczne(game)

        if self.czy_wejscie(self.location):
            if len(bezpieczne):
                return ['move', bezpieczne[0]]

        if self.czy_wejscie(self.location):
             return ['move', rg.toward(self.location, rg.CENTER_POINT)]
        wrogowie=self.wrogowie(game)
        if self.location !=rg.CENTER_POINT:
            if len(wrogowie) < 3 and self.hp>20:
                return ['attack', wrogowie[0]]
            else:
                if len(wrogowie) >= 3 and self.hp<30:
                    return ['suicide']
                else:
                    return ['move', rg.toward(self.location, rg.CENTER_POINT)]

            return ['guard']
        if self.location == rg.CENTER_POINT:
            return ['suicide']


        # idź do środka planszy, ruch domyślny
        return ['move', rg.toward(self.location, rg.CENTER_POINT)]
