#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：Chen GangQiang
@Date    ：2024/1/19 19:03 
@Desc    ：
"""
from PySide6.QtGui import QPen, QColor, QBrush, QPainterPath, QFont
from PySide6.QtWidgets import QGraphicsItem, QGraphicsTextItem
from PySide6.QtCore import QRectF, Qt
from editor.vg_node_port import NodePort


class GraphNode(QGraphicsItem):
    def __init__(self, title='', scene=None, parent=None):
        super().__init__(parent)

        self._title = title
        self._scene = scene

        # # 初始化节点的大小
        self._node_width = 240
        self._node_height = 160
        self.node_radius = 10

        # 初始化节点的边框样式
        self._pen_default = QPen(QColor("#151515"))  # 默认边框颜色
        self._pen_selected = QPen(QColor("#aaffee00"))  # 选中时的边框颜色

        # 初始化节点的背景样式
        self._brush_background = QBrush(QColor("#aa151515"))  # 背景颜色

        # 设置节点的交互属性：可选择、可移动
        self.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)

        # 设置节点title
        self._title_height = 35
        self._title_font = QFont('Arial', 13)
        self._title_color = Qt.white
        self._title_padding = 3
        self._brush_title_back = QBrush(QColor("#aa00003f"))

        self.init_title()

        # port
        self._port_padding = 10

    def add_scene(self, scene):
        self._scene = scene

    def init_title(self):
        self._title_item = QGraphicsTextItem(self)
        self._title_item.setPlainText(self._title)
        self._title_item.setFont(self._title_font)
        self._title_item.setDefaultTextColor(self._title_color)
        self._title_item.setPos(self._title_padding, self._title_padding)

    def boundingRect(self) -> QRectF:
        # 定义图形项的边界矩形，用于绘制和碰撞检测
        return QRectF(0, 0, self._node_width, self._node_height)

    def paint(self, painter, option, widget=None) -> None:
        # 绘制图形项的外观
        node_outline = QPainterPath()
        node_outline.addRoundedRect(0, 0, self._node_width, self._node_height, self.node_radius, self.node_radius)

        # 绘制背景
        painter.setPen(Qt.NoPen)  # 不使用边框
        painter.setBrush(self._brush_background)  # 设置背景画刷
        painter.drawPath(node_outline.simplified())

        # 绘制title背景
        title_outline = QPainterPath()
        title_outline.setFillRule(Qt.WindingFill)
        title_outline.addRoundedRect(0, 0, self._node_width, self._title_height, self.node_radius, self.node_radius)
        title_outline.addRect(0, self.node_radius, self.node_radius, self._title_height - self.node_radius)
        title_outline.addRect(self._node_width - self.node_radius, self.node_radius, self.node_radius,
                              self._title_height - self.node_radius)
        painter.setPen(Qt.NoPen)
        painter.setBrush(self._brush_title_back)
        painter.drawPath(title_outline.simplified())

        # 根据是否被选中绘制边框
        painter.setPen(self._pen_selected if self.isSelected() else self._pen_default)
        painter.setBrush(Qt.NoBrush)  # 不填充
        painter.drawPath(node_outline)

    def add_port(self, port):
        if port._port_type == NodePort.PORT_TYPE_EXEC_IN:
            self.add_exec_in_port(port)
        elif port._port_type == NodePort.PORT_TYPE_EXEC_OUT:
            self.add_exec_out_port(port)
        elif port._port_type == NodePort.PORT_TYPE_PARAM:
            self.add_param_port(port)
        elif port._port_type == NodePort.PORT_TYPE_OUTPUT:
            self.add_output_port(port)

    def add_exec_in_port(self, port: NodePort):
        port.add_to_parent_node(self, self._scene)
        port.setPos(self._port_padding, self._title_height)

    def add_exec_out_port(self, port: NodePort):
        port.add_to_parent_node(self, self._scene)

        x = self._node_width - port._port_width
        y = self._title_height
        port.setPos(x, y)

    def add_param_port(self, port: NodePort):
        port.add_to_parent_node(self, self._scene)
        port.setPos(self._port_padding, self._title_height + self._port_padding + port._port_icon_size)

    def add_output_port(self, port: NodePort):
        port.add_to_parent_node(self, self._scene)

        x = self._node_width - port._port_width - self._port_padding
        y = self._title_height + self._port_padding + port._port_icon_size
        port.setPos(x, y)