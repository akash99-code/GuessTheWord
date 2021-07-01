
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QRegExpValidator, QFont, QColor
from PyQt5.QtCore import QRegExp, Qt
import threading
import sys
import random
import time

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(300,70,580,400)
        self.setFixedWidth(700)
        self.setFixedHeight(400)
        self.setWindowTitle('Guess The Word')
        self.setStyleSheet("background-color: white;")
        self.initUI()
        threading.Thread(target=self.simulate).start()
        #self.simulate()
    
    def initUI(self):
        
        self.txtbox = QtWidgets.QLineEdit(self)
        self.txtbox.move(600,600)
        self.txtbox.resize(50,50)
        validator = QRegExpValidator(QRegExp("[A-Za-z]{1}"))
        self.txtbox.setValidator(validator)

        self.chances = QtWidgets.QLabel(self)
        self.chances.setText("remaining chances - 100")
        self.chances.setGeometry(500,30, 180,31)
        self.chances.setStyleSheet("font: 12pt 'Comic Sans MS'; color: rgb(149, 141, 139); ")

        self.questWord = QtWidgets.QLabel(self)
        self.questWord.setText("_ _ _ _ _ _ _ _")
        self.questWord.setGeometry(40,150, 591,51)
        self.questWord.setStyleSheet('font: 24pt "Comic Sans MS";color: rgb(34, 1, 1);')
        self.questWord.setAlignment(Qt.AlignCenter)
        
        self.charac = QtWidgets.QLabel(self)
        self.charac.setText("?")
        self.charac.setGeometry(300,270, 71,61)
        self.charac.setStyleSheet('font: 19pt "Comic Sans MS"; color: rgb(69, 55, 51);')
        self.charac.setAlignment(Qt.AlignCenter)
        
        
        self.status = QtWidgets.QLabel(self)
        self.status.setText("~ Guess and Press the Alphabet ~")
        self.status.setGeometry(110,360,451,21)
        self.status.setStyleSheet('font: 12pt "Comic Sans MS";color: rgb(255, 135, 65);')
        self.status.setAlignment(Qt.AlignCenter)

        self.running=True

        
    
    def getWord(self, level=0):
        self.Word='DISTRCI'
    
    def generate(self):
        L= len(self.Word)
        self.filWord = [False]* L
        c= int(0.3*L)
        if c==0: 
            c+=1
        while c>0:
            i = random.randint(0, L-1)
            ch=self.Word[i]
            ind = -1
            while(True):
                ind = self.Word.find(ch, ind+1)
                if(ind==-1):
                    break
                self.filWord[ind] = True
                c=c-1
    
    def inp(self):
        while True:
            time.sleep(0.1)
            alpha = self.txtbox.text()
            if alpha!='' and alpha.isalpha():
                return alpha.upper()

    def displayW(self):
        i=0
        str=''
        for c in self.Word:
            if(self.filWord[i]):
                str+=c+' '
            else:
                str+='_ '
            i+=1
        self.questWord.setText(str)
    
    def checks(self,c):
        p=self.Word.find(c)
        if (p==-1):
            return -1

        if(self.filWord[p]):
            return 0

        ind = -1
        while(True):
            ind = self.Word.find(c, ind+1)
            if ind==-1:
                break
            self.filWord[ind] = True
        return 1
    
    def simulate(self):
        self.getWord()
        self.generate()
        chance = 7
        while( (chance!=0) and (False in self.filWord) ):=
            self.chances.setText("Chances Remaining - "+str(chance))
            self.displayW()
            self.txtbox.setText('')
            ch = self.inp()
            self.charac.setText(ch)
            s = self.checks(ch)
            if s==-1:
                self.status.setText('Wrong Guess!')
                chance-=1
                continue
            if s==0:
                self.status.setText('Try New Alphabet')
                continue
            if s==1:
                self.status.setText('Awesome, nice guess')
                continue

        if(not(False in self.filWord)):
            self.status.setText('Voila!! you have cracked the word')
        else:
            self.chances.setText("Chances Remaining - 0")
            self.status.setText('Chances perished! better luck next time ')
        
        self.questWord.setText(self.Word)
        return
               


    
    
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    try:
        sys.exit(app.exec_())
    except:
        print('game terminated')

window()
