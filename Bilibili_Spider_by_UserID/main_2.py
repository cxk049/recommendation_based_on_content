import subprocess
from py_mysql import fetch_uids_from_database as fetch_uid
from itertools import islice

def batch_process_uids(uid_list):
    processed_uids = []  # 用于存储已处理的 UID
    
    for uid in uid_list[:]:  # 使用 uid_list[:] 遍历副本，防止原列表修改影响循环
        print(f"开始处理用户 UID: {uid}")
        
        # 调用 main.py 并传入 uid
        result = subprocess.run(['python', 'main.py', '--uid', uid], capture_output=True, text=True)
        
        # 输出 main.py 的执行结果
        print(result.stdout)
        print(result.stderr)
        
        # 将处理过的 UID 添加到 processed_uids 列表，并从 uid_list 中移除
        processed_uids.append(uid)
        uid_list.remove(uid)
    
    # 返回已处理的 UID 列表
    return processed_uids , uid_list

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "fcx240719",
    "database": "SNM_learning"
}

# 定义用户 ID 字典
uid_dict = fetch_uid(db_config)

N = 900
uid_list = [uid for _, uid in islice(uid_dict.items(), N)]

#print(uid_list)

'''
a_list = uid_list[0:16]

print(a_list)

too_larger_list = ['686127']

processed_uids , unprocessed_uids = batch_process_uids(a_list)

print(processed_uids)
print(unprocessed_uids)
'''

b_list = uid_list[18:50]

print(b_list)

#processed_uids , unprocessed_uids = batch_process_uids(b_list)

#print(processed_uids)
#print(unprocessed_uids)



c_list = uid_list[51:100]

print(c_list)

#processed_uids , unprocessed_uids = batch_process_uids(c_list)

#print(processed_uids)
#print(unprocessed_uids)

#目前是完成了前100个uid的BVID的获取