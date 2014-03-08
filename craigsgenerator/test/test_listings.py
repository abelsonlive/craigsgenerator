import datetime

import nose.tools as n

import craigsgenerator.test.util as util
from craigsgenerator.listings import listings, join

fake_response = lambda url: util.FakeResponse(url = url, text = '<a href="%s">Look!</a>' % url)
fake_datetime = datetime.datetime(2014,1,1)

def fake_result(url):
    return {
        'html': fake_response(url).text,
        'downloaded': fake_datetime,
        'url': url,
        'site': 'chicago.craigslist.org',
        'section': 'sub',
    }

def fake_download_many(_, urls, __, ___, ____):
    return (fake_response(url) for url in urls)

def test_listings():
    scheme = 'https'
    gotten = []
    def get(url):
        gotten.append(url)
        return fake_response(url)
    n_threads = 4
    warehouse = {}
    site = 'chicago.craigslist.org'
    section = 'sub'

    parse_listing = lambda _: {}
    parse_search = lambda _: [{'href':None,'date' :None}]

    def parse_next_search_url(scheme, site, section, html, searched_urls = 0):
        if html == None:
            searched_urls *= 0
        url = '%s://%s/%s/index%03d.html' % (scheme, site, section, searched_urls)
        searched_urls += 1
        return url

    l = listings(scheme, get, n_threads, warehouse, site, section,
                 parse_listing, parse_search, parse_next_search_url,
                 fake_download_many, None, lambda: fake_datetime)
    n.assert_list_equal(gotten, [])

    response = next(l)
    n.assert_equal(response, fake_result('https://chicago.craigslist.org/sub/index000.html'))
    n.assert_list_equal(gotten, ['https://chicago.craigslist.org/sub/index000.html'])

    response = next(l)
    n.assert_equal(response, fake_result('https://chicago.craigslist.org/sub/index100.html'))
    n.assert_list_equal(gotten, list(map(fake_result, [
        'https://chicago.craigslist.org/sub/index000.html',
        'https://chicago.craigslist.org/sub/index100.html'])))

def test_join():
    url = 'http://example.com'
    search_row = {'href': url, 'date': '3 months ago'}
    response = fake_response(url)
    site = 'chicago.craigslist.org'
    section = 'sub'
    datetime_func = lambda: fake_datetime

    observed = join(search_row, listing_response, datetime_func, site, section)
    expected = { 'url': url, 'site': site, 'section': section,
        'html': response.text, 'downloaded': datetime_func()}
    n.assert_dict_equal(search_row, {'href': url, 'date': '3 months ago'}) # should not mutate
    n.assert_dict_equal(observed, expected)
