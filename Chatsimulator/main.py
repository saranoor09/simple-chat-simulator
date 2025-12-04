import tkinter as tk
from tkinter import font as tkfont
import threading
import time
import random
from datetime import datetime

# =============================
# Message Factory (Factory Pattern)
# =============================
class Message:
    def get_text(self): raise NotImplementedError

class UserMessage(Message):
    def __init__(self, text): self.text = text
    def get_text(self): return self.text

class IncomingMessage(Message):
    def __init__(self, text): self.text = text
    def get_text(self): return self.text

class MessageFactory:
    @staticmethod
    def create_message(kind, text):
        if kind == "user": return UserMessage(text)
        return IncomingMessage(text)

# =============================
# ChatEngine (Singleton + Observer)
# =============================
class ChatEngine:
    _instance = None
    def __init__(self):
        self.chat_log = []
        self.observers = []

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = ChatEngine()
        return cls._instance

    def register(self, obs):
        self.observers.append(obs)

    def notify(self, msg):
        self.chat_log.append((datetime.now(), msg))
        for obs in self.observers:
            obs.update(msg)

class NotificationObserver:
    def update(self, msg):
        print("LOG:", msg.get_text())

# =============================
# MAIN GUI – DARK DISCORD PINK
# =============================
class ChatGUI:
    def __init__(self, root):
        self.root = root
        root.title("Pink Discord Chat")
        root.geometry("520x700")
        root.configure(bg="#1e1f22")  # Discord dark

        # Fonts
        self.main_font = tkfont.Font(family="Segoe UI", size=11)
        self.small_font = tkfont.Font(family="Segoe UI", size=9)

        # Title
        title = tk.Label(root, text="Pink Discord Chat 💗", bg="#1e1f22",
                         fg="#ff7bcb", font=("Segoe UI", 14, "bold"))
        title.pack(pady=10)

        # Chat window
        self.canvas = tk.Canvas(root, bg="#2b2d31", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=12, pady=(0,10))
        self.canvas.bind("<Configure>", self._resize)

        self.msg_y = 20
        self.chat_width = 480

        # Typing label
        self.typing = tk.Label(root, text="", bg="#1e1f22",
                               fg="#ff99dd", font=self.small_font)
        self.typing.pack(anchor="w", padx=20)

        # Entry + Send
        bottom = tk.Frame(root, bg="#1e1f22")
        bottom.pack(fill=tk.X, padx=12, pady=12)

        self.entry = tk.Entry(bottom, font=self.main_font, bg="#383a40",
                              fg="white", insertbackground="white")
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=6)
        self.entry.bind("<Return>", lambda e: self.on_send())

        self.send_btn = tk.Label(bottom, text="Send", bg="#ff4fb8",
                                 fg="white", padx=16, pady=6, cursor="hand2")
        self.send_btn.pack(side=tk.RIGHT, padx=6)
        self.send_btn.bind("<Button-1>", lambda e: self.on_send())

        # Chat engine
        self.engine = ChatEngine.instance()
        self.engine.register(NotificationObserver())

        # Welcome
        self._insert_bubble("Welcome to Pink Discord Chat! 💗", "left")

    # =============================
    # Bubble Creation (Discord-style)
    # =============================
    def _insert_bubble(self, text, align="left"):
        max_w = self.chat_width * 0.65

        # wrap text
        words = text.split()
        lines, cur = [], ""

        for w in words:
            test = (cur + " " + w).strip()
            if self.main_font.measure(test) > max_w:
                lines.append(cur)
                cur = w
            else:
                cur = test
        if cur: lines.append(cur)

        line_h = self.main_font.metrics("linespace")
        bubble_h = len(lines)*line_h + 18
        bubble_w = min(max(self.main_font.measure(l) for l in lines) + 20, max_w)

        x = 20 if align == "left" else (self.canvas.winfo_width() - bubble_w - 20)
        y = self.msg_y

        # bubble colors
        color = "#ff4fb8" if align == "right" else "#3a3c42"
        text_color = "white"

        # bubble rectangle
        self.canvas.create_round_rect = self.canvas.create_rectangle(
            x, y, x+bubble_w, y+bubble_h, fill=color, outline="", width=0
        )

        # text drawing
        ty = y + 10
        for line in lines:
            self.canvas.create_text(
                x + 12, ty, anchor="nw", text=line,
                fill=text_color, font=self.main_font
            )
            ty += line_h

        # timestamp
        ts = datetime.now().strftime("%H:%M")
        self.canvas.create_text(
            x + bubble_w - 6, y + bubble_h - 6, anchor="se",
            text=ts, fill="#ffb8e8", font=self.small_font
        )

        self.msg_y += bubble_h + 12
        self.canvas.configure(scrollregion=(0, 0, 1000, self.msg_y))
        self.canvas.yview_moveto(1.0)

    def _resize(self, event):
        self.chat_width = event.width - 40

    # =============================
    # Sending Message
    # =============================
    def on_send(self):
        text = self.entry.get().strip()
        if not text: return

        msg = MessageFactory.create_message("user", text)
        self.engine.notify(msg)
        self._insert_bubble(msg.get_text(), align="right")
        self.entry.delete(0, tk.END)

        threading.Thread(target=self._bot_reply, args=(text,), daemon=True).start()

    # =============================
    # Bot Reply (No spam)
    # =============================
    def _bot_reply(self, user_text):
        self._typing(True)
        time.sleep(random.uniform(1.0, 1.4))
        self._typing(False)

        # simple smart reply
        if "hello" in user_text.lower():
            reply = "Hey! 💗"
        elif "bye" in user_text.lower():
            reply = "See you! 💖"
        elif "love" in user_text.lower():
            reply = "Aww that's cute 💗💗"
        else:
            reply = random.choice([
                "That's interesting 💗",
                "Tell me more!",
                "Niceee 💕"
            ])

        msg = MessageFactory.create_message("incoming", reply)
        self.engine.notify(msg)
        self.root.after(0, lambda: self._insert_bubble(reply, "left"))

    def _typing(self, on):
        self.typing.config(text="Bot is typing..." if on else "")
        self.typing.update()


# =============================
# RUN PROGRAM
# =============================
def main():
    root = tk.Tk()
    ChatGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
