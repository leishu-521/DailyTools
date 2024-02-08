import os
import shutil

def copy_files(src_root, dest_root):
    # 获取源文件夹下所有文件夹的列表
    folders = [f for f in os.listdir(src_root) if os.path.isdir(os.path.join(src_root, f))]

    for folder in folders:
        src_folder_path = os.path.join(src_root, folder)
        dest_folder_path = os.path.join(dest_root, folder)

        # 创建目标文件夹（如果不存在）
        if not os.path.exists(dest_folder_path):
            os.makedirs(dest_folder_path)
            print("创建新文件夹：{}".format(dest_folder_path))

        # 获取源文件夹中的所有文件
        files = [f for f in os.listdir(src_folder_path) if os.path.isfile(os.path.join(src_folder_path, f))]

        # 复制文件到目标文件夹
        for file in files:
            src_file_path = os.path.join(src_folder_path, file)
            dest_file_path = os.path.join(dest_folder_path, file)
            shutil.copy2(src_file_path, dest_file_path)

if __name__ == "__main__":
    src_root = "/media/zhurenzhang/c6007feb-7020-405a-8157-a8e2d400069f/home/zhurenzhang/Documents/zotero/storage"
    dest_root = "/home/zhurenzhang/Zotero/storage"


    copy_files(src_root, dest_root)
