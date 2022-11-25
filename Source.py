import sys
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import source

def veriçek():
    con = sqlite3.connect("Hesaplar.db")
    imleç = con.cursor()
    imleç.execute("CREATE TABLE IF NOT EXISTS Hesaplar(Başlık TEXT,İçerik TEXT)")
    con.commit()
    a = imleç.execute("Select * From Hesaplar")
    sözlük = {}
    for i,j in a:
        if i.strip(" ") == "" or j.strip(" ") == "":
            continue
        sözlük[i] = j
    con.close()
    return sözlük

def veri_güncelle(isim,değişim,yeni):
    con = sqlite3.connect("Hesaplar.db")
    imleç = con.cursor()
    imleç.execute("Update Hesaplar set {} = '{}' where Başlık = '{}'".format(değişim,yeni,isim))
    con.commit()
    con.close()

def veri_sil(isim):
    con = sqlite3.connect("Hesaplar.db")
    imleç = con.cursor()
    imleç.execute("Delete from Hesaplar where Başlık = '{}'".format(isim))
    con.commit()
    con.close()
def veri_ekle(başlık,içerik):
    con = sqlite3.connect("Hesaplar.db")
    imleç = con.cursor()
    imleç.execute("Insert into Hesaplar Values(?,?)", (başlık,içerik))
    con.commit()
    con.close()


sözlük = veriçek()


sözlük["a"] = "a"

# **************************************************************************************************************
#                       Hesap_oluştur
# **************************************************************************************************************

class Hesap_olustur(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        #----------------------------------------içerik------------------------------------------------
        self.hesap_baslık_yazısı = QLabel("Hesap Başlığı: ")
        self.hesap_baslık_lineEdit = QLineEdit()
        self.hesap_içerik_yazısı = QLabel("Hesap İçeriği: ")
        self.hesap_içerik = QTextEdit()
        self.ekle_butonu = QPushButton("Ekle")

        #----------------------------------------------------------------------------------------------
        #Sözlük ile arayüz arasındaki bağlanytıyı kurman gerek enswith
        



        #-----------------------------------Boxlamalar-------------------------------------------------
        h_box = QHBoxLayout()
        h_box.addWidget(self.hesap_baslık_yazısı)
        h_box.addWidget(self.hesap_baslık_lineEdit)

        h_box_2 = QHBoxLayout()
        h_box_2.addWidget(self.hesap_içerik_yazısı)
        h_box_2.addWidget(self.hesap_içerik)

        v_box = QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addLayout(h_box_2)
        v_box.addWidget(self.ekle_butonu)
        self.kesici = QLabel("Ludos™")
        self.kesici.setFont(QFont("Calibri", 14))
        h2 = QHBoxLayout()
        h2.addStretch()
        h2.addWidget(self.kesici)
        v_box.addLayout(h2)
        self.setLayout(v_box)
        #-----------------------------------------------------------------------------------------------


        #------------------Fonksiyonel------------------------------------------------------------------
        self.ekle_butonu.clicked.connect(self.ekle_butonu_fonksiyon)
        #-----------------------------------------------------------------------------------------------









    def ekle_butonu_fonksiyon(self):
        self.hesapb =   self.hesap_baslık_lineEdit.text()
        self.hesapi1 = self.hesap_içerik.toPlainText()
        self.hesap_baslık_lineEdit.clear()
        self.hesap_içerik.clear()
        veri_ekle(self.hesapb,self.hesapi1)
        sözlük = veriçek()



# **************************************************************************************************************
#                       Hesap_ara
# **************************************************************************************************************


class Hesap_ara(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # ----------------------------------------içerik------------------------------------------------
        self.arama_lineEdit = QLineEdit()
        self.arama_butonu = QPushButton("Ara")
        self.arama_butonu.setIcon(QIcon("icons/Arama.png"))
        self.gösterge = QScrollArea()
        #self.gösterge.setStyleSheet("background-color: grey")
        self.gösterge.setWidgetResizable(True)




        #self.gösterge.
        # -----------------------------------------------------------------------------------------------

        # -----------------------------------Boxlamalar-------------------------------------------------
        h_box = QHBoxLayout()
        h_box.addWidget(self.arama_lineEdit)
        h_box.addWidget(self.arama_butonu)

        v_box = QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addWidget(self.gösterge)
        self.kesici = QLabel("Ludos™")
        self.kesici.setFont(QFont("Calibri", 14))
        h2 = QHBoxLayout()
        h2.addStretch()
        h2.addWidget(self.kesici)
        v_box.addLayout(h2)

        self.setLayout(v_box)
        # -----------------------------------------------------------------------------------------------

        # ------------------Fonksiyonel------------------------------------------------------------------
        self.arama_butonu.setShortcut("Ctrl+A")
        self.arama_butonu.clicked.connect(self.arama_butonu_func)
        # -----------------------------------------------------------------------------------------------
        istek = self.arama_lineEdit.text()
        sonuçlar = []
        sözlük = veriçek()
        for i in sözlük.keys():
            if istek in i:
                sonuçlar.append(i)
        """
        if len(istek) == 0:
            for i in sözlük.keys():
                sonuçlar.append(i)
        if len(sonuçlar) == 0:
            self.fg = QLabel("Hiçbir İçerik Bulunamadı !")
            self.fg.setFont(QFont("Ariel",36))
            h = QHBoxLayout()
            h.addStretch()
            h.addWidget(self.fg)
            h.addStretch()
            self.gösterge.setLayout(h)
        """

        # -----------------------------------Arama sonuçları--------------------------------------------
        self.fg = QLabel("")
        self.fg.setText("")

        form = QFormLayout()
        for i in sonuçlar:
            self.i = QPushButton(i)
            self.i.clicked.connect(self.k)
            form.addRow(self.i)
        g = QGroupBox()
        g.setLayout(form)
        self.gösterge.setWidgetResizable(True)
        self.gösterge.setWidget(g)




        self.i = 1
    def arama_butonu_func(self):
        istek = self.arama_lineEdit.text()
        sonuçlar = []
        sözlük = veriçek()
        for i in sözlük.keys():
            if istek in i:
                sonuçlar.append(i)
        """
        if len(istek) == 0:
            for i in sözlük.keys():
                sonuçlar.append(i)
        if len(sonuçlar) == 0:
            self.fg = QLabel("Hiçbir İçerik Bulunamadı !")
            self.fg.setFont(QFont("Ariel",36))
            h = QHBoxLayout()
            h.addStretch()
            h.addWidget(self.fg)
            h.addStretch()
            self.gösterge.setLayout(h)
        """





        #-----------------------------------Arama sonuçları--------------------------------------------
        self.fg = QLabel("")
        self.fg.setText("")

        form = QFormLayout()
        for i in sonuçlar:
            self.i = QPushButton(i)
            self.i.clicked.connect(self.k)
            form.addRow(self.i)
        g = QGroupBox()
        g.setLayout(form)
        self.gösterge.setWidgetResizable(True)
        self.gösterge.setWidget(g)

    def k(self):
        send = self.sender()
        a = Arama_sonuç(send.text())
        Main.setCentralWidget(m,a)


# **************************************************************************************************************
#                       Hesap_ara
# **************************************************************************************************************



class Arama_sonuç(QWidget):

    def __init__(self,sender):
        super().__init__()
        sözlük = veriçek()
        self.gönderen = sender
        #self.gönderen = self.sender()
        

        
        self.init_ui()

    def init_ui(self):
        #-------------------------İçerik-------------------------------------
        #self.başlık = QLabel(self.gönderen)
        self.başlık = QLineEdit()
        self.başlık.setText(self.gönderen)
        sözlük = veriçek()
        sözlük["a"] = "a"
        #self.başlık.setFont(QFont("Constantia",25))
        self.içerik = QTextEdit(sözlük[self.gönderen])


        self.içerik.setStyleSheet("background-color: White")

        #self.içerik.setFont(QFont("Calibri",13))
        self.başlık.setStyleSheet("Background-color: White")
        self.başlık_işaret = QLabel("Hesap Başlığı: ")
        #self.başlık_işaret.setFont(QFont("",25))
        self.kesici = QLabel("Ludos™")
        self.kesici.setFont(QFont("Calibri",14))
        self.içerik_işaret = QLabel("Hesap İçeriği :")
        #self.içerik_işaret.setFont(QFont("Calibri",25))
        self.kaydet = QPushButton("Kaydet")
        self.sil = QPushButton("Sil")
        #----------------------------------------------------------------------------------

        #-----------------------------------------func-----------------------------
        self.kaydet.clicked.connect(self.kayit)
        self.sil.clicked.connect(self.silq)
        #------------------------------------------------------------------------------------


        #-------------------------------Boxlama----------------------------------------------
        h = QHBoxLayout()
        h.addWidget(self.başlık_işaret)
        h.addWidget(self.başlık)
        h.addWidget(self.kaydet)
        h.addWidget(self.sil)
        h.addStretch()

        h1 = QHBoxLayout()
        h1.addWidget(self.içerik_işaret)
        h1.addWidget(self.içerik)


        v = QVBoxLayout()
        v.addLayout(h)

        v.addLayout(h1)
        h2 = QHBoxLayout()
        h2.addStretch()
        h2.addWidget(self.kesici)
        v.addLayout(h2)
        self.setLayout(v)
    #-----------------------------------------------------------------------------------------
    def silq(self):
        try:
            veri_sil(self.başlık.text())
            a = Hesap_ara()
            Main.setCentralWidget(m,a)
        except:
            pass

    def kayit(self):
        self.başlık1 = self.başlık.text()
        self.içerik1 = self.içerik.toPlainText()
        veri_güncelle(self.gönderen,"İçerik",self.içerik1)
        veri_güncelle(self.gönderen, "Başlık", self.başlık1)
        sözlük = veriçek()



# **************************************************************************************************************
#                       Hesap_ara
# **************************************************************************************************************

class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.hesap_oluştur = Hesap_olustur()
        self.hesap_ara = Hesap_ara()
        self.arama_sonuç = Arama_sonuç("a")
        self.initui()

    def initui(self):
        self.setGeometry(500, 200, 500, 800)
        menü = self.menuBar()
        self.setWindowTitle("Hesabım")
        self.setWindowIcon(QIcon("icons/indir.png"))
        self.setCentralWidget(self.hesap_ara)


        hesap_oluştur1 = QAction("Hesap Oluştur", self)

        hesap_oluştur1.setShortcut("Ctrl+p")
        hesap_oluştur1.triggered.connect(self.hesap_olu)
        ara = QAction("Hesap Ara", self)
        ara.triggered.connect(self.arama)
        menü.addAction(ara)
        menü.addAction(hesap_oluştur1)

        #self.hesap_ara.i.clicked.connect(self.tik)
        self.show()

    def sip(self,isim):
        veri_sil(isim)
        self.hesap_ara = Hesap_ara()
        self.setCentralWidget(self.hesap_ara)
    def arama(self):
        self.hesap_ara = Hesap_ara()
        self.setCentralWidget(self.hesap_ara)
    def hesap_olu(self):
        self.hesap_oluştur = Hesap_olustur()
        self.setCentralWidget(self.hesap_oluştur)
    def tik(self):

        send = self.hesap_ara.sender()
        self.aramas = Arama_sonuç(send.text)









app = QApplication(sys.argv)
m = Main()
sys.exit(app.exec_())
