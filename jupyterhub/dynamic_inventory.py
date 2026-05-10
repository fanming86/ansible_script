#!/usr/bin/env python3
import sys
import json
from pathlib import Path

def parse_user_file(file_path):
    """解析用户文件，生成主机和用户信息"""
    hosts = {}
    
    try:
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                    
                parts = line.split()
                if len(parts) != 3:
                    print(f"警告: 格式不正确的行被忽略: {line}", file=sys.stderr)
                    continue
                    
                ip, username, password = parts
                
                # 为每个IP创建一个主机组
                group_name = f"host_{ip.replace('.', '_')}"
                
                # 初始化主机组
                if group_name not in hosts:
                    hosts[group_name] = {
                        "hosts": [ip],
                        "vars": {
                            "ansible_user": "root",
                            "ansible_password": password,  # 假设root密码与用户密码相同
                            "users": []
                        }
                    }
                
                # 添加用户信息到主机组变量
                hosts[group_name]["vars"]["users"].append({
                    "username": username,
                    "password": password
                })
                
    except Exception as e:
        print(f"错误: 无法读取文件 {file_path}: {str(e)}", file=sys.stderr)
        sys.exit(1)
        
    return hosts

def generate_ansible_inventory(hosts):
    """生成Ansible动态清单格式的JSON"""
    inventory = {
        "_meta": {
            "hostvars": {}
        }
    }
    
    # 添加所有主机组
    for group_name, group_data in hosts.items():
        inventory[group_name] = {
            "hosts": group_data["hosts"],
            "vars": group_data["vars"]
        }
        
        # 为主机添加变量
        for host in group_data["hosts"]:
            inventory["_meta"]["hostvars"][host] = {
                "ansible_user": "root",
                "ansible_password": group_data["vars"]["ansible_password"],
                "users": group_data["vars"]["users"]
            }
    
    return inventory

def main():
    """主函数"""
    # 默认文件路径
    default_file = "iplist"
    
    # 获取命令行参数
    if len(sys.argv) > 1:
        if sys.argv[1] in ['--list', '-l']:
            file_path = default_file
        else:
            file_path = sys.argv[1]
    else:
        file_path = default_file
    
    # 检查文件是否存在
    if not Path(file_path).exists():
        print(f"错误: 文件 {file_path} 不存在", file=sys.stderr)
        sys.exit(1)
    
    # 解析文件并生成清单
    hosts = parse_user_file(file_path)
    inventory = generate_ansible_inventory(hosts)
    
    # 输出生成的清单
    print(json.dumps(inventory, indent=2))

if __name__ == "__main__":
    main()
