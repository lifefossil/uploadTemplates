from itertools import islice

from utils import common_utils
import oss2


class Alioss:
    def __init__(self):
        alioss = common_utils.get_token()
        self.access_key_id = alioss.get("AccessKeyID")
        self.access_key_secret = alioss.get("AccessKeySecret")
        self.l_bucket = alioss.get("bucket")
        self.region = alioss.get("region")
        self.auth = oss2.Auth(self.access_key_id, self.access_key_secret)
        self.bucket = oss2.Bucket(self.auth, self.region, self.l_bucket)

    def upload_file(self, local_file_path, remote_file_path):
        self.bucket.put_object_from_file(remote_file_path, local_file_path)

    def list_files(self, prefix):
        for obj in oss2.ObjectIterator(self.bucket, prefix=prefix):
            print(obj.key)