
import argparse
import sys
import os
from PySide2.QtWidgets import QApplication

import mdpertool


def run_mdpertool():
    print("===== GUI APP WILL COME HERE =====")

    if os.name == 'nt':
        print("PLATFORM IS WINDOWS ..")
        import PySide2
        pyqt = os.path.dirname(PySide2.__file__)
        QApplication.addLibraryPath(os.path.join(pyqt, "plugins"))

    parser = argparse.ArgumentParser(description="GUI APP WILL COME HERE")
    parser.add_argument("-gui", "--show_gui", action='store_true')
    parser.add_argument("-cli", "--commandline", action='store_true')
    args = parser.parse_args()

    if args.show_gui:
        mdpertool.run_gui()

    if args.commandline:
        pass

    else:
        sys.exit()

# if __name__ == '__main__':
#
