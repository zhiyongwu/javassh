import pymysql
import os
import filetype
import json

_db_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'passwd',
    'use_unicode': True,
    'db': 'file_system',
    'charset': 'utf8'
}

conn = pymysql.connect(**_db_config)


class File:
    def __init__(self, path):
        self.path = path
        if not os.path.exists(self.path):
            return
        self.asb_path = os.path.abspath(self.path)
        self.file_name = os.path.splitext(os.path.split(self.path)[-1])[0]
        self.full_name = os.path.split(self.path)[-1]
        self.file_size = os.path.getsize(self.path)
        self.humanize_file_size = humanize_bytes(self.file_size)
        self.file_extension = os.path.splitext(os.path.split(self.path)[-1])[-1]
        file_type = 'unknown'
        file_selector = {
            filetype.is_audio: 'audio',
            filetype.is_archive: 'archive',
            filetype.is_image: 'image',
            filetype.is_video: 'video',
        }
        try:
            for func, returen_type in file_selector.items():
                if func(self.path):
                    file_type = returen_type
        except PermissionError:
            pass
        self.file_type = file_type
        self.json_format = json.dumps(self, default=lambda obj: obj.__dict__, ensure_ascii=False)

    def __str__(self) -> str:
        return (
                   "file : path = %s ,full_name =  %s, name = %s , file_size = %s , humanize_size = %s ,file_extension = %s ,file_type = %s  ") % (
                   self.path, self.full_name, self.file_name, self.file_size, self.humanize_file_size,
                   self.file_extension,
                   self.file_type
               )


def humanize_bytes(bytes, precision=1):
    abbrevs = (
        (1 << 50, 'PB'),
        (1 << 40, 'TB'),
        (1 << 30, 'GB'),
        (1 << 20, 'MB'),
        (1 << 10, 'kB'),
        (1, 'bytes')
    )
    if bytes == 1:
        return '1 byte'
    for factor, suffix in abbrevs:
        if bytes >= factor:
            break
    return '%.*f %s' % (precision, bytes / factor, suffix)


def list_files(path: str):
    for root, dirs, files in os.walk(path):
        for file_name in files:
            file = os.path.join(root, file_name)
            yield File(file)


if __name__ == '__main__':
    cur = conn.cursor()
    values = []
    for each in list_files("E:\\"):
        values.append((each.full_name, each.file_name, each.path, each.asb_path, each.file_extension, each.file_type,
                       each.file_size,
                       each.humanize_file_size))
    sql = "insert into local_files (full_name,file_name,file_path,abs_path,file_extension,file_type,file_size,humanize_file_size) values (%s,%s,%s,%s,%s,%s,%s,%s)"
    cur.executemany(sql, values)
    conn.commit()
