#!/usr/bin/python3
""" contains the entry point of the command interpreter."""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Exit the command interpreter."""
        return True

    def do_help(self, arg):
        """help for the command interpreter."""
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """Exit the command interpreter."""
        print()
        return True



if __name__ == '__main__':
    HBNBCommand().cmdloop()
