import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolTip
from PyQt5.QtGui import QIcon



def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    
    win.setWindowTitle("Instagram")
    win.setGeometry(200,300,300,300)
    win.setWindowIcon(QIcon("indir.png"))
    win.setToolTip("my tooltip")

    lbl_name= QtWidgets.QLabel(win)
    lbl_name.setText("Kullanıcı Adı:")
    lbl_name.move(50,30)

    lbl_password= QtWidgets.QLabel(win)
    lbl_password.setText("Şifre:")  ""
    lbl_password.move(50,70)    

    txt_name=QtWidgets.QLineEdit(win)
    txt_name.move(130,30)
    
    txt_password=QtWidgets.QLineEdit(win)
    txt_password.move(130,70)
    
    def clicked(self):
         print("Butona tıklandı:" + txt_name.text() + txt_password.text())

    btn_save=QtWidgets.QPushButton(win)
    btn_save.move(130,110)
    btn_save.setText("Kaydet")
    btn_save.clicked.connect(clicked)


    win.show()
    sys.exit(app.exec_())

    






window()

