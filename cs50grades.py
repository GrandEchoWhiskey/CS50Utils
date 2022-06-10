import requests
import sys

URL = 'https://cs50.me'

def getResponse(url, session_cookie):

    if url == None:
        url = URL

    r = requests.get(url, cookies={'session': session_cookie})
    return r.text


def is_valid(html):

    complete = html.find('Click on a course to view your gradebook.') != -1
    return complete and html.find('<div class="list-group">') != -1


def get_subsites(html):

    div_index = html.find('<div class="list-group">')

    if div_index == -1:
        return None

    end_div_index = html.find('</div>', div_index)
    subsites = list()

    while True:

        if end_div_index <= div_index:
            break

        ref_item = '<a href="'
        ref_index = html.find(ref_item, div_index)
        end_ref_index = html.find('"', ref_index + len(ref_item))

        if end_ref_index == -1 or end_ref_index >= end_div_index:
            break

        current_subsite = str()

        for i in range(ref_index + len(ref_item), end_ref_index):
            current_subsite = current_subsite + html[i]

        subsites.append(current_subsite)
        div_index = end_ref_index

    return subsites


def percent(html):

    keyword = 'aria-valuenow="'
    start_index = html.find(keyword)
    end_index = html.find('"', start_index + len(keyword))

    perc = str()
    for i in range(start_index + len(keyword), end_index):
        perc = perc + html[i]

    return int(perc)


def main():

    if len(sys.argv) == 2:
        session = sys.argv[1]
    elif len(sys.argv) > 2:
        return
    else:
        session = input("Set your session cookie from 'cs50.me': ")

    site = getResponse(None, session)

    if not is_valid(site):
        print('Wrong cookie, or empty gradebook.')
        return

    sub = get_subsites(site)

    site_responses = dict()

    for i in range(len(sub)):
        site_responses[sub[i]] = percent(getResponse(URL + sub[i], session))

    for key in site_responses:
        print(key[1::] + ': ' + str(site_responses[key]) + '%')


if __name__ == '__main__':
    main()