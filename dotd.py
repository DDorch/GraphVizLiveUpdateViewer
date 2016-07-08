## Deamon that compile GraphViz script into image and display it automatically when the script file is modified
# @author David Dorchies
# @date 07/07/2016

from PyQt5 import QtWidgets
import os
import sys


## Read a section in an .ini file and return a dictionnary
#  @param sIniFile Path to the .ini file to read
#  @param sSection Section name to read in the .ini file
#  @return Dictionnary of strings made from couples (key, value)
def GetItemsIniFile(sIniFile, sSection) :
    import configparser as cp
    CfgPrm = cp.ConfigParser()
    CfgPrm.read(sIniFile)
    #initialisation de dPrm : dictionnaire des paramètres généraux de la compilation
    dPrm={}
    if not CfgPrm.has_section(sSection):
        return {}
    for item in CfgPrm.items(sSection):
        dPrm[item[0]]=item[1]
    return dPrm


## Class that add the daemon to the QLabel object
class myLabel(QtWidgets.QLabel):
    
    def __init__(self):
        super( myLabel, self ).__init__()
        # Load parameters in dotd.ini
        self.dDOT = GetItemsIniFile("dotd.ini","DOT")
        self.mTime = 0 # Last modified file time  

    ## Daemon that run the GraphViz dot tool and display the image in a QLabel window   
    def daemon(self):
        from subprocess import call
        from PyQt5 import QtGui
        import datetime

        if self.mTime!=os.path.getmtime(sys.argv[1]):
            # Run DOT     
            tRunDOT = "{0} -T{1} \"{2}\" -o \"{2}.{1}\"".format(self.dDOT["exe"], self.dDOT["format"], sys.argv[1])
            call(tRunDOT)
            self.setWindowTitle("GraphViz {}.{} {}".format(sys.argv[1], self.dDOT["format"],     datetime.datetime.fromtimestamp(os.path.getmtime(sys.argv[1])).strftime('%Y-%m-%d %H:%M:%S')))
            pixmap = QtGui.QPixmap("{}.{}".format(sys.argv[1], self.dDOT["format"]))
            self.setPixmap(pixmap)
            self.setFixedSize(pixmap.size());
            self.show()
            self.mTime = os.path.getmtime(sys.argv[1])

## Main program
def main():  
    from PyQt5 import QtCore
    # Define script path (Cf. http://diveintopython.adrahon.org/functional_programming/finding_the_path.html)
    sCurrentPath = os.path.abspath(os.path.dirname(sys.argv[0]))
    os.chdir(sCurrentPath)
    
    # Bootstraping QT GUI
    app = QtWidgets.QApplication(sys.argv)
    label = myLabel()

    # Defining loop timer for the daemon
    timer = QtCore.QTimer()
    timer.timeout.connect(label.daemon)
    dDaemon = GetItemsIniFile("dotd.ini","DAEMON")
    timer.start(int(dDaemon["sleep"])) 
    
    # Exit script when the window is closed
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    