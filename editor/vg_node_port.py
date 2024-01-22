#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：Chen GangQiang
@Date    ：2024/1/19 19:03 
@Desc    ：
"""

from PySide6.QtWidgets import QGraphicsItem
from PySide6.QtGui import QColor, QPen, QBrush, QPainter, QPainterPath, QPolygonF, QFont
from PySide6.QtCore import QRectF, Qt, QPointF


class NodePort(QGraphicsItem):
    PORT_TYPE_EXEC_IN = 1001
    PORT_TYPE_EXEC_OUT = 1002
    PORT_TYPE_PARAM = 1003
    PORT_TYPE_OUTPUT = 1004

    def __init__(self, port_label='', port_class='str', port_color="#ffffff", port_type=PORT_TYPE_EXEC_IN, parent=None):
        super().__init__(parent)

        self._port_label = port_label
        self._port_class = port_class
        self._port_color = QColor(port_color)
        self._port_type = port_type

        self._pen_default = QPen(QColor(self._port_color))  # 默认边框颜色
        self._pen_default.setWidth(1.5)  # 默认边框宽度
        self._brush_default = QBrush(QColor(self._port_color))  # 默认填充颜色
        self._font_size = 12
        self._port_font = QFont('Arial', self._font_size)

        self._port_icon_size = 20
        self._port_label_size = len(self._port_label) * self._font_size
        self._port_width = self._port_icon_size + self._port_label_size

    def boundingRect(self):
        return QRectF(0, 0, self._port_width, self._port_icon_size)

    def add_to_parent_node(self, parent_node, scene):
        self.setParentItem(parent_node)
        self._parent = parent_node
        self._scene = scene


class EXECPort(NodePort):
    def __init__(self, port_label='', port_class='str', port_color="#ffffff", port_type=NodePort.PORT_TYPE_EXEC_IN,
                 parent=None):
        super().__init__(port_label, port_class, port_color, port_type, parent)

    def paint(self, painter: QPainter, option, widget=None) -> None:
        port_outline = QPainterPath()
        poly = QPolygonF()
        poly.append(QPointF(0, 0.2 * self._port_icon_size))
        poly.append(QPointF(0.25 * self._port_icon_size, 0.2 * self._port_icon_size))
        poly.append(QPointF(self._port_icon_size * 0.5, self._port_icon_size * 0.5))
        poly.append(QPointF(0.25 * self._port_icon_size, 0.8 * self._port_icon_size))
        poly.append(QPointF(0, 0.8 * self._port_icon_size))

        port_outline.addPolygon(poly)

        painter.setPen(self._pen_default)
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(port_outline.simplified())


class EXECInPort(EXECPort):
    def __init__(self, port_label='', port_class='str', port_color="#ffffff", port_type=NodePort.PORT_TYPE_EXEC_IN,
                 parent=None):
        super().__init__(port_label, port_class, port_color, port_type, parent)


class EXECOutPort(EXECPort):
    def __init__(self, port_label='', port_class='str', port_color="#ffffff", port_type=NodePort.PORT_TYPE_EXEC_OUT,
                 parent=None):
        super().__init__(port_label, port_class, port_color, port_type, parent)


class ParamPort(NodePort):
    def __init__(self, port_label='', port_class='str', port_color="#ffffff", port_type=NodePort.PORT_TYPE_PARAM,
                 parent=None):
        super().__init__(port_label, port_class, port_color, port_type, parent)

    def paint(self, painter, option, widget=...):
        # 画圆
        painter.setPen(self._pen_default)
        painter.setBrush(Qt.NoBrush)
        painter.drawEllipse(QPointF(self._port_icon_size * 0.25, self._port_icon_size * 0.5),
                            self._port_icon_size * 0.25, self._port_icon_size * 0.25)

        # 画小三角
        poly = QPolygonF()
        poly.append(QPointF(self._port_icon_size * 0.6, self._port_icon_size * 0.35))
        poly.append(QPointF(self._port_icon_size * 0.75, self._port_icon_size * 0.5))
        poly.append(QPointF(self._port_icon_size * 0.6, self._port_icon_size * 0.65))
        painter.setBrush(self._brush_default)
        painter.setPen(Qt.NoPen)
        painter.drawPolygon(poly)

        # 画文字
        painter.setPen(self._pen_default)
        painter.drawText(
            QRectF(self._port_icon_size, 0.1 * self._port_icon_size, self._port_label_size, self._port_icon_size),
            Qt.AlignmentFlag.AlignLeft, self._port_label)


class OutputPort(NodePort):
    def __init__(self, port_label='', port_class='str', port_color="#ffffff", port_type=NodePort.PORT_TYPE_OUTPUT,
                 parent=None):
        super().__init__(port_label, port_class, port_color, port_type, parent)

    def paint(self, painter, option, widget=...):
        # 画文字
        painter.setPen(self._pen_default)
        painter.drawText(
            QRectF(0, 0.1 * self._port_icon_size, self._port_label_size, self._port_icon_size),
            Qt.AlignmentFlag.AlignRight, self._port_label)


        # 画圆
        painter.setPen(self._pen_default)
        painter.setBrush(Qt.NoBrush)
        painter.drawEllipse(QPointF(self._port_label_size + self._port_icon_size * 0.5, self._port_icon_size * 0.5),
                            self._port_icon_size * 0.25, self._port_icon_size * 0.25)

        # 画小三角
        poly = QPolygonF()
        poly.append(QPointF(self._port_label_size + self._port_icon_size * 0.85, self._port_icon_size * 0.35))
        poly.append(QPointF(self._port_label_size + self._port_icon_size * 1, self._port_icon_size * 0.5))
        poly.append(QPointF(self._port_label_size + self._port_icon_size * 0.85, self._port_icon_size * 0.65))
        painter.setBrush(self._brush_default)
        painter.setPen(Qt.NoPen)
        painter.drawPolygon(poly)

