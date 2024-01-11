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
            self.narrative_3()
        else:
            print("\nYou cautiously avoid the creature and continue your journey.")

        time.sleep(1)
        self.narrative_3()

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
            self.narrative_4()

    def narrative_3(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision("You find a hidden cave. enter the cave or continue your journey outside?",
                              "Enter the mysterious cave.",
                              "Continue your journey outside."):
            print("\nInside the cave, you discover a treasure chest. Congratulations, you've found a valuable artifact!")
            self.inventory.append("Treasure Artifact")

            time.sleep(1)
            self.narrative_5()
        else:
            print("\nYou decide to continue your journey outside the cave.")

            time.sleep(1)
            self.narrative_6()

    def narrative_4(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision(""):
            print("\nYou")
            self.inventory.append("")

            time.sleep(1)
            self.narrative_7()
        else:
            print("\nYou decide to continue your journey outside the cave.")

            time.sleep(1)
            self.narrative_8()

    def narrative_5(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision(""):
            print("\nYou")
            self.inventory.append("")

            time.sleep(1)
            self.narrative_9()
        else:
            print("\nYou decide to continue your journey outside the cave.")

            time.sleep(1)
            self.narrative_10()

    def narrative_6(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision(""):
            print("\nYou")
            self.inventory.append("")

            time.sleep(1)
            self.narrative_11()
        else:
            print("\nYou decide to continue your journey outside the cave.")

            time.sleep(1)
            self.narrative_12()

    def narrative_7(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision(""):
            print("\nYou")
            self.inventory.append("")

            time.sleep(1)
            self.narrative_13()
        else:
            print("\nYou decide to continue your journey outside the cave.")

            time.sleep(1)
            self.narrative_14()

    def narrative_8(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision(""):
            print("\nYou")
            self.inventory.append("")

            time.sleep(1)
            self.narrative_15()
        else:
            print("\nYou decide to continue your journey outside the cave.")

            time.sleep(1)
            self.narrative_16()

    def narrative_9(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision(""):
            print("\nYou")
            self.inventory.append("")

            time.sleep(1)
            self.narrative_17()
        else:
            print("\nYou decide to continue your journey outside the cave.")

            time.sleep(1)
            self.narrative_18()

    def narrative_10(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision(""):
            print("\nYou")
            self.inventory.append("")

            time.sleep(1)
            self.narrative_19()
        else:
            print("\nYou decide to continue your journey outside the cave.")

            time.sleep(1)
            self.narrative_20()

    def narrative_11(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision(""):
            print("\nYou")
            self.inventory.append("")

            time.sleep(1)
            self.narrative_12()
        else:
            print("\nYou decide to continue your journey outside the cave.")

            time.sleep(1)
            self.narrative_12()

    def narrative_12(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision(""):
            print("\nYou")
            self.inventory.append("")

            time.sleep(1)
            self.narrative_13()
        else:
            print("\nYou decide to continue your journey outside the cave.")

            time.sleep(1)
            self.narrative_13()

    def narrative_13(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision(""):
            print("\nYou")
            self.inventory.append("")

            time.sleep(1)
            self.narrative_14()
        else:
            print("\nYou decide to continue your journey outside the cave.")

            time.sleep(1)
            self.narrative_14()

    def narrative_14(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision(""):
            print("\nYou")
            self.inventory.append("")

            time.sleep(1)
            self.narrative_15()
        else:
            print("\nYou decide to continue your journey outside the cave.")

            time.sleep(1)
            self.narrative_15()

    def narrative_15(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision(""):
            print("\nYou")
            self.inventory.append("")

            time.sleep(1)
            self.narrative_16()
        else:
            print("\nYou decide to continue your journey outside the cave.")

            time.sleep(1)
            self.narrative_16()

    def narrative_16(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision(""):
            print("\nYou")
            self.inventory.append("")

            time.sleep(1)
            self.narrative_17()
        else:
            print("\nYou decide to continue your journey outside the cave.")

            time.sleep(1)
            self.narrative_17()

    def narrative_17(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision(""):
            print("\nYou")
            self.inventory.append("")

            time.sleep(1)
            self.narrative_18()
        else:
            print("\nYou decide to continue your journey outside the cave.")

            time.sleep(1)
            self.narrative_18()

    def narrative_18(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision(""):
            print("\nYou")
            self.inventory.append("")

            time.sleep(1)
            self.narrative_19()
        else:
            print("\nYou decide to continue your journey outside the cave.")

            time.sleep(1)
            self.narrative_19()

    def narrative_19(self):
        print("\nYour journey continues...")
        time.sleep(1)

        if self.make_decision(""):
            print("\nYou")
            self.inventory.append("")

            time.sleep(1)
            self.narrative_20()
        else:
            print("\nYou decide to continue your journey outside the cave.")

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
        else:
            print("\nYou decide to stay in the current realm, exploring its wonders further.")

            print(f"\nCongratulations, {self.player_name}! you've completed the fantasy Adventure.")
            print("Final Status: ")
            print(f"Player Name: {self.player_name}")
            print(f"Player Health: {self.player_health}")


if __name__ == "__main__":
    game = ChooseYourAdventure()
    game.run_game()


