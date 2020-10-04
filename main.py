import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
import pyqtgraph as pg



time = QtCore.QTime(00, 00, 00)
class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.current_page = 1
        self.year = [1985, 1990, 1995, 2000, 2005, 2010, 2015]
        self.year2 = [1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
        self.co2_detailed = [349.2455, 353.1911, 353.2114, 361.1918, 359.0334, 359.9294, 362.4789, 362.8766, 360.5145, 363.6523, 366.3633, 366.8917, 369.3032, 371.8859, 372.7013, 374.2448, 376.7752, 379.0771, 386.2578, 383.1204, 387.1723, 388.4726, 389.3948, 390.8826, 392.9254, 395.7466, 399.8249, 399.2103, 403.2681, 404.1179, 407.4729, 411.3681, 411.4201, 415.7653]
        self.n2o = [304.471, 308.091, 311.628, 315.710, 319.557, 323.172, 327.060]
        self.ch4 = [1650.347, 1715.451, 1751.392, 1770.643, 1773.296, 1810.512, 1847.842]
        self.co2_2018 = [415.8542, 415.8523, 415.8451, 415.8291, 415.8054, 415.7759, 415.7382, 415.6971, 415.6483, 415.6077, 415.5788, 415.5766]
        self.co2 = [344.730, 353.917, 360.028, 369.099, 379.183, 388.208, 400.024]
        self.dates = [1,2,3,4,5,6,7,8,9,10,11,12]
        self.styles = {"color" : "k", "font-size": "20px"}
        self.pen = pg.mkPen(color=(255,0,0))
        self.pie1()
        self.pie2()
        self.graph1()
        self.graph2()
        self.graph3()
        self.graph4()





        self.previousButton = QtWidgets.QPushButton("Previous Page")
        self.nextButton = QtWidgets.QPushButton("Next Page")
        self.nextButton.clicked.connect(self.next_button)
        self.previousButton.clicked.connect(self.previous_button)
        self.teamName = QtWidgets.QLabel("Apophis")
        self.info = QtWidgets.QLabel("""        In accordance with the data calculated, 
        petrol rafineries,iron and steel factories account 
        for 10% of the carbon emissions in the region and Izmir
        """)
        self.logo = QtWidgets.QLabel()
        self.logo.setPixmap(QtGui.QPixmap("logo.jpeg"))
        self.HBoxlayout1 = QtWidgets.QHBoxLayout() #UstGrafHBox
        self.HBoxlayout2 = QtWidgets.QHBoxLayout() #AltGrafHBox
        self.VBoxlayout1 = QtWidgets.QVBoxLayout() #GrafToplamVBox
        self.HBoxlayout3 = QtWidgets.QVBoxLayout() #PanelHBox
        self.HBoxlayout4 = QtWidgets.QHBoxLayout() #UIHBox
        self.HBoxlayout1.addWidget(self.chartview)
        self.HBoxlayout1.addWidget(self.chartview2)
        self.HBoxlayout1.addWidget(self.chartview2)
        self.VBoxlayout1.addLayout(self.HBoxlayout1)
        self.HBoxlayout3.addWidget(self.logo)
        self.HBoxlayout3.addWidget(self.teamName)
        self.HBoxlayout3.addWidget(self.nextButton)
        self.HBoxlayout3.addWidget(self.previousButton)
        self.HBoxlayout3.addWidget(self.info)
        self.HBoxlayout3.addStretch()
        self.HBoxlayout4.addLayout(self.VBoxlayout1)

        self.HBoxlayout4.addLayout(self.HBoxlayout3)

        self.setLayout(self.HBoxlayout4)
        self.setWindowTitle("Apophis")



    def graph1(self):
        self.n2ograph = pg.PlotWidget()
        self.n2ograph.setBackground("w")
        self.n2ograph.setTitle("N2O", color="k", size="20pt")
        self.n2ograph.setLabel("left", "ppb", **self.styles)
        self.n2ograph.setLabel("bottom", "Years", **self.styles)
        self.n2ograph.plot(self.year, self.n2o, pen=self.pen)

    def graph2(self):
        self.ch4graph = pg.PlotWidget()
        self.ch4graph.setBackground("w")
        self.ch4graph.setTitle("CH4", color="k", size="20pt")
        self.ch4graph.setLabel("left", "ppb", **self.styles)
        self.ch4graph.setLabel("bottom", "Years", **self.styles)
        self.ch4graph.plot(self.year, self.ch4, pen=self.pen)
    def graph3(self):
        self.co2graph = pg.PlotWidget()
        self.co2graph.setBackground("w")
        self.co2graph.setTitle("CO2", color="k", size="20pt")
        self.co2graph.setLabel("left", "ppm", **self.styles)
        self.co2graph.setLabel("bottom", "Years", **self.styles)
        self.co2graph.plot(self.year, self.co2, pen=self.pen)

    def graph4(self):
        self.co2graph2 = pg.PlotWidget()
        self.co2graph2.setBackground("w")
        self.co2graph2.setTitle("CO2", color="k", size="20pt")
        self.co2graph2.setLabel("left", "ppm", **self.styles)
        self.co2graph2.setLabel("bottom", "Years", **self.styles)
        self.co2graph2.plot(self.year2, self.co2_detailed, pen=self.pen)
    def pie1(self):
        series = QPieSeries()
        series.append("O2", 56.7)
        series.append("N2", 210.6)
        series.append("CO2", 1.08)
        series.append("Other", 2.592)

        slice = QPieSlice()
        slice = series.slices()[2]
        slice.setExploded(True)
        slice.setLabelVisible(True)
        slice.setPen(QPen(Qt.darkGreen, 2))
        slice.setBrush(Qt.green)

        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Gas Rates in Atmosphere")

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        self.chartview = QChartView(chart)
        self.chartview.setRenderHint(QPainter.Antialiasing)

    def pie2(self):
        series = QPieSeries()
        series.append("CH4", 37.8)
        series.append("N2O", 21.6)
        series.append("CO2", 207.9)
        series.append("F-gases", 2.7)

        slice = QPieSlice()
        slice = series.slices()[2]
        slice.setExploded(True)
        slice.setLabelVisible(True)
        slice.setPen(QPen(Qt.darkGreen, 2))
        slice.setBrush(Qt.green)

        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Greenhouse Gases")

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        self.chartview2 = QChartView(chart)
        self.chartview2.setRenderHint(QPainter.Antialiasing)


    def next_button(self):
        print("Button clicked")
        self.current_page += 1
        print(self.current_page)
        if self.current_page == 2:
            self.HBoxlayout1.removeWidget(self.chartview)
            self.HBoxlayout1.removeWidget(self.chartview2)
            self.chartview.deleteLater()
            self.chartview2.deleteLater()
            self.HBoxlayout1.addWidget(self.n2ograph)
            self.HBoxlayout1.addWidget(self.co2graph)
            self.HBoxlayout1.addWidget(self.ch4graph)
            self.update()
            self.pie1()
            self.pie2()
            print(self.current_page)
        elif self.current_page == 3:
            self.HBoxlayout1.removeWidget(self.n2ograph)
            self.HBoxlayout1.removeWidget(self.co2graph)
            self.HBoxlayout1.removeWidget(self.ch4graph)
            self.ch4graph.deleteLater()
            self.co2graph.deleteLater()
            self.n2ograph.deleteLater()
            self.HBoxlayout1.addWidget(self.co2graph2)
            self.update()
            self.graph1()
            self.graph2()
            self.graph3()

    def previous_button(self):
        if self.current_page >= 2:
            print("Button clicked")
            self.current_page -= 1
            print(self.current_page)
            if self.current_page == 1:
                self.HBoxlayout1.removeWidget(self.n2ograph)
                self.HBoxlayout1.removeWidget(self.co2graph)
                self.HBoxlayout1.removeWidget(self.ch4graph)
                self.n2ograph.deleteLater()
                self.ch4graph.deleteLater()
                self.co2graph.deleteLater()
                self.HBoxlayout1.addWidget(self.chartview)
                self.HBoxlayout1.addWidget(self.chartview2)
                self.graph1()
                self.graph2()
                self.graph3()
                self.update()
            elif self.current_page == 2:
                self.HBoxlayout1.removeWidget(self.co2graph2)
                self.co2graph2.deleteLater()
                self.HBoxlayout1.addWidget(self.n2ograph)
                self.HBoxlayout1.addWidget(self.co2graph)
                self.HBoxlayout1.addWidget(self.ch4graph)
                self.update()
                self.graph4()











def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
