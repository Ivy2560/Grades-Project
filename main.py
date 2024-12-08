from gui import *

def main():
    window = Tk()
    window.title('Grade Entry')
    window.geometry('300x260')
    window.resizable(False, False)
    Gui(window)
    window.mainloop()

if __name__ == '__main__':
    main()
