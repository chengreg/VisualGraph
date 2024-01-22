from PySide6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem
import sys

app = QApplication(sys.argv)

scene = QGraphicsScene()

# 创建两个视图
view1 = QGraphicsView(scene)
view2 = QGraphicsView(scene)

# 在场景中添加椭圆图形项
ellipse_item = QGraphicsEllipseItem(0, 0, 100, 100)
scene.addItem(ellipse_item)

view1.show()
view2.show()
sys.exit(app.exec_())
