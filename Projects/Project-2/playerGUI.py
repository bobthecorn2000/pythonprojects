import tkinter as tk
from tkinter import messagebox
from DB import datawork
# ok i sped ran this with cuz its 8pm on 12/15 and i need to get this in lol
class PlayerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Player Data Management")

        self.player_id_label = tk.Label(root, text="Player ID:")
        self.player_id_label.grid(row=0, column=0, padx=10, pady=10)

        self.player_id_entry = tk.Entry(root)
        self.player_id_entry.grid(row=0, column=1, padx=10, pady=10)

        self.get_player_button = tk.Button(root, text="Get Player", command=self.get_player)
        self.get_player_button.grid(row=0, column=2, padx=10, pady=10)

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=1, column=0, padx=10, pady=10)

        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=1, column=1, padx=10, pady=10)

        self.position_label = tk.Label(root, text="Position:")
        self.position_label.grid(row=2, column=0, padx=10, pady=10)

        self.position_entry = tk.Entry(root)
        self.position_entry.grid(row=2, column=1, padx=10, pady=10)

        self.at_bats_label = tk.Label(root, text="At Bats:")
        self.at_bats_label.grid(row=3, column=0, padx=10, pady=10)

        self.at_bats_entry = tk.Entry(root)
        self.at_bats_entry.grid(row=3, column=1, padx=10, pady=10)

        self.hits_label = tk.Label(root, text="Hits:")
        self.hits_label.grid(row=4, column=0, padx=10, pady=10)

        self.hits_entry = tk.Entry(root)
        self.hits_entry.grid(row=4, column=1, padx=10, pady=10)

        self.save_changes_button = tk.Button(root, text="Save Changes", command=self.save_changes)
        self.save_changes_button.grid(row=5, column=0, padx=10, pady=10)

        self.cancel_button = tk.Button(root, text="Cancel", command=self.cancel_changes)
        self.cancel_button.grid(row=5, column=1, padx=10, pady=10)

        # Store original player data
        self.original_data = {}

    def get_player(self):
        player_name = self.player_id_entry.get()
        try:
            player_data = datawork.get_player_by_name(player_name)
            if player_data:
                # Display player data
                self.original_data = player_data
                self.name_entry.delete(0, tk.END)
                self.name_entry.insert(0, player_data['name'])

                self.position_entry.delete(0, tk.END)
                self.position_entry.insert(0, player_data['position'])

                self.at_bats_entry.delete(0, tk.END)
                self.at_bats_entry.insert(0, str(player_data['at_bats']))

                self.hits_entry.delete(0, tk.END)
                self.hits_entry.insert(0, str(player_data['hits']))
            else:
                messagebox.showerror("Error", f"Player with name '{player_name}' not found.")
        except ValueError:
            messagebox.showerror("Error", "Invalid Player name. Please enter a valid string.")

    def save_changes(self):
        # Update the player data in the database
        player_id = self.player_id_entry.get()
        try:
            new_at_bats = int(self.at_bats_entry.get())
            new_hits = int(self.hits_entry.get())

            datawork.update_player(int(player_id), new_at_bats, new_hits)

            messagebox.showinfo("Success", "Changes saved successfully.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for At Bats or Hits. Please enter valid integers.")

    def cancel_changes(self):
        # Restore the original player data in the text entry fields
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, self.original_data.get('name', ''))

        self.at_bats_entry.delete(0, tk.END)
        self.at_bats_entry.insert(0, str(self.original_data.get('at_bats', '')))

        self.hits_entry.delete(0, tk.END)
        self.hits_entry.insert(0, str(self.original_data.get('hits', '')))

if __name__ == "__main__":
    root = tk.Tk()
    app = PlayerGUI(root)
    root.mainloop()