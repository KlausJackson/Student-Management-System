from PyQt6.QtWidgets import (QLineEdit, QMessageBox, QPushButton, QLabel, QDialog, 
                             QVBoxLayout, QComboBox, QGridLayout)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import pyqtSignal, Qt
import sqlite3


class InsertDialog(QDialog):
    def __init__(self, sms):
        super().__init__()
        self.setWindowTitle("Add Student")
        self.setWindowIcon(QIcon("icons/logo.png"))       
        self.setFixedHeight(250)
        self.setFixedWidth(370)
        self.sms = sms        
        
        layout = QVBoxLayout()
        self.id = QLineEdit()
        self.id.setPlaceholderText("ID")
        layout.addWidget(self.id)
        
        self.name = QLineEdit() 
        self.name.setPlaceholderText("Name")
        layout.addWidget(self.name)
        
        self.course = QComboBox() 
        courses = ["Biology", "Math", "Physics", "Literature", "English", "History", "Geography", "Chemistry"]
        self.course.addItems(courses)
        layout.addWidget(self.course)
        
        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText("Phone Number, Email, etc.")
        layout.addWidget(self.mobile)
        
        self.note = QLineEdit()
        self.note.setPlaceholderText("Note")
        layout.addWidget(self.note)
        
        button = QPushButton("Submit")
        button.clicked.connect(self.add_student)
        layout.addWidget(button)
        self.setLayout(layout)
        
        
    def add_student(self):
        id, name = self.id.text(), self.name.text() 
        if name == "" or id == "":
            message = QMessageBox()
            message.setWindowTitle("ERROR")
            message.setWindowIcon(QIcon("icons/logo.png"))
            message.setText("Name or ID cannot be empty.")
            message.exec()
            return
        course, mobile, note = self.course.itemText(self.course.currentIndex()), self.mobile.text(), self.note.text()
        connection = sqlite3.connect("database.db")    
        cursor = connection.cursor()
        cursor.execute("INSERT INTO student (id, name, course, mobile, note) VALUES (?, ?, ?, ?, ?)", 
                       (id, name, course, mobile, note))
        
        connection.commit()
        cursor.close()
        connection.close()
        self.sms.load_data()
        self.id.clear()
        self.name.clear()
        self.mobile.clear()
        self.note.clear()  
         
 
class FindDialog(QDialog):
    search_result = pyqtSignal(list)
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Find Student")
        self.setWindowIcon(QIcon("icons/logo.png"))
        self.setFixedHeight(100)
        self.setFixedWidth(370)
        self.result = 0
        
        layout = QVBoxLayout()
        self.find = QLineEdit()
        self.find.setPlaceholderText("ID, Name, Course, Contact Info, Note")
        self.find.textChanged.connect(self.search)
        layout.addWidget(self.find)
        
        self.report = QLabel(f"{self.result} matched.")
        layout.addWidget(self.report)        
        self.setLayout(layout)        

    def search(self):
        info = self.find.text()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        rows = list(cursor.execute("SELECT * FROM student WHERE name LIKE ? OR id LIKE ? OR course LIKE ? OR mobile LIKE ? OR note LIKE ?"
                                   , ('%' + info + '%', '%' + info + '%', '%' + info + '%', '%' + info + '%', '%' + info + '%')))
        self.result = len(rows)
        self.report.setText(f"{self.result} matched.")
        self.search_result.emit(rows)
        
                    
class EditDialog(QDialog):
    def __init__(self, sms):
        super().__init__()                    
        self.setWindowTitle("Edit Student Data")
        self.setWindowIcon(QIcon("icons/logo.png"))       
        self.setFixedHeight(250)
        self.setFixedWidth(370)
        self.sms = sms
        
        i = self.sms.table.currentRow()
        name = self.sms.table.item(i, 1).text()            
        id = self.sms.table.item(i, 0).text()
        self.original_id = id
        mobile = self.sms.table.item(i, 3).text()                        
        course = self.sms.table.item(i, 2).text()
        note = self.sms.table.item(i, 4).text()
                    
        layout = QVBoxLayout()
        self.id = QLineEdit(id)
        self.id.setPlaceholderText("ID")
        layout.addWidget(self.id)
        
        self.name = QLineEdit(name) 
        self.name.setPlaceholderText("Name")
        layout.addWidget(self.name)
        
        self.course = QComboBox() 
        courses = ["Biology", "Math", "Physics", "Literature", "English", "History", "Geography", "Chemistry"]
        self.course.addItems(courses)
        self.course.setCurrentText(course)
        layout.addWidget(self.course)
        
        self.mobile = QLineEdit(mobile)
        self.mobile.setPlaceholderText("Phone Number, Email, etc.")
        layout.addWidget(self.mobile)
        
        self.note = QLineEdit(note)
        self.note.setPlaceholderText("Note")
        layout.addWidget(self.note)
        
        button = QPushButton("Update")
        button.clicked.connect(self.update)
        layout.addWidget(button)
        self.setLayout(layout)
        
    def update(self):
        id, name, course, mobile = self.id.text(), self.name.text(), self.course.currentText(), self.mobile.text()
        note = self.note.text()
        if name == "" or id == "":
            message = QMessageBox()
            message.setWindowTitle("ERROR")
            message.setWindowIcon(QIcon("icons/logo.png"))
            message.setText("Name or ID cannot be empty.")
            message.exec()
            return        
        
        connection = sqlite3.connect("database.db")                    
        cursor = connection.cursor()    
        cursor.execute("UPDATE student SET id = ?, name = ?, course = ?, mobile = ?, note = ? WHERE id = ?",
                       (id, name, course, mobile, note, self.original_id))    
        connection.commit()
        cursor.close()    
        connection.close()
        self.sms.load_data()
                    
class DeleteDialog(QDialog):
    def __init__(self, sms):
        super().__init__()                    
        self.setWindowTitle("Delete Student Data")
        self.setWindowIcon(QIcon("icons/logo.png"))       
        self.setFixedHeight(100)
        self.setFixedWidth(400)
        self.sms = sms                             
                    
        layout = QGridLayout()
        message = QLabel("Delete this student? This action cannot be reversed.")    
        y, n = QPushButton("Yes"), QPushButton("No")
        layout.addWidget(message, 0, 0, 1, 2)
        layout.addWidget(y, 1, 0)
        layout.addWidget(n, 1, 1)   
        self.setLayout(layout)
        y.clicked.connect(self.delete)
        n.clicked.connect(self.shut_down)
    
    def shut_down(self):
        self.close()    
                
                    
    def delete(self):
        i = self.sms.table.currentRow()                
        name = self.sms.table.item(i, 1).text()            
        connection = sqlite3.connect("database.db")            
        cursor = connection.cursor()
        cursor.execute("DELETE FROM student WHERE name = ?", (name, ))
        connection.commit()
        cursor.close()
        connection.close()
        self.sms.load_data()
        self.close()
        message = QMessageBox()
        message.setWindowTitle("Action Made")
        message.setWindowIcon(QIcon("icons/logo.png"))
        message.setText(f"{name} has been delete from the database.")
        message.exec()
                    
class AboutDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edit Student Data")
        self.setWindowIcon(QIcon("icons/logo.png"))          
        content = """
Author: Klaus Jackson
My Github: https://github.com/KlausJackson
My LinkedIn: https://www.linkedin.com/in/klausjackson
My Upwork: https://www.upwork.com/freelancers/~01f978d2d010b8b6c7
You can find other ways to contact me on my Github page.

The process of making this app is inspired by: Ardit Sulce.

MIT Lisence
        """               
        self.setText(content)           
        self.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)            
                    