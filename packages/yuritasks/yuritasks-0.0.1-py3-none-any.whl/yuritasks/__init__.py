#!/usr/bin/env python
""" Yuki - Task automation tool

Module with utilities to automate boring and repetitive tasks.
"""

__author__ = "edo0xff"
__credits__ = ["edo0xff"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "edo0xff"
__email__ = "edo0xff@proton.me"
__status__ = "Development"

import sys

from colorama import Fore
from typing import Callable
from colorama import init as init_colorama

from ._tasker import Tasker
from ._environment import Task, Environment
from ._assets import banner as yuki_banner

do: Tasker = Tasker()
environment: Environment = Environment()

init_colorama()


def _choose_namepace_id() -> int:
    """Request for user input to choose a valid 
    namespace and returns its id.
    """        
    while True:
        do.clear()

        print(yuki_banner)

        print("")
        print(" ~ Choose a namespace:")
        print("")

        for namespace in environment.get_namespaces():
            print(" ~ id(%s%s%s) %s%s%s" % (Fore.GREEN, environment.get_namespace_id(namespace), Fore.RESET, Fore.MAGENTA, namespace, Fore.RESET))

        namespace_id = input("\n ~ namespace id: ")

        if namespace_id.isnumeric() and environment.is_valid_namespace_id(int(namespace_id)):
            return int(namespace_id)
        
        else:
            do.clear()\
                .waifu_print("%sInvalid namespace :((%s" % (Fore.RED, Fore.RESET))\
                .pause()


def _command_help(namespace: str, args: list) -> None:
    """Prints the help of help command or the help
    of a task specifying its task_id in the args list.
    """
    if len(args) < 1:
        do.clear()\
            .waifu_print("Use help <task_id> to get help about the task!")\
            .pause()
        
        return None

    task_id = args[0]

    if task_id.isnumeric() and environment.is_valid_task_id(namespace, int(task_id)):
        task = environment.get_task(namespace, int(task_id))

        do.clear()\
            .waifu_print(task.help)\
            .pause()
        
        return None
    
    do.clear()\
        .waifu_print("%sInvalid task id :((%s" % (Fore.RED, Fore.RESET))\
        .pause()


def task(func) -> Callable:
    """Decorator to registre a task function.
    """
    environment.add_task(Task(func, subtask=False))
    return func


def subtask(func) -> Callable:
    """Decorator to registre a task function that
    runs in a new console in a secondary thread.
    """
    environment.add_task(Task(func, subtask=True))
    return func


def execute_task(task: Task, args: list) -> None:
    """Calls the tasj callback if the task is a normal task
    if the task is a subtask it opens a subprocess to run it
    in a new console in a secondary thread.
    """
    do.clear()\
        .log_print("Running task (%s%s%s)" % (Fore.MAGENTA, task.name, Fore.RESET))\
        .ignore_errors()
    
    if not task.subtask:
        task.callback(args)

    else:
        do.cd(environment.homepath)\
            .subprocess(f"python {sys.argv[0]} {task.namespace} {task.id}")

    if not do.keep_going:
        do.ignore_errors()\
            .log_print(Fore.RED + "Error running task (" + task.name + ")" + Fore.RESET)

    else:
        do.waifu_print(Fore.GREEN + "It's done oni-chan!" + Fore.RESET)

    do.wait()\
        .clear()


def run() -> None:
    """Main menu loop
    """
    if len(sys.argv) > 2:
        # we can indicate which task run by cli args
        namespace = sys.argv[1]
        task_id = sys.argv[2]

        if not environment.is_valid_namespace(namespace):
            do.waifu_print("Invalid namespace oni-chan :(")\
                .pause()
            
            return None
        
        if not task_id.isnumeric() or not environment.is_valid_task_id(namespace, int(task_id)):
            do.waifu_print("Invalid task_id oni-chan :(")\
                .pause()
            
            return None

        task = environment.get_task(namespace, int(task_id))

        task.callback([])

        if not do.keep_going:
            do.pause()

        return None

    namespace_id = _choose_namepace_id()
    namespace = environment.get_namespace_name(namespace_id)

    while True:
        do.clear()\
            .waifu_print("Showing tasks for %s%s%s oni-chan!" % (Fore.MAGENTA, namespace, Fore.RESET))

        for task in environment.get_tasks(namespace):
            print(" ~ id(%s%s%s) %s%s%s" % (Fore.GREEN, task.id, Fore.RESET, Fore.MAGENTA, task.name, Fore.RESET))

        print(" ~" + Fore.GREEN + " h/help <" + Fore.RESET + "task_number" + Fore.GREEN + ">" + Fore.RESET)
        print(" ~" + Fore.GREEN + " n/namespace" + Fore.RESET)
        print(" ~" + Fore.GREEN + " e/exit" + Fore.RESET)
        print("")

        task_command = input(" ~ command/task_id to execute: ")

        args = task_command.split(" ")
        task_id = args.pop(0)

        if task_id.isnumeric() and environment.is_valid_task_id(namespace, int(task_id)):
            execute_task(environment.get_task(namespace, int(task_id)), args)

        elif task_id == "help" or  task_id == "h":
            _command_help(namespace, args)

        elif task_id == "namespace" or task_id == "n":
            namespace_id = _choose_namepace_id()
            namespace = environment.get_namespace_name(namespace_id)

        elif task_id == "exit" or  task_id == "e":
            do.waifu_print("Good bye oni-chan!")
            break

        else:
            do.clear()\
                .waifu_print("%sInvalid command/task id :((%s" % (Fore.RED, Fore.RESET))\
                .pause()
