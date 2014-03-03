import os
from collections import namedtuple

import nose.tools as n
import lxml.html

import craigsgenerator.parse as parse

p = lxml.html.fromstring('''
 <p class="row" data-latitude="30.289600" data-longitude="-97.739600" data-pid="4331364900"> <a href="/sub/4331364900.html" class="i"></a> <span class="star"></span> <span class="pl"> <span class="date">Feb 15</span>  <a href="/sub/4331364900.html">Pre-leasing Apt in WEST CAMPUS for Summer 2014</a> </span> <span class="l2">  <span class="price">&#x0024;925</span> / 1br -  <span class="pnr"> <small> (806 West 24th St)</small> <span class="px"> <span class="p"> <a href="#" class="maptag" data-pid="4331364900">map</a></span></span> </span>  </span> </p>
''')
p.make_links_absolute('https://austin.craigslist.org/sub/index200.html')

FakeResponse = namedtuple('Response', ['url', 'text'])

def test_search_row_with_location():
    o = parse.search_row(p)
    e = {
        'href': 'https://austin.craigslist.org/sub/4331364900.html',
        'latitude': 30.289600,
        'longitude': -97.739600,
        'date': 'Feb 15',
        'title': 'Pre-leasing Apt in WEST CAMPUS for Summer 2014',
        'price': 925,
    }
    assert o == e

def _read(fn):
    with open(os.path.join('craigsgenerator','test','fixtures',fn)) as fp:
        r = FakeResponse('https://foo.bar/baz', fp.read())
    return r

def test_search():
    observed = parse.search(_read(fn = 'austin-sub.html'))
    n.assert_equal(len(observed), 100)

def check_listing(fn, expected):
    r = _read(fn)
    observed = parse.listing(r)
    n.assert_dict_equal(observed, expected)

listing_testcases = [
    '', {},
    '', {},
    '', {},
]

def test_listing():
    for fn, expected in listing_testcases:
        yield check_listing, fn, expected
