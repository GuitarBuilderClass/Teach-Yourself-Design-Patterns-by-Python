#! /usr/bin/env python3
from abc import ABCMeta, abstractmethod

FILE = 'test.txt'


class DataObject(metaclass=ABCMeta):

    @staticmethod
    def create():
        # 戻り値となるクラスを DataObject クラスを継承しているものと入れ替えれば
        # Client クラス側は DataObject.create() を呼び出すだけでよく、変更後の影響範囲は少ない
        return FileDataObject()

    @abstractmethod
    def read_data_object(self, num):
        pass


class FileDataObject(DataObject):

    def __init__(self):
        self.data_list = list()

        with open(FILE, 'r') as f:
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
        # つまり、 Client クラスはFileDataObject の存在を知らなくても FileDataObject を利用できる
        # コーディングする時は DataObject.create() を呼び出すだけなので Client クラス側には変更の影響が少なくなる
        person = self.data_object.read_data_object(num)
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
