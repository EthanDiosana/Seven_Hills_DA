import datetime

class Session():
    """Holds all of the information of a single Session."""

    def __init__(self):

        self.date_and_time = datetime.datetime.now()

        self.day = self.date_and_time.strftime("%d") # Day of month, 01-31
        self.month = self.date_and_time.strftime("%b") # Month name, short version
        self.year = self.date_and_time.strftime("%Y") # Year, full version

        self.hour_24 = self.date_and_time.strftime("%H") # Hour, 00-23
        self.hour_12 = self.date_and_time.strftime("%I") # Hour, 00-12
        self.am_pm = self.date_and_time.strftime("%p") # AM /PM
        self.minute = self.date_and_time.strftime("%M") # Minute, 00-59

        self.date_string = self.month + " " + self.day + " " + self.year # The day, month, and year as a readable string.
        self.time_string_24_hour = self.hour_24 + ":" + self.minute  # The hours and minutes, as a readable string. 24-hour format.
        self.time_string_12_hour = self.hour_12 + ":" + self.minute + " " + self.am_pm # The hours and minutes, as a readable string. 12-hour format.

        self.notes = ""

    def to_dictionary(self):
        """Returns a dictionary of the Session information."""
        session_info = {
            "date_and_time" : self.date_and_time,
            "notes" : self.notes
        }
        return session_info

    def to_string(self):
        """Prints the Session information as a readable string."""
        print(
            self.date_and_time + "\n" +
            self.time_string_24_hour + "\n" +
            self.time_string_12_hour + "\n"
        )
