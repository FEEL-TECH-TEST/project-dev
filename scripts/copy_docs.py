import os
import shutil
from datetime import datetime

SRC_DIR = "docs/docs1"
DEST_DIR = "project-docs1_repo/docs"

today= datetime.now().strftime("%Y%m%d")


def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def generate_new_filename(dest_path):
    """同名ファイルが存在する場合、日付を付加して新しいファイル名を生成する"""
    dirname, filename = os.path.split(dest_path)

    if "." in filename:
        name, ext = filename.rsplit(".", 1)
        new_name = f"{name}_{today}.{ext}"
    else:
        new_name = f"{filename}_{today}"

    return os.path.join(dirname, new_name)


def copy_files():
    ensure_dir(DEST_DIR)

    for root, _, files in os.walk(SRC_DIR):
        for file in files:
            src_file = os.path.join(root, file)

            # サブディレクトリ構造維持したい場合
            rel_path= os.path.relpath(src_file, SRC_DIR)
            dest_file = os.path.join(DEST_DIR, rel_path)

            ensure_dir(os.path.dirname(dest_file))

            if os.path.exists(dest_file):
                dest_file = generate_new_filename(dest_file)

            shutil.copy2(src_file, dest_file)
            print(f"Copied: {src_file} -> {dest_file}")


if __name__ == "__main__":
    copy_files()