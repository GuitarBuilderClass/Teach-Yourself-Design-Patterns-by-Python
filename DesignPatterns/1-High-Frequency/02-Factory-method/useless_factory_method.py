#! /usr/bin/env python3
"""本番ではデータベースに接続するが、開発中はcsvファイルを使う"""


class FileDataObject:
    def __init__(self):
        self.data_list = list()

        with open('test.csv', 'r') as f:
            for line in f:
                self.data_list.append(line)

    def read_data_object(self, id):
        return self.data_list[id]


class DbDataObject:
    """未実装クラスだが、将来的に FileDataObject と差し替える予定"""

    def __init__(self):
        # DBへの接続手続きなど
        pass

    def read_data_object(self, row_num):
        pass


class Client:
    def __init__(self):
        # あとでFileDataObjectからDbDataObjectへ変更するときは
        # ここで呼び出すクラスを変更すればよいという目論見

        # ただし、Clientを呼び出すたびにFileDataObjectクラスが生成される
        self.data_object = FileDataObject()

    def operating(self, id):
        person = self.data_object.read_data_object(id)
        return person


if __name__ == '__main__':
    client = Client()

    i = 0
    while True:
        try:
            print(client.operating(i), end="")
            i += 1
        except IndexError:
            break

    row = client.operating(1)
    print("\n")
    print(row)
