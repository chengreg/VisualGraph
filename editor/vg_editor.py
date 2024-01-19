#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：Chen GangQiang
@Date    ：2024/1/19 19:02 
@Desc    ：
"""

from PySide6.QtWidgets import QWidget, QBoxLayout


class VisualGraphEditor(QWidget):
    def __init__(self, parent=None):
        super(VisualGraphEditor, self).__init__(parent)

        self.layout = None
        self.setup_editor()

    def setup_editor(self):
        # 设置窗口大小
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Visual Graph")

        # 设置布局
        self.layout = QBoxLayout(QBoxLayout.LeftToRight, self)
        self.layout.setContentsMargins(0, 0, 0, 0)


