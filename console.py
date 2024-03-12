#!/usr/bin/python3
""""the project terminal"""
import cmd


class HBNBCommand(cmd.Cmd):
    """"to handle the CLI"""
    prompt = "(hbnb)"

    def do_EOF(self, line):
        """handle the case of EOF"""
        return True

    def do_quit(self, line):
        """handle the exit case"""
        return True
    

    def do_help(self, line):
        """show the help"""
        cmd.Cmd.do_help(self, line)

    def emptyline(self) -> bool:
        """handle empty line"""
        pass
    
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()