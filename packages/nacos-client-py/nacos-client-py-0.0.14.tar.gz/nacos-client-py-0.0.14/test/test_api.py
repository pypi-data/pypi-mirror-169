import makepath
from nacos_client import NacosClient

import config

nc = NacosClient(**config.NACOS_CONFIG)
nc.get_config('BASE-CONFIG', 'public')
# nc.add_config_listener()


@nc.request(service='xxxxx', path='/proxy', method='GET', group_name='public')
def get_proxy():
    pass


print(get_proxy(headers={'Authorization': 'Token 11111'}))
