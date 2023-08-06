from .range_borders import Date, FromInfinity, ToInfinity
from datetime import timedelta


class DateRange:
    """
    This class implements date ranges that support open borders,
    so it is possible to create date ranges that contain all dates up to
    a specific date or all dates from a specific date on. Strict ranges with
    specific dates as borders are supported as well.
    The implementation does not support any kind of daytime measurement.
    """

    # DateRange supports all formats that are supported by the datetime module
    # '%Y-%m-%d' is the predefined format
    DATE_FORMAT: str = '%Y-%m-%d'

    #######################################################################################
    # the following methods can be called on every DateRange instance (infinite and finite)
    def __init__(self, date_from: str or None, date_to: str or None):
        """
        Creates a new Daterange. date_to must be greater or equal to date_form
        :param date_from: None value represents an open border
        :param date_to: None value represents an open border
        """
        if date_from is None:
            self._date_from = FromInfinity()
        else:
            self._date_from = Date(date_from, DateRange.DATE_FORMAT)

        if date_to is None:
            self._date_to = ToInfinity()
        else:
            self._date_to = Date(date_to, DateRange.DATE_FORMAT)

        # is set in the first call of the __len__ function
        self._length = None

        self._is_infinite = date_from is None or date_to is None

        if not self._is_infinite:
            if date_to < date_from:
                raise ValueError(f"date_to must be equal or greater than date_form. "
                                 f"{self.__repr__()}")


    def __repr__(self):
        return f"DateRange({self._date_from.to_string(DateRange.DATE_FORMAT)}, " \
               f"{self._date_to.to_string(DateRange.DATE_FORMAT)})"


    def __contains__(self, item: str):
        date = Date(item, DateRange.DATE_FORMAT)
        return self._date_from <= date <= self._date_to


    def intersects(self, date_from: str or None, date_to: str or None) -> bool:
        # returns true if at least one date is contained in both ranges
        date_range = DateRange(date_from=date_from, date_to=date_to)
        return not (self._date_to < date_range._date_from or date_range._date_to < self._date_from)


    def is_infinite(self) -> bool:
        return self._is_infinite


    ##########################################################################
    # the following methods raise exceptions if called on infinite DateRanges
    def __iter__(self):
        if self._is_infinite:
            raise ValueError(f"infinite date ranges are not iterable. date_range: {self.__repr__()}")
        else:
            self._current = self._date_from.date
        return self

    def __next__(self):
        if self._current > self._date_to.date:
            raise StopIteration
        else:
            ret = self._current.strftime(DateRange.DATE_FORMAT)
            self._current += timedelta(1)
            return ret

    def __len__(self):
        if self._is_infinite:
            raise ValueError(f"length infinite date ranges is not defined. date_range: {self.__repr__()}")

        # length has to be calculated and set only once because the
        # length of a date range can not change
        # !!!---if you want to implement the borders of date ranges to be changeable
        # this method must be reimplemented---!!!
        if self._length is None:
            counter = 0
            # __iter__ can safely be used because __len__ requires a finite date range as well
            for _ in self.__iter__():
                counter += 1
            self._length = counter

        return self._length
