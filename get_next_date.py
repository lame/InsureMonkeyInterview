from datetime import date, timedelta
import calendar
import dateutil


class GetNextDate:

    def __init__(self, in_date, month_offset, day_cutoff):
        self.in_date = in_date
        self.month_offset = month_offset
        self.day_cutoff = day_cutoff


