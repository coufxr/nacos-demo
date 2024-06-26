import tomllib

import nacos_sdk_rust_binding_py as nacos

from settings import set_settings


class NacosService:
    service_name = "todo-service-name"

    def __init__(self):
        server_address = "127.0.0.1:8848"
        namespace = "python"
        username = "admin"
        password = "admin"
        app_name = "demo"

        self.data_id = "test_config"
        self.group = "DEFAULT_GROUP"

        client_options = nacos.ClientOptions(server_address, namespace, app_name, username, password, None, None)
        self.client = nacos.AsyncNacosConfigClient(client_options)
        self.naming_client = nacos.AsyncNacosNamingClient(client_options)
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
        config = tomllib.loads(res)
        print(config)

        set_settings(config)

    async def execute(self):
        # 获取配置，返回值为 `nacos.NacosConfigResponse`
        config_content_resp = await self.client.get_config_resp(self.data_id, self.group)
        self._load_config(config_content_resp)

        # 添加配置监听（对目标 data_id, group 配置变化的监听）
        await self.client.add_listener(self.data_id, self.group, self._load_config)

        # 添加配置监听（对目标 data_id, group 配置变化的监听）
        await self.naming_client.subscribe(
            self.service_name, self.group, None, self.subscribe_instances
        )

        # 注册服务实例
        await self.naming_client.register_instance(
            self.service_name, self.group, self.service_instance
        )


async def init_nacos():
    svr = NacosService()
    await svr.execute()
