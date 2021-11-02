import time
from re import sub
from praw.reddit import Comment, Submission
from praw.models import MoreComments
import requests, shutil, praw, os, datetime, json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QWidget, QPushButton, QVBoxLayout

reddit = praw.Reddit(

)

print(reddit.user.me())

# Made with PyQt5 Designer
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 520)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(650, 20, 555, 415))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_13.setObjectName("label_13")
        self.label_13.setFont(font)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.move(0, 250)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_14.setObjectName("label_14")
        self.label_14.move(0, 50)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_15.setObjectName("label_15")
        self.label_15.move(0, 100)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.move(75, 97)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_16.setObjectName("label_16")
        self.label_16.move(0, 130)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.move(75, 127)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_17.setObjectName("label_17")
        self.label_17.move(0, 180)
        self.textEdit_2 = QtWidgets.QTextEdit(self.verticalLayoutWidget_4)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.move(75, 160)
        self.textEdit_2.resize(150,50)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 70, 254, 414))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_4 = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout.addWidget(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout.addWidget(self.checkBox_6)
        self.checkBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_7 = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout.addWidget(self.checkBox_7)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.spinBox_2 = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_2.addWidget(self.spinBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.comboBox.setObjectName("comboBox")
        icon = QtGui.QIcon.fromTheme("ed")
        self.comboBox.addItem(icon, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(3, "")
        self.verticalLayout.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton.setEnabled(True)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(280, -30, 61, 791))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(600, -30, 61, 791))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(340, 10, 261, 305))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setMinimumSize(QtCore.QSize(0, 55))
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_5.addWidget(self.label_10)
        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_5.addWidget(self.textEdit)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_6.addWidget(self.label_11)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_6.addWidget(self.lineEdit_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_6)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(60, 20, 181, 41))
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.ok_clicked)
        self.pushButton_2.clicked.connect(self.run_post_bot)
        self.pushButton_3.clicked.connect(self.comment_bot)
        self.ww = Warning()
    
    def comment_bot(self):
        print("Bot is running...")
        sys.stdout.flush()
        while True:
            url = self.lineEdit_6.text()
            submission = reddit.submission(url=url)
            for top_level_comment in submission.comments:
                if isinstance(top_level_comment, MoreComments):
                    continue
                if top_level_comment.body == self.lineEdit_7.text():
                    comment_to_reply = reddit.comment(id=str(top_level_comment.id))
                    try:
                        comment_to_reply.reply(self.textEdit_2.toPlainText())
                    except:
                        print("Bot cannot reply here!")
                        sys.stdout.flush()
                time.sleep(2)


    def ok_clicked(self):
        self.ww.show()

    def run_post_bot(self):
        questions = self.textEdit.toPlainText().split(".")
        print("Bot is running...")
        sys.stdout.flush()

        subreddit = reddit.subreddit(self.lineEdit_2.text().lower())
        try:
            for submission in subreddit.stream.submissions():
                s_title = submission.title.lower()
                for question_phrase in questions:
                    if question_phrase in s_title:
                        submission.reply(self.lineEdit_3.text())
                        break
        except:
            print("SubReddit dosent exist!")
            sys.stdout.flush()
            self.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Enter a subreddit you want to pull information from. "))
        self.label_3.setText(_translate("MainWindow", "Just the subreddit not /r/ or r/ ex: r/pics -> pics"))
        self.label.setText(_translate("MainWindow", "Subreddit"))
        self.label_4.setText(_translate("MainWindow", "Check what information you want pulled"))
        self.checkBox_2.setText(_translate("MainWindow", "Title"))
        self.checkBox.setText(_translate("MainWindow", "Body text (if applicable)"))
        self.checkBox_4.setText(_translate("MainWindow", "Upvotes"))
        self.checkBox_5.setText(_translate("MainWindow", "Downvotes"))
        self.checkBox_6.setText(_translate("MainWindow", "Author"))
        self.checkBox_3.setText(_translate("MainWindow", "Download Photos"))
        self.checkBox_7.setText(_translate("MainWindow", "Download Videos"))
        self.label_6.setText(_translate("MainWindow", "How Many Posts?"))
        self.label_5.setText(_translate("MainWindow", "Select from what filter"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Hot"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Top"))
        self.comboBox.setItemText(2, _translate("MainWindow", "New"))
        self.pushButton.setText(_translate("MainWindow", "Ok"))
        self.label_7.setText(_translate("MainWindow", "Post Bot"))
        self.label_8.setText(_translate("MainWindow", "Subreddit"))
        self.label_9.setText(_translate("MainWindow", "Enter phrases for the bot to respond to."))
        self.label_10.setText(_translate("MainWindow", "Seperate phrases by a period no spaces.\nex: Who are you.Where are you.What are you"))
        self.label_11.setText(_translate("MainWindow", "Enter Bots Respone"))
        self.pushButton_2.setText(_translate("MainWindow", "Run"))
        self.pushButton_3.setText(_translate("MainWindow", "Run"))
        self.label_12.setText(_translate("MainWindow", "Info Grabber"))
        self.label_13.setText(_translate("MainWindow", "Comment Bot"))
        self.label_14.setText(_translate("MainWindow", "This bot will run through the post at the url submitted.\nIt will then search for your provided phrase and if found\nrespons with your submitted response."))
        self.label_15.setText(_translate("MainWindow", "Subreddit URL"))
        self.label_16.setText(_translate("MainWindow", "Trigger"))
        self.label_17.setText(_translate("MainWindow", "Bots Response"))

class Warning(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("\n Clicking Ok will create a text file with all the information inside called results.txt\n If you chose to download images they will be in a folder called imgs\n Click cancel if you are not ok with this.")
        w = QWidget()
        btn = QPushButton(w)
        btn.setText("Ok")
        btnCancel = QPushButton(w)
        btnCancel.setText("Cancel")
        layout.addWidget(self.label)
        layout.addWidget(btn)
        layout.addWidget(btnCancel)
        self.setLayout(layout)

        btn.clicked.connect(self.agreed)
        btnCancel.clicked.connect(self.cancel)

    def agreed(self):
        try:
            subreddit = reddit.subreddit(ui.lineEdit.text().lower())
        except:
            print('subreddit dosent exist')
            sys.stdout.flush()

        hm = ui.spinBox_2.value()
        filterby = ''
        if ui.comboBox.currentText() == "Top":
            filterby = subreddit.top(limit=int(hm))
        elif ui.comboBox.currentText() == "Hot":
            filterby = subreddit.hot(limit=int(hm))
        elif ui.comboBox.currentText() == "new":
            filterby = subreddit.new(limit=int(hm))

        if ui.checkBox_7.isChecked() or ui.checkBox_3.isChecked():
            try:
                for submission in filterby:
                    self.dl_media(submission, subreddit)
            except:
                print("Subreddit may not exist - ln 346")
                sys.stdout.flush()
        else:


            if not os.path.exists("./results"):
                os.mkdir("./results")
            date = datetime.datetime.now()
            x = str(date).split(" ")
            s = date.strftime("%f")
            fn = (f"./results/{x[0]}{s}_{subreddit}.txt")
            f = open(str(fn), "w+")


            for submission in filterby:
                if ui.checkBox_2.isChecked():
                    f.write(f"Title: {str(submission.title)} \n")
                if ui.checkBox.isChecked():
                    f.write(f"Text: {submission.selftext} \n")
                if ui.checkBox_4.isChecked():
                    f.write(f"Upvotes: {submission.ups} \n")
                if ui.checkBox_5.isChecked():
                    f.write(f"Downvotes: {submission.downs} \n")
                if ui.checkBox_6.isChecked():
                    f.write(f"Author: {submission.author} \n")
                f.write("------------------------------------- \n\n\n")
        
            f.close()
        self.close()
    
    def cancel(self):
        self.close()

    def dl_media(self, submission, subreddit):
        sys.stdout.flush()
        dte = datetime.datetime.now()
        # MONTH
        formated = dte.strftime("%B")
        # MICROSECOND USED SO FILES HAVE DIFFRENT NAMES
        formatedms = dte.strftime("%f")
        # YEAR/WEEKDAY/WEEKNUMBER
        formateddate = dte.strftime("%G%u%V")
        path_media = f"./imgs/{formated}/{formateddate}_{subreddit}"
        if not os.path.exists(path_media):
            os.makedirs(path_media)

        # PHOTOS
        if ui.checkBox_3.isChecked():
            extension = self.ft_img(submission.url[-3:])
            try:
                if not extension:
                    raise Exception("NoMedia")
                fp = f"{path_media}/{formateddate}_{formatedms}.{extension}"
                r = requests.get(submission.url, stream=True)
                with open(fp, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
            except:
                print("No Media")

        # VIDEOS
        if ui.checkBox_7.isChecked():
            try:
                # GET JSON TO ACCESS FALLBACK URLS FOR VIDEO
                # NOT ALL VIDEOS HAVE A FALLBACK URL, THIS IS THE ONLY WAY IVE FIGURED TO GET THE MP4 OF A POST
                url = reddit.config.reddit_url + submission.permalink + ".json"
                data = requests.get(url, , stream=True).json()
                vUrl = data[0]["data"]["children"][0]["data"]["preview"]["reddit_video_preview"]["fallback_url"]
                extension = self.ft_videos(vUrl[-3:])
                fpv = f"{path_media}/{formateddate}_{formatedms}.{extension}"
                r = requests.get(vUrl, , stream=True)
                with open(fpv, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
            except KeyError or UnicodeDecodeError:           
                print('No Key FALLBACK_URL for video')
                sys.stdout.flush()

    def ft_img(self, ft):
        match ft:
            case "jpg":
                return "jpg"
            case _:
                print("Not Image")
                sys.stdout.flush()
                return False

    def ft_videos(self, ft):
        match ft:
            case "mp4":
                return "mp4"
            case "ifv":
                return "gifv"
            case "gif":
                return "gif"
            case _:
                print("Not available format")
                sys.stdout.flush()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setFixedSize(950, 530)
    MainWindow.setWindowIcon(QtGui.QIcon('./icon.png'))
    MainWindow.show()
    sys.exit(app.exec_())
