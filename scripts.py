import calendar
import re

from datetime import date


class CommaSeparatedValues (object):
    """
    This class takes is made to take a number
    and add the correct comma placement relating
    to hundreds, thousands, etc. and account for
    arbitrary decimal numbers
    """
    def __init__(self):
        pass

    def comma_separated_numbers(self, num):
        self.num_str = str(num).split('.')
        return self.insert_commas()

    def insert_commas(self):
        output = ''
        for pos, numeric in enumerate(self.num_str[0][::-1]):
            if not pos % 3 and pos != 0:
                output += ',' + numeric
            else:
                output += numeric
        output = output[::-1]
        if len(self.num_str) > 1:
            output += '.' + self.num_str[1]
        return output


class FlattenList(object):
    """
    This class will take a list or arbitrary list of lists
    and return a list with just the alpha elements int the
    order they were received regardless of list depth.
    """
    def __init__():
        pass

    def flatten(in_list):
        """
        Though this can be done easily iteratively I thought I'd have a little
        fun and do it with regular expressions. Naively I believe not iterating
        might provide some performance enhancements depending on depth of lists.
        """
        return re.findall('(\w[a-zA-Z]*)', str(in_list))


class GetNextDate(object):

    def __init__(self):
        pass

    def add_day(self, year, month, day, day_cutoff):
        if day < self.cutoff(year, month, day_cutoff):
            day += 1
        else:
            day = 1
            if month < 12:
                month += 1
            else:
                month = 1
                year += 1
        return(year, month, day)

    def add_month(self, year, month):
        if month < 12:
            month += 1
        else:
            month = 1
            year += 1
        return (year, month)

    def calculate_day_cutoff(self, day_cutoff, in_date):
        if day_cutoff == 0:
            day_cutoff = calendar.monthrange(in_date.year, in_date.month)[1]
        elif day_cutoff < 0:
            day_cutoff = (calendar.monthrange(in_date.year, in_date.month)[1] + day_cutoff)
        return day_cutoff

    def cutoff(self, year, month, day_cutoff):
        return min(calendar.monthrange(year, month)[1], day_cutoff)

    def calculate_month_offset(self, in_date, month_offset, day_cutoff):
        """
        Month offset will add the floor of 365/12,
        which equates to exactly 30 days
        """
        day = in_date.day
        month = in_date.month
        year = in_date.year

        total_day_offset = month_offset * (31)

        for x in range(total_day_offset):
            tmp = self.add_day(year, month, day, day_cutoff)
            year = tmp[0]
            month = tmp[1]
            day = tmp[2]
        return date(year, month, day)

    def create_month_list(self, month_list, count, year, month):
        for x in range(count - 1):
            tmp = self.add_month(year, month)
            year = tmp[0]
            month = tmp[1]
            month_list.append(date(year, month, 1))
        return month_list

    def get_next_dates(self, in_date, count, month_offset, day_cutoff):

        day_cutoff = self.calculate_day_cutoff(day_cutoff, in_date)

        month_list = []

        if month_offset == 0 and day_cutoff >= in_date.day:
            month_list.append(in_date)
        elif month_offset == 0 and day_cutoff < in_date.day:
            self.create_month_list(month_list, 2, in_date.year, in_date.month)
        else:  # month_offset > 0
            month_list.append(self.calculate_month_offset(in_date, month_offset, day_cutoff))

        month = month_list[0].month
        year = month_list[0].year

        month_list = self.create_month_list(month_list, count, year, month)
        return month_list
