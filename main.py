import sys
import os
from time import strftime, gmtime
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow
from PyQt6.QtCore import QObject, pyqtSignal
import threading
from time import sleep
import subprocess

class Backend(QObject):

    def __init__(self):
        QObject.__init__(self)
    updated = pyqtSignal(str, arguments=['updater'])
    def updater(self, curr_time):
        self.updated.emit(curr_time)
    def bootUp(self):
        t_thread = threading.Thread(target=self._bootUp)
        t_thread.daemon = True
        t_thread.start()
    def _bootUp(self):
        while True:
            curr_time = strftime("%H:%M:%S", gmtime())
            engine.rootObjects()[0].setProperty('currTime', curr_time)
            self.updater(curr_time)
            #print(curr_time)
            sleep(1)

QQuickWindow.setSceneGraphBackend('software')
curr_time = strftime("%H:%M:%S", gmtime())
back_end = Backend()
sleep(0.1)
app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('./UI/main.qml')
engine.rootObjects()[0].setProperty('backend', back_end)
engine.rootObjects()[0].setProperty('currTime', curr_time)
back_end.bootUp()

# subprocess.call([r'H:\NutraBio\z_ Data-Backups\_Automated Directory Backups\ftpUpload-ProductImages.bat'])
# subprocess.call([r'H:\NutraBio\z_ Data-Backups\_Automated Directory Backups\backup.bat'])
# subprocess.call([r'H:\NutraBio\z_ Data-Backups\_Automated Directory Backups\ZipBrandingFolders.bat'])
# subprocess.call([r'H:\NutraBio\z_ Data-Backups\_Automated Directory Backups\Upload Test Results - Full Process.bat'])
sys.exit(app.exec())