import sys
c = get_config()  #noqa
# 对外登录设置的ip
c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 8888
c.PAMAuthenticator.encoding = 'utf8'

c.Authenticator.allow_all = True
c.Authenticator.admin_users = {'ubuntu'}  # 管理员用户
c.JupyterHub.admin_access = True  # 则管理员有权在各自计算机上以其他用户身份登录，以进行调试
c.LocalAuthenticator.create_system_users=True  # 此选项通常用于 JupyterHub 的托管部署，以避免在启动服务之前手动创建所有 用户

# 设置每个用户的 book类型 和 工作目录（创建.ipynb文件自动保存的地方）
c.Spawner.notebook_dir = '~'
c.Spawner.default_url = ''
c.Spawner.args = ['--allow-root']

c.Authenticator.add_user_cmd = ['adduser']

c.JupyterHub.load_roles = [
    {
        "name": "jupyterhub-idle-culler-role",
        "scopes": [
            "list:users",
            "read:users:activity",
            "read:servers",
            "delete:servers",
            # "admin:users", # if using --cull-users
        ],
        # assignment of role's permissions to:
        "services": ["jupyterhub-idle-culler-service"],
    }
]

c.JupyterHub.services = [
    {
        "name": "jupyterhub-idle-culler-service",
        "command": [
            sys.executable,
            "-m", "jupyterhub_idle_culler",
            "--timeout=3600",
        ],
        # "admin": True,
    }
]


