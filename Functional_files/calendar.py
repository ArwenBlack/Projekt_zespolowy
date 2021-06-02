from calendar import HTMLCalendar
from Projekt_zespołowy.models import Meeting
import locale

locale.setlocale(locale.LC_ALL, 'pl_PL')


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    def formatday(self, day, events):
        events_per_day = events.filter(start_time__day=day)

        hour = ''
        for event in events_per_day:
            time = event.start_time.time().strftime('%H:%M')

            if event.is_free:
                hour += f'<li> <a style="color: #8bcc9c;" ' \
                        f'href="/meeting/?meeting={ event.id }"> { time } </a> </li>'
            else:
                hour += f'<li> <a style="color: #cc8d8b;" ' \
                        f'href="/meeting/?meeting={ event.id }"> { time } </a> </li>'

        if day != 0:
            return f"<td>" \
                   f"<div class='number-background'>" \
                   f"<span class='hour'> " \
                   f"{ day } " \
                   f"</span>" \
                   f"</div>" \
                   f"<ul>" \
                   f" { hour }" \
                   f"</ul>"\
                   f"</td>"
        return '<td></td>'

    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr> {week} </tr>'

    def formatmonth(self, withyear=True):
        events = Meeting.objects.filter(start_time__year=self.year, start_time__month=self.month)

        cal = f'<table class="table table-bordered" ' \
              f'style="margin-right: 50px;">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        return cal
