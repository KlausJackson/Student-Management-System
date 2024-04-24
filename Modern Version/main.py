import sys
from src.ui_interface import *
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from src.functions import Func



# This is to merge all _icons_rc_{}.py files together into one file named _icons_rc.py
# Because I can't upload the entire _icons_rc.py to my repo, it's too big.
# I can't use Git at the moment because I'm not near my PC and I just want get 
# this shit down fast so I can move on to a new personal project.
import os.path

if os.path.isfile('src/_icons_rc.py'):
    import src.merge as merge
    input_prefix = "_icons_rc"  # Prefix of the input files
    output_file = "_icons_rc.py"  # Name of the merged output file
    merge.merge_files(input_prefix, output_file)
else:
    print(f"{output_file} has already existed.")
    print("you can now delete these lines in main.py from line 9 to line 26.")
    
# You can also use `pyside6-rcc _icons_rc.qrc -o _icons_rc.py` instead. 
# Remember to have PySide 6 installed and script directory included in the 
# system environment path to be able to use PySide6 commands.



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        # Use this if you only have one json file named "style.json" inside
        # the root directory, "json" directory or "jsonstyles" folder.
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
 
