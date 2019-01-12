#! /usr/bin/env python3
from abc import ABCMeta, abstractmethod


class DataObject(metaclass=ABCMeta):
    """ABCMetaを利用して子クラスとなるFileDataObjectとDbDataObjectの切り替えを行なう"""

    @staticmethod
    def create():
        # クライアント側はFileDataObjectもDbDataObjectの存在を知る必要がなく
        # オブジェクト生成を一箇所にまとめられる
        return FileDataObject()

    @abstractmethod
    def read_data_object(self, id):
        # read_data_objectは抽象メソッドで、
        # 実際の処理は子メソッドで実装したものが実行される
        pass


class FileDataObject(DataObject):

    def __init__(self):
        self.data_list = list()

        with open('test.csv', 'r') as f:
            for line in f:
                self.data_list.append(line)

    def read_data_object(self, row_num):
        return self.data_list[row_num]


class DbDataObject(DataObject):
    """未実装クラスだが、将来的に FileDataObject と差し替える予定"""

    def __init__(self):
        # DBへの接続手続きなど
        pass

    def read_data_object(self, id_num):
        pass


class Client:

    def __init__(self):
        self.data_object = DataObject.create()

    def operating(self, num):
        # DataObject.create() で FileDataObject を呼び出しているため
        # 呼び出し元のクラスは FileDataObject から別のクラスへ容易に変更ができる
        # つまり、Client クラスは FileDataObject の存在を知らなくても FileDataObject を利用できる
        # DbDataObject への変更を Client クラス側で行なう必要がなくなる
        person = self.data_object.read_data_object(num)
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
