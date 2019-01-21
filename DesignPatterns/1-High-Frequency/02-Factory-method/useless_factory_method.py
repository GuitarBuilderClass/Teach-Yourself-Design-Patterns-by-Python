#! /usr/bin/env python3
"""本番ではデータベースに接続するが、開発中はcsvファイルを使う"""
from typing import List


class FileDataObject:
    def __init__(self) -> None:
        self.data_list: List[str] = list()

        with open('test.csv', 'r') as f:
            for line in f:
                self.data_list.append(line)

    def fetch_data_object(self, row_num: int) -> str:
        return self.data_list[row_num]


class DbDataObject:
    """未実装クラスだが、将来的に FileDataObject と差し替える予定"""

    def __init__(self) -> None:
        # DBへの接続手続きなど
        pass

    def fetch_data_object(self, row_num: int) -> str:
        pass


class Client:
    def __init__(self) -> None:
        # あとでFileDataObjectからDbDataObjectへ変更するときは
        # ここで呼び出すクラスを変更すればよいという目論見

        # ただし、Clientを呼び出すたびにFileDataObjectクラスが生成される
        self.data_object: FileDataObject = FileDataObject()

    def operating(self, row_num: int) -> str:
        person: str = self.data_object.fetch_data_object(row_num)
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
