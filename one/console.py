#!/usr/bin/python3
'''Command Line Interpreter'''
import cmd
import json
import re
import sys

from models import *
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_EOF(self, *args):
        '''Usage: EOF
           Function: Exits the program
        '''
        print()
        return True

    def do_quit(self, *args):
        '''Usage: quit
           Function: Exits the program
        '''
        # quit()
        return True

    def do_create(self, line):
        '''Usage: 1. create <class name> | 2. <class name>.create()
Function: Creates an instance of the class
        '''
        if line != "" or line is not None:
            if line not in storage.classes():
                print("** class doesn't exist **")
            else:
                # create an instance of the given class
                obj_intance = storage.classes()[line]()
                obj_intance.save()
                print(obj_intance.id)
        else:
            print("** class name missing **")

    def do_show(self, line):
        '''Usage: 1. show <class name> <id> | 2. <class name>.show(<id>)
Function: Shows the instance details of the class
        '''
        # check if class name and instance id was provided
        if line == "" or line is None:
            print("** class name missing **")

        else:
            # get all the arguments passed via the command line
            class_info = line.split(" ")
            if len(class_info) < 2:
                print("** instance id missing **")
            else:
                class_name = class_info[0]
                instance_id = class_info[1]
                # check if class name exists
                if class_name in storage.classes():
                    # check if instance_id exists
                    key = f"{class_name}.{instance_id}"
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        instance_dict = storage.all()[key]
                        print(instance_dict)

                else:
                    print("** class doesn't exist **")

    def do_destroy(self, line):
        '''Usage: 1. destroy <class name> <id> | 2. <class name>.delete(<id>)
Function: Deletes the instance  of the class
        '''
        # check if class name and instance id was provided
        if line == "" or line is None:
            print("** class name missing **")

        else:
            # get all the arguments passed via the command line
            class_info = line.split(" ")
            if len(class_info) < 2:
                print("** instance id missing **")
            else:
                class_name = class_info[0]
                instance_id = class_info[1]
                # check if class name exists
                if class_name in storage.classes():
                    # check if instance_id exists
                    key = f"{class_name}.{instance_id}"
                    if key not in storage.all():
                        print("** no instance found **")

