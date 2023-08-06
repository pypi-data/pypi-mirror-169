### 编译
```
python3 setup.py build && python3 setup.py install
```
### 上传到pypi
```
twine upload dist/*
```
### 封装组件
1. MQ组件：rabbitmq
1. 对象存储：cos
1. 环境变量：env