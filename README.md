# nacos-demo

使用 [`nacos-sdk-rust-binding-py`](https://github.com/opc-source/nacos-sdk-rust-binding-py) 库作为 nacos 的 python sdk  支持 api2.0接口和异步  
使用 [`rnacos`](https://github.com/nacos-group/r-nacos) 作为测试服务端

测试使用nacos的一个demo  
数据库连接等 好像无法在修改后进行重新初始化

---

## django

需要在nacos的监听回调函数中对 django.conf.settings 进行修改.

--- 

## flask

推荐在使用 settings 的地方 进行依赖注入,  
否则始终需要从 settings.py 中导入 `get_settings` 函数

--- 

## fastapi

支持异步  
使用依赖注入获取 settings 接口侧使用方便, 但其他地方使用依旧会遇到 flask 的问题
