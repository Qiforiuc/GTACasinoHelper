from PyQt5 import QtCore, QtGui, QtWidgets
import atexit

class Ui_MainWindow(object):

    logText = ""

    def __init__(self):
        self.clicked_numbers = []  # List to store the clicked numbers
        self.button_counter = {}  # Dictionary to store button counters
        self.history_list = []  # List to store the whole history of numbers
        self.historyListString = ""
        self.top_number_text = ""  # String to display the top numbers

        button_numbers = ["00", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                          "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
                          "20", "21", "22", "23", "24", "25", "26", "27", "28", "29",
                          "30", "31", "32", "33", "34", "35", "36"]
        for number in button_numbers:
            self.button_counter[number] = 0


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 685)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.button_00 = QtWidgets.QPushButton(self.centralwidget)
        self.button_00.setGeometry(QtCore.QRect(10, 20, 75, 31))
        self.button_00.setStyleSheet("background-color:rgb(42, 201, 57);")
        self.button_00.setObjectName("button_00")
        self.button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.button_0.setGeometry(QtCore.QRect(10, 60, 75, 31))
        self.button_0.setStyleSheet("background-color:rgb(42, 201, 57);")
        self.button_0.setObjectName("button_0")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 10, 521, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.button_26 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_26.setStyleSheet("background-color:rgb(17, 10, 21); color:\"white\"")
        self.button_26.setObjectName("button_26")
        self.gridLayout_2.addWidget(self.button_26, 1, 8, 1, 1)
        self.button_24 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_24.setStyleSheet("background-color:rgb(17, 10, 21); color:\"white\"")
        self.button_24.setObjectName("button_24")
        self.gridLayout_2.addWidget(self.button_24, 0, 7, 1, 1)
        self.button_22 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_22.setStyleSheet("background-color:rgb(17, 10, 21); color:\"white\"")
        self.button_22.setObjectName("button_22")
        self.gridLayout_2.addWidget(self.button_22, 2, 7, 1, 1)
        self.button_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_10.setStyleSheet("background-color:rgb(17, 10, 21); color:\"white\"")
        self.button_10.setObjectName("button_10")
        self.gridLayout_2.addWidget(self.button_10, 2, 3, 1, 1)
        self.button_12 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_12.setStyleSheet("background-color:rgb(255, 42, 57);")
        self.button_12.setObjectName("button_12")
        self.gridLayout_2.addWidget(self.button_12, 0, 3, 1, 1)
        self.button_11 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_11.setStyleSheet("background-color:rgb(17, 10, 21); color:\"white\"")
        self.button_11.setObjectName("button_11")
        self.gridLayout_2.addWidget(self.button_11, 1, 3, 1, 1)
        self.button_23 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_23.setStyleSheet("background-color:rgb(255, 42, 57);")
        self.button_23.setObjectName("button_23")
        self.gridLayout_2.addWidget(self.button_23, 1, 7, 1, 1)
        self.button_17 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_17.setStyleSheet("background-color:rgb(17, 10, 21); color:\"white\"")
        self.button_17.setObjectName("button_17")
        self.gridLayout_2.addWidget(self.button_17, 1, 5, 1, 1)
        self.button_13 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_13.setStyleSheet("background-color:rgb(17, 10, 21); color:\"white\"")
        self.button_13.setObjectName("button_13")
        self.gridLayout_2.addWidget(self.button_13, 2, 4, 1, 1)
        self.button_14 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_14.setStyleSheet("background-color:rgb(255, 42, 57);")
        self.button_14.setObjectName("button_14")
        self.gridLayout_2.addWidget(self.button_14, 1, 4, 1, 1)
        self.button_20 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_20.setStyleSheet("background-color:rgb(17, 10, 21); color:\"white\"")
        self.button_20.setObjectName("button_20")
        self.gridLayout_2.addWidget(self.button_20, 1, 6, 1, 1)
        self.button_18 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_18.setStyleSheet("background-color:rgb(255, 42, 57);")
        self.button_18.setObjectName("button_18")
        self.gridLayout_2.addWidget(self.button_18, 0, 5, 1, 1)
        self.button_15 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_15.setStyleSheet("background-color:rgb(17, 10, 21); color:\"white\"")
        self.button_15.setObjectName("button_15")
        self.gridLayout_2.addWidget(self.button_15, 0, 4, 1, 1)
        self.button_16 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_16.setStyleSheet("background-color:rgb(255, 42, 57);")
        self.button_16.setObjectName("button_16")
        self.gridLayout_2.addWidget(self.button_16, 2, 5, 1, 1)
        self.button_25 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_25.setStyleSheet("background-color:rgb(255, 42, 57);")
        self.button_25.setObjectName("button_25")
        self.gridLayout_2.addWidget(self.button_25, 2, 8, 1, 1)
        self.button_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_1.setStyleSheet("background-color:rgb(255, 42, 57);")
        self.button_1.setObjectName("button_1")
        self.gridLayout_2.addWidget(self.button_1, 2, 0, 1, 1)
        self.button_19 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_19.setStyleSheet("background-color:rgb(255, 42, 57);")
        self.button_19.setObjectName("button_19")
        self.gridLayout_2.addWidget(self.button_19, 2, 6, 1, 1)
        self.button_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_6.setStyleSheet("background-color:rgb(17, 10, 21); color:\"white\"")
        self.button_6.setObjectName("button_6")
        self.gridLayout_2.addWidget(self.button_6, 0, 1, 1, 1)
        self.button_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_5.setStyleSheet("background-color:rgb(255, 42, 57);")
        self.button_5.setObjectName("button_5")
        self.gridLayout_2.addWidget(self.button_5, 1, 1, 1, 1)
        self.button_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_2.setStyleSheet("background-color:rgb(17, 10, 21); color:\"white\"")
        self.button_2.setObjectName("button_2")
        self.gridLayout_2.addWidget(self.button_2, 1, 0, 1, 1)
        self.button_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_3.setStyleSheet("background-color:rgb(255, 42, 57);")
        self.button_3.setObjectName("button_3")
        self.gridLayout_2.addWidget(self.button_3, 0, 0, 1, 1)
        self.button_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_8.setStyleSheet("background-color:rgb(17, 10, 21); color:\"white\"")
        self.button_8.setObjectName("button_8")
        self.gridLayout_2.addWidget(self.button_8, 1, 2, 1, 1)
        self.button_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_4.setStyleSheet("background-color:rgb(17, 10, 21); color:\"white\"")
        self.button_4.setObjectName("button_4")
        self.gridLayout_2.addWidget(self.button_4, 2, 1, 1, 1)
        self.button_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_9.setStyleSheet("background-color:rgb(255, 42, 57);")
        self.button_9.setObjectName("button_9")
        self.gridLayout_2.addWidget(self.button_9, 0, 2, 1, 1)
        self.button_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_7.setStyleSheet("background-color:rgb(255, 42, 57);")
        self.button_7.setObjectName("button_7")
        self.gridLayout_2.addWidget(self.button_7, 2, 2, 1, 1)
        self.button_21 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_21.setStyleSheet("background-color:rgb(255, 42, 57);")
        self.button_21.setObjectName("button_21")
        self.gridLayout_2.addWidget(self.button_21, 0, 6, 1, 1)
        self.button_27 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_27.setStyleSheet("background-color:rgb(255, 42, 57);")
        self.button_27.setObjectName("button_27")
        self.gridLayout_2.addWidget(self.button_27, 0, 8, 1, 1)
        self.button_28 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_28.setStyleSheet("background-color:rgb(17, 10, 21); color:\"white\"")
        self.button_28.setObjectName("button_28")
        self.gridLayout_2.addWidget(self.button_28, 2, 9, 1, 1)
        self.button_33 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_33.setStyleSheet("background-color:rgb(17, 10, 21); color:\"white\"")
        self.button_33.setObjectName("button_33")
        self.gridLayout_2.addWidget(self.button_33, 0, 10, 1, 1)
        self.button_29 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_29.setStyleSheet("background-color:rgb(17, 10, 21); color:\"white\"")
        self.button_29.setObjectName("button_29")
        self.gridLayout_2.addWidget(self.button_29, 1, 9, 1, 1)
        self.button_30 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_30.setStyleSheet("background-color:rgb(255, 42, 57);")
        self.button_30.setObjectName("button_30")
        self.gridLayout_2.addWidget(self.button_30, 0, 9, 1, 1)
        self.button_31 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_31.setStyleSheet("background-color:rgb(17, 10, 21); color:\"white\"")
        self.button_31.setObjectName("button_31")
        self.gridLayout_2.addWidget(self.button_31, 2, 10, 1, 1)
        self.button_32 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_32.setStyleSheet("background-color:rgb(255, 42, 57);")
        self.button_32.setObjectName("button_32")
        self.gridLayout_2.addWidget(self.button_32, 1, 10, 1, 1)
        self.button_34 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_34.setStyleSheet("background-color:rgb(255, 42, 57);")
        self.button_34.setObjectName("button_34")
        self.gridLayout_2.addWidget(self.button_34, 2, 11, 1, 1)
        self.button_36 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_36.setStyleSheet("background-color:rgb(255, 42, 57);")
        self.button_36.setObjectName("button_36")
        self.gridLayout_2.addWidget(self.button_36, 0, 11, 1, 1)
        self.button_35 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_35.setStyleSheet("background-color:rgb(17, 10, 21); color:\"white\"")
        self.button_35.setObjectName("button_35")
        self.gridLayout_2.addWidget(self.button_35, 1, 11, 1, 1)
        self.top_numbers = QtWidgets.QLabel(self.centralwidget)
        self.top_numbers.setGeometry(QtCore.QRect(380, 150, 231, 500))
        self.top_numbers.setText("")
        self.top_numbers.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.top_numbers.setObjectName("top_numbers")
        self.history = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.history.setGeometry(QtCore.QRect(80, 150, 281, 500))
        self.history.setObjectName("history")
        self.clear_all_bets = QtWidgets.QPushButton(self.centralwidget)
        self.clear_all_bets.setGeometry(QtCore.QRect(630, 60, 121, 51))
        self.clear_all_bets.setStyleSheet("background-color:rgb(255, 42, 57);")
        self.clear_all_bets.setObjectName("clear_all_bets")
        self.delete_last_bet = QtWidgets.QPushButton(self.centralwidget)
        self.delete_last_bet.setGeometry(QtCore.QRect(630, 0, 121, 51))
        self.delete_last_bet.setStyleSheet("background-color:rgb(111, 193, 255);")
        self.delete_last_bet.setObjectName("delete_last_bet")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 130, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 130, 91, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 759, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Connect Buttons
        button_numbers = ["00", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                          "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
                          "20", "21", "22", "23", "24", "25", "26", "27", "28", "29",
                          "30", "31", "32", "33", "34", "35", "36"]

        # Connect button clicks to the slot using a loop
        for number in button_numbers:
            button = getattr(self, f"button_{number}")
            button.clicked.connect(lambda checked, num=number: self.handle_button_click(num))

        # Connect Delete Last Number button
        self.delete_last_bet.clicked.connect(self.delete_last_number)

        # Connect Clear All button
        self.clear_all_bets.clicked.connect(self.clear_all_numbers)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Casino Helper by QIFORIUC"))
        self.button_00.setText(_translate("MainWindow", "00"))
        self.button_0.setText(_translate("MainWindow", "0"))
        self.button_1.setText(_translate("MainWindow", "1"))
        self.button_2.setText(_translate("MainWindow", "2"))
        self.button_3.setText(_translate("MainWindow", "3"))
        self.button_4.setText(_translate("MainWindow", "4"))
        self.button_5.setText(_translate("MainWindow", "5"))
        self.button_6.setText(_translate("MainWindow", "6"))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_8.setText(_translate("MainWindow", "8"))
        self.button_9.setText(_translate("MainWindow", "9"))
        self.button_10.setText(_translate("MainWindow", "10"))
        self.button_11.setText(_translate("MainWindow", "11"))
        self.button_12.setText(_translate("MainWindow", "12"))
        self.button_13.setText(_translate("MainWindow", "13"))
        self.button_14.setText(_translate("MainWindow", "14"))
        self.button_15.setText(_translate("MainWindow", "15"))
        self.button_16.setText(_translate("MainWindow", "16"))
        self.button_17.setText(_translate("MainWindow", "17"))
        self.button_18.setText(_translate("MainWindow", "18"))
        self.button_19.setText(_translate("MainWindow", "19"))
        self.button_20.setText(_translate("MainWindow", "20"))
        self.button_21.setText(_translate("MainWindow", "21"))
        self.button_22.setText(_translate("MainWindow", "22"))
        self.button_23.setText(_translate("MainWindow", "23"))
        self.button_24.setText(_translate("MainWindow", "24"))
        self.button_25.setText(_translate("MainWindow", "25"))
        self.button_26.setText(_translate("MainWindow", "26"))
        self.button_27.setText(_translate("MainWindow", "27"))
        self.button_28.setText(_translate("MainWindow", "28"))
        self.button_29.setText(_translate("MainWindow", "29"))
        self.button_30.setText(_translate("MainWindow", "30"))
        self.button_31.setText(_translate("MainWindow", "31"))
        self.button_32.setText(_translate("MainWindow", "32"))
        self.button_33.setText(_translate("MainWindow", "33"))
        self.button_34.setText(_translate("MainWindow", "34"))
        self.button_35.setText(_translate("MainWindow", "35"))
        self.button_36.setText(_translate("MainWindow", "36"))
        self.clear_all_bets.setText(_translate("MainWindow", "Clear All"))
        self.delete_last_bet.setText(_translate("MainWindow", "Delete Previous Bet"))
        self.label.setText(_translate("MainWindow", "History"))
        self.label_2.setText(_translate("MainWindow", "Top Numbers"))

    def handle_button_click(self, number):
        # This slot will be called when a button is clicked
        # Add the clicked number to the list
        self.clicked_numbers.append(number)

        # Update the button counter
        if number not in self.button_counter:
            self.button_counter[number] = 0
        else:
            self.button_counter[number] = 0

        # Print the clicked numbers with counters
        for num, count in sorted(self.button_counter.items(), key=lambda x: x[1], reverse=True):
            if count >= 20:
                self.top_number_text += f'"{num}" ->  {count} times ago' + "\n"

        self.top_numbers.setText(self.top_number_text)
        self.top_number_text = ""
        # Increment counters for other buttons
        for num in self.button_counter:
            self.button_counter[num] += 1

        self.history_list.append(number)

        for number in self.history_list:
            self.historyListString += number + ", "

        self.history.setPlainText(self.historyListString)
        Ui_MainWindow.logText = self.historyListString
        self.historyListString = ""


    def delete_last_number(self):
        # Function to delete the last element from the list
        if self.clicked_numbers:
            last_number = self.clicked_numbers.pop()
            if last_number in self.button_counter:
                self.button_counter[last_number] = 0
                self.button_counter.pop(last_number)
            self.top_numbers.setText(self.top_number_text)
            self.history_list.pop()

    def clear_all_numbers(self):
        # Function to clear all elements from the list
        self.clicked_numbers.clear()
        for num in self.button_counter:
            self.button_counter[num] = 0
        self.button_counter.clear()

        self.top_numbers.setText(self.top_number_text)
        self.history_list.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    app_icon = QtGui.QIcon("./assets/casino_Logo.png")  # Replace "icon.png" with the path to your icon file
    app.setWindowIcon(app_icon)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()


    # Define a function to create the log file and save logs on program exit
    def create_log_file():
        log_filename = "casino_logs.txt"

        # Open the log file for writing
        with open(log_filename, "w") as log_file:
            log_file.write("Casino Helper Log:\n")
            log_file.write(Ui_MainWindow.logText)


    # Register the exit function
    atexit.register(create_log_file)

    sys.exit(app.exec_())







