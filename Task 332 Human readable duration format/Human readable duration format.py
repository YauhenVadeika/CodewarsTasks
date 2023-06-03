"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def format_duration(seconds):

    if seconds == 0:
        return "now"

    year, seconds = divmod(seconds, 31536000)
    day, seconds = divmod(seconds, 86400)
    hour, seconds = divmod(seconds, 3600)
    min, seconds = divmod(seconds, 60)

    # print(year, day, hour, min, seconds)
    arr = [
        str(i) + ' ' + j + ('s' if i > 1 else '')
        for i, j in zip([year, day, hour, min, seconds],
                        ['year', 'day', 'hour', 'minute', 'second']) if i > 0
    ]
    return ', '.join(arr[:-2] + [' and '.join(arr[-2:])])


print(format_duration(33243586))
print(format_duration(15731080))
print(format_duration(9041160))
print(format_duration(0))
print(format_duration(1))
print(format_duration(62))
print(format_duration(3600))
print(format_duration(60))

# codewars task best solution
times = [("year", 365 * 24 * 60 * 60), ("day", 24 * 60 * 60),
         ("hour", 60 * 60), ("minute", 60), ("second", 1)]


def format_duration(seconds):

    if not seconds:
        return "now"

    chunks = []
    for name, secs in times:
        qty = seconds // secs
        if qty:
            if qty > 1:
                name += "s"
            chunks.append(str(qty) + " " + name)

        seconds = seconds % secs

    return ', '.join(
        chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]


# codewars task best solution
def format_duration(seconds):
    if seconds == 0:
        return "now"
    #if seconds==132375840:
    #return '4 years, 68 days, 3 hours and 4 minutes'
    minu, sec = divmod(seconds, 60)
    hour, minu = divmod(minu, 60)
    day, hour = divmod(hour, 24)
    year, day = divmod(day, 365)
    if year == 0:
        if day == 0:
            if hour == 0:
                if minu == 0:
                    if sec == 1:
                        return str(sec) + ' second'
                    return str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(minu) + ' minute'
                    if sec == 1:
                        return str(minu) + ' minute and ' + str(
                            sec) + ' second'
                    return str(minu) + ' minute and ' + str(sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(minu) + ' minutes'
                    if sec == 1:
                        return str(minu) + ' minutes and ' + str(
                            sec) + ' second'
                    return str(minu) + ' minutes and ' + str(sec) + ' seconds'

            if hour == 1:
                if minu == 0:
                    if sec == 0:
                        return str(hour) + ' hour'

                    if sec == 1:
                        return str(hour) + ' hour and ' + str(sec) + ' second'
                    return str(hour) + ' hour and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(hour) + ' hour, ' + str(minu) + ' minute'

                    if sec == 1:
                        return str(hour) + ' hour, ' + str(
                            minu) + ' minute and ' + str(sec) + ' second'
                    return str(hour) + ' hour, ' + str(
                        minu) + ' minute and ' + str(sec) + ' seconds'
                if sec == 0:
                    return str(hour) + ' hour, ' + str(minu) + ' minutes'

                if sec == 1:
                    return str(hour) + ' hour, ' + str(
                        minu) + ' minutes and ' + str(sec) + ' second'
                return str(hour) + ' hour, ' + str(
                    minu) + ' minutes and ' + str(sec) + ' seconds'
            if hour > 1:
                if minu == 0:
                    if sec == 0:
                        return str(hour) + ' hours'

                    if sec == 1:
                        return str(hour) + ' hours and ' + str(sec) + ' second'
                    return str(hour) + ' hours and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(hour) + ' hours and ' + str(
                            minu) + ' minute'

                    if sec == 1:
                        return str(hour) + ' hours, ' + str(
                            minu) + ' minute and ' + str(sec) + ' second'
                    return str(hour) + ' hours, ' + str(
                        minu) + ' minute and ' + str(sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(hour) + ' hours and ' + str(
                            minu) + ' minutes'

                    if sec == 1:
                        return str(hour) + ' hours, ' + str(
                            minu) + ' minutes and ' + str(sec) + ' second'
                    return str(hour) + ' hours, ' + str(
                        minu) + ' minutes and ' + str(sec) + ' seconds'

        if day == 1:
            if hour == 0:
                if minu == 0:
                    if sec == 0:
                        return str(day) + ' day'
                    if sec == 1:
                        return str(day) + ' day and ' + str(sec) + ' second'
                    return str(day) + ' day and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(day) + ' day and ' + str(minu) + ' minute'
                    if sec == 1:
                        return str(day) + ' day, ' + str(
                            minu) + ' minute and ' + str(sec) + ' second'
                    return str(day) + ' day, ' + str(
                        minu) + ' minute and ' + str(sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(day) + ' day and ' + str(minu) + ' minutes'
                    if sec == 1:
                        return str(day) + ' day, ' + str(
                            minu) + ' minutes and ' + str(sec) + ' second'
                    return str(day) + ' day, ' + str(
                        minu) + ' minutes and ' + str(sec) + ' seconds'

            if hour == 1:
                if minu == 0:
                    if sec == 0:
                        return str(day) + ' day and ' + str(
                            hour) + ' hour and ' + str(sec)

                    if sec == 1:
                        return str(day) + ' day, ' + str(
                            hour) + ' hour and ' + str(sec) + ' second'
                    return str(day) + ' day, ' + str(
                        hour) + ' hour and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(day) + ' day, ' + str(
                            hour) + ' hour, ' + str(minu) + ' minute'

                    if sec == 1:
                        return str(day) + ' day, ' + str(
                            hour) + ' hour, ' + str(
                                minu) + ' minute and ' + str(sec) + ' second'
                    return str(day) + ' day, ' + str(hour) + ' hour, ' + str(
                        minu) + ' minute and ' + str(sec) + ' seconds'
                if sec == 0:
                    return str(day) + ' day, ' + str(hour) + ' hour, ' + str(
                        minu) + ' minutes'

                if sec == 1:
                    return str(day) + ' day, ' + str(hour) + ' hour, ' + str(
                        minu) + ' minutes and ' + str(sec) + ' second'
                return str(day) + ' day, ' + str(hour) + ' hour, ' + str(
                    minu) + ' minutes and ' + str(sec) + ' seconds'
            if hour > 1:
                if minu == 0:
                    if sec == 0:
                        return str(day) + ' day and ' + str(hour) + ' hours'

                    if sec == 1:
                        return str(day) + ' day, ' + str(
                            hour) + ' hours and ' + str(sec) + ' second'
                    return str(day) + ' day, ' + str(
                        hour) + ' hours and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(day) + ' day, ' + str(
                            hour) + ' hours and ' + str(minu) + ' minute'

                    if sec == 1:
                        return str(day) + ' day, ' + str(
                            hour) + ' hours, ' + str(
                                minu) + ' minute and ' + str(sec) + ' second'
                    return str(day) + ' day, ' + str(hour) + ' hours, ' + str(
                        minu) + ' minute and ' + str(sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(day) + ' day, ' + str(
                            hour) + ' hours and ' + str(minu) + ' minutes'

                    if sec == 1:
                        return str(day) + ' day, ' + str(
                            hour) + ' hours, ' + str(
                                minu) + ' minutes and ' + str(sec) + ' second'
                    return str(day) + ' day, ' + str(hour) + ' hours, ' + str(
                        minu) + ' minutes and ' + str(sec) + ' seconds'
        if day > 1:
            if hour == 0:
                if minu == 0:
                    if sec == 0:
                        return str(day) + ' days'
                    if sec == 1:
                        return str(day) + ' days and ' + str(sec) + ' second'
                    return str(day) + ' days and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(day) + ' days and ' + str(minu) + ' minute'
                    if sec == 1:
                        return str(day) + ' days, ' + str(
                            minu) + ' minute and ' + str(sec) + ' second'
                    return str(day) + ' days, ' + str(
                        minu) + ' minute and ' + str(sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(day) + ' days and ' + str(minu) + ' minutes'
                    if sec == 1:
                        return str(day) + ' days, ' + str(
                            minu) + ' minutes and ' + str(sec) + ' second'
                    return str(day) + ' days, ' + str(
                        minu) + ' minutes and ' + str(sec) + ' seconds'

            if hour == 1:
                if minu == 0:
                    if sec == 0:
                        return str(day) + ' days and ' + str(
                            hour) + ' hour and ' + str(sec)

                    if sec == 1:
                        return str(day) + ' days, ' + str(
                            hour) + ' hour and ' + str(sec) + ' second'
                    return str(day) + ' days, ' + str(
                        hour) + ' hour and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(day) + ' days, ' + str(
                            hour) + ' hour, ' + str(minu) + ' minute'

                    if sec == 1:
                        return str(day) + ' days, ' + str(
                            hour) + ' hour, ' + str(
                                minu) + ' minute and ' + str(sec) + ' second'
                    return str(day) + ' days, ' + str(hour) + ' hour, ' + str(
                        minu) + ' minute and ' + str(sec) + ' seconds'
                if sec == 0:
                    return str(day) + ' days, ' + str(hour) + ' hours'

                if sec == 1:
                    return str(day) + ' days, ' + str(hour) + ' hour, ' + str(
                        minu) + ' minutes and ' + str(sec) + ' second'
                return str(day) + ' days, ' + str(hour) + ' hour, ' + str(
                    minu) + ' minutes and ' + str(sec) + ' seconds'
            if hour > 1:
                if minu == 0:
                    if sec == 0:
                        return str(day) + ' days and ' + str(hour) + ' hours'

                    if sec == 1:
                        return str(day) + ' days, ' + str(
                            hour) + ' hours and ' + str(sec) + ' second'
                    return str(day) + ' days, ' + str(
                        hour) + ' hours and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(day) + ' days, ' + str(
                            hour) + ' hours and ' + str(minu) + ' minute'

                    if sec == 1:
                        return str(day) + ' days, ' + str(
                            hour) + ' hours, ' + str(
                                minu) + ' minute and ' + str(sec) + ' second'
                    return str(day) + ' days, ' + str(hour) + ' hours, ' + str(
                        minu) + ' minute and ' + str(sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(day) + ' days, ' + str(
                            hour) + ' hours and ' + str(minu) + ' minutes'

                    if sec == 1:
                        return str(day) + ' days, ' + str(
                            hour) + ' hours, ' + str(
                                minu) + ' minutes and ' + str(sec) + ' second'
                    return str(day) + ' days, ' + str(hour) + ' hours, ' + str(
                        minu) + ' minutes and ' + str(sec) + ' seconds'
    if year == 1:
        if day == 0:
            if hour == 0:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' year'
                    if sec == 1:
                        return str(year) + ' year and ' + str(sec) + ' second'
                    return str(year) + ' year and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' year and ' + str(minu) + ' minute'
                    if sec == 1:
                        return str(year) + ' year, ' + str(
                            minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(
                        minu) + ' minute and ' + str(sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(year) + ' year and ' + str(
                            minu) + ' minutes'
                    if sec == 1:
                        return str(year) + ' year, ' + str(
                            minu) + ' minutes and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(
                        minu) + ' minutes and ' + str(sec) + ' seconds'

            if hour == 1:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' year and  ' + str(hour) + ' hour'

                    if sec == 1:
                        return str(year) + ' year, ' + str(
                            hour) + ' hour and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(
                        hour) + ' hour and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' year, ' + str(
                            hour) + ' hour, ' + str(minu) + ' minute'

                    if sec == 1:
                        return str(year) + ' year, ' + str(
                            hour) + ' hour, ' + str(
                                minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(hour) + ' hour, ' + str(
                        minu) + ' minute and ' + str(sec) + ' seconds'
                if sec == 0:
                    return str(year) + ' year, ' + str(hour) + ' hour, ' + str(
                        minu) + ' minutes'

                if sec == 1:
                    return str(year) + ' year, ' + str(hour) + ' hour, ' + str(
                        minu) + ' minutes and ' + str(sec) + ' second'
                return str(year) + ' year, ' + str(hour) + ' hour, ' + str(
                    minu) + ' minutes and ' + str(sec) + ' seconds'
            if hour > 1:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' year and ' + str(hour) + ' hours'

                    if sec == 1:
                        return str(year) + ' year, ' + str(
                            hour) + ' hours and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(
                        hour) + ' hours and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' year, ' + str(
                            hour) + ' hours and ' + str(minu) + ' minute'

                    if sec == 1:
                        return str(year) + ' year, ' + str(
                            hour) + ' hours, ' + str(
                                minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(
                        hour) + ' hours, ' + str(minu) + ' minute and ' + str(
                            sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(year) + ' year, ' + str(
                            hour) + ' hours and ' + str(minu) + ' minutes'

                    if sec == 1:
                        return str(year) + ' year, ' + str(
                            hour) + ' hours, ' + str(
                                minu) + ' minutes and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(
                        hour) + ' hours, ' + str(minu) + ' minutes and ' + str(
                            sec) + ' seconds'

        if day == 1:
            if hour == 0:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' year and  ' + str(day) + ' day'
                    if sec == 1:
                        return str(year) + ' year, ' + str(
                            day) + ' day and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(
                        day) + ' day and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' year, ' + str(
                            day) + ' day and ' + str(minu) + ' minute'
                    if sec == 1:
                        return str(year) + ' year, ' + str(
                            day) + ' day, ' + str(minu) + ' minute and ' + str(
                                sec) + ' second'
                    return str(year) + ' year, ' + str(day) + ' day, ' + str(
                        minu) + ' minute and ' + str(sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(year) + ' year, ' + str(
                            day) + ' day and ' + str(minu) + ' minutes'
                    if sec == 1:
                        return str(year) + ' year, ' + str(
                            day) + ' day, ' + str(
                                minu) + ' minutes and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(day) + ' day, ' + str(
                        minu) + ' minutes and ' + str(sec) + ' seconds'

            if hour == 1:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' year, ' + str(
                            day) + ' day and ' + str(
                                hour) + ' hour and ' + str(sec)

                    if sec == 1:
                        return str(year) + ' year, ' + str(
                            day) + ' day, ' + str(hour) + ' hour and ' + str(
                                sec) + ' second'
                    return str(year) + ' year, ' + str(day) + ' day, ' + str(
                        hour) + ' hour and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' year, ' + str(
                            day) + ' day, ' + str(hour) + ' hour, ' + str(
                                minu) + ' minute'

                    if sec == 1:
                        return str(year) + ' year, ' + str(
                            day) + ' day, ' + str(hour) + ' hour, ' + str(
                                minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(day) + ' day, ' + str(
                        hour) + ' hour, ' + str(minu) + ' minute and ' + str(
                            sec) + ' seconds'
                if sec == 0:
                    return str(year) + ' year, ' + str(day) + ' day, ' + str(
                        hour) + ' hour, ' + str(minu) + ' minutes'

                if sec == 1:
                    return str(year) + ' year, ' + str(day) + ' day, ' + str(
                        hour) + ' hour, ' + str(minu) + ' minutes and ' + str(
                            sec) + ' second'
                return str(year) + ' year, ' + str(day) + ' day, ' + str(
                    hour) + ' hour, ' + str(minu) + ' minutes and ' + str(
                        sec) + ' seconds'
            if hour > 1:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' year, ' + str(
                            day) + ' day and ' + str(hour) + ' hours'

                    if sec == 1:
                        return str(year) + ' year, ' + str(
                            day) + ' day, ' + str(hour) + ' hours and ' + str(
                                sec) + ' second'
                    return str(year) + ' year, ' + str(day) + ' day, ' + str(
                        hour) + ' hours and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' year, ' + str(
                            day) + ' day, ' + str(hour) + ' hours and ' + str(
                                minu) + ' minute'

                    if sec == 1:
                        return str(year) + ' year, ' + str(
                            day) + ' day, ' + str(hour) + ' hours, ' + str(
                                minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(day) + ' day, ' + str(
                        hour) + ' hours, ' + str(minu) + ' minute and ' + str(
                            sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(year) + ' year, ' + str(
                            day) + ' day, ' + str(day) + ' day, ' + str(
                                hour) + ' hours and ' + str(minu) + ' minutes'

                    if sec == 1:
                        return str(year) + ' year, ' + str(
                            day) + ' day, ' + str(hour) + ' hours, ' + str(
                                minu) + ' minutes and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(day) + ' day, ' + str(
                        hour) + ' hours, ' + str(minu) + ' minutes and ' + str(
                            sec) + ' seconds'
        if day > 1:
            if hour == 0:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' year, and ' + str(day) + ' days'
                    if sec == 1:
                        return str(year) + ' year, ' + str(
                            day) + ' days and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(
                        day) + ' days and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' year, ' + str(
                            day) + ' days and ' + str(minu) + ' minute'
                    if sec == 1:
                        return str(year) + ' year, ' + str(
                            day) + ' days, ' + str(
                                minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(day) + ' days, ' + str(
                        minu) + ' minute and ' + str(sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(year) + ' year, ' + str(
                            day) + ' days and ' + str(minu) + ' minutes'
                    if sec == 1:
                        return str(year) + ' year, ' + str(
                            day) + ' days, ' + str(
                                minu) + ' minutes and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(day) + ' days, ' + str(
                        minu) + ' minutes and ' + str(sec) + ' seconds'

            if hour == 1:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' year, ' + str(
                            day) + ' days and ' + str(
                                hour) + ' hour and ' + str(sec)

                    if sec == 1:
                        return str(year) + ' year, ' + str(
                            day) + ' days, ' + str(hour) + ' hour and ' + str(
                                sec) + ' second'
                    return str(year) + ' year, ' + str(day) + ' days, ' + str(
                        hour) + ' hour and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' year, ' + str(
                            day) + ' days, ' + str(hour) + ' hour, ' + str(
                                minu) + ' minute'

                    if sec == 1:
                        return str(year) + ' year, ' + str(
                            day) + ' days, ' + str(hour) + ' hour, ' + str(
                                minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(day) + ' days, ' + str(
                        hour) + ' hour, ' + str(minu) + ' minute and ' + str(
                            sec) + ' seconds'
                if sec == 0:
                    return str(year) + ' year, ' + str(day) + ' days, ' + str(
                        hour) + ' hours'

                if sec == 1:
                    return str(year) + ' year, ' + str(day) + ' days, ' + str(
                        hour) + ' hour, ' + str(minu) + ' minutes and ' + str(
                            sec) + ' second'
                return str(year) + ' year, ' + str(day) + ' days, ' + str(
                    hour) + ' hour, ' + str(minu) + ' minutes and ' + str(
                        sec) + ' seconds'
            if hour > 1:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' year, ' + str(
                            day) + ' days and ' + str(hour) + ' hours'

                    if sec == 1:
                        return str(year) + ' year, ' + str(
                            day) + ' days, ' + str(hour) + ' hours and ' + str(
                                sec) + ' second'
                    return str(year) + ' year, ' + str(day) + ' days, ' + str(
                        hour) + ' hours and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' year, ' + str(
                            day) + ' days, ' + str(hour) + ' hours and ' + str(
                                minu) + ' minute'

                    if sec == 1:
                        return str(year) + ' year, ' + str(
                            day) + ' days, ' + str(hour) + ' hours, ' + str(
                                minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(day) + ' days, ' + str(
                        hour) + ' hours, ' + str(minu) + ' minute and ' + str(
                            sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(year) + ' year, ' + str(
                            day) + ' days, ' + str(hour) + ' hours and ' + str(
                                minu) + ' minutes'

                    if sec == 1:
                        return str(year) + ' year ' + str(
                            day) + ' days, ' + str(hour) + ' hours, ' + str(
                                minu) + ' minutes and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(day) + ' days, ' + str(
                        hour) + ' hours, ' + str(minu) + ' minutes and ' + str(
                            sec) + ' seconds'
    if year > 1:
        if day == 0:
            if hour == 0:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' years'
                    if sec == 1:
                        return str(year) + ' years and ' + str(sec) + ' second'
                    return str(year) + ' years and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' years and ' + str(
                            minu) + ' minute'
                    if sec == 1:
                        return str(year) + ' years, ' + str(
                            minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(
                        minu) + ' minute and ' + str(sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(year) + ' years and ' + str(
                            minu) + ' minutes'
                    if sec == 1:
                        return str(year) + ' years, ' + str(
                            minu) + ' minutes and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(
                        minu) + ' minutes and ' + str(sec) + ' seconds'

            if hour == 1:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' years and  ' + str(hour) + ' hour'

                    if sec == 1:
                        return str(year) + ' years, ' + str(
                            hour) + ' hour and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(
                        hour) + ' hour and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' years, ' + str(
                            hour) + ' hour, ' + str(minu) + ' minute'

                    if sec == 1:
                        return str(year) + ' years, ' + str(
                            hour) + ' hour, ' + str(
                                minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(
                        hour) + ' hour, ' + str(minu) + ' minute and ' + str(
                            sec) + ' seconds'
                if sec == 0:
                    return str(year) + ' years, ' + str(
                        hour) + ' hour, ' + str(minu) + ' minutes'

                if sec == 1:
                    return str(year) + ' years, ' + str(
                        hour) + ' hour, ' + str(minu) + ' minutes and ' + str(
                            sec) + ' second'
                return str(year) + ' years, ' + str(hour) + ' hour, ' + str(
                    minu) + ' minutes and ' + str(sec) + ' seconds'
            if hour > 1:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' years and ' + str(hour) + ' hours'

                    if sec == 1:
                        return str(year) + ' years, ' + str(
                            hour) + ' hours and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(
                        hour) + ' hours and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' years, ' + str(
                            hour) + ' hours and ' + str(minu) + ' minute'

                    if sec == 1:
                        return str(year) + ' years, ' + str(
                            hour) + ' hours, ' + str(
                                minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(
                        hour) + ' hours, ' + str(minu) + ' minute and ' + str(
                            sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(year) + ' years, ' + str(
                            hour) + ' hours and ' + str(minu) + ' minutes'

                    if sec == 1:
                        return str(year) + ' years, ' + str(
                            hour) + ' hours, ' + str(
                                minu) + ' minutes and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(
                        hour) + ' hours, ' + str(minu) + ' minutes and ' + str(
                            sec) + ' seconds'

        if day == 1:
            if hour == 0:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' years and  ' + str(day) + ' day'
                    if sec == 1:
                        return str(year) + ' years, ' + str(
                            day) + ' day and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(
                        day) + ' day and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' years, ' + str(
                            day) + ' day and ' + str(minu) + ' minute'
                    if sec == 1:
                        return str(year) + ' years, ' + str(
                            day) + ' day, ' + str(minu) + ' minute and ' + str(
                                sec) + ' second'
                    return str(year) + ' years, ' + str(day) + ' day, ' + str(
                        minu) + ' minute and ' + str(sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(year) + ' years, ' + str(
                            day) + ' day and ' + str(minu) + ' minutes'
                    if sec == 1:
                        return str(year) + ' years, ' + str(
                            day) + ' day, ' + str(
                                minu) + ' minutes and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(day) + ' day, ' + str(
                        minu) + ' minutes and ' + str(sec) + ' seconds'

            if hour == 1:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' years, ' + str(
                            day) + ' day and ' + str(
                                hour) + ' hour and ' + str(sec)

                    if sec == 1:
                        return str(year) + ' years, ' + str(
                            day) + ' day, ' + str(hour) + ' hour and ' + str(
                                sec) + ' second'
                    return str(year) + ' years, ' + str(day) + ' day, ' + str(
                        hour) + ' hour and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' years, ' + str(
                            day) + ' day, ' + str(hour) + ' hour, ' + str(
                                minu) + ' minute'

                    if sec == 1:
                        return str(year) + ' years, ' + str(
                            day) + ' day, ' + str(hour) + ' hour, ' + str(
                                minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' yeas, ' + str(day) + ' day, ' + str(
                        hour) + ' hour, ' + str(minu) + ' minute and ' + str(
                            sec) + ' seconds'
                if sec == 0:
                    return str(year) + ' years, ' + str(day) + ' day, ' + str(
                        hour) + ' hour, ' + str(minu) + ' minutes'

                if sec == 1:
                    return str(year) + ' years, ' + str(day) + ' day, ' + str(
                        hour) + ' hour, ' + str(minu) + ' minutes and ' + str(
                            sec) + ' second'
                return str(year) + ' years, ' + str(day) + ' day, ' + str(
                    hour) + ' hour, ' + str(minu) + ' minutes and ' + str(
                        sec) + ' seconds'
            if hour > 1:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' years, ' + str(
                            day) + ' day and ' + str(hour) + ' hours'

                    if sec == 1:
                        return str(year) + ' years, ' + str(
                            day) + ' day, ' + str(hour) + ' hours and ' + str(
                                sec) + ' second'
                    return str(year) + ' years, ' + str(day) + ' day, ' + str(
                        hour) + ' hours and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' years, ' + str(
                            day) + ' day, ' + str(hour) + ' hours and ' + str(
                                minu) + ' minute'

                    if sec == 1:
                        return str(year) + ' years, ' + str(
                            day) + ' day, ' + str(hour) + ' hours, ' + str(
                                minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(day) + ' day, ' + str(
                        hour) + ' hours, ' + str(minu) + ' minute and ' + str(
                            sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(year) + ' years, ' + str(
                            day) + ' day, ' + str(day) + ' day, ' + str(
                                hour) + ' hours and ' + str(minu) + ' minutes'

                    if sec == 1:
                        return str(year) + ' years, ' + str(
                            day) + ' day, ' + str(hour) + ' hours, ' + str(
                                minu) + ' minutes and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(day) + ' day, ' + str(
                        hour) + ' hours, ' + str(minu) + ' minutes and ' + str(
                            sec) + ' seconds'
        if day > 1:
            if hour == 0:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' years, and ' + str(day) + ' days'
                    if sec == 1:
                        return str(year) + ' years, ' + str(
                            day) + ' days and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(
                        day) + ' days and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' years, ' + str(
                            day) + ' days and ' + str(minu) + ' minute'
                    if sec == 1:
                        return str(year) + ' years, ' + str(
                            day) + ' days, ' + str(
                                minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(day) + ' days, ' + str(
                        minu) + ' minute and ' + str(sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(year) + ' years, ' + str(
                            day) + ' days and ' + str(minu) + ' minutes'
                    if sec == 1:
                        return str(year) + ' years, ' + str(
                            day) + ' days, ' + str(
                                minu) + ' minutes and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(day) + ' days, ' + str(
                        minu) + ' minutes and ' + str(sec) + ' seconds'

            if hour == 1:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' years, ' + str(
                            day) + ' days and ' + str(
                                hour) + ' hour and ' + str(sec)

                    if sec == 1:
                        return str(year) + ' years, ' + str(
                            day) + ' days, ' + str(hour) + ' hour and ' + str(
                                sec) + ' second'
                    return str(year) + ' years, ' + str(day) + ' days, ' + str(
                        hour) + ' hour and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' years, ' + str(
                            day) + ' days, ' + str(hour) + ' hour, ' + str(
                                minu) + ' minute'

                    if sec == 1:
                        return str(year) + ' years, ' + str(
                            day) + ' days, ' + str(hour) + ' hour, ' + str(
                                minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(day) + ' days, ' + str(
                        hour) + ' hour, ' + str(minu) + ' minute and ' + str(
                            sec) + ' seconds'
                if sec == 0:
                    return str(year) + ' years, ' + str(day) + ' days, ' + str(
                        hour) + ' hours'

                if sec == 1:
                    return str(year) + ' years, ' + str(day) + ' days, ' + str(
                        hour) + ' hour, ' + str(minu) + ' minutes and ' + str(
                            sec) + ' second'
                return str(year) + ' years, ' + str(day) + ' days, ' + str(
                    hour) + ' hour, ' + str(minu) + ' minutes and ' + str(
                        sec) + ' seconds'
            if hour > 1:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' years, ' + str(
                            day) + ' days and ' + str(hour) + ' hours'

                    if sec == 1:
                        return str(year) + ' years, ' + str(
                            day) + ' days, ' + str(hour) + ' hours and ' + str(
                                sec) + ' second'
                    return str(year) + ' years, ' + str(day) + ' days, ' + str(
                        hour) + ' hours and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' years, ' + str(
                            day) + ' days, ' + str(hour) + ' hours and ' + str(
                                minu) + ' minute'

                    if sec == 1:
                        return str(year) + ' years, ' + str(
                            day) + ' days, ' + str(hour) + ' hours, ' + str(
                                minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(day) + ' days, ' + str(
                        hour) + ' hours, ' + str(minu) + ' minute and ' + str(
                            sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(year) + ' years, ' + str(
                            day) + ' days, ' + str(hour) + ' hours and ' + str(
                                minu) + ' minutes'

                    if sec == 1:
                        return str(year) + ' years, ' + str(
                            day) + ' days, ' + str(hour) + ' hours, ' + str(
                                minu) + ' minutes and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(day) + ' days, ' + str(
                        hour) + ' hours, ' + str(minu) + ' minutes and ' + str(
                            sec) + ' seconds'


# codewars task best solution
def f(n, unit):
    return [', ', '{} {}{}'.format(n, unit, 's' if n > 1 else '')]


def format_duration(seconds):
    if not seconds: return 'now'

    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    years, days = divmod(days, 365)

    fs = []
    if years: fs.extend(f(years, 'year'))
    if days: fs.extend(f(days, 'day'))
    if hours: fs.extend(f(hours, 'hour'))
    if minutes: fs.extend(f(minutes, 'minute'))
    if seconds: fs.extend(f(seconds, 'second'))

    fs[-2] = ' and '
    fs.pop(0)
    return ''.join(fs)


# codewars task best solution
def format_duration(seconds):

    if seconds is 0: return 'now'

    scale = [('second', 1), ('minute', 60), ('hour', 60 * 60),
             ('day', 60 * 60 * 24), ('year', 60 * 60 * 24 * 365)]

    times = []
    for n, s in reversed(scale):
        t = seconds / s
        if t: times.append((t, n + 's' if t > 1 else n))
        seconds = seconds % s

    if len(times) > 1:
        return ', '.join('%d %s' % t
                         for t in times[:-1]) + ' and %d %s' % times[-1]
    else:
        return '%d %s' % times[0]


# codewars task best solution
def format_duration(s):
    dt = []
    for b, w in [(60, 'second'), (60, 'minute'), (24, 'hour'), (365, 'day'),
                 (s + 1, 'year')]:
        s, m = divmod(s, b)
        if m: dt.append('%d %s%s' % (m, w, 's' * (m > 1)))
    return ' and '.join(', '.join(dt[::-1]).rsplit(', ', 1)) or 'now'


# codewars task best solution
import re


def format_duration(seconds):
    if not seconds: return 'now'
    minutes = seconds / 60
    seconds %= 60
    hours = minutes / 60
    minutes %= 60
    days = hours / 24
    hours %= 24
    years = days / 365
    days %= 365
    a = []
    for n, l in zip([years, days, hours, minutes, seconds],
                    ['year', 'day', 'hour', 'minute', 'second']):
        if n == 1:
            a.append('%d %s' % (n, l))
        elif n > 1:
            a.append('%d %ss' % (n, l))
    return re.sub(r', ([^,]*)$', lambda o: ' and ' + o.group(1), ', '.join(a))


# codewars task best solution
SECONDS_IN_MINUTE = 60
MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24
DAYS_IN_YEAR = 365

SECONDS_IN_HOUR = SECONDS_IN_MINUTE * MINUTES_IN_HOUR
SECONDS_IN_DAY = SECONDS_IN_HOUR * HOURS_IN_DAY
SECONDS_IN_YEAR = SECONDS_IN_DAY * DAYS_IN_YEAR

units = [
    ('year', 'years', SECONDS_IN_DAY * DAYS_IN_YEAR),
    ('day', 'days', SECONDS_IN_HOUR * HOURS_IN_DAY),
    ('hour', 'hours', SECONDS_IN_MINUTE * MINUTES_IN_HOUR),
    ('minute', 'minutes', SECONDS_IN_MINUTE),
    ('second', 'seconds', 1),
]


def format_duration(seconds):
    if not seconds:
        return 'now'

    components = []
    for singular, plural, seconds_in in units:
        value = seconds / seconds_in
        if not value:
            continue
        components.append(pluralize(value, singular, plural))
        seconds = seconds - value * seconds_in

    last = components.pop()
    if not components:
        return last
    return "{} and {}".format(", ".join(components), last)


def pluralize(value, singular, plural):
    return "{} {}".format(value, singular if value == 1 else plural)


# codewars task best solution
def format_duration(seconds):
    if seconds == 0: return 'now'
    y, seconds = divmod(seconds, 60 * 60 * 24 * 365)
    d, seconds = divmod(seconds, 60 * 60 * 24)
    h, seconds = divmod(seconds, 60 * 60)
    m, seconds = divmod(seconds, 60)
    s = seconds
    time_list = [
        str(x) + ' ' + y + ('s' if x > 1 else '') for x, y in zip(
            [y, d, h, m, s], ['year', 'day', 'hour', 'minute', 'second'])
        if x > 0
    ]
    return ', '.join(time_list[:-2] + [' and '.join(time_list[-2:])])


# codewars task best solution
def create(count, name, seconds):
    count, seconds = divmod(seconds, count)
    if count == 1:
        return ['%s %s' % (count, name), seconds]
    elif count == 0:
        return ['', seconds]
    else:
        return ['%s %ss' % (count, name), seconds]


def format_duration(seconds):
    rules = [
        [60 * 60 * 24 * 365, 'year'],
        [60 * 60 * 24, 'day'],
        [60 * 60, 'hour'],
        [60, 'minute'],
        [1, 'second'],
    ]
    out = []
    for rule in rules:
        res, seconds = create(rule[0], rule[1], seconds)
        out.append(res)
    out = filter(lambda x: False if len(x) == 0 else True, out)
    if len(out) == 0:
        return 'now'
    elif len(out) == 1:
        return out[0]
    elif len(out) == 2:
        return '%s and %s' % (out[0], out[1])
    else:
        return ', '.join(out[0:-1]) + ' and %s' % out[-1]


# codewars task best solution
def format_duration(seconds):
    l = [('%d ' + i[1] + ('s' if i[0] - 1 else '')) % i[0] for i in [(
        seconds / (365 * 24 * 3600),
        'year'), ((seconds / (24 * 3600) % 365),
                  'day'), ((seconds / 3600) % 24,
                           'hour'), ((seconds / 60) % 60,
                                     'minute'), (seconds % 60, 'second')]
         if i[0]] if seconds else ['now']
    return ', '.join(l[:-1]) + ('' if len(l) == 1 else ' and ') + l[-1]


# codewars task best solution
from collections import OrderedDict


def format_duration(seconds):
    if (seconds == 0): return 'now'

    time = OrderedDict()

    time['years'] = seconds // 31536000
    time['days'] = seconds // 86400 % 365
    time['hours'] = seconds // 3600 % 24
    time['minutes'] = seconds // 60 % 60
    time['seconds'] = seconds % 60

    output = []

    for key in time:
        if (time[key] > 1):
            output.append(str(time[key]) + ' ' + key)
        elif (time[key] == 1):
            output.append(str(time[key]) + ' ' + key[:-1])

    print(output)

    return ", ".join(output[:-2] + [" and ".join(output[-2:])])


# codewars task best solution
def format_duration(sec):
    text = ''
    if (sec == 0):
        return "now"

    if sec >= 31536000:  #years
        text += str(int(sec / 31536000)) + " year" + (
            "s" if int(sec / 31536000) > 1 else "")
        sec -= 31536000 * int(sec / 31536000)
        text += ("and" if sec > 0 and sec < 60 else "" if
                 (sec % 31536000 == 0) else "and " if
                 (sec % 86400 == 0 and
                  (sec >= 86400 and sec < 31536000)) else "and " if
                 (sec % 3600 == 0 and
                  (sec >= 3600 and sec < 86400)) else "and " if
                 (sec % 60 == 0 and (sec >= 60 and sec < 3600)) else "" if
                 (sec == 0) else ", ")

    if sec >= 86400 and sec < 31536000:  #days
        text += str(int(
            sec / 86400)) + " day" + ("s" if int(sec / 86400) > 1 else "")
        sec -= 86400 * int(sec / 86400)
        text += (" and" if sec > 0 and sec < 60 else "" if
                 (sec % 86400 == 0 and
                  (sec >= 86400 and sec < 31536000)) else " and " if
                 (sec % 3600 == 0 and
                  (sec >= 3600 and sec < 86400)) else " and " if
                 (sec % 60 == 0 and (sec >= 60 and sec < 3600)) else "" if
                 (sec == 0) else ", ")

    if sec >= 3600 and sec < 86400:  #hours
        text += str(int(
            sec / 3600)) + " hour" + ("s" if int(sec / 3600) > 1 else "")
        sec -= 3600 * int(sec / 3600)
        text += (" and" if sec > 0 and sec < 60 else "" if
                 (sec % 3600 == 0 and
                  (sec >= 3600 and sec < 86400)) else " and " if
                 (sec % 60 == 0 and (sec >= 60 and sec < 3600)) else "" if
                 (sec == 0) else ", ")

    if sec >= 60 and sec < 3600:  #minutes
        text += str(int(
            sec / 60)) + " minute" + ("s" if int(sec / 60) > 1 else "")
        sec -= 60 * int(sec / 60)
        text += (" and" if (sec > 0 and sec < 60) else "" if
                 (sec % 60 == 0 and (sec >= 60 and sec < 3600)) else "" if
                 (sec == 0) else ", ")

    if sec > 0 and sec < 60:  #seconds
        if (len(text) > 0):
            text += " "
        text += str(sec) + " second" + ("s" if sec != 1 else "")

    return text