from WinSwitcher.SwitcherMenu import SwitcherMenu

if __name__ == "__main__":
    s = SwitcherMenu("dmenu -c -i -bw 1 -l 10 -p 'Select a Window'")
    s.start()
