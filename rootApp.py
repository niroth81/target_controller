
import sys
from PyQt5 import QtWidgets
from scripts.mainMenuProgram import mainMenu


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = mainMenu()
    application.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
