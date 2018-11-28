# usr/bin/env/ python3

from abc import abstractclassmethod


@abstractclassmethod
class RentalProduct(object):

    def __init__(self, title: str) -> None:
        """
        貸出状態のインスタンス化
        Args:
            self.title (str): 作品タイトル
            self.rental (bool): レンタル中フラグ

        """
        self.title = title
        self.rental = False


class CD(RentalProduct):

    def cd(self, title: str) -> None:
        """
        CDのインスタンス化
        Args:
            title (str): CDのタイトル

        """
        super().__init__(title)

    @staticmethod
    def calc(days: int) -> int:
        """
        CDの料金計算
        Args:
            days (int): 貸出日数

        Returns:
            CDの貸出料金 (int)

        """
        return 30 * days


class JapaneseCD(CD):

    def calc(self, days: int):
        """
        邦楽CDの料金計算
        Args:
            days (int): 貸出日数

        Returns:
            邦楽CDの貸出料金 (int)

        """
        return 40 * days


class ImportCD(CD):

    def calc(self, days: int):
        """
        洋楽CDの料金計算
        Args:
            days (int): 貸出日数

        Returns:
            洋楽CDの貸出料金 (int)

        """

        return 25 * days


class Video(RentalProduct):

    def video(self, title: str) -> None:
        """
        Videoのインスタンス化
        Args:
            title (str): Videoのタイトル

        """
        super().__init__(title)

    @staticmethod
    def calc(days: int) -> int:
        """
        Videoの料金計算
        Args:
            days (int): 貸出日数

        Returns:
            Videoの貸出料金 (int)

        """
        return 50 * days


class DVD(RentalProduct):

    def dvd(self, title: str) -> None:
        """
        Dvdのインスタンス化
        Args:
            title (str): DVDのタイトル

        """
        super().__init__(title)

    @staticmethod
    def calc(days: int) -> int:
        """
        DVDの料金計算
        Args:
            days (int): 貸出日数

        Returns:
            DVDの貸出料金 (int)

        """
        return 120 * days
