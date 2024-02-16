import tkinter as tk
import random

class RiskGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Risk Game")
        self.canvas = tk.Canvas(master, width=800, height=600)
        self.canvas.pack()

        self.territories = {
            "Territory 1": {"x": 100, "y": 100, "owner": None, "troops": 0},
            "Territory 2": {"x": 250, "y": 200, "owner": None, "troops": 0},
            "Territory 3": {"x": 400, "y": 150, "owner": None, "troops": 0},
            "Territory 4": {"x": 550, "y": 100, "owner": None, "troops": 0},
            "Territory 5": {"x": 100, "y": 300, "owner": None, "troops": 0},
            "Territory 6": {"x": 250, "y": 400, "owner": None, "troops": 0},
            "Territory 7": {"x": 400, "y": 350, "owner": None, "troops": 0},
            "Territory 8": {"x": 550, "y": 300, "owner": None, "troops": 0},
            "Territory 9": {"x": 200, "y": 500, "owner": None, "troops": 0},
            "Territory 10": {"x": 350, "y": 450, "owner": None, "troops": 0},
            "Territory 11": {"x": 500, "y": 500, "owner": None, "troops": 0},
            "Territory 12": {"x": 650, "y": 400, "owner": None, "troops": 0},
        }

        self.players = ["Player", "AI"]
        self.current_player_index = 0

        self.draw_map()
        self.place_troops()

    def draw_map(self):
        for territory, data in self.territories.items():
            x = data["x"]
            y = data["y"]
            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill='gray', outline='black')
            self.canvas.create_text(x, y, text=territory)

    def place_troops(self):
        for territory in self.territories:
            owner = random.choice(self.players)
            self.territories[territory]["owner"] = owner
            self.territories[territory]["troops"] = random.randint(1, 5)
            self.canvas.create_text(self.territories[territory]["x"], self.territories[territory]["y"] + 30,
                                    text=f"{owner}: {self.territories[territory]['troops']} troops")

    def roll_dice(self, event):
        attacker = self.players[self.current_player_index]
        if attacker == "AI":
            self.ai_attack()
        else:
            defender = "Player"
            attacker_rolls = sorted([random.randint(1, 6) for _ in range(3)], reverse=True)
            defender_rolls = sorted([random.randint(1, 6) for _ in range(2)], reverse=True)

            result_text = f"{attacker} rolls: {attacker_rolls}\n{defender} rolls: {defender_rolls}\n"
            for a, d in zip(attacker_rolls, defender_rolls):
                if a > d:
                    result_text += f"{attacker} wins a battle!\n"
                else:
                    result_text += f"{defender} wins a battle!\n"
            self.current_player_index = (self.current_player_index + 1) % len(self.players)
            result_text += f"\nNext turn: {self.players[self.current_player_index]}"
            self.result_label.config(text=result_text)

    def ai_attack(self):
        attacker = "AI"
        defender = "Player"
        territories_to_attack = [territory for territory, data in self.territories.items() if data["owner"] == attacker]

        if territories_to_attack:
            attacking_territory = random.choice(territories_to_attack)
            defending_territory = random.choice([territory for territory in self.territories if territory != attacking_territory and self.territories[territory]["owner"] == defender])

            attacker_rolls = sorted([random.randint(1, 6) for _ in range(3)], reverse=True)
            defender_rolls = sorted([random.randint(1, 6) for _ in range(2)], reverse=True)

            result_text = f"{attacker} attacks {defending_territory} from {attacking_territory}\n"
            result_text += f"{attacker} rolls: {attacker_rolls}\n{defender} rolls: {defender_rolls}\n"
            for a, d in zip(attacker_rolls, defender_rolls):
                if a > d:
                    result_text += f"{attacker} wins a battle!\n"
                else:
                    result_text += f"{defender} wins a battle!\n"

            self.current_player_index = (self.current_player_index + 1) % len(self.players)
            result_text += f"\nNext turn: {self.players[self.current_player_index]}"
            self.result_label.config(text=result_text)

root = tk.Tk()
risk_game = RiskGame(root)
risk_game.result_label = tk.Label(root, text="")
risk_game.result_label.pack()
root.bind("<space>", risk_game.roll_dice)
root.mainloop()
