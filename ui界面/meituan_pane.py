import sys, os

if hasattr(sys, 'frozen'):

    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.Qt import *
from meituan import Ui_Form
class MeiTuanPane(QWidget,Ui_Form):
    btn_1_signal=pyqtSignal()
    btn_2_signal=pyqtSignal()
    btn_3_signal = pyqtSignal()
    btn_4_signal = pyqtSignal()


    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.setWindowTitle('点评哦')
        self.label.setVisible(False)
        self.label_2.setVisible(False)
        self.label_3.setVisible(False)
        self.label_4.setVisible(False)
        self.label_5.setVisible(False)
        self.label_6.setVisible(False)
        self.label_7.setVisible(False)
    def btn_1(self):
        self.btn_1_signal.emit()
        #self.textEdit.setText('1')
        self.label.setVisible(False)
        self.label_2.setVisible(False)
        self.label_3.setVisible(False)
        self.label_4.setVisible(False)
        self.label_5.setVisible(False)
        self.label_6.setVisible(False)
        self.label_7.setVisible(False)
        self.label_5.setVisible(True)
    def btn_2(self):
        self.btn_2_signal.emit()
        #self.textEdit.setText('50以下：'+'hh\n50-100：'+'hh\n100-200：'+'hh\n200以上：'+'hh\n')
        self.label.setVisible(False)
        self.label_2.setVisible(False)
        self.label_3.setVisible(False)
        self.label_4.setVisible(False)
        self.label_5.setVisible(False)
        self.label_6.setVisible(False)
        self.label_7.setVisible(False)
        self.label.setVisible(True)
        self.label_2.setVisible(True)
        self.label_3.setVisible(True)
        self.label_4.setVisible(True)

    def btn_3(self):
        self.btn_3_signal.emit()
        #self.textEdit.setText('3')
        self.label.setVisible(False)
        self.label_2.setVisible(False)
        self.label_3.setVisible(False)
        self.label_4.setVisible(False)
        self.label_5.setVisible(False)
        self.label_6.setVisible(False)
        self.label_7.setVisible(False)
        self.label_6.setVisible(True)
    def btn_4(self):
        self.btn_4_signal.emit()
        #self.textEdit.setText('4')
        self.label.setVisible(False)
        self.label_2.setVisible(False)
        self.label_3.setVisible(False)
        self.label_4.setVisible(False)
        self.label_5.setVisible(False)
        self.label_6.setVisible(False)
        self.label_7.setVisible(False)
        self.label_7.setVisible(True)





if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MeiTuanPane()#创建控件
    window.show()
    sys.exit(app.exec_())
