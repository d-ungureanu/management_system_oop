#! python3
import choice_selection_oop


if __name__ == '__main__':
    print("This is the management_system.py")
    try:
        choice_selection_oop.select_option()
    except KeyboardInterrupt:
        print("\n -----------------------------------------------------------")
        print("| Program execution interrupted by user from keyboard input.|")
        print(" -----------------------------------------------------------")


