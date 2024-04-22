import sys
from src.ui_interface import *
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from src.functions import Func


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        #Use this if you only have one json file named "style.json" inside the root directory, "json" directory or "jsonstyles" folder.
        # loadJsonStyle(self, self.ui) 
        # Use this to specify your json file(s) path/name
        
        loadJsonStyle(self, self.ui, jsonFiles = {
            "json-styles/style.json"
            }) 
        self.show()
        self.ui.edit.hide()
        self.ui.delete_2.hide()
        self.func = Func(self.ui) 
        self.connection = False
        self.ui.csv.clicked.connect(self.func.csv)
        self.ui.doc.clicked.connect(self.func.doc)
        self.ui.pdf.clicked.connect(self.func.pdf)
        self.ui.excel.clicked.connect(self.func.excel)
        self.ui.choose_file.clicked.connect(self.func.get_database)
        self.ui.submit.clicked.connect(self.func.add)   
        self.ui.search.clicked.connect(self.func.search)
        
        self.ui.table.cellClicked.connect(self.button_visibility)

        ########################################################################
        # UPDATE APP SETTINGS LOADED FROM JSON STYLESHEET 
        # ITS IMPORTANT TO RUN THIS AFTER SHOWING THE WINDOW
        # THIS PROCESS WILL RUN ON A SEPARATE THREAD WHEN GENERATING NEW ICONS
        # TO PREVENT THE WINDOW FROM BEING UNRESPONSIVE
        ########################################################################
        # self = QMainWindow class
        QAppSettings.updateAppSettings(self)

        
    def button_visibility(self):
        selected_items = self.ui.table.selectedItems()
        if len(selected_items) == 0:
            self.ui.edit.hide()
            self.ui.delete_2.hide()
            if self.connection:
                self.ui.edit.clicked.disconnect()
                self.ui.delete_2.clicked.disconnect()
        if len(selected_items) == 1:
            self.ui.edit.show()
            self.ui.delete_2.show()  
            if not self.connection:
                self.ui.edit.clicked.connect(self.func.edit)
                self.ui.delete_2.clicked.connect(self.func.delete)
                self.connection = True

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
 
