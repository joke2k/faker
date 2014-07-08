# coding=utf-8

from __future__ import unicode_literals

from bs4 import BeautifulSoup
import requests


_URL = 'http://nl.wikipedia.org/w/index.php?title=ISO_3166-1&printable=yes'


def _replace_quotes(s):
    r = s
    for c in '"`':
        r = r.replace(c, "'")
    return r


def get_address_countries(url):
    lst = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    # get the first table
    tbl = soup.body.find_all('table', class_="wikitable")[0]
    # process all rows
    for tr in tbl.find_all('tr'):
        # get the text of all columns
        rec = [td.get_text(strip=True) for td in tr.find_all('td')]
        if len(rec) > 0:
            # get the first column
            txt = _replace_quotes(rec[0])
            lst.append(txt)
    return lst


def _quote(s):
    if s.find("'") >= 0:
        return u'"%s"' % (s,)
    else:
        return u"'%s'" % (s,)


def out_list(lst, indent=8):
    lines = []
    line = (indent-1)*' '
    for e in lst:
        part = _quote(e) + ','
        if (len(line) + 1 + len(part)) >= 80:
            lines.append(line.rstrip())
            line = indent*' ' + part
        else:
            line += ' ' + part
    line = line.rstrip()
    if line:
        lines.append(line)
    return lines


def out_address_countries(lst, indent=4):
    return out_list(lst, indent=2*indent)


if __name__ == "__main__":
    print('### faker/providers/nl_NL/address.py')
    print('')
    
    indent = 4
    lst = get_address_countries(_URL)
    lst.sort()
    print(indent*' ' + '# countries are from ' + _URL)
    print(indent*' ' + 'countries = (')
    for line in out_address_countries(lst, indent=indent):
        print(line)
    print(indent*' ' + ')')
