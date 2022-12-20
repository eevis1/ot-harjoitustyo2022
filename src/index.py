from tkinter import Tk
from ui.ui import UI

def main():
    screen = Tk()
    screen.title("Course App")
    view = UI(screen)
    view.start()
    screen.mainloop()

if __name__ == "__main__":
    main()
    