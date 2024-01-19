#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：Chen GangQiang
@Date    ：2024/1/19 19:03 
@Desc    ：
"""

import math
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QGraphicsScene
from PySide6.QtGui import QPen, QBrush, QColor
from PySide6.QtCore import Qt, QLine

from editor.vg_config import EditorConfig


class VisualGraphScene(QGraphicsScene):
    def __init__(self, parent=None):
        super(VisualGraphScene, self).__init__(parent)

        self._width = EditorConfig.editor_scene_width
        self._height = EditorConfig.editor_scene_height
        self._grid_size = EditorConfig.editor_scene_grid_size
        self._grid_chunk = EditorConfig.editor_scene_grid_chunk

        # 设置背景颜色
        self.setBackgroundBrush(QBrush(QColor("#212121")))

        # 设置背景大小
        self.setSceneRect(-self._width / 2, -self._height / 2, self._width, self._height)

        # 画网格
        self._normal_line_pen = QPen(QColor(EditorConfig.editor_scene_grid_normal_color))
        self._normal_line_pen.setWidth(EditorConfig.editor_scene_grid_normal_line_width)

        self._dark_line_pen = QPen(QColor(EditorConfig.editor_scene_grid_dark_line_color))
        self._dark_line_pen.setWidth(EditorConfig.editor_scene_grid_dark_line_width)

    def drawBackground(self, painter: QPainter, rect) -> None:
        super(VisualGraphScene, self).drawBackground(painter, rect)

        # 计算网格线
        lines, dark_lines = self.cal_grid_lines(rect)

        # 画普通的线
        painter.setPen(self._normal_line_pen)
        painter.drawLines(lines)

        # 画深色的线
        painter.setPen(self._dark_line_pen)
        painter.drawLines(dark_lines)

    def cal_grid_lines(self, rect):
        """
        计算网格线
        :param rect: 视图的矩形区域
        :return: lines, dark_lines
        """
        left, top, right, bottom = math.floor(rect.left()), math.floor(rect.top()), math.ceil(rect.right()), math.ceil(
            rect.bottom())
        first_left = left - (left % self._grid_size)
        first_top = top - (top % self._grid_size)

        lines = []
        dark_lines = []

        # 画横线
        for v in range(first_top, bottom, self._grid_size):
            line = QLine(left, v, right, v)

            if v % (self._grid_size * self._grid_chunk) == 0:
                dark_lines.append(line)
            else:
                lines.append(line)

        # 画竖线
        for h in range(first_left, right, self._grid_size):
            line = QLine(h, top, h, bottom)

            if h % (self._grid_size * self._grid_chunk) == 0:
                dark_lines.append(line)
            else:
                lines.append(line)

        return lines, dark_lines
