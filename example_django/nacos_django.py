import json

import nacos_sdk_rust_binding_py as nacos
from django.conf import settings

config: dict


class NacosService:
    service_name = "todo-service-name"

    def __init__(self):
        server_address = "127.0.0.1:8848"
        namespace = "python"
        username = "admin"
        password = "admin"
        app_name = "demo"

        self.data_id = "django_config"
        self.group = "DEFAULT_GROUP"

        client_options = nacos.ClientOptions(server_address, namespace, app_name, username, password, None, None)
        self.client = nacos.NacosConfigClient(client_options)
        self.naming_client = nacos.NacosNamingClient(client_options)
        self.service_instance = nacos.NacosServiceInstance("127.0.0.1", 8080)

    @staticmethod
    def subscribe_instances(instances: [nacos.NacosServiceInstance]):
        """自定义服务订阅函数，接受的参数为 `nacos.NacosConfigResponse`"""
        print(f"subscribe_instances,instances={str(instances)}")
        for ins in instances:
            print(f"subscribe_instances,instances[x].ip={ins.ip}")

    @staticmethod
    def _load_config(resp: nacos.NacosConfigResponse):
        res = resp.content

        global config
        config = json.loads(res)
        print(config)

        # 在这里对 settings 中的变量进行替换
        # 但好像无法切换数据库连接等需要程序初始化的配置
        for k, v in config.items():
            setattr(settings, k, v)

    def execute(self):
        # 获取配置，返回值为 `nacos.NacosConfigResponse`
        config_content_resp = self.client.get_config_resp(self.data_id, self.group)
        self._load_config(config_content_resp)

        # 添加配置监听（对目标 data_id, group 配置变化的监听）
        self.client.add_listener(self.data_id, self.group, self._load_config)

        # 添加配置监听（对目标 data_id, group 配置变化的监听）
        self.naming_client.subscribe(
            self.service_name, self.group, None, self.subscribe_instances
        )

        # 注册服务实例
        self.naming_client.register_instance(
            self.service_name, self.group, self.service_instance
        )


def init_nacos():
    svr = NacosService()
    svr.execute()
