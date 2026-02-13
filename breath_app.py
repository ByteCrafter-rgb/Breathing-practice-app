import tkinter as tk
import time
import threading

# Breathing configuration
PATTERN = [
    ("Inhale", 4),
    ("Hold", 4),
    ("Exhale", 4),
    ("Hold", 4),
]

TOTAL_DURATION = 120  # 2 minutes in seconds

class BreathingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Breathing Guide")
        self.root.geometry("400x300")
        self.root.configure(bg="black")

        self.label = tk.Label(
            root,
            text="Press Start",
            font=("Helvetica", 32),
            fg="white",
            bg="black"
        )
        self.label.pack(expand=True)

        self.start_button = tk.Button(
            root,
            text="Start",
            font=("Helvetica", 16),
            command=self.start_breathing
        )
        self.start_button.pack(pady=20)

        self.running = False

    def start_breathing(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self.run_breathing).start()

    def run_breathing(self):
        start_time = time.time()

        while time.time() - start_time < TOTAL_DURATION and self.running:
            for phase, duration in PATTERN:
                for remaining in range(duration, 0, -1):
                    self.update_label(f"{phase}\n{remaining}")
                    time.sleep(1)

        self.update_label("Done 🌿")
        self.running = False

    def update_label(self, text):
        self.label.config(text=text)

if __name__ == "__main__":
    root = tk.Tk()
    app = BreathingApp(root)
    root.mainloop()
