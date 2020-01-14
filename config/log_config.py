import os
# 定义三种日志输出格式
from config.common import BASE_PATH

standard_format = '[%(levelname)s][%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s]' \
                  '\n[%(filename)s:%(lineno)d][%(message)s]'

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

# 日志目录
LOG_DIR = os.path.join(BASE_PATH, 'logs')

# 日志配置
LOGGING_DIC = {
    'version': 1,
    # 禁用已经存在的logger实例
    'disable_existing_loggers': False,
    # 日志格式化(负责配置log message 的最终顺序，结构，及内容)
    'formatters': {
        'distinct': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
        'less_simple': {
            'format': id_simple_format
        },
    },
    # 过滤器，决定哪个log记录被输出
    'filters': {},
    # 负责将Log message 分派到指定的destination
    'handlers': {
        # 打印到终端的日志
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'distinct'
        },
        # 打印到info文件的日志,收集info及以上的日志
        'info': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'simple',
            'filename': os.path.join(LOG_DIR, 'info.log'),  # 日志文件路径
            'maxBytes': 1024 * 1024 * 5,  # 日志大小 5M
            'backupCount': 5,  # 备份5个日志文件
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
        # 打印到error文件的日志,收集error及以上的日志
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'distinct',
            'filename': os.path.join(LOG_DIR, 'error.log'),  # 日志文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 5,  # 备份5个日志文件
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    # logger实例
    'loggers': {
        # 默认的logger应用如下配置
        'root': {
            'handlers': ['console'],  # log数据打印到控制台
            'level': 'DEBUG',
            'propagate': True,  # 向上（更高level的logger）传递
        },
        'default': {
            'handlers': ['console', 'info', 'error'],
            'level': 'INFO',
            'propagate': True,  # 向上（更高level的logger）传递
        },
        'info': {
            'handlers': ['console','info'],
            'level': 'INFO',
            'propagate': True,  # 向上（更高level的logger）传递
        },
        'error': {
            'handlers': ['console', 'error'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到控制台
            'level': 'ERROR'
        },

    },
}
