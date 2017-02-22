#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton, QHBoxLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt


class Kalkulator(QWidget):
    def __init__(self, parent=None):
        super(Kalkulator, self).__init__(parent)

        self.interfejs()

    def interfejs(self):

        # etykiety
        etykieta1 = QLabel("Liczba 1:")
        etykieta2 = QLabel("Liczba 2:")
        etykieta3 = QLabel("Wynik:")

        # pola edycyjne
        self.liczba1 = QLineEdit()
        self.liczba2 = QLineEdit()
        self.wynik = QLineEdit()

        # układ tabelaryczny
        ukladT = QGridLayout()
        ukladT.addWidget(etykieta1, 0, 0)
        ukladT.addWidget(etykieta2, 0, 1)
        ukladT.addWidget(etykieta3, 0, 2)
        ukladT.addWidget(self.liczba1, 1, 0)
        ukladT.addWidget(self.liczba2, 1, 1)
        ukladT.addWidget(self.wynik, 1, 2)

        # przyciski
        dodajBtn = QPushButton("&Dodaj", self)
        odejmijBtn = QPushButton("&Odejmij", self)
        mnozBtn = QPushButton("&Mnóż", self)
        dzielBtn = QPushButton("D&ziel", self)

        ukladH = QHBoxLayout()
        ukladH.addWidget(dodajBtn)
        ukladH.addWidget(odejmijBtn)
        ukladH.addWidget(mnozBtn)
        ukladH.addWidget(dzielBtn)

        ukladT.addLayout(ukladH, 2, 0, 1, 3)

        koniecBtn = QPushButton("&Koniec", self)
        ukladT.addWidget(koniecBtn, 3, 0, 1, 3)

        self.setLayout(ukladT)

        # obsługa zdarzeń
        koniecBtn.clicked.connect(self.koniec)
        dodajBtn.clicked.connect(self.dzialanie)

        self.resize(300, 200)
        self.setWindowTitle("Prosty kalkulator")
        self.show()

    def closeEvent(self, event):

        odp = QMessageBox.question(
            self, 'Komunikat',
            "Czy na pewno koniec?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if odp == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def koniec(self):
        self.close()

    def dzialanie(self):
        nadawca = self.sender()

        try:

            liczba1 = float(self.liczba1.text())
            liczba2 = float(self.liczba2.text())

            if nadawca.text() == "&Dodaj":
                wynik = liczba1 + liczba2
            else:
                pass

            self.wynik.setText(str(wynik))

        except (ValueError, ZeroDivisionError):
            QMessageBox.warning(self, "Błąd", "Błędne dane!", QMessageBox.Ok)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Kalkulator()
    sys.exit(app.exec_())
