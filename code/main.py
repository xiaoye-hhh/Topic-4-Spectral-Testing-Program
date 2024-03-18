import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QPushButton, QFileDialog, QVBoxLayout, QHBoxLayout, QLabel

class SpectralPredictionApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 700, 200)
        self.setFixedSize(700, 150)

        self.setWindowTitle('违禁品痕迹追踪与关联智能分析算法')

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # 文件选择行
        hbox = QHBoxLayout()
        layout.addLayout(hbox)

        hbox.addWidget(QLabel('光谱文件:'))

        self.file_name = QLineEdit()
        self.file_name.setReadOnly(True)
        hbox.addWidget(self.file_name)

        self.select_file_button = QPushButton('选择光谱', self)
        hbox.addWidget(self.select_file_button)
        self.select_file_button.clicked.connect(self.select_file)

        # 预测行
        hbox = QHBoxLayout()
        layout.addLayout(hbox)
 
        hbox.addWidget(QLabel('样品成分:'))

        self.sample_name = QLineEdit()
        self.sample_name.setReadOnly(True)
        hbox.addWidget(self.sample_name)

        self.analysis_button = QPushButton('成分分析', self)
        hbox.addWidget(self.analysis_button)
        self.analysis_button.clicked.connect(self.analysis_sample)

        # 设置样式表
        self.setStyleSheet("""
            * {
                font-family: Arial;
                font-size: 24px;
            }"""
        )


    def select_file(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,"选择光谱文件", "","Text Files (*.txt)", options=options)
        if fileName:
            # print("选择的文件名:", fileName)
            self.file_name.setText(fileName)
            self.sample_name.setText("")

    def analysis_sample(self):
        # 预测

        # 显示结果
        self.sample_name.setText("TNT")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SpectralPredictionApp()
    ex.show()
    sys.exit(app.exec_())
