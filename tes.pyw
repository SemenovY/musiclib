# from PySide6.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTextBrowser
# from PySide6.QtUiTools import QUiLoader
# from PySide6.QtCore import QFile
#
# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         # Загрузка файла .ui
#         loader = QUiLoader()
#         ui_file = QFile('/home/yuriy/dev/musiclib/test_v2.ui')
#         ui_file.open(QFile.ReadOnly)
#         self.ui = loader.load(ui_file)
#         ui_file.close()
#
#         # Получение объектов виджетов из файла .ui
#         treeWidget = self.ui.findChild(QTreeWidget, 'treeWidget')
#         textBrowser = self.ui.findChild(QTextBrowser, 'textBrowser')
#
#         # Установка соединения между сигналом и слотом
#         treeWidget.itemClicked.connect(textBrowser.show)
#
#         # Установка загруженного интерфейса как главного виджета
#         self.setCentralWidget(self.ui)
#
# if __name__ == '__main__':
#     app = QApplication([])
#     window = MyWindow()
#     window.show()
#     app.exec()
from PySide6.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTextBrowser, QTreeWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QCoreApplication, QFile

# Установка опции Qt::AA_ShareOpenGLContexts до создания QCoreApplication
import sys
from PySide6.QtCore import Qt
QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        ui_file = QFile('/home/yuriy/dev/musiclib/test_v2.ui')  # Путь к вашему файлу .ui
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file)
        ui_file.close()

        treeWidget = self.ui.findChild(QTreeWidget, 'treeWidget')

        # Привязываем событие itemClicked к обработчику
        treeWidget.itemClicked.connect(self.on_item_clicked)

        self.setCentralWidget(self.ui)

    def on_item_clicked(self, item: QTreeWidgetItem):
        textBrowser = self.ui.findChild(QTextBrowser, 'textBrowser')

        # Получаем текст текущей выбранной строки в treeWidget
        selected_text = item.text(0)  # Предполагается, что text(0) содержит текст строки

        # Выполняем нужные действия в зависимости от текста строки
        if selected_text == 'первая строка':
            textBrowser.hide()
        elif selected_text == 'вторая строка':
            textBrowser.show()


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
