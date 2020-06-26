#!/usr/bin/python3
"""
The prompt and whatnot
This is where we hide the cheese
Ian is talking right now
He's got an i7
I have an i7 too
That's crazy
"""
import cmd
from models.base_model import BaseModel
from models import storage as pineapple
objs = pineapple.all()


class HBNBCommand(cmd.Cmd):
    """This is where the class is and where it belongs"""
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command line"""
        return True

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id. Ex: $ create BaseModel
        """
        if len(arg) == 0:
            print("** class name missing **")
        if (arg == "BaseModel"):
            new_model = BaseModel()
            print(new_model.id)
            new_model.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based
        on the class name and id. Ex: $ show BaseModel 1234-1234-1234
        """
        arg = arg.split()
        if len(arg[0]) == 0:
            print("** class name missing **")
        elif arg[0] == "BaseModel":
            if len(arg[1]) == 0:
                print("** instance id missing **")
            else:
                if arg[0]+"."+arg[1] in objs:
                    print(objs[arg[0]+"."+arg[1]])
                else:
                    print("** no instance found **")
        else:
             print("** class doesn't exist **")
if __name__ == "__main__":
    HBNBCommand().cmdloop()
