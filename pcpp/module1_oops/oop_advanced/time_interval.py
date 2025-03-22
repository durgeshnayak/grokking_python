class TimeInterval:

    def __init__(self, hours, minutes, seconds):
        # Sanitize the values
        if hours > 23:
            raise TypeError("Hours cannot be greate than 23.")
        if minutes > 59:
            raise TypeError("Minutes cannot be greater than 59.")
        if seconds > 59:
            raise TypeError("Seconds cannot be greater than 59.")

        self.hour = hours
        self.minute = minutes
        self.second = seconds

    def __str__(self):
        str_hour = str(self.hour) if self.hour > 9 else "0" + str(self.hour)
        str_minute = str(self.minute) if self.minute > 9 else "0" + str(self.minute)
        str_second = str(self.second) if self.second > 9 else "0" + str(self.second)
        return str_hour + ":" + str_minute + ":" + str_second

    def __add__(self, other):
        if not isinstance(other, TimeInterval):
            raise TypeError("Only time intervals can be added to other time intervals.")

        self_seconds = (self.hour * 60 * 60) + (self.minute * 60) + self.second
        other_seconds = (other.hour * 60 * 60) + (other.minute * 60) + other.second
        total_seconds = self_seconds + other_seconds
        if total_seconds < 0:
            total_seconds = -total_seconds
        total_minutes = int(total_seconds / 60)
        total_seconds = total_seconds % 60
        total_hours = int(total_minutes / 60)
        if total_hours == 24:
            total_hours = 0
        total_minutes = total_minutes % 60
        return TimeInterval(hours=total_hours, minutes=total_minutes, seconds=total_seconds)

    def __sub__(self, other):
        negative_other = TimeInterval(hours=-other.hour, minutes=-other.minute, seconds=-other.second)
        return self.__add__(negative_other)


time_interval = TimeInterval(11, 15, 30)
print(time_interval)
add_interval = TimeInterval(hours=12, minutes=0, seconds=0)
print(time_interval - add_interval)
