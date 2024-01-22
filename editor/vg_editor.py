#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：Chen GangQiang
@Date    ：2024/1/19 19:02 
@Desc    ：
"""

from PySide6.QtWidgets import QWidget, QBoxLayout

from editor.vg_node_port import EXECInPort, EXECOutPort, ParamPort, OutputPort
from editor.vg_scene import VisualGraphScene
from editor.vg_view import VisualGraphView
from editor.vg_node import GraphNode


class VisualGraphEditor(QWidget):
    def __init__(self, parent=None):
        super(VisualGraphEditor, self).__init__(parent)

        self._view = None
        self._scene = None
        self.layout = None

        self.setup_editor()

        self.debug_add_node()

    def setup_editor(self):
        # 设置窗口大小
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Visual Graph")

        # 设置布局
        self.layout = QBoxLayout(QBoxLayout.LeftToRight, self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # 设置场景
        self._scene = VisualGraphScene(self)
        self._view = VisualGraphView(self._scene, self)

        self.layout.addWidget(self._view)

    def debug_add_node(self):
        params = []
        params.append(ParamPort("width", "int", "#99ff22"))
        params.append(ParamPort("height", "int", "#99ff22"))

        outputs = []
        outputs.append(OutputPort("area", "int", "#99ff22"))

        node = GraphNode(title="test", param_ports=params, output_ports=outputs, is_pure=False)
        self._view.add_graph_node(node, [-100, -100])
