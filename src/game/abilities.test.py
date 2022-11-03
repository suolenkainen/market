#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/market

import unittest
import abilities


class AbilitiesTests(unittest.TestCase):

    def test_1_awaken(self):
        # Allows one inactive card to activate

        class Card: pass
        
        target_card = Card()
        target_card.id = 1
        target_card.active = False
        target_card.conditions = []

        abilities.awaken(target_card)

        self.assertEqual(target_card.active, True)


    def test_2_awaken_blocked(self):
        # Allows one inactive card to activate

        class Card: pass
        
        target_card = Card()
        target_card.id = 1
        target_card.active = False
        target_card.conditions = ["blocked", "shield"]

        abilities.awaken(target_card)

        self.assertEqual(target_card.active, True)
        self.assertEqual(target_card.conditions, ["shield"])


    def test_blocker(self):
        # Causes the target enemy card to be blocked

        class Card: pass
        
        target_card = Card()
        target_card.id = 1
        target_card.active = True
        target_card.conditions = ["shield"]

        abilities.blocker(target_card)

        self.assertEqual(target_card.conditions, ["shield", "blocked"])
        self.assertEqual(target_card.active, False)


    def test_1_building(self):
        # Cannot attack

        class Card: pass
        
        test_card = Card()
        test_card.id = 1
        test_card.qualities = ["building"]
        test_card.abilities = ["cycle"]
        test_card.attack = 0
        abilities.building(test_card)

        self.assertEqual(test_card.qualities, ["building"])
        self.assertEqual(test_card.abilities, ["cycle"])
        self.assertEqual(test_card.attack, 0)


    def test_2_building_remove_offensive_abilities(self):
        # Cannot attack

        class Card: pass
        
        test_card = Card()
        test_card.id = 1
        test_card.qualities = ["building"]
        test_card.abilities = ["cycle", "strenght"]
        test_card.attack = 2
        abilities.building(test_card)

        self.assertEqual(test_card.qualities, ["building"])
        self.assertEqual(test_card.abilities, ["cycle"])
        self.assertEqual(test_card.attack, 0)


    def test_counter(self):
        # Disables any opponent ability for 1 round

        abilities.counter()

        self.assertEqual(True, True)


    def test_curse(self):
        # Lower target defence

        abilities.curse()

        self.assertEqual(True, True)


    def test_cycle(self):
        # Can be moved from hand to discard and be replaced with a new card

        abilities.cycle()

        self.assertEqual(True, True)


    def test_draw(self):
        # Allows drawing a card

        abilities.draw()

        self.assertEqual(True, True)


    def test_draw2(self):
        # Allows drawing two cards

        abilities.draw2()

        self.assertEqual(True, True)


    def test_draw3(self): 
        # Allows drawing three cards

        abilities.draw3()

        self.assertEqual(True, True)


    def test_equip(self):
        # Can be attached to a creature to grant abilities

        abilities.equip()

        self.assertEqual(True, True)


    def test_goad(self):
        # Can take cause enemy to attack it instead of other creatures

        abilities.goad()

        self.assertEqual(True, True)


    def test_haste(self):
        # Can attack twice in a turn

        abilities.haste()

        self.assertEqual(True, True)


    def test_healing(self):
        # Heals player with one point

        abilities.healing()

        self.assertEqual(True, True)


    def test_healing2(self):
        # Heals player with two points

        abilities.healing2()

        self.assertEqual(True, True)


    def test_healing3(self):
        # Heals player with three points

        abilities.healing3()

        self.assertEqual(True, True)


    def test_healing4(self):
        # Heals player with four points

        abilities.healing4()

        self.assertEqual(True, True)


    def test_instant(self):
        # Can be played on the turn it arrives to table and is discarded

        abilities.instant()

        self.assertEqual(True, True)


    def test_mana(self):
        # Grants mana to mana pool

        abilities.mana()

        self.assertEqual(True, True)


    def test_rage(self):
        # Wounds any creature attacking it

        abilities.rage()

        self.assertEqual(True, True)


    def test_rend(self):
        # If attack is larger than target defence, the excess is damage is dealt to the player

        abilities.rend()

        self.assertEqual(True, True)


    def test_resurrect(self):
        # Returns latest card in discard deck to hand

        abilities.resurrect()

        self.assertEqual(True, True)


    def test_shield(self):
        # Add 1 to target defence

        abilities.shield()

        self.assertEqual(True, True)


    def test_strenght(self):
        # Add 1 to target attack

        abilities.strenght()

        self.assertEqual(True, True)


    def test_wither(self):
        # Lower target attack

        abilities.wither()

        self.assertEqual(True, True)



if __name__ == '__main__':
    unittest.main()