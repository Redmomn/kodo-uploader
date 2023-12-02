import os
from src.utils import get_env

access_key: str
secret_key: str
upload_dir: str
bucket_name: str
tag: str


# TODO 在上传单个文件的函数实现解析文件的本地路径和上传到存储空间的路径

def init():
    access_key = get_env('access_key')
    secret_key = get_env('secret_key')
    upload_dir = get_env('upload_dir')
    bucket_name = get_env('bucket_name')
    tag = os.environ.get('TAG')
    global access_key, secret_key, upload_dir, bucket_name, tag


def main():
    init()


if __name__ == '__main__':
    main()
