from intcode import IntCodeComputer


def main():
    """Main function that loads a program to the 'computer'."""
    computer = IntCodeComputer('day_9.input')
    computer.run()


if __name__ == '__main__':
    main()
