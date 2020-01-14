LOGIN_URL = 'http://192.168.163.194:9999'  # 登录地址
USERNAME = 'admin'  # 登录账号
PASSWORD = 'q1234567'  # 登录密码
NEW_PASSWORD = 'q1234567'  # 新登录密码

IP_ADDR = '192.168.163.194'  # IP地址
POOL_NAME = 'a2'
HOST_NAME = 'hostname_' + IP_ADDR.replace('.', '_')  # 主机名
NEW_HOST_NAME = HOST_NAME + '_new'

HOST_NAME_LIST = ["iscloud163-191", "iscloud163-192", "iscloud163-193"]

HOST_TYPE_NAME = "12盘位"  # 主机型号
NEW_HOST_TYPE_NAME = "24盘位"

START_IP_ADDR = '192.168.163.194'  # 起始IP地址
END_IP_ADDR = '192.168.163.194'  # 结束IP地址

VIRTUL_NIC_NAME = 'eth1'  # 虚拟网卡1名称
VIRTUL_NIC_IP = '77.77.77.66'  # 虚拟网卡IP

VIRTUL_NIC_NAME2 = 'eth2'  # 虚拟网卡2名称
VIRTUL_NIC_IP2 = '88.88.88.84'  # 虚拟网卡IP

VIRTUL_NIC_NAME_LIST = ['eth2']  # 虚拟网卡名称列表

IPV4_GATEWAY = VIRTUL_NIC_IP[:VIRTUL_NIC_IP.rindex('.')] + '.1'  # IPV4网关
IPV4_ADDR = START_IP_ADDR  # IPV4地址
IPV4_SUBNET_MASK = '255.255.0.0'  # 子网掩码

VIRTUL_NIC_TYPE = '高可用'  # 虚拟网卡类型 （高可用、负载均衡）

POOL_DESC = POOL_NAME + '的描述信息'

NEW_POOL_NAME = POOL_NAME + '_new'
NEW_POOL_DESC = POOL_DESC + '_new'
