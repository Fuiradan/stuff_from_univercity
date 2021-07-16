import platform, time, subprocess, sys
import md5
from PyQt5 import QtWidgets
import design

tmp_md5 = ''

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.activate)
        self.pushButton_2.clicked.connect(self.deactivate)
        self.pushButton_3.clicked.connect(self.check)
        self.textEdit.insertPlainText('Нажмите "Активировать" для активации приложения\nНажмите "Деактивировать" \
        для деактивации приложения\nНажмите "Проверка" для проверки активации.')
    def activate(self):
        global tmp_md5
        tmp_md5 = save_current_machine_md5()
        self.textEdit.clear()
        self.textEdit.insertPlainText('Активация прошла успешно!')
    def deactivate(self):
        global tmp_md5
        tmp_md5 = save_imitate_dif_machine_md5()
        self.textEdit.clear()
        self.textEdit.insertPlainText('Деактивация прошла успешно!')
    def check(self):
        global tmp_md5
        tmp = save_current_machine_md5()
        if tmp_md5 == tmp:
            self.textEdit.clear()
            self.textEdit.insertPlainText('Продукт активирован')
        else:
            self.textEdit.clear()
            self.textEdit.insertPlainText(' Используется нелицензионная копия')

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

def save_current_machine_md5():
    info = platform.uname()
    info = info.processor + info.node + info.system
    sp_return = subprocess.Popen("dmesg | grep 'MAC address' | gawk '{print $14}'", shell=True, stdout=subprocess.PIPE)
    hash_md5 = md5.create_md5(info + sp_return.stdout.read().decode())
    return hash_md5

def save_imitate_dif_machine_md5():
    info_d = str(time.time())
    hash_md5 = md5.create_md5(info_d)
    return hash_md5


if __name__ == '__main__':
    main()






