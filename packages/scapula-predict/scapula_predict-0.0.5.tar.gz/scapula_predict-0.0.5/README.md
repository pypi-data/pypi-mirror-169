# Scapula Predict

这是一个用于RTSA术式术前辅助设计的包。

它提供了关节盂平面确定、入钉位置计算两个功能。

这两个功能通过如下步骤实现：

1. 读入3D模型文件。
```python
import scapula_predict
s = scapula_predict.scapula('2.ply')
```
2. 选择关节盂平面并计算圆心。
```python
s.select_points()
s.computer_circle()
```
3. 将圆心移动至O点，并计算平面法向量。
```python
s.move_center_to_O()
s.find_vector()
```
4. 计算最合适的钉子位置
```python
s.find_nail()
print (s.location)
```
5. 计算导板面的模式
```python
s.find_guide()
```

我们同时提供了一个模型可视化的代码，它通过传递一个包含需要可视化模型的列表实现。
```python
s.show([s.mesh, s.cylinder, s.guide_mesh])
```