#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：Chen GangQiang
@Date    ：2024/1/19 19:03 
@Desc    ：
"""

from PySide6.QtWidgets import QGraphicsView
from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt


class VisualGraphView(QGraphicsView):
    def __init__(self, scene, parent=None):
        super(VisualGraphView, self).__init__(parent)

        # 设置视图
        self._scene = scene
        self.setScene(self._scene)

        # 设启用抗锯齿和平滑变换
        self.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform | QPainter.TextAntialiasing)

        # 设置视图更新模式
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

        # 设置滚动条
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
