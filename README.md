# pairwise-towing-hitch-joint

## 领域

游戏、图形与多媒体

## 主题

拖车铰接约束

## 说明

子步迭代、服务端挂接与载重阻尼。

初始状态下 `gameplay/towing_hitch_joint.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
