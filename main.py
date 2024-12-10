from gui import *

def main() -> None:
    """
    Creates an instance of the grade score
    entry gui
    :return: None
    """
    window = Tk()
    window.title('Grade Entry')
    window.geometry('300x260')
    window.resizable(False, False)
    Gui(window)
    window.mainloop()

if __name__ == '__main__':
    main()
