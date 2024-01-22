#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：Chen GangQiang
@Date    ：2024/1/19 19:03 
@Desc    ：
"""

from PySide6.QtWidgets import QGraphicsView
from PySide6.QtGui import QPainter, QMouseEvent
from PySide6.QtCore import Qt, QEvent
from editor.vg_node import GraphNode


class VisualGraphView(QGraphicsView):
    def __init__(self, scene, parent=None):
        super(VisualGraphView, self).__init__(parent)

        # 设置视图
        self._scene = scene
        self.setScene(self._scene)

        # 设启用抗锯齿和平滑变换
        self.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform | QPainter.TextAntialiasing)

        # 设置视图更新模式
        self.setViewportUpdateMode(QGraphicsView.ViewportUpdateMode.FullViewportUpdate)

        # 设置滚动条
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # scale
        self._zoom_clamp = [0.5, 3]
        self._zoom_factor = 1.05
        self._view_scale = 1.0
        self._last_scale = 1.0
        # 以鼠标位置为中心缩放
        self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)

        # 画布拖动
        self._drag_mode = False

    def wheelEvent(self, event):
        """
        鼠标滚轮事件
        :param event: 事件
        """
        if not self._drag_mode:
            # 确定缩放因子。如果向上滚动（放大），使用 self._zoom_factor；向下滚动（缩小）时，使用其倒数。
            zoom_factor = self._zoom_factor if event.angleDelta().y() > 0 else 1 / self._zoom_factor

            # 试探性地更新视图的缩放级别，以检查是否超出缩放限制。
            new_scale = self._view_scale * zoom_factor

            # 检查新缩放级别是否在允许的范围内。
            if self._zoom_clamp[0] <= new_scale <= self._zoom_clamp[1]:
                # 如果新缩放级别在允许的范围内，更新视图的缩放级别并应用缩放。
                self._view_scale = new_scale
                self.scale(zoom_factor, zoom_factor)
                self._last_scale = self._view_scale  # 更新上一次的缩放级别

            # print(self._view_scale)

    @staticmethod
    def createMouseEvent(event_type, original_event):
        """
        辅助函数，用于创建鼠标事件
        """
        return QMouseEvent(event_type, original_event.localPos(), Qt.LeftButton, Qt.NoButton,
                           original_event.modifiers())

    def mousePressEvent(self, event):
        """
        鼠标按下事件
        """
        if event.button() == Qt.MouseButton.MiddleButton:
            if self.itemAt(event.pos()) is None:
                self._drag_mode = True  # 进入拖动模式
                release_event = self.createMouseEvent(QEvent.MouseButtonRelease, event)
                super().mouseReleaseEvent(release_event)

                self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)

                press_event = self.createMouseEvent(QEvent.MouseButtonPress, event)
                super().mousePressEvent(press_event)
                return

        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        """
        鼠标释放事件
        """
        if event.button() == Qt.MouseButton.MiddleButton and self._drag_mode:
            self._drag_mode = False  # 退出拖动模式
            release_event = self.createMouseEvent(QEvent.MouseButtonRelease, event)
            super().mouseReleaseEvent(release_event)

            self.setDragMode(QGraphicsView.DragMode.NoDrag)
            return

        super().mouseReleaseEvent(event)

    def mouseDoubleClickEvent(self, event):
        """
        鼠标双击事件
        """
        if event.button() == Qt.MouseButton.MiddleButton:
            # 重置视图的所有变换（如缩放和旋转），恢复到其初始状态
            self.resetTransform()
            self._view_scale = 1.0
        super().mouseDoubleClickEvent(event)

    def add_graph_node(self, node: GraphNode, pos=[0, 0]):
        self._scene.addItem(node)

        node.setPos(pos[0], pos[1])
        node.add_scene(self._scene)
