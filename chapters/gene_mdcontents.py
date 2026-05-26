import os

def sort_txt_files():
    # 当前脚本所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    txt_list = []

    # 遍历目录文件
    for file in os.listdir(current_dir):
        # 筛选 txt 文件，排除自身生成的 contents.txt
        if file.lower().endswith(".txt") and file != "contents.txt":
            name_without_suffix = os.path.splitext(file)[0]
            txt_list.append(name_without_suffix)

    # 按 az09 标准排序
    txt_list.sort()

    # 写入 contents.txt
    with open(os.path.join(current_dir, "contents.txt"), "w", encoding="utf-8") as f:
        for name in txt_list:
            f.write(f"{name}\n")

    print("排序完成，已生成 contents.txt")

if __name__ == "__main__":
    sort_txt_files()
