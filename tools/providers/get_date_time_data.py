# coding=utf-8

"""
Extract country code, name, and list of timezones from pytz_.

Requires (local) installation of pytz_::

  pip install pytz
  
.. _pytz: http://pytz.sourceforge.net/
"""

from __future__ import unicode_literals

import pytz


def _replace_quotes(s):
    r = s
    for c in '"`':
        r = r.replace(c, "'")
    return r


def out_country_details(indent=8):
    # get the ISO 3166-1 alpha-2 codes
    codes = [cc for cc in pytz.country_timezones]
    codes.sort()
    # build list with 
    lines = []
    line = (indent-1)*' '
    for code in codes:
        # first part: code and name
        line = indent*' '
        line += "{'code': %s, 'name': %s," % (code, pytz.country_names[code],)
        lines.append(line)
        # second part: timezones, can span multiple lines
        line = indent*' ' + ' '
        line += "'timezones': ["
        offset = len(line)
        # only get the timezones that are commonly used
        tzs = [tz for tz in pytz.country_timezones[code]
               if tz in pytz.common_timezones_set]
        tzs.sort()
        for tz in tzs:
            part = _quote(tz) + ','
            if (len(line) + 1 + len(part)) >= 80:
                lines.append(line.rstrip())
                line = offset*' ' + part
            else:
                line += part + ' '
        # finalize second part
        part = '],'
        if (len(line) + len(part)) >= 80:
            lines.append(line.rstrip())
            line = (offset - 1)*' ' + part
        else:
            line = line.rstrip() + part
        lines.append(line.rstrip())
    return lines


def _quote(s):
    if s.find("'") >= 0:
        return u'"%s"' % (s,)
    else:
        return u"'%s'" % (s,)


if __name__ == "__main__":
    print('### faker/providers/date_time.py')
    print('')
    
    indent = 4
    offset = indent*' '
    print(offset + '# countries are from pytz ' + pytz.__version__)
    print(offset + '# see: http://pytz.sourceforge.net/')
    print(offset + '# with ISO 3166-1 alpha-2 code, English country name')
    print(offset + '# and a list of (commonly used) timezones per country')
    print(indent*' ' + 'countries = (')
    for line in out_country_details(indent=2*indent):
        print(line)
    print(indent*' ' + ')')
