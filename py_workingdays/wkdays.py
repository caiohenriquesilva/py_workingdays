from datetime import datetime, timedelta

class Wkdays(object):
    @staticmethod
    def get_easter(year = None):
        """ Return the easter for the given year
            If an year wasn't given then returns the easter for current year
        """

        if not year:
            year = datetime.now().year

        x = 24
        y = 5
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + x) % 30
        e = (2 * b + 4 * c + 6 * d + y) % 7 
        if d + e > 9:
            easter_d = "%02d" % (d + e - 9) 
            easter_m = "04"
            easter = "%s-%s-%s" % (year, easter_m, easter_d)
        else:
            easter_d = "%02d" % (d + e + 22) 
            easter_m = "03"
            easter = "%s-%s-%s" % (year, easter_m, easter_d)

        easter = datetime.strptime(easter, "%Y-%m-%d")
        return easter

    @staticmethod
    def add_working_days(days, date = None):
        """
            Add given working days in given date
            If date wasn't given add working days to current date

            Parameters:
                date -> datetime object i.e. datetime.now()
                days -> positive integer
        """

        if not date:
            date = datetime.now()
        
        easter = Wkdays.get_easter(int(date.year))
        carnival = Wkdays.add_sub_day(easter, -47)
        good_friday = Wkdays.add_sub_day(easter, -2)
        corpus_christi = Wkdays.add_sub_day(easter, 60)

        holidays = [
            "01-01", # JAN
            "%02d-%02d" % (carnival.month, carnival.day),
            "%02d-%02d" % (good_friday.month, good_friday.day),
            "%02d-%02d" % (easter.month, easter.day),
            "%02d-%02d" % (corpus_christi.month, corpus_christi.day),
            "04-21", # APR
            "05-01", # MAY
            "06-12", # JUN
            "07-09", "07-16", # JUL
            "09-07", # SEP
            "10-12", # OCT
            "11-02", "11-15", # NOV
            "12-24", "12-25", "12-31" # DEC
        ]

        count_days = 0
        count_working_days = 0
        while count_working_days < days:
            count_days = count_days + 1
            working_m = (date + timedelta(days=count_days)).month
            working_d = (date + timedelta(days=count_days)).day
            working_md = "%02d-%02d" % (working_m, working_d)
            working_ymd = "%s-%02d-%02d" % (date.year, working_m, working_d)
            working_day_date = datetime.strptime(working_ymd, "%Y-%m-%d")
            
            # check if the day is a holiday or saturday or sunday
            if working_md in holidays or working_day_date.weekday() is 5 or working_day_date.weekday() is 6:
                continue

            count_working_days = count_working_days + 1

        ret_date = date + timedelta(days=count_days)
        ret_date = "%s-%02d-%02d" % (ret_date.year, ret_date.month, ret_date.day)

        return ret_date

    @staticmethod
    def add_sub_day(date, days):
        """ Add or subtract the given days into given date
            Parameters:
                date -> YYYY-MM-DD
                days -> positive integer to add or negative integer to subtract
            Return:
                ret_date -> YYYY-MM-DD
        """

        ret_date = date + timedelta(days=days)
        return ret_date
            