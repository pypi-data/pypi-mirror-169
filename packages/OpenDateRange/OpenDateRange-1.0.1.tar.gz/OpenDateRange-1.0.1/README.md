# OpenDateRange
This is a Python package that provides date ranges which allows open borders.
Thereby it is possible to create date ranges that contain all dates 
up to a certain date or all dates from a certain date on. Of course date ranges 
with concrete dates as borders are supported as well.

## Technical information
The package was developed with python 2.7.18 and only uses the build in 
python packages abc and datetime.

## Installation
``$ pip install OpenDateRange``

## Description of the provided Interface
This package provides only one class which is the DateRange class.
The following sections describe how to use this class and how to 
interact with its instances.
* [Date formats](#date-formats)
* [Creating date ranges](#creating-date-ranges)
* [Contains operator](#contains-operator)
* [Intersection between date ranges](#intersection-between-date-ranges)
* [Infinite date ranges](#infinite-date-ranges)
* [Date range iterator](#date-range-iterator)
* [Date range length](#date-range-length)

### Date formats
The package supports all date formats that are supported by the 
build in datetime package. The date format can be changed via 
the static attribute DATE_FORMAT that belongs to the DateRange class and
is predefined as "%Y-%m-%d". When the date format is changed 
all dates that are involved in interactions with instances of the DateRange
class must match the new date format. Furthermore, all dates that are returned
by any methods of the DateRange class match the new format as well.
#### Example

```python
from openDateRange import DateRange

# change date format from %Y-%m-%d to %Y/%m/%d
DateRange.DATE_FORMAT = "%Y/%m/%d"
```
All DateRange instances now only accept and output dates in %Y/%m/%d format.

### Creating date ranges
A DateRange instance takes two parameters. A date from where the range
should start and a date up to which the range should go. If one of 
these parameters is set to None the corresponding border will be
an open border. Both, the start and the end date are included in the date range.
#### Example

```python
from openDateRange import DateRange

# holds all dates from 2000-12-12 up to 2001-12-12
dr1 = DateRange(date_from="2000-12-12", date_to="2001-12-12")

# holds all dates from 2000-12-12 on
dr2 = DateRange(date_from="2000-12-12", date_to=None)

# holds all dates up to 2001-12-12
dr3 = DateRange(date_from=None, date_to="2001-12-12")

# holds all dates
dr4 = DateRange(date_from=None, date_to=None)
```

### Contains operator
Pythons `in` operator can be used to proof whether a date is contained in
a date range.
#### Example

```python
from openDateRange import DateRange

dr = DateRange(date_from="2000-12-12", date_to=None)
# true
print("2000-12-12" in dr)
# true
print("2040-12-12" in dr)
# false
print("1990-12-12" in dr)
```

### Intersection between date ranges
The `intersects` method of the DateRange class takes in
two borders that span a date range and proofs if the two date
ranges intersect. The method returns true if at least 
one date is contained in both date ranges.
#### Example

```python
from openDateRange import DateRange

dr = DateRange(date_from="2000-12-12", date_to="2001-12-12")
# true
dr.intersects(date_from="2001-05-05", date_to="2002-06-06")
# false
dr.intersects(date_from="2002-12-12", date_to="2003-12-12")
```

### Infinite date ranges
Date ranges that have at least one open border are called to be infinite.
The following functions can not be called on infinite date ranges. These
include the iterator functionality and the len() function. Due to the fact
that an iterator on an infinite date range would be an endless loop and
the length of an infinite date range is not defined. The `is_infinite()` 
method of the DateRange class proofs whether a DateRange instance is infinite.

### Date range iterator
If a date range is finite it is possible to iterate over the date range
using the build in iterator functionalities. The iterator returns
each date as a String of the format that is currently set.
#### Example

```python
from openDateRange import DateRange

dr = DateRange(date_from="2000-12-12", date_to="2000-12-15")

print([date for date in dr])
# output: ["2000-12-21", "2000-12-13", "2000-12-14", "2000-12-15"]
```

### Date range length
A finite date range also has a length which is just the number of dates
it contains. The length can be determined with the build in len() function.
Note that the length of a date range can not change so the length of 
a date range is calculated in the first call of the len() function and 
is just read from memory in the following calls. Due to this implementation the first call 
of the len() function may be a little slower especially for very 
long date ranges.

