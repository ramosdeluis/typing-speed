import tkinter as tk
from PIL import ImageTk, Image
from tkinter.scrolledtext import ScrolledText


class Typing(tk.Tk):

    def __init__(self):
        super().__init__()
        self.accuracy = 0
        self.words_per_minute = 0
        self.time = None
        self.seconds = 0
        self.timer_running = False
        self.title('Typing Speed Test')
        self.geometry('1300x820')
        self.alphabet_image = ImageTk.PhotoImage(Image.open('alphabet.jpeg').resize((400, 400)))
        self.open_alphabet()
        self.text_box = tk.LabelFrame(self, text="Typing Test", pady=60, padx=200)
        self.text_to_write = tk.Label(self.text_box, wraplength=700, text='Era uma vez um pequeno pássaro chamado Piu-Piu. Ele vivia em uma árvore com sua família e amigos. Um dia, ele decidiu sair em uma aventura para explorar o mundo. Ele voou por montanhas e vales, viu rios e lagos e conheceu muitos outros animais. No final do dia, ele voltou para casa cansado mas feliz. Ele contou a todos sobre sua aventura e eles ficaram muito orgulhosos dele. Piu-Piu percebeu que o mundo era grande e cheio de coisas maravilhosas para descobrir. E assim ele viveu muito feliz para sempre, explorando novos lugares todos os novos dias.')
        self.user_input_text = tk.Label(self.text_box, text="Typing:")
        self.user_input = ScrolledText(
            self.text_box,
            wrap=tk.WORD,
            width=100,
            height=5,
            font=("Times New Roman", 15)
        )
        self.text_box.grid(column=0, row=2, columnspan=2, padx=(40, 40))
        self.user_input.grid(column=1, row=3)
        self.text_to_write.grid(column=0, row=2, columnspan=2, pady=(0, 10))
        self.user_input.bind('<KeyRelease>', self.update_text)
        self.score_board = tk.Label(
            self, text=f"Speed: {self.words_per_minute:.2f} words/min Accuracy: {self.accuracy * 100:.2f}%"
        )
        self.score_board.grid(column=0, row=1, columnspan=2)
        self.start_timer()

    def open_alphabet(self):
        panel = tk.Label(self, image=self.alphabet_image)
        panel.grid(column=0, row=0, columnspan=2, padx=(50, 10), pady=(20, 0))

    def update_text(self, event):
        text = self.user_input.get("1.0", tk.END)
        self.words_per_minute = len(text.split())/(self.seconds/60)
        self.make_numbers(text)
        self.score_board.config(
            text=f"Speed: {self.words_per_minute:.2f} words/min Accuracy: {self.accuracy * 100:.2f}%"
        )
        if text.strip() == '':
            self.seconds = 0

    def make_numbers(self, text):
        correct_words = []
        for number, word in enumerate(text.split()):
            if word == self.text_to_write.cget('text').split()[number]:
                correct_words.append(word)
        self.accuracy = len(correct_words) / len(self.text_to_write.cget('text').split())

    def start_timer(self):
        self.timer_running = True
        self.update_timer()

    def stop_timer(self):
        self.timer_running = False

    def update_timer(self):
        if self.timer_running:
            self.seconds += 1
            minutes, seconds = divmod(self.seconds, 60)
            hours, minutes = divmod(minutes, 60)
            self.time = [hours, minutes, seconds]
            self.after(1000, self.update_timer)


if __name__ == '__main__':
    root = Typing()
    root.mainloop()
