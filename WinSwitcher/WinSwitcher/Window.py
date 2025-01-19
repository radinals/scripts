from RunPromptWrapper.MenuEntry import MenuEntry

import subprocess


class Window(MenuEntry):
    def __init__(self, win_id, win_name, pid):
        super().__init__(win_name)
        self.win_id = win_id
        self.pid = pid

    def getWinID(self):
        return self.win_id

    def _getCMDName(self):
        return subprocess.run(f"ps -h -p {self.pid} -o cmd", shell=True, capture_output=True, text=True).stdout.split('\n')[0]

    def getLabel(self):
        return f"({self._getCMDName()}) {self.label}"

    def onSelected(self):
        subprocess.run(f"wmctrl -i -a {self.win_id}", shell=True)
