from __future__ import annotations
from datetime import datetime
from abc import abstractmethod


class RangeBroder:
    """
    An interface that defines all methods that must be implemented by concrete range border
    to make the borders comparable to each other.
    """
    @abstractmethod
    def __lt__(self, other: RangeBroder):
        pass

    @abstractmethod
    def __gt__(self, other: RangeBroder):
        pass

    @abstractmethod
    def __eq__(self, other: RangeBroder):
        pass

    @abstractmethod
    def __le__(self, other: RangeBroder):
        pass

    @abstractmethod
    def __ge__(self, other: RangeBroder):
        pass

    # can not use __repr__ because the Date class requires the date format
    @abstractmethod
    def to_string(self, date_format: str):
        pass



class Date(RangeBroder):
    """
    Class that implements a range border with a concrete date.
    """
    def __init__(self, date: str, date_format: str):
        self.date = datetime.strptime(date, date_format)

    def __lt__(self, other: RangeBroder):
        if isinstance(other, Date):
            return self.date < other.date
        elif isinstance(other, FromInfinity):
            return False
        elif isinstance(other, ToInfinity):
            return True

    def __gt__(self, other: RangeBroder):
        if isinstance(other, Date):
            return self.date > other.date
        if isinstance(other, FromInfinity):
            return True
        if isinstance(other, ToInfinity):
            return False

    def __eq__(self, other: RangeBroder):
        if isinstance(other, Date) and self.date == other.date:
            return True
        else:
            return False

    def __le__(self, other: RangeBroder):
        return self < other or self == other

    def __ge__(self, other: RangeBroder):
        return self > other or self == other

    def to_string(self, date_format: str):
        return self.date.strftime(date_format)


class ToInfinity(RangeBroder):
    """
    Class that implements an open range border into the future.
    This border can only be used as a date_to border.
    When this border is used in a DateRange all dates that are
    greater than or equal to the date_from border are contained
    in the DateRange.
    """
    def __lt__(self, other: RangeBroder):
        return False

    def __gt__(self, other: RangeBroder):
        return True

    def __eq__(self, other: RangeBroder):
        return isinstance(other, ToInfinity)

    def __le__(self, other: RangeBroder):
        return self < other or self == other

    def __ge__(self, other: RangeBroder):
        return self > other or self == other

    def to_string(self, date_format: str):
        return 'None'


class FromInfinity(RangeBroder):
    """
     Class that implements an open range border into the past.
     This border can only be used as a date_from border.
     When this border is used in a DateRange all dates that are
     less than or equal to the date_to border are contained
     in the DateRange.
     """
    def __lt__(self, other: RangeBroder):
        return True

    def __gt__(self, other: RangeBroder):
        return False

    def __eq__(self, other: RangeBroder):
        return isinstance(other, FromInfinity)

    def __le__(self, other: RangeBroder):
        return self < other or self == other

    def __ge__(self, other: RangeBroder):
        return self > other or self == other

    def to_string(self, date_format: str):
        return 'None'