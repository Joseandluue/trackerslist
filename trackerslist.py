import requests
from datetime import datetime

# 要下载的文件链接列表
urls = [
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt",
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_ip.txt",
]

# 下载文件并保存到内存中
def download_file(url):
    response = requests.get(url)
    return response.content

# 合并文件并去除空行
def merge_files(contents):
    merged_content = ""
    for content in contents:
        lines = content.decode().split("\n")
        for line in lines:
            line = line.strip()  # 去除首尾空格和换行符
            if line:  # 如果不是空行则加入合并内容
                merged_content += line + "\n"
    return merged_content

# 下载文件并保存到内存中
file_contents = []
for url in urls:
    file_content = download_file(url)
    file_contents.append(file_content)

# 合并文件并去除空行
merged_content = merge_files(file_contents)

# 添加当前时间到合并结果的第一行，同时在第一行下方添加一个空行
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("当前时间:" + {current_time})
merged_content_with_time = f"更新时间: {current_time}\n\n{merged_content}"

# 保存合并结果到文件
output_file = "trackerslist.txt"
with open(output_file, "w") as file:
    file.write(merged_content_with_time)

print("文件已合并为 " + output_file)
