from RunPromptWrapper.RunPromptWrapper import RunPromptWrapper
from WinSwitcher.Window import Window

import subprocess
import re


class SwitcherMenu(RunPromptWrapper):
    def __init__(self, run_prompt_cmd):
        super().__init__(run_prompt_cmd)
        self.generateMenuEntries()

    def getWindowList(self):
        return subprocess.run("wmctrl -p -l", shell=True,
                              capture_output=True, text=True).stdout.split('\n')

    def generateMenuEntries(self):
        p = re.compile("SP-*")
        for window in self.getWindowList():
            window = window.split(" ")
            if (window and len(window) > 1):
                id = window[0]
                pid = window[3]
                win_name = " ".join(window[6:])

                if re.match(p, win_name):
                    continue

                self.addMenuEntry(Window(id, win_name, pid))

    def _generateExecStr(self):
        exec_string = ""
        for entry in self.menu_entries:
            if (entry.isVisible()):
                exec_string += (f"{entry.getLabel()}\n")

        return exec_string
