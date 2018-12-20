#! /usr/bin/env python3

# 読み込み対象ファイル
FILE = "test.txt"


class FileDataObject:

    def __init__(self):
        self.data_list = list()

        with open(FILE, 'r') as f:
            for line in f:
                self.data_list.append(line)

    def read_data_object(self, row_num):
        return self.data_list[row_num]


class DbDataObject:
    """未実装クラスだが、将来的に FileDataObject と差し替える予定"""

    def __init__(self):
        # DBへの接続手続きなど
        pass

    def read_data_object(self, row_num):
        pass


class Client:
    def __init__(self):
        self.data_object = FileDataObject()

    def operating(self, row):
        person = self.data_object.read_data_object(row)
        return person


if __name__ == '__main__':
    client = Client()

    i = 0
    while True:
        try:
            print(client.operating(i))
            i += 1
        except IndexError:
            break
