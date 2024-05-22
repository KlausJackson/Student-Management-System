# Student-Management-System
[![Python version](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://shields.io/) 
![License](https://img.shields.io/badge/License-MIT-blue.svg)
[![GitHub top language](https://img.shields.io/github/languages/top/KlausJackson/Student-Management-System?logo=github)](https://github.com/KlausJackson/Student-Management-System) 
[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/KlausJackson/Student-Management-System?logo=github)](https://github.com/KlausJackson/Student-Management-System) 
[![GitHub issues](https://img.shields.io/github/issues/KlausJackson/Student-Management-System?logo=github)](https://github.com/KlausJackson/Student-Management-System)
[![GitHub issues](https://img.shields.io/github/issues-closed/KlausJackson/Student-Management-System?logo=github)](https://github.com/KlausJackson/Student-Management-System)
[![GitHub issues](https://img.shields.io/github/issues-pr/KlausJackson/Student-Management-System?logo=github)](https://github.com/KlausJackson/Student-Management-System)
[![GitHub issues](https://img.shields.io/github/issues-pr-closed/KlausJackson/Student-Management-System?logo=github)](https://github.com/KlausJackson/Student-Management-System)

![](https://img.shields.io/github/forks/KlausJackson/DataStructures_Algorithms.svg)
![](https://img.shields.io/github/stars/KlausJackson/DataStructures_Algorithms.svg)
![](https://img.shields.io/github/watchers/KlausJackson/DataStructures_Algorithms.svg)

A user-friendly GUI application designed to manage student records using SQLite database integration and Qt Designer. <br>

## How To Contact Me
[![Patreon](https://img.shields.io/badge/Patreon-AC7AC2?style=for-the-badge&logo=patreon&logoColor=white)](patreon.com/KlausJackson)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/KlausJackson/) 
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:KlausJackson2@gmail.com)
[![Steam](https://img.shields.io/badge/Steam-000050?style=for-the-badge&logo=steam&logoColor=white)](https://steamcommunity.com/id/KlausJackson/)
[![Twitter](https://img.shields.io/badge/Twitter-0044BB?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/Klaus_Jackson2)

## Preview

### Basic Version
This is a short clip showing you how to add a student in the Basic Version and what information a student would have in this database. Some information can't be leave blank like Name and ID. <br>
I have many other tutorial videos on how to use the Basic Version in the [Tutorial Videos](Tutorial%20Videos) directory. <br>

**NOTE**: Ignore the dark theme in this short clip of the Basic Version, it won't look like that when you download the code to your computer, unless you have installed a dark theme using ThemeTool. It would be a light theme like many other applications.

![Tutorial Video](Add-Student.gif)

### Modern Version
This is a short clip of the Modern Version, similar to Basic Version, but with modern-looking GUI, very easy to use. <br>

![Tutorial Video](Modern-Version.gif)

This version is made with Qt Designer (generates .ui files), PySide6 and Custom_Widgets by Khamisi Kibet. <br>

**NOTE**: Dark theme is the default theme of this version. 

## Overview
Intuitive Interface: Student Manager boasts a clean and intuitive graphical user interface, making it accessible for users of all levels of technical proficiency. <br>

Comprehensive Student Profiles: Each student record includes essential information such as student ID, name, course details, contact information, and additional notes, ensuring all pertinent details are easily accessible and organized. <br>

Effortless Data Management: With the ability to add, delete, and edit student records, Student Manager simplifies the process of keeping your database up-to-date and accurate. The database file is saved locally so you don't need internet connection to access it. <br>

Advanced Search Functionality: Quickly find specific student records using the search feature, allowing you to locate information with precision and ease. <br>

Export Options: Student Manager offers versatile export capabilities, allowing you to convert your SQLite database to various formats including Word, Excel, PDF, and CSV. Whether you need to create reports, share information, or integrate data into other systems, Student Manager ensures compatibility and flexibility. <br>


## Requirements & Usage
* General requirements:
  - Python 3.8 or higher
  - sqlite3 (Python's default library)
  - pandas (Python's default library)
  - docx 
  - reportlab
  - openpyxl
<br>

* Specific requirements for Basic Version: PyQt6 <br>
```
pip install -r requirements-B.txt
```

* Specific requirements for Modern Version:
  - PySide6 (you can still use PyQt if you don't want to install PySide6, just change the imports in each file)
  - [GTK+ for Windows Runtime Environment](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases/download/2022-01-04/gtk3-runtime-3.24.31-2022-01-04-ts-win64.exe) (to use Custom_Widgets on Windows)
  - Custom_Widgets (`pip install QT-PyQt-PySide-Custom-Widgets` then add `Scripts` directory to the system environment path, you probably know how to do this or just Google it). <br>
  ```
  pip install -r requirements-B.txt
  ```

* Usage: Open the terminal and type `python3 main.py` for Modern Version, `python3 SMS.py` for Basic Version.

## Note
If you're interested in learning how to use QT Designer and Custom-Widgets library, you can check out Khamisi Kibet for reference. <br>

Khamisi Kibet's Github: https://github.com/KhamisiKibet <br>
Custom-Widgets's repo: https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets <br>
Custom-Widgets's Documentation: https://khamisikibet.github.io/Docs-QT-PyQt-PySide-Custom-Widgets/ <br>
Khamisi Kibet's YouTube channel: https://www.youtube.com/@SpinnTV <br>

He posts a lot of helpful tutorials about making modern-looking desktop application using QT Designer, Python and Custom-Widgets. <br>

## The End
This is only a basic and user-friendly GUI application that interact with the database file stored locally in your computer. <br>

I would've done a MySQL version but I didn't want to.
Please file an issue if there's any problem with the code. <br>

The process of making this application is inspired by: Ardit Sulce. <br>
The process of making the Modern Version is inspired by: Khamisi Kibet <br>
