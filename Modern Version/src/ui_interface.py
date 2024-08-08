from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import src._icons_rc
from Custom_Widgets.Widgets import (QCustomSlideMenu, QCustomStackedWidget)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(840, 515)
        MainWindow.setStyleSheet(u"QWidget *, QFrame *, QComboBox * {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	color: #fff;\n"
"	margin: 0;\n"
"}\n"
"\n"
"#centralwidget, #home, #mid, QLineEdit {\n"
"	background-color: #1b1b27;\n"
"}\n"
"\n"
"#header, #main_body {\n"
"	background-color: #1C2541;\n"
"}\n"
"\n"
"#user {\n"
"	border: 1px solid #5BC0BE;\n"
"	border-radius: 20px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"#submit, #add, #edit, #delete_2, #choose_file, #csv, #analysisButton, #excel, #pdf, #doc {\n"
"	background-color: #5BC0BE;\n"
"	border-radius: 10px;\n"
"}\n"
"	\n"
"QPushButton {\n"
"	text-align: left;\n"
"	padding: 3px 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"	border-top-left-radius: 10px;\n"
"}\n"
"\n"
"#home {\n"
"	border-left: 3px solid #5BC0BE;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QComboBox {\n"
"	background: #1b1b27;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #1b1b27; \n"
"}\n"
"\n"
"\n"
"\n"
""
                        "\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        
        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.menu = QPushButton(self.frame_2)
        self.menu.setObjectName(u"menu")
        self.menu.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        
        icon.addFile(u":/feather/icons/feather/align-justify.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu.setIcon(icon)
        self.menu.setIconSize(QSize(30, 30))
        self.horizontalLayout_4.addWidget(self.menu, 0, Qt.AlignLeft)
        self.app = QLabel(self.frame_2)
        self.app.setObjectName(u"app")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.app.setFont(font)
        self.horizontalLayout_4.addWidget(self.app)
        
        self.horizontalLayout.addWidget(self.frame_2, 0, Qt.AlignLeft)
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.search = QPushButton(self.frame)
        self.search.setObjectName(u"search")
        self.search.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        
        icon1.addFile(u":/feather/icons/feather/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search.setIcon(icon1)
        self.search.setIconSize(QSize(20, 20))
        self.horizontalLayout_2.addWidget(self.search)
        self.user = QPushButton(self.frame)
        self.user.setObjectName(u"user")
        self.user.setMinimumSize(QSize(42, 42))
        self.user.setMaximumSize(QSize(42, 42))
        font1 = QFont()
        font1.setPointSize(9)
        self.user.setFont(font1)
        self.user.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        
        icon2.addFile(u":/feather/icons/feather/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.user.setIcon(icon2)
        self.user.setIconSize(QSize(30, 30))
        self.horizontalLayout_2.addWidget(self.user)
        self.horizontalLayout.addWidget(self.frame, 0, Qt.AlignRight)
        self.verticalLayout.addWidget(self.header)
        self.main_body = QWidget(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy)
        self.main_body.setMinimumSize(QSize(800, 411))
        self.horizontalLayout_3 = QHBoxLayout(self.main_body)
        self.horizontalLayout_3.setSpacing(0)
        
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.left = QCustomSlideMenu(self.main_body)
        self.left.setObjectName(u"left")
        self.left.setMinimumSize(QSize(0, 0))
        self.left.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.left)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 10)
        
        self.widget = QWidget(self.left)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 0))
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 0, 0, 0)
        self.top = QFrame(self.widget)
        self.top.setObjectName(u"top")
        self.top.setFrameShape(QFrame.StyledPanel)
        self.top.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.top)
        self.verticalLayout_5.setSpacing(10)
        
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.home = QPushButton(self.top)
        self.home.setObjectName(u"home")
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(False)
        self.home.setFont(font2)
        self.home.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        
        icon3.addFile(u":/feather/icons/feather/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home.setIcon(icon3)
        self.home.setIconSize(QSize(25, 25))
        self.verticalLayout_5.addWidget(self.home)
        self.reports = QPushButton(self.top)
        self.reports.setObjectName(u"reports")
        font3 = QFont()
        font3.setPointSize(13)
        self.reports.setFont(font3)
        self.reports.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        
        icon4.addFile(u":/feather/icons/feather/printer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.reports.setIcon(icon4)
        self.reports.setIconSize(QSize(25, 25))
        self.verticalLayout_5.addWidget(self.reports)
        self.accounts = QPushButton(self.top)
        self.accounts.setObjectName(u"accounts")
        self.accounts.setFont(font3)
        self.accounts.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        
        icon5.addFile(u":/feather/icons/feather/database.png", QSize(), QIcon.Normal, QIcon.Off)
        self.accounts.setIcon(icon5)
        self.accounts.setIconSize(QSize(25, 25))
        self.verticalLayout_5.addWidget(self.accounts)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.verticalLayout_5.addItem(self.verticalSpacer)
        self.verticalLayout_4.addWidget(self.top)
        self.down = QFrame(self.widget)
        self.down.setObjectName(u"down")
        
        self.down.setFrameShape(QFrame.StyledPanel)
        self.down.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.down)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.settings = QPushButton(self.down)
        self.settings.setObjectName(u"settings")
        self.settings.setFont(font3)
        self.settings.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        
        icon6.addFile(u":/feather/icons/feather/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings.setIcon(icon6)
        self.settings.setIconSize(QSize(25, 25))
        self.verticalLayout_6.addWidget(self.settings)
        self.help = QPushButton(self.down)
        self.help.setObjectName(u"help")
        self.help.setFont(font3)
        self.help.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        
        icon7.addFile(u":/feather/icons/feather/help-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.help.setIcon(icon7)
        self.help.setIconSize(QSize(25, 25))
        self.verticalLayout_6.addWidget(self.help)
        self.about = QPushButton(self.down)
        self.about.setObjectName(u"about")
        self.about.setFont(font3)
        self.about.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        
        icon8.addFile(u":/feather/icons/feather/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.about.setIcon(icon8)
        self.about.setIconSize(QSize(25, 25))
        self.verticalLayout_6.addWidget(self.about)
        self.verticalLayout_4.addWidget(self.down)
        self.verticalLayout_3.addWidget(self.widget)
        self.horizontalLayout_3.addWidget(self.left)
        self.mid = QWidget(self.main_body)
        self.mid.setObjectName(u"mid")
        self.verticalLayout_2 = QVBoxLayout(self.mid)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QCustomStackedWidget(self.mid)
        self.stackedWidget.setObjectName(u"stackedWidget")
        
        font4 = QFont()
        font4.setBold(False)
        self.stackedWidget.setFont(font4)
        self.stackedWidget.setAcceptDrops(False)
        self.stackedWidget.setAutoFillBackground(False)
        self.homep = QWidget()
        self.homep.setObjectName(u"homep")
        self.verticalLayout_10 = QVBoxLayout(self.homep)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_3 = QWidget(self.homep)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_11 = QVBoxLayout(self.widget_3)
        self.verticalLayout_11.setSpacing(0)
        
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.widget_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        self.label.setFont(font5)
        
        self.horizontalLayout_7.addWidget(self.label, 0, Qt.AlignLeft|Qt.AlignTop)
        self.add = QPushButton(self.frame_4)
        self.add.setObjectName(u"add")
        font6 = QFont()
        font6.setPointSize(10)
        self.add.setFont(font6)
        self.add.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalLayout_7.addWidget(self.add, 0, Qt.AlignRight|Qt.AlignTop)
        self.verticalLayout_11.addWidget(self.frame_4, 0, Qt.AlignTop)
        self.table = QTableWidget(self.widget_3)
        if (self.table.columnCount() < 5):
            self.table.setColumnCount(5)
            
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        
        self.table.setObjectName(u"table")
        self.table.setFont(font1)
        self.table.verticalHeader().setDefaultSectionSize(30)
        self.verticalLayout_11.addWidget(self.table)
        self.frame_5 = QFrame(self.widget_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.total = QLabel(self.frame_5)
        self.total.setObjectName(u"total")
        
        font7 = QFont()
        font7.setPointSize(11)
        font7.setBold(False)
        self.total.setFont(font7)
        self.horizontalLayout_8.addWidget(self.total)
        self.edit = QPushButton(self.frame_5)
        self.edit.setObjectName(u"edit")
        self.edit.setMinimumSize(QSize(0, 0))
        self.edit.setFont(font6)
        self.edit.setCursor(QCursor(Qt.PointingHandCursor))
        self.edit.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_8.addWidget(self.edit, 0, Qt.AlignRight)
        self.delete_2 = QPushButton(self.frame_5)
        self.delete_2.setObjectName(u"delete_2")
        self.delete_2.setMinimumSize(QSize(0, 0))
        self.delete_2.setFont(font6)
        
        self.delete_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_2.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_8.addWidget(self.delete_2, 0, Qt.AlignRight)
        self.verticalLayout_11.addWidget(self.frame_5, 0, Qt.AlignBottom)
        self.verticalLayout_10.addWidget(self.widget_3)
        self.stackedWidget.addWidget(self.homep)
        
        self.reportp = QWidget()
        self.reportp.setObjectName(u"reportp")
        self.frame_6 = QFrame(self.reportp)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 350))
        self.frame_6.setGeometry(QRect(29, 29, 291, 231))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_6)
        self.verticalLayout_12.setSpacing(20)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.report_info = QLabel(self.frame_6)
        self.report_info.setObjectName(u"report_info")
        self.analysis = QLabel(self.frame_6)
        self.analysis.setObjectName(u"analysis")
        
        font8 = QFont()
        font8.setPointSize(14)
        font8.setBold(True)
        self.report_info.setFont(font8)
        self.analysis.setFont(font8)       
        self.verticalLayout_12.addWidget(self.report_info, 0, Qt.AlignTop)
        self.csv = QPushButton(self.frame_6)
        self.csv.setObjectName(u"csv")
        font9 = QFont()
        font9.setPointSize(12)
        self.csv.setFont(font9)
        
        self.csv.setCursor(QCursor(Qt.PointingHandCursor))
        self.verticalLayout_12.addWidget(self.csv)
        self.excel = QPushButton(self.frame_6)
        self.excel.setObjectName(u"excel")
        self.excel.setFont(font9)
        self.excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.verticalLayout_12.addWidget(self.excel)
        self.pdf = QPushButton(self.frame_6)
        self.pdf.setObjectName(u"pdf")
        self.pdf.setFont(font9)
        self.pdf.setCursor(QCursor(Qt.PointingHandCursor))
        self.verticalLayout_12.addWidget(self.pdf)
        self.doc = QPushButton(self.frame_6)
        self.doc.setObjectName(u"doc")
        self.doc.setFont(font9)
        self.doc.setCursor(QCursor(Qt.PointingHandCursor))
        
        self.verticalLayout_12.addWidget(self.doc)
        self.verticalLayout_12.addWidget(self.analysis, 0, Qt.AlignBottom)
        self.analysisButton = QPushButton(self.frame_6)
        self.analysisButton.setObjectName(u"analysisButton")
        self.analysisButton.setFont(font9)
        self.analysisButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.verticalLayout_12.addWidget(self.analysisButton)    
        self.stackedWidget.addWidget(self.reportp)
        self.accountp = QWidget()
        
        self.accountp.setObjectName(u"accountp")
        self.horizontalLayout_9 = QHBoxLayout(self.accountp)
        self.horizontalLayout_9.setSpacing(50)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(20, 0, 0, 0)
        self.label_2 = QLabel(self.accountp)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font8)
        self.label_2.setWordWrap(True)
        self.horizontalLayout_9.addWidget(self.label_2)
        self.choose_file = QPushButton(self.accountp)
        self.choose_file.setObjectName(u"choose_file")
        self.choose_file.setFont(font9)
        self.choose_file.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalLayout_9.addWidget(self.choose_file, 0, Qt.AlignLeft)

        self.stackedWidget.addWidget(self.accountp)
        self.settingsp = QWidget()
        self.settingsp.setObjectName(u"settingsp")
        self.setting_info = QLabel(self.settingsp)
        self.setting_info.setObjectName(u"setting_info")
        self.setting_info.setGeometry(QRect(20, 70, 361, 281))
        self.setting_info.setFont(font8)
        self.setting_info.setAlignment(Qt.AlignCenter)
        self.setting_info.setWordWrap(True)
        self.stackedWidget.addWidget(self.settingsp)
        self.helpp = QWidget()
        self.helpp.setObjectName(u"helpp")
        
        self.horizontalLayout_6 = QHBoxLayout(self.helpp)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.help_info = QLabel(self.helpp)
        self.help_info.setObjectName(u"help_info")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.help_info.sizePolicy().hasHeightForWidth())
        self.help_info.setSizePolicy(sizePolicy1)
        font10 = QFont()
        font10.setPointSize(14)
        font10.setBold(False)
        
        font10.setStyleStrategy(QFont.PreferDefault)
        self.help_info.setFont(font10)
        self.help_info.setTabletTracking(False)
        self.help_info.setFocusPolicy(Qt.NoFocus)
        self.help_info.setAcceptDrops(False)
        self.help_info.setLayoutDirection(Qt.LeftToRight)
        self.help_info.setAutoFillBackground(False)
        self.help_info.setFrameShape(QFrame.NoFrame)
        self.help_info.setTextFormat(Qt.MarkdownText)
        self.help_info.setScaledContents(False)
        self.help_info.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.help_info.setWordWrap(True)
        self.help_info.setMargin(-1)
        self.help_info.setOpenExternalLinks(True)
        self.help_info.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.horizontalLayout_6.addWidget(self.help_info)

        self.stackedWidget.addWidget(self.helpp)
        self.aboutp = QWidget()
        self.aboutp.setObjectName(u"aboutp")
        self.horizontalLayout_5 = QHBoxLayout(self.aboutp)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.about_info = QLabel(self.aboutp)
        self.about_info.setObjectName(u"about_info")
        sizePolicy1.setHeightForWidth(self.about_info.sizePolicy().hasHeightForWidth())
        self.about_info.setSizePolicy(sizePolicy1)
        font11 = QFont()
        font11.setPointSize(14)
        font11.setBold(False)
        
        self.about_info.setFont(font11)
        self.about_info.setCursor(QCursor(Qt.ArrowCursor))
        self.about_info.setLayoutDirection(Qt.LeftToRight)
        self.about_info.setAutoFillBackground(False)
        self.about_info.setTextFormat(Qt.MarkdownText)
        self.about_info.setScaledContents(False)
        self.about_info.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.about_info.setWordWrap(True)
        self.about_info.setMargin(-1)
        self.about_info.setOpenExternalLinks(True)
        
        self.about_info.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.horizontalLayout_5.addWidget(self.about_info)
        self.stackedWidget.addWidget(self.aboutp)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout_3.addWidget(self.mid)
        self.right = QCustomSlideMenu(self.main_body)
        self.right.setObjectName(u"right")
        self.right.setMinimumSize(QSize(250, 0))
        self.verticalLayout_7 = QVBoxLayout(self.right)
        self.verticalLayout_7.setSpacing(0)
        
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.right)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(210, 353))
        self.verticalLayout_8 = QVBoxLayout(self.widget_2)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.icon_add = QLabel(self.widget_2)
        self.icon_add.setObjectName(u"icon_add")
        self.icon_add.setMinimumSize(QSize(70, 70))
        self.icon_add.setMaximumSize(QSize(70, 70))
        
        self.icon_add.setPixmap(QPixmap(u":/feather/icons/feather/edit.png"))
        self.icon_add.setScaledContents(True)
        self.verticalLayout_8.addWidget(self.icon_add, 0, Qt.AlignHCenter)
        self.frame_3 = QFrame(self.widget_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 10, 0, 10)
        self.id = QLineEdit(self.frame_3)
        self.id.setObjectName(u"id")
        
        self.id.setMinimumSize(QSize(210, 35))
        font12 = QFont()
        font12.setPointSize(11)
        self.id.setFont(font12)
        self.verticalLayout_9.addWidget(self.id)
        self.name = QLineEdit(self.frame_3)
        self.name.setObjectName(u"name")
        self.name.setMinimumSize(QSize(210, 35))
        self.name.setFont(font12)
        self.verticalLayout_9.addWidget(self.name)
        self.course = QComboBox(self.frame_3)
        
        self.course.addItem("")
        self.course.addItem("")
        self.course.addItem("")
        self.course.addItem("")
        self.course.addItem("")
        self.course.addItem("")
        self.course.addItem("")
        self.course.addItem("")
        
        self.course.setObjectName(u"course")
        self.course.setMinimumSize(QSize(210, 35))
        self.course.setFont(font12)
        self.verticalLayout_9.addWidget(self.course)
        self.contact = QLineEdit(self.frame_3)
        self.contact.setObjectName(u"contact")
        self.contact.setMinimumSize(QSize(210, 35))
        self.contact.setFont(font12)
        self.verticalLayout_9.addWidget(self.contact)
        self.note = QLineEdit(self.frame_3)
        self.note.setObjectName(u"note")
        self.note.setMinimumSize(QSize(210, 35))
        self.note.setFont(font12)
        
        self.verticalLayout_9.addWidget(self.note)
        self.verticalLayout_8.addWidget(self.frame_3)
        self.submit = QPushButton(self.widget_2)
        self.submit.setObjectName(u"submit")
        font13 = QFont()
        font13.setPointSize(12)
        font13.setBold(False)
        font13.setItalic(False)
        self.submit.setFont(font13)
        self.submit.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.submit, 0, Qt.AlignHCenter)
        self.verticalLayout_7.addWidget(self.widget_2, 0, Qt.AlignHCenter|Qt.AlignTop)
        self.horizontalLayout_3.addWidget(self.right)
        self.verticalLayout.addWidget(self.main_body)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu.setText("")
        self.app.setText(QCoreApplication.translate("MainWindow", u"Student Management Application", None))
        self.search.setText("")
        self.user.setText("")
        
        self.home.setText(QCoreApplication.translate("MainWindow", u"  Home", None))
        self.reports.setText(QCoreApplication.translate("MainWindow", u"  Reports", None))
        self.accounts.setText(QCoreApplication.translate("MainWindow", u"  Database", None))
        self.settings.setText(QCoreApplication.translate("MainWindow", u"  Settings", None))
        self.help.setText(QCoreApplication.translate("MainWindow", u"  Help", None))
        self.about.setText(QCoreApplication.translate("MainWindow", u"  About", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Home Page", None))
        self.add.setText(QCoreApplication.translate("MainWindow", u"Add Student", None))
        
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Course", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Contact Info", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        
        for column in range(self.table.columnCount()):
            header_item = self.table.horizontalHeaderItem(column)
            header_font = QFont("Arial", 12)  # You can set your desired font family and size here
            header_item.setFont(header_font)       
        
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Note", None));
        self.total.setText(QCoreApplication.translate("MainWindow", u"Total: ", None))
        self.edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.delete_2.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.report_info.setText(QCoreApplication.translate("MainWindow", u"Save your data to a file", None))
        self.csv.setText(QCoreApplication.translate("MainWindow", u"Save to CSV", None))
        self.excel.setText(QCoreApplication.translate("MainWindow", u"Save to Excel Spreadsheet", None))
        self.pdf.setText(QCoreApplication.translate("MainWindow", u"Save to PDF", None))
        self.doc.setText(QCoreApplication.translate("MainWindow", u"Save to Doc", None))
        self.analysisButton.setText(QCoreApplication.translate("MainWindow", u"Bases on Courses", None))
        
        self.analysis.setText(QCoreApplication.translate("MainWindow", u"Generate data visualization\n(function not finish)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Select Database File to Load in Home Page", None))
        self.choose_file.setText(QCoreApplication.translate("MainWindow", u"Choose File", None))
        self.setting_info.setText(QCoreApplication.translate("MainWindow", u"Nothing here, I add Settings for visual appealing", None))
        self.help_info.setText(QCoreApplication.translate("MainWindow", u"To reduce the size of this app, tutorial about how to use this app is on my Github:\n"
"\n"
"https://github.com/KlausJackson/Student-Management-System/tree/main/Tutorial%20Videos", None))
        self.about_info.setText(QCoreApplication.translate("MainWindow", u"Author: Klaus Jackson\n"
"\n"
"My Github: https://github.com/KlausJackson\n"
"\n"
"My LinkedIn: https://www.linkedin.com/in/klausjackson\n"
"\n"
"My Upwork: https://www.upwork.com/freelancers/~01f978d2d010b8b6c7\n"
"\n"
"The process of making this app is inspired by: Ardit Sulce and Khamisi Kibet.\n"
"\n"
"MIT Lisence", None))
        self.icon_add.setText("")
        self.id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.course.setItemText(0, QCoreApplication.translate("MainWindow", u"Mathematics", None))
        self.course.setItemText(1, QCoreApplication.translate("MainWindow", u"Chemistry", None))
        self.course.setItemText(2, QCoreApplication.translate("MainWindow", u"History", None))
        self.course.setItemText(3, QCoreApplication.translate("MainWindow", u"Physics", None))
        self.course.setItemText(4, QCoreApplication.translate("MainWindow", u"English", None))
        self.course.setItemText(5, QCoreApplication.translate("MainWindow", u"Literature/Literacy", None))
        self.course.setItemText(6, QCoreApplication.translate("MainWindow", u"Biology", None))
        self.course.setItemText(7, QCoreApplication.translate("MainWindow", u"Geography", None))
        self.course.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Course", None))
        self.contact.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contact Infos", None))
        self.note.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Note", None))
        self.submit.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
    # retranslateUi

