from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtCore import Slot
from PySide2.QtGui import QPen, QColor, QTransform
from ui_mainwindow import Ui_MainWindow
from particulas import Particulas
from particula import Particula


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.particulas = Particulas()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)
        self.ui.actionAbrir.triggered.connect(self.click_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.click_guardar_archivo)
        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

        self.ui.dibujar_pushButton.clicked.connect(self.dibujar)
        self.ui.limpiar_pushButton.clicked.connect(self.limpiar)

        self.ui.ordenar_id_pushButton.clicked.connect(self.ordenar_id)
        self.ui.ordenar_distancia_pushButton.clicked.connect(self.ordenar_distancia)
        self.ui.ordenar_velocidad_pushButton.clicked.connect(self.ordenar_velocidad)

        self.ui.actionGrafo.triggered.connect(self.mostrar_grafos)

        self.ui.action_busqueda.triggered.connect(self.busqueda)

    @Slot()
    def busqueda(self):
        self.particulas.peso()
        self.ui.salida.clear()

        origenes = (int(self.ui.origenx_lineEdit.text()),int(self.ui.origeny_lineEdit.text()))
        recorrido = self.particulas.recorrido_profundidad(origenes)

        print ("Profundidad")

        self.ui.salida.insertPlainText("Profundidad" + '\n')
        for i in recorrido:
            self.ui.salida.insertPlainText(str(i) + '\n')
            print(i)

        recorrido_2 = self.particulas.recorrido_amplitud(origenes)

        print ("\nAmplitud")

        self.ui.salida.insertPlainText('\n'"Amplitud" + '\n')
        for i in recorrido_2:
            self.ui.salida.insertPlainText(str(i) + '\n')
            print(i)

    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)
    
    @Slot()
    def mostrar_grafos(self):
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(self.particulas.mostrar_diccionario())

    @Slot()
    def ordenar_id(self):
        self.particulas.ordenarid()
    
    @Slot()
    def ordenar_distancia(self):
        self.particulas.ordenardistancia()

    @Slot()
    def ordenar_velocidad(self):
        self.particulas.ordenarvelocidad()

    @Slot()
    def dibujar(self):

        for particula in self.particulas:
            pen = QPen()
            pen.setWidth(1)
            c_red = particula.red
            c_green = particula.green
            c_blue = particula.blue
            color = QColor(c_red,c_green, c_blue)
            pen.setColor(color)

            c_origenx = particula.origenx       
            c_origeny = particula.origeny
            c_destinox = particula.destinox
            c_destinoy = particula.destinoy
            
            self.scene.addEllipse(c_origenx, c_origeny,.8,.8, pen)
            self.scene.addEllipse(c_destinox, c_destinoy,.8,.8, pen)
            self.scene.addLine(c_origenx, c_origeny, c_destinox, c_destinoy, pen)

    @Slot()
    def limpiar(self):
        self.scene.clear()

    @Slot()
    def buscar_id(self):
        ident = self.ui.buscar_lineEdit.text()
        encontrado = False
        for particula in self.particulas:
            if ident == str(particula.identificacion):
                self.ui.tabla.clear()
                self.ui.tabla.setRowCount(1)

                identificacion_widget = QTableWidgetItem(str(particula.identificacion))
                origenx_widget = QTableWidgetItem(str(particula.origenx))
                origeny_widget = QTableWidgetItem(str(particula.origeny))
                destinox_widget = QTableWidgetItem(str(particula.destinox))
                destinoy_widget = QTableWidgetItem(str(particula.destinoy))
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                red_widget = QTableWidgetItem(str(particula.red))
                blue_widget = QTableWidgetItem(str(particula.blue))
                green_widget = QTableWidgetItem(str(particula.green))
                d_widget = QTableWidgetItem(str(particula.d))

                self.ui.tabla.setItem(0, 0, identificacion_widget)
                self.ui.tabla.setItem(0, 1, origenx_widget)
                self.ui.tabla.setItem(0, 2, origeny_widget)
                self.ui.tabla.setItem(0, 3, destinox_widget)
                self.ui.tabla.setItem(0, 4, destinoy_widget)
                self.ui.tabla.setItem(0, 5, velocidad_widget)
                self.ui.tabla.setItem(0, 6, red_widget)
                self.ui.tabla.setItem(0, 7, blue_widget)
                self.ui.tabla.setItem(0, 8, green_widget)
                self.ui.tabla.setItem(0, 9, d_widget)

                encontrado = True
                return

        if not encontrado:
            QMessageBox.warning(
            self,
            "Atención",
            f'La particula con el id"{ident}"no fue encontrada'
            )

    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(10)
        headers = ["ID", "Origen en x", "Origen en y", "Destino en x", "Destino en y", "Velocidad", "Red", "Blue", "Green", "Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)
        self.ui.tabla.setRowCount(len(self.particulas))

        row = 0
        for particula in self.particulas:
            identificacion_widget = QTableWidgetItem(str(particula.identificacion))
            origenx_widget = QTableWidgetItem(str(particula.origenx))
            origeny_widget = QTableWidgetItem(str(particula.origeny))
            destinox_widget = QTableWidgetItem(str(particula.destinox))
            destinoy_widget = QTableWidgetItem(str(particula.destinoy))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            blue_widget = QTableWidgetItem(str(particula.blue))
            green_widget = QTableWidgetItem(str(particula.green))
            d_widget = QTableWidgetItem(str(particula.d))

            self.ui.tabla.setItem(row, 0, identificacion_widget)
            self.ui.tabla.setItem(row, 1, origenx_widget)
            self.ui.tabla.setItem(row, 2, origeny_widget)
            self.ui.tabla.setItem(row, 3, destinox_widget)
            self.ui.tabla.setItem(row, 4, destinoy_widget)
            self.ui.tabla.setItem(row, 5, velocidad_widget)
            self.ui.tabla.setItem(row, 6, red_widget)
            self.ui.tabla.setItem(row, 7, blue_widget)
            self.ui.tabla.setItem(row, 8, green_widget)
            self.ui.tabla.setItem(row, 9, d_widget)

            row +=1

    @Slot()
    def click_abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.particulas.abrir(ubicacion):
            QMessageBox.information(
                self, 
                "Éxito",
                "Se abrió el archivo" + ubicacion
            )
        else: 
            QMessageBox.critical(
                self, 
                "Error",
                "Error al abrir el archivo" + ubicacion
            )

    @Slot()
    def click_guardar_archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guadar Archivo',
            '.',
            'JSON(*.json)'
        )[0]
        print(ubicacion)
        if self.particulas.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se pudo crear el archivo" + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo" + ubicacion
            )

    @Slot()
    def click_mostrar(self):
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.particulas))

    @Slot()
    def click_agregar(self):
        identificacion = int(self.ui.id_lineEdit.text())
        origenx = int(self.ui.origenx_lineEdit.text())
        origeny = int(self.ui.origeny_lineEdit.text())
        destinox = int(self.ui.destinox_lineEdit.text())
        destinoy = int(self.ui.destinoy_lineEdit.text())
        velocidad = int(self.ui.velocidad_lineEdit.text())
        red = int(self.ui.red_lineEdit.text())
        green = int(self.ui.green_lineEdit.text())
        blue = int(self.ui.blue_lineEdit.text())

        particula = Particula(identificacion, origenx, origeny, destinox, destinoy, velocidad, red, green, blue)
        self.particulas.agregar_final(particula)

    @Slot()
    def click_agregar_inicio(self):
        identificacion = int(self.ui.id_lineEdit.text())
        origenx = int(self.ui.origenx_lineEdit.text())
        origeny = int(self.ui.origeny_lineEdit.text())
        destinox = int(self.ui.destinox_lineEdit.text())
        destinoy = int(self.ui.destinoy_lineEdit.text())
        velocidad = int(self.ui.velocidad_lineEdit.text())
        red = int(self.ui.red_lineEdit.text())
        green = int(self.ui.green_lineEdit.text())
        blue = int(self.ui.blue_lineEdit.text())

        particula = Particula(identificacion, origenx, origeny, destinox, destinoy, velocidad, red, green, blue)
        self.particulas.agregar_inicio(particula)
