#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：Chen GangQiang
@Date    ：2024/1/19 19:03 
@Desc    ：
"""

import sys
from PySide6.QtWidgets import QApplication
from editor.vg_editor import VisualGraphEditor


if __name__ == '__main__':
    app = QApplication(sys.argv)
    vg_editor = VisualGraphEditor()
    vg_editor.show()
    sys.exit(app.exec())
