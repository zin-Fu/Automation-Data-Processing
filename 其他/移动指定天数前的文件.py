import argparse
import os
import shutil
import time

# 脚本的用途和使用说明
usage = "python move_files_over_x_days.py -src [SRC] -dst [DST] -days [DAYS]"
description = "将文件从源目录移动到目标目录，如果文件的修改时间超过指定的天数。默认是240天。"

# 设置参数解析器，定义命令行参数
args_parser = argparse.ArgumentParser(usage=usage, description=description)
args_parser.add_argument(
    "-src",
    "--src",
    type=str,
    nargs="?",
    default=".",
    help="（可选）文件将被移动的源目录，默认为当前目录",
)
args_parser.add_argument(
    "-dst",
    "--dst",
    type=str,
    nargs="?",
    required=True,
    help="（必选）文件将被移动的目标目录。",
)
args_parser.add_argument(
    "-days",
    "--days",
    type=int,
    nargs="?",
    default=240,
    help="（可选）指定文件最小的修改时间，以天为单位。默认是240天。",
)
args = args_parser.parse_args()

# 确保天数不为负
if args.days < 0:
    args.days = 0

# 设置源目录、目标目录和天数参数
src = args.src
dst = args.dst
days = args.days
now = time.time()

# 检查目标目录是否存在，不存在则创建
if not os.path.exists(dst):
    os.mkdir(dst)

# 遍历源目录中的所有文件
for f in os.listdir(src):
    # 计算文件的修改时间，如果文件修改时间超过指定天数，则移动文件
    if os.stat(f).st_mtime < now - days * 86400:
        if os.path.isfile(f):  # 确保是文件而非文件夹
            shutil.move(f, dst)  # 移动文件
