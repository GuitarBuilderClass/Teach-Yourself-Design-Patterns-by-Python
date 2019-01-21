#! /usr/bin/env python3
from abc import ABC, ABCMeta, abstractmethod


class DataObject(metaclass=ABCMeta):
    @abstractmethod
    def read_data_object(self, num: int) -> str:
        # read_data_objectは抽象メソッドで、
        # 実際の処理は子メソッドで実装したものが実行される
        pass


class FileDataObject(DataObject):

    def __init__(self) -> None:
        self.data_list: list = list()

        with open('test.csv', 'r') as f:
            for line in f:
                self.data_list.append(line)

    def read_data_object(self, id_num: int) -> str:
        return self.data_list[id_num]


class DbDataObject(DataObject):
    """未実装クラスだが、将来的に FileDataObject と差し替える予定"""

    def __init__(self) -> None:
        # DBへの接続手続きなど
        pass

    def read_data_object(self, id_num: int) -> str:
        pass


class DefaultDataObject(DataObject):
    """デバッグ用クラスを実装する"""

    def __init__(self) -> None:
        pass

    def read_data_object(self, id_num: int) -> str:
        pass


class DataObjectFactory(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def create(self):
        pass
    #     if self._db_type == DbMode.STANDALONE:
    #         return FileDataObject()
    #     if self._db_type == DbMode.NETWORKING:
    #         return DbDataObject()
    #
    #     if self._db_type == DbMode.DEBUGGING: <- このように追加するとコード修正時に他の部分へ影響が出るかもしれない
    #         return DefaultDataObject()
    # そこで DataObjectFactory クラスをインターフェースにする


class FileDataObjectFactory(DataObjectFactory):
    def __init__(self) -> None:
        pass

    def create(self) -> FileDataObject:
        return FileDataObject()


class DbDataObjectFactory(DataObjectFactory):
    def __init__(self) -> None:
        pass

    def create(self) -> DbDataObject:
        return DbDataObject()


class DefaultObjectFactory(DataObjectFactory):
    def __init__(self) -> None:
        pass

    def create(self) -> DefaultDataObject:
        return DefaultDataObject()


class Client:

    def __init__(self) -> None:
        self.factory: DataObjectFactory = FileDataObjectFactory()
        self.data_object: DataObject = self.factory.create()

    def operating(self, num: int) -> str:
        # self.factory.create() で FileDataObject を呼び出しているため
        # 呼び出し元のクラスは FileDataObject から別のクラスへ容易に変更ができる
        # つまり、Client クラスは FileDataObject の存在を知らなくても FileDataObject を利用できる
        # DbDataObject への変更を Client クラス側で行なう必要がなくなる
        person: str = self.data_object.read_data_object(num)
        return person


if __name__ == '__main__':

    client1 = Client()

    i = 0
    while True:
        try:
            print(client1.operating(i), end="")
            i += 1
        except IndexError:
            break

    client2: Client = Client()
    row = client2.operating(1)
    print("\n")
    print(row)
