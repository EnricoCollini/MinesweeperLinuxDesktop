#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:40:10 2019

@author: enrico
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 14:12:58 2019

@author: enrico
"""

# Import stuff
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from Controller import Controllore


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Controllore()
    window.show()
    app.exec_()
