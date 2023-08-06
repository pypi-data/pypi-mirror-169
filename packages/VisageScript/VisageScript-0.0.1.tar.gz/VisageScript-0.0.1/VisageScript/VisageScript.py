"""
This file containts code for VisageScript programming language.
Author: PythonApkDev
"""


# Language version: 0.0.1


# Importing necessary libraries


import sys
import os
import copy
import mpmath
from mpmath import mp, mpf

mp.pretty = True


# Creating static functions.


def is_number(string: str) -> bool:
    try:
        mpf(string)
        return True
    except ValueError:
        return False


def open_file(file_name: str):
    file = open(file_name, 'r')
    contents: str = file.read()
    file.close()
    return contents


def parse_file(file_name, terminal):
    # type: (str, Terminal) -> None
    if file_name[-6::] != ".vsgsc":
        print("ERROR: Invalid file extension! File extension should be '.vsgsc'!")

    contents = open_file(file_name)
    lines = contents.split("\n")
    for line in lines:
        parse_line(line, terminal)


def parse_line(line, terminal):
    # type: (str, Terminal) -> None
    # Checking for empty lines
    if len(line.split(" ")) == 0:
        return

    # Checking whether there is a semicolon at the end of the line or not.
    if line[-1] != ";":
        print("ERROR!!!")
        return

    line = line[:-1]
    line_words: list = line.split(" ")

    # Case where new variables are declared.
    if line_words[0] in ["var", "int", "float"]:
        # Proceed to variable name.
        var_name: str = line_words[1]
        if terminal.variable_exists(var_name):
            print("ERROR!!!")
            return

        # Check whether "=" sign exists or not
        if line_words[2] != "=":
            print("ERROR!!!")
            return

        after: list = line_words[3::]
        after_words: str = ""
        for i in range(len(after)):
            if terminal.variable_exists(after[i]):
                curr_var_name: str = after[i]
                after[i] = str(terminal.get_variable(curr_var_name).value)

            if "." in str(after[i]):
                after[i] = "mpf(" + after[i] + ")"

            if i < len(after) - 1:
                after_words += after[i] + " "
            else:
                after_words += after[i]

        value: object = eval(after_words)
        if line_words[0] == "int":
            value = int(value)
        elif line_words[0] == "float":
            value = mpf(value)

        terminal.add_variable(Variable(var_name, line_words[0], value))

    # Case where existing variables have their values changed
    elif line_words[0] not in ["var", "int", "float", "print"]:
        # Get variable name
        var_name: str = line_words[0]
        if not terminal.variable_exists(var_name):
            print("ERROR!!!")
            return
        elif len(line_words) <= 1:
            print("ERROR!!!")
            return

        # Check whether "=" sign exists or not
        if line_words[1] != "=":
            print("ERROR!!!")
            return

        after: list = line_words[2::]
        after_words: str = ""
        for i in range(len(after)):
            if terminal.variable_exists(after[i]):
                curr_var_name: str = after[i]
                after[i] = str(terminal.get_variable(curr_var_name).value)

            if "." in str(after[i]):
                after[i] = "mpf(" + after[i] + ")"

            if i < len(after) - 1:
                after_words += after[i] + " "
            else:
                after_words += after[i]

        value: object = eval(after_words)
        if line_words[0] == "int":
            value = int(value)
        elif line_words[0] == "float":
            value = mpf(value)

        terminal.update_variable(terminal.get_variable(var_name), value)

    # Case where values are printed out
    elif line_words[0] == "print":
        try:
            after: list = line_words[1::]
            after_words: str = ""
            for i in range(len(after)):
                if terminal.variable_exists(after[i]):
                    curr_var_name: str = after[i]
                    after[i] = str(terminal.get_variable(curr_var_name).value)

                if "." in str(after[i]):
                    after[i] = "mpf(" + after[i] + ")"

                if i < len(after) - 1:
                    after_words += after[i] + " "
                else:
                    after_words += after[i]

            print(eval(after_words))
        except SyntaxError:
            print("ERROR!!!")

    # Else, an error occurs
    else:
        print("ERROR!!!")


def clear():
    # type: () -> None
    if sys.platform.startswith('win'):
        os.system('cls')  # For Windows System
    else:
        os.system('clear')  # For Linux System


# Creating necessary classes.


class Variable:
    """
    This class contains attributes of a variable.
    """

    def __init__(self, name, type_, value):
        # type: (str, str, object) -> None
        self.name: str = name
        self.type: str = type_
        self.value: object = value

    def __str__(self):
        # type: () -> str
        return str(self.type) + " " + str(self.name) + " : " + str(self.value)

    def clone(self):
        # type: () -> Variable
        return copy.deepcopy(self)


class Terminal:
    """
    This class contains attributes of the current terminal.
    """

    def __init__(self):
        # type: () -> None
        self.__variables: list = []

    def get_variable(self, var_name):
        # type: (str) -> Variable or None
        if self.variable_exists(var_name):
            for variable in self.__variables:
                if variable.name == var_name:
                    return variable

        return None

    def variable_exists(self, var_name):
        # type: (str) -> bool
        return var_name in [var.name for var in self.__variables]

    def add_variable(self, variable):
        # type: (Variable) -> None
        self.__variables.append(variable)

    def update_variable(self, variable, new_value):
        # type: (Variable, object) -> bool
        if variable not in self.__variables:
            return False

        if not self.type_matches(new_value, variable.type):
            return False

        variable.value = new_value
        return True

    def type_matches(self, value, type_):
        # type: (object, str) -> bool
        if type_ == "int":
            return isinstance(value, int)
        elif type_ == "float":
            return is_number(str(value))
        return True

    def get_variables(self):
        # type: () -> list
        return self.__variables

    def clone(self):
        # type: () -> Terminal
        return copy.deepcopy(self)


# Creating main function used to run the application.


def main():
    """
    This main function is used to run the application.
    :return: None
    """

    print("Welcome to VisageScript Runner by 'PythonApkDev'.")
    print("VisageScript is a programming language inspired by Python, Java, JavaScript, and Ruby.")
    print("The extension for VisageScript files is '.vsgsc.'.")
    print("Enter 'Y' for yes.")
    print("Enter anything else for no.")
    continue_using: str = input("Do you want to continue using VisageScript Runner? ")
    while continue_using == "Y":
        clear()
        file_name: str = input("Please enter the name of the file you want to parse: ")
        terminal: Terminal = Terminal()
        print("\n")
        parse_file(file_name, terminal)
        print("\n")
        print("Enter 'Y' for yes.")
        print("Enter anything else for no.")
        continue_using = input("Do you want to continue using VisageScript Runner? ")
    sys.exit()


if __name__ == '__main__':
    main()
