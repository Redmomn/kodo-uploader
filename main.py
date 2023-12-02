import os
from src.utils import get_env, upload_file

access_key: str
secret_key: str
upload_dir: str
bucket_name: str
tag: str
repo_path: str


# TODO 在上传单个文件的函数实现解析文件的本地路径和上传到存储空间的路径

def init():
    global access_key, secret_key, upload_dir, bucket_name, tag, repo_path
    access_key = get_env('access_key')
    secret_key = get_env('secret_key')
    upload_dir = get_env('upload_dir')
    bucket_name = get_env('bucket_name')
    tag = os.environ.get('TAG')
    repo_path = os.environ.get('REPO_PATH')



def main():
    init()
    upload_file(access_key, secret_key, upload_dir, bucket_name, tag, repo_path)


if __name__ == '__main__':
    main()
