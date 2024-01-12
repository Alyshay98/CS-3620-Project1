import time
import sys


class ChooseYourAdventure:
    def __init__(self):
        self.player_name = ""
        self.player_health = 100
        self.inventory = []

    def display_intro(self):
        print("Welcome to the Fantasy Adventure Game!")
        print("You find yourself in a mysterious land filled with magic and creatures of unknown existence.")
        print("Your decisions will affect your destiny in ways unimaginable. Let the adventure begin!\n")

    def get_player_name(self):
        self.player_name = input("Enter your character's name: ")
        print(f"Welcome to the land of Faerundale {self.player_name}!\n")

    def make_decision(self, decision_text, option_a, option_b):
        print(decision_text)
        print("A. " + option_a)
        print("B. " + option_b)
        user_choice = input("Your choice (A/B): ").upper()

        if user_choice == "A":
            return True
        elif user_choice == "B":
            return False
        else:
            print("Invalid input. Please choose A or B.")
            return self.make_decision(decision_text, option_a, option_b)

    def run_game(self):
        self.display_intro()
        self.get_player_name()

        if self.make_decision("You stand at a crossroads. Do you go left or right?",
                              "Explore the mysterious forest on the left.",
                              "Head towards the dark mountains on the right."):
            self.narrative_1()
        else:
            self.narrative_2()

    def narrative_1(self):
        print("\nYou enter the mystical forest.")
        time.sleep(1)

        if self.make_decision("As you wander deeper, you encounter a magical creature. Do you approach it?",
                              "Approach the creature cautiously.",
                              "Avoid the creature and continue your journey."):
            print(f"\nThe creature welcomes you, granting you a magical amulet. {self.player_name} feels empowered!")
            self.inventory.append("Magical Amulet")

            time.sleep(1)
            self.narrative_4()
        else:
            print("\nYou cautiously avoid the creature and continue your journey.")

        time.sleep(1)
        self.narrative_4()

    def narrative_2(self):
        print("\nYou climb the dark mountains.")
        time.sleep(1)

        if self.make_decision("At the mountain's peak, you see a dragon. Do you try to befriend it or fight?",
                              "Attempt to befriend the dragon.",
                              "Draw your sword and prepare to battle the dragon."):
            print(f"\nThe dragon recognizes your courage and bows in respect to {self.player_name}. "
                  f"{self.player_name} gains a dragon companion!")
            self.inventory.append("Dragon Companion")

            time.sleep(1)
            self.narrative_3()
        else:
            print("\nYou engage in a fierce battle with the dragon, and you lost some health. "
                  "It was a tough fight, but you slay the dragon, "
                  "emerging victorious!")
            self.player_health = self.player_health - 10

            time.sleep(1)
            self.narrative_3()

    def narrative_3(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision("You find a hidden cave. enter the cave or continue your journey outside?",
                              "Enter the mysterious cave.",
                              "Continue your journey outside."):
            print("\nInside the cave, you discover a treasure chest. Congratulations, "
                  "you've found a valuable artifact!")
            self.inventory.append("Treasure Artifact")

            time.sleep(1)
            self.narrative_11()
        else:
            print("\nYou decide to continue your journey outside the cave.")

            time.sleep(1)
            self.narrative_12()

    def narrative_4(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision("You find a secret glenn while walking through the forest. You see some water, "
                              "do you take a drink or continue on your journey?",
                              "Drink the water from the glenn",
                              "Continue your journey through the forest"):
            print("\nYou drink the water which gives you mysterious powers to see animals in the glenn")
            self.inventory.append("Mysterious Powers")

            time.sleep(1)
            self.narrative_5()
        else:
            print("\nYou decide to continue your journey through the forest.")

            time.sleep(1)
            self.narrative_6()

    def narrative_5(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision("From drinking the water you see a unicorn. Do you run away or become friends with it?",
                              "Become friends with the Unicorn",
                              "Run Away"):
            print("\nYou approach the unicorn, and as a friendly gift, you are given a lock of unicorn hair.")
            self.inventory.append("Unicorn Hair")

            time.sleep(1)
            self.narrative_6()
        else:
            print("\nYou decide to run away from the Glenn and the Unicorn.")

            time.sleep(1)
            self.narrative_6()

    def narrative_6(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision("You continue walking through the forest. You come to a split in the road. "
                              "Do you got Left or Go Right?",
                              "Keep going left into the dark part of the forest",
                              "Head out of the forest by taking the right path"):
            print("\nYou decide to keep on your journey through the dark part of the forest.")

            time.sleep(1)
            self.narrative_7()
        else:
            print("\nYou decide to continue your journey outside the forest")

            time.sleep(1)
            self.narrative_8()

    def narrative_7(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision("As you walk through the dark forest you come across some dwarves. "
                              "They look mighty hostile though, Do you stay and fight or avoid them?",
                              "Stay and fight",
                              "Let's avoid them"):
            print("\nYou fight the dwarves off. Swords clash and you take a bit of damage. "
                  "You emerge victorious with a red ruby!")
            self.inventory.append("Red Ruby")
            self.player_health = self.player_health - 10

            time.sleep(1)
            self.narrative_8()
        else:
            print("\nYou decide to avoid the dwarves.")

            time.sleep(1)
            self.narrative_8()

    def narrative_8(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision("You finally make it out of the forest. "
                              "Do you go the the closest town or take a nap in the sun?",
                              "Go to the closest town",
                              "Take a nap in the sun"):
            print("\nYou decide to go to the closest town")

            time.sleep(1)
            self.narrative_9()
        else:
            print("\nYou decide to refresh some of your health and take a nap in the sun.")

            if self.player_health == 100:
                print("\nYour health is already refreshed")
            else:
                self.player_health = self.player_health + 5

            time.sleep(1)
            self.narrative_9()

    def narrative_9(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision("You make it to closest town. Do you shop around or ask for directions?",
                              "Stay and shop around.",
                              "Ask for some directions."):
            print("\nYou decide to stay and shop around.")

            time.sleep(1)
            self.narrative_10()
        else:
            print("\nYou decide to ask for some directions.")

            time.sleep(1)
            self.narrative_19()

    def narrative_10(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision("After Shopping, you get bored and figure you need to do something else."
                              "Do you leave the town or Go on a Quest?",
                              "Leave the town",
                              "Go on a Quest"):
            print("\nYou decide to leave the town to continue your journey.")

            time.sleep(1)
            self.narrative_20()
        else:
            print("\nYou decide to go on a quest.")

            time.sleep(1)
            self.narrative_20()

    def narrative_11(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision("You continue your journey through the cave. You find the Dwarf King!"
                              "Do you fight him or leave the cave?",
                              "Fight the Dwarf King",
                              "Leave the cave"):
            print("\nYou Decide to fight the Dwarf King! Your sword is thrown from your hand and you are wounded. "
                  "You are cunning and slide around the dwarf king to get his sword and cut him down, "
                  "attaining the dwarf king's crown!")
            self.inventory.append("Dwarf King's Crown")
            self.player_health = self.player_health - 20

            time.sleep(1)
            self.narrative_12()
        else:
            print("\nYou decide to leave the cave and continue your journey.")

            time.sleep(1)
            self.narrative_12()

    def narrative_12(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision("On the outside of the cave, you come to a resting spot. "
                              "Do you stop to rest or continue your journey?",
                              "Stop to rest",
                              "Continue on your journey"):
            print("\nYou decide to stop an rest up on your journey.")
            if self.player_health == 100:
                print("\nYour health is already refreshed")
            else:
                self.player_health = self.player_health + 5

            time.sleep(1)
            self.narrative_13()
        else:
            print("\nYou decide to continue your journey .")

            time.sleep(1)
            self.narrative_13()

    def narrative_13(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision("As your journey continues, you come across a gorge with a swinging rope"
                              " bridge strung across it. Do you cross the rope bridge or find another way down?",
                              "Cross the Rope Bridge",
                              "Find another way down"):
            print("\nYou decide to cross the rickety old bridge. It swings in the wind, "
                  "testing the integrity of the rope that binds it together. "
                  "You make it across just as it snaps and falls apart.")

            time.sleep(1)
            self.narrative_14()
        else:
            print("\nYou decide to try find another way down the gorge")

            time.sleep(1)
            self.narrative_14()

    def narrative_14(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision("After your journey across the gorge, you come down to the river. "
                              "Do you try to find a bridge to cross or swim across it?",
                              "Find a bridge",
                              "Swim Across"):
            print("\nYou decide to be safer than sorry and find a bridge to cross the river")

            time.sleep(1)
            self.narrative_15()
        else:
            print("\nYou decide to swim across. As you swim across, you are attacked by a horde or crocodiles. "
                  "You swim quicker for land to fight and fend off the crocodiles, gaining some teeth in the end.")
            self.inventory.append("Crocodile Teeth")
            self.player_health = self.player_health - 5

            time.sleep(1)
            self.narrative_15()

    def narrative_15(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision("After your journey across the river, you come to a fork in the road. "
                              "Do you head left to Dead Valley or right to the Grasslands?",
                              "Head Right to the grasslands",
                              "Head Left to Dead Valley"):
            print("\nYou head off in the path of the grasslands.")

            time.sleep(1)
            self.narrative_16()
        else:
            print("\nYou take the path off towards Dead Valley.")

            time.sleep(1)
            self.narrative_17()

    def narrative_16(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision("After walking for a good amount of time, you start to feel tired. "
                              "Do you stop to take a rest or continue on?",
                              "Stop to take a rest",
                              "Continue On"):
            print("\nYou decide to take a rest")
            if self.player_health == 100:
                print("\nYour health is already refreshed")
            else:
                self.player_health = self.player_health + 5

            time.sleep(1)
            self.narrative_18()
        else:
            print("\nYou decide to continue your journey.")

            time.sleep(1)
            self.narrative_18()

    def narrative_17(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision("Headed off towards Dead Valley, you feel the crunch of the sands beneath your feet. "
                              "Suddenly you hear something start to rustle. It's a Giant Sand Cicada! "
                              "Do you Fight or will you make a dash for town?",
                              "Fight the Cicada!",
                              "Make a dash for town!"):
            print("\nYou pull your sword out to defend your honor. You slash and hack away at the cicada. "
                  "You are able to pull off the battle and walk away unscathed taking the wings along with you.")
            self.inventory.append("Cicada Wings")

            time.sleep(1)
            self.narrative_18()
        else:
            print("\nYou Make a mad dash for the nearest town.")

            time.sleep(1)
            self.narrative_18()

    def narrative_18(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision("You finally make it to a town where you can enjoy the scenery. "
                              "Do you stop to shop or find a quest to go on?",
                              "Stop to shop around",
                              "Go on a quest"):
            print("\nYou decide to stay and shop around the town for a bit.")

            time.sleep(1)
            self.narrative_19()
        else:
            print("\nYou decide its time to go on another quest!")

            time.sleep(1)
            self.narrative_19()

    def narrative_19(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision("On your way out of town you decide where to go on a quest. "
                              "Do you had for the Water lands or head for another unknown place?",
                              "Head for the water lands",
                              "Head for another unknown place"):
            print("\nYou decide to head to the water lands for another adventure.")

            time.sleep(1)
            self.narrative_20()
        else:
            print("\nYou decide to continue your journey in another unknown place")

            time.sleep(1)
            self.narrative_20()

    def narrative_20(self):
        print("\nYour journey unfolds...")
        time.sleep(1)

        if self.make_decision("A Magical portal appears before you. Enter the portal or stay in the current realm?",
                              "Step into the magical portal.",
                              "Stay in the current realm."):
            print(f"\nYou step into the portal and find yourself in a new realm."
                  f"{self.player_name} continues the adventure")

            print(f"\nCongratulations, {self.player_name}! you've completed the fantasy Adventure.")
            print("Final Status: ")
            print(f"Player Name: {self.player_name}")
            print(f"Player Health: {self.player_health}")
        else:
            print("\nYou decide to stay in the current realm, exploring its wonders further.")

            print(f"\nCongratulations, {self.player_name}! you've completed the fantasy Adventure.")
            print("Final Status: ")
            print(f"Player Name: {self.player_name}")
            print(f"Player Health: {self.player_health}")
            print("Inventory: ", self.inventory)


if __name__ == "__main__":
    game = ChooseYourAdventure()
    game.run_game()


