from __future__ import annotations

import os
import re
import random
import webbrowser
import threading
import subprocess

from typing import Any
from colorama import Fore

from ._assets import dialogues as yuri_dialogues


class Tasker:

    def __init__(self) -> None:
        """Actions, commands and process execution class.
        """
        self.vars: dict = {}
        self.dialogues: list = yuri_dialogues
        self.keep_going: bool = True
    
    def _parse_vars(self, string: str) -> str:
        """Replaces $var_string by its value (but only if
        it was added to vars using `yuri.do.var()` method).

        ### Args
        - `string` The string where vars will be replaced.
        """
        regex = re.compile(r'\$(\w+)', re.DOTALL)
        matches = regex.findall(string)

        for var in matches:
            val = self.var(var)

            if not val:
                val = var

            string = string.replace('$%s' % var, val)
        
        return string
    
    def pause(self) -> None:
        """Tasker waits until enter key is pressed.
        """
        input("Press enter to continue...")
    
    def waifu_print(self, string: str) -> Tasker:
        """Prints an string using the waifu banner.

        ### Args
        - `string` String to display.
        """
        if not self.keep_going:
            return self

        print("\n -------------------------------------------")
        print(" " + string)
        print(random.choice(self.dialogues))

        return self

    def log_print(self, string: str) -> Tasker:
        """Prints an string but also displays the current 
        working folder.

        ### Args
        - `string` String to display.
        """
        if not self.keep_going:
            return self

        print("> %s%s%s%s" % (Fore.RESET, Fore.GREEN, os.getcwd(), Fore.RESET))
        print(string)

        return self

    def ignore_errors(self) -> Tasker:
        """Tasker will keep excecuting the following tasks
        even prev tasks could fail.
        """
        self.keep_going = True
        return self

    def var(self, name: str, val: Any=None) -> Any:
        """Stores a var that could be used like $var_name
        in the tasker method arguments strings.

        By example, if you set `yuri.do.var('foo_dir', 'c:\\bar')`
        then you can do `yuri.do.cd('$foo_dir')`.

        ### Args
        - `name` The var name. 
        - `val` The value of the var.
        """
        if not val:
            if not name in self.vars.keys():
                return None
            return self.vars[name]

        self.vars[name] = val

    def clear(self) -> Tasker:
        """Clears the console.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        return self

    def dirs_list(self) -> list:
        """Returns the directories lists of the current working dir.
        """
        if not self.keep_going:
            return []

        _list = os.listdir(os.getcwd())
        list = []

        for e in _list:
            if os.path.isdir(e):
                list.append(e)

        return list

    def files_list(self) -> list:
        """Returns the files lists of the current working dir.
        """
        if not self.keep_going:
            return []

        _list = os.listdir(os.getcwd())
        list = []

        for e in _list:
            if not os.path.isdir(e):
                list.append(e)

        return list

    def terminate(self) -> None:
        """Terminates the running task.
        """
        self.waifu_print(Fore.YELLOW + "An spooky task has terminated me :(" + Fore.RESET)
        exit()

    def wait(self) -> Tasker:
        """Pauses task excecution but only if prev task was terminated correctly.
        """
        if not self.keep_going:
            return self

        self.pause()

        return self

    def cd(self, dir: str) -> Tasker:
        """Changes the current working dir.

        ### Args
        - `dir` Directory to move on.
        """
        if not self.keep_going:
            return self

        path = self._parse_vars(dir)
        self.log_print("%scd%s %s" % (Fore.YELLOW, Fore.RESET, path))

        if not os.path.isdir(path):
            self.waifu_print("%sNo such directory onii-chan :(%s" % (Fore.RED, Fore.RESET))
            self.keep_going = False
            return self

        os.chdir(path)
        return self

    def navto(self, url: str) -> Tasker:
        """Opens the url in a webbrowser.

        ### Args
        - `url` Url to open.
        """
        if not self.keep_going:
            return self

        self.log_print("%snavto%s %s" % (Fore.YELLOW, Fore.RESET, url))

        webbrowser.open(url, new=2)
        return self

    def run(self, cmd: str) -> Tasker:
        """Excecutes a system command.

        ### Args
        - `cmd` Command to execute.
        """
        if not self.keep_going:
            return self

        cmd = self._parse_vars(cmd)
        self.log_print("%s%s%s" % (Fore.YELLOW, cmd, Fore.RESET))
        print(Fore.CYAN)
        output = os.system(cmd)
        print(Fore.RESET, end="")

        if output != 0:
            self.waifu_print("%sError while I was executing %s :(%s" % (Fore.RED, cmd, Fore.RESET))
            self.pause()

            self.keep_going = False
            return self

        return self
    
    def get_input(self, msg: str, default: str=None, can_be_null: bool=False) -> str:
        """Read keyboard input with an optional default value.

        ### Args
        - `msg` Text to display when input request.
        - `default` Default value used if user do not type anything.
        - `can_be_null` If true, input can be empty.
        """
        if not self.keep_going:
            return ""

        i = None

        if default:
            def_string = f"(def.:<{default}>)"
        else:
            def_string = ''

        while True:
            i = input("(%s%s%s) %s %s" % (Fore.GREEN, os.getcwd(), Fore.RESET, msg, def_string))

            if default and not i:
                i = default

            if can_be_null and not i:
                break

            if i:
                break
        
        return i

    def run_with_input(self, cmd: str, msg: str) -> Tasker:
        """Runs a command but request an keyboard input and `{i}`
        string in the command line is replaced by the input result
        before excecute the command.

        By example. `yuri.do.run_with_input("cd {i}", "Type a directory: ")`
        will run `cd the_typed_directory`.

        ### Args
        - `cmd` Comand to run. it must contain '{i}' string to be replaced with 
        the input result.
        - `msg` Message showed to request the input.
        """
        if not self.keep_going:
            return self

        i = self.get_input(msg)
        cmd = cmd.replace("{i}", i)

        cmd = self._parse_vars(cmd)
        self.run(cmd)

        return self

    def copy(self, elements: list, destiny: str) -> Tasker:
        """Copies files or directories to the destiny directory. If
        the element that is beeing copied it's a directory its content
        will be copied recursively.

        ### Args
        - `elements` It could be a list of files, directories or both.
        - `destiny` Path where elements will be copied.
        """
        if not self.keep_going:
            return self

        print(Fore.CYAN)
        for element in elements:

            if os.path.isdir(element):
                self.run('xcopy %s %s /E/I/Y' % (element, os.path.join(destiny, element)))

            else:
                self.run('copy /Y %s %s' % (element, destiny))

        print(Fore.RESET)

        return self

    def delete(self, elements: list) -> Tasker:
        """Deletes files or directories.

        ### Args
        - `elements` A list of files, directories or both to delete.
        """
        if not self.keep_going:
            return self

        print(Fore.CYAN)
        for element in elements:
            self.log_print(f"{Fore.YELLOW}rm{Fore.RESET} {element}")
            self.run('del /Q "%s"' % element)

        print(Fore.RESET)

        return self

    def filter(self, elements: list, filters: list) -> list:
        """Removes the elements from a list that does not contains
        any of the string in the filters list.

        By example. yuri.do.filter(["foo.png", "bar.jpg", "baz.mp3"], [".png", ".jpg"])
        will return ["foo.png", "bar.png"].

        ### Args
        - `elements` List of elements that will be filtered.
        - `filters` List of strings that elements must contain.
        """
        filtered = []

        print(Fore.CYAN)
        for element in elements:
            for query in filters:
                if query in element:
                    filtered.append(element)

        print(Fore.RESET)

        return filtered

    def subprocess(self, cmd: str)  -> Tasker:
        """Runs a command in a new console using a secondary thread.
        This means that command excecuted by this way will not interrupt
        tasks execution even if that command havent finished yet.

        ### Args
        - `cmd` Command to excecute.
        """
        if not self.keep_going:
            return self

        def callback(c_cmd):
            subprocess.call(c_cmd, creationflags=subprocess.CREATE_NEW_CONSOLE)

        self.log_print(f"{Fore.YELLOW}subprocess{Fore.RESET} {cmd}")

        print(Fore.CYAN)

        sp = threading.Thread(target=callback, args=(cmd,))
        sp.start()

        print(Fore.RESET)

        return self
