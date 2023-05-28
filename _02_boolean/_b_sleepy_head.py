"""
Use boolean variables to control program logic between two different code
paths.
"""
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    # TODO)
    #  1. Use a boolean variable to indicate if it is the weekend.
    #     Display a different message to the user depending on whether it is
    #     the weekend or not.
    #  2. Use a boolean variable to indicate if a student passed an exam.
    #     Display a different message to the user depending on whether they
    #     passed or not.
    window = Tk()
    window.withdraw()
    # hi = simpledialog.askstring(title=None, prompt="What day of the week is it")
    # is_weekend = hi == "saturday" or hi == "sunday"
    # if is_weekend:
    #     messagebox.showinfo(title="", message="ITS THE WEEKEND! LETS PARTY")
    # else:
    #     messagebox.showinfo(title="", message="ARGH I CANT WAIT FOR THE WEEKEND!")

    hi = simpledialog.askinteger(title="PASS/FAIL?", prompt="WHAT DID YOU GET ON THE TEST: /10")
    passed = 5 < hi <= 10
    failed = hi <= 5
    if passed:
        messagebox.showinfo(title="", message="YOU PASSED!")
    elif failed:
        messagebox.showinfo(title="", message="YOU FAILED!")
    else:
        messagebox.showinfo(title="", message="ITS OUT OF 10!")

    pass
