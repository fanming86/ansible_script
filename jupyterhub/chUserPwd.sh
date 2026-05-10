#!/bin/bash

# 检查输入文件是否提供
if [ $# -ne 1 ]; then
    echo "使用方法: $0 <用户信息文件>"
    echo "示例: $0 user_list.txt"
    exit 1
fi

USER_FILE="$1"

# 检查文件是否存在
if [ ! -f "$USER_FILE" ]; then
    echo "错误: 文件 $USER_FILE 不存在!"
    exit 1
fi

# 读取文件内容并处理
#while IFS='[:space:]+' read -r server_ip target_user new_password; do
while read -r server_ip target_user new_password; do

    echo "============================================="
    echo "正在处理服务器: $server_ip"
    echo "目标用户: $target_user"
    
    # 执行密码修改操作
    # 注意: 需确保ubuntu用户已配置免密登录或输入密码的方式
    #ssh ubuntu@"$server_ip" "echo -e '$new_password\n$new_password' | sudo passwd $target_user"
    ssh -n ubuntu@"$server_ip" "echo '$target_user:$new_password' | sudo chpasswd"

        # 检查命令执行结果
    if [ $? -eq 0 ]; then
        echo "✅ 服务器 $server_ip 的用户 $target_user 密码修改成功"
    else
        echo "❌ 服务器 $server_ip 的用户 $target_user 密码修改失败"
    fi
    
done < "$USER_FILE"

echo "============================================="
echo "所有服务器处理完毕"
