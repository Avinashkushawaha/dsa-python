from datetime import datetime

date = "Oct 14 1997 7:15AM"

date_time = datetime.strptime(date, "%b %d %Y %I: %M%P")