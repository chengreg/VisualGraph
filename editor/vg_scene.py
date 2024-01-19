#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：Chen GangQiang
@Date    ：2024/1/19 19:03 
@Desc    ：
"""

from PySide6.QtWidgets import QGraphicsScene
from PySide6.QtGui import QPen, QBrush, QColor

from editor.vg_config import EditorConfig


class VisualGraphScene(QGraphicsScene):
    def __init__(self, parent=None):
        super(VisualGraphScene, self).__init__(parent)

        # 设置背景颜色
        self.setBackgroundBrush(QBrush(QColor("#212121")))

        # 设置背景大小
        self._width = EditorConfig.editor_scene_width
        self._height = EditorConfig.editor_scene_height
        self.setSceneRect(-self._width/2, -self._height/2, self._width, self._height)


