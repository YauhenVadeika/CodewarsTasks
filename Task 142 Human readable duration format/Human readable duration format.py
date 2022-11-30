# my task solution
def format_duration(seconds):

    words = ["year", "day", "hour", "minute", "second"]

    if not seconds:
        return "now"
    else:
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        y, d = divmod(d, 365)

        time = [y, d, h, m, s]

        duration = []

        for x, i in enumerate(time):
            if i == 1:
                duration.append(f"{i} {words[x]}")
            elif i > 1:
                duration.append(f"{i} {words[x]}s")

        if len(duration) == 1:
            return duration[0]
        elif len(duration) == 2:
            return f"{duration[0]} and {duration[1]}"
        else:
            return ", ".join(duration[:-1]) + " and " + duration[-1]


print(format_duration(3662))


# codewars task best solution
def format_duration(seconds):
    if seconds == 0: return "now"
    units = ((31536000, "year"), (86400, "day"), (3600, "hour"),
             (60, "minute"), (1, "second"))
    ts, t = [], seconds
    for unit in units:
        u, t = divmod(t, unit[0])
        ts += ["{} {}{}".format(u, unit[1], "s" if u > 1 else "")
               ] if u != 0 else []
    return ", ".join([str(d) for d in ts[:-1]
                      ]) + (" and " if len(ts) > 1 else "") + ts[-1]


# codewars task best solution
def format_duration(s):
    dt = []
    for b, w in [(60, 'second'), (60, 'minute'), (24, 'hour'), (365, 'day'),
                 (s + 1, 'year')]:
        s, m = divmod(s, b)
        if m: dt.append('%d %s%s' % (m, w, 's' * (m > 1)))
    return ' and '.join(', '.join(dt[::-1]).rsplit(', ', 1)) or 'now'


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