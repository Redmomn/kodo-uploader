import os

from qiniu import Auth, put_file


def get_env(key: str) -> str:
    return os.environ.get('INPUT_' + key.upper())


def upload_file(ak: str, sk: str, directory: str, bucket_name: str, tag: str, repo: str):
    """
    上传文件
    :param repo:
    :param ak:
    :param sk:
    :param directory: 本地文件目录
    :param bucket_name: 存储空间名称
    :param tag: github的tag
    :return:
    """
    q = Auth(ak, sk)

    files = get_filenames(directory)
    for file in files:
        token = q.upload_token(bucket_name, repo + "/releases/download/" + tag + "/" + file, 3600)
        put_file(token, repo + "/releases/download/" + tag + "/" + file, directory + file, version='v2')
    return


def get_filenames(directory: str) -> list[str]:
    """
    获取目录下所有的文件名
    :param directory:
    :return:
    """
    # 获取目录下的所有文件
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    return files
