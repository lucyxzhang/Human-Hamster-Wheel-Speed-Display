from PyQt5.QtWidgets import QApplication, QMainWindow,\
    QVBoxLayout, QLabel, QWidget, QHBoxLayout, QMenuBar
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import serial

# CHANGE 'COM5' TO NAME OF SERIAL PORT CONNECTED TO ARDUINO
ser = serial.Serial('COM5', 9600)

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # window title
        self.setWindowTitle('Hamster Data Viewer')

        # QLabel widget to display data
        self.data_label = QLabel()
        self.data_label.setAlignment(Qt.AlignCenter)
        self.data_label.setStyleSheet('font-size: 300px;')

        # QLabel widget to display graphic
        self.image_label = QLabel()
        pixmap = QPixmap('hamster.png') # image must be in same directory and named 'hamster.png'
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(Qt.AlignCenter)

        # QLabel widget to offset heading (technically a textbox)
        self.text_label = QLabel(' ')
        self.text_label.setAlignment(Qt.AlignCenter)
        self.text_label.setStyleSheet('font-size: 100px;')

        # QLabel widget to display 'Hamster Power'
        self.additional_text_label = QLabel('Hamster Power')
        self.additional_text_label.setAlignment(Qt.AlignCenter)
        self.additional_text_label.setStyleSheet('font-size: 150px;')

        # sets layout for window
        layout = QVBoxLayout()
        layout.addWidget(self.text_label)
        data_and_text_layout = QHBoxLayout()
        data_and_text_layout.addWidget(self.data_label, stretch=1)
        data_and_text_layout.addWidget(self.additional_text_label, stretch=1)
        data_and_text_layout.setContentsMargins(50, 0, 50,0)
        layout.addLayout(data_and_text_layout)
        layout.addWidget(self.image_label, stretch=1)

        # sets layout for central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # menu bar; honestly not sure what this is for
        menu_bar = QMenuBar()
        self.setMenuBar(menu_bar)

        # timer to read data from the serial port every 100ms
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data)
        self.timer.start(100) # change this to increase or decrease frequency; milliseconds

    def update_data(self):
        # reads data from the serial port (from arduino) and update the label
        data = ser.readline().decode().strip()
        self.data_label.setText(data)


if __name__ == '__main__':
    # creates the application & window
    app = QApplication([])
    window = mainwindow()
    window.show()

    # runs the application on loop
    app.exec_()
