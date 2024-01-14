import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the command interpreter."""
        return True

    def do_EOF(self, arg):
        """Exit the command interpreter."""
        return True

    def default(self, line):
        """Called on an input line when the command prefix is not recognized."""
        if line == '':
            return
        else:
            print(f"*** Unknown syntax: {line}")

    
if __name__ == '__main__':
    HBNBCommand().cmdloop()