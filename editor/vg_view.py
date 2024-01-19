#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：Chen GangQiang
@Date    ：2024/1/19 19:03 
@Desc    ：
"""

from PySide6.QtWidgets import QGraphicsView


class VisualGraphView(QGraphicsView):
    def __init__(self, scene, parent=None):
        super(VisualGraphView, self).__init__(parent)

        # 设置视图
        self._scene = scene
        self.setScene(self._scene)
