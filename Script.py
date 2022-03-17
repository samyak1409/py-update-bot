# IMPORTS:

from requests import get as get_request
from bs4 import BeautifulSoup
from sys import version
from platform import system


# ATTRIBUTES:

# print('\n' + version); input()  # debugging
current_version = version.split()[0]
BASE_URL = 'https://www.python.org'
DEBUG = True  # (default: True)


# SENDING REQUEST AND GETTING RESPONSE:

response = get_request(url=f'{BASE_URL}/downloads', stream=False)
# print(response.status_code); input()  # debugging


# PARSING THE HTML:

soup = BeautifulSoup(markup=response.text, features='html.parser')
# print(soup.prettify()); input()  # debugging

download_info = soup.find(name='div', class_='download-for-current-os')
# print(download_info.prettify()); input()  # debugging

latest_version = download_info.find(name='p', class_='download-buttons').a.text.split()[-1]
print('\n' + 'Current Version:', current_version, '\n' + 'Latest Version :', latest_version)


# COMPARING THE VERSION:

if current_version == latest_version:
    print('\n' + 'Latest version is already installed!')
else:
    print('\n' + 'Version update is available.')

    # PARSING THE DOWNLOAD LINKS:

    all_os = download_info.find(name='p', recursive=False)
    # print(all_os.prettify()); input()  # debugging
    download_pages = {os.text: BASE_URL+os['href'] for os in all_os.find_all(name='a')}
    if DEBUG:
        print('\n' + 'Download Pages:', download_pages)

    direct_download_links = download_pages

    for os in download_info.find_all(name='p', class_='download-buttons'):

        link = os.a['href']
        if link.startswith('/'):  # absolute path
            link = BASE_URL + link

        file_extension = link.rsplit('.', maxsplit=1)[1]
        # print(file_extension)  # debugging
        match file_extension:
            case 'exe':
                direct_download_links['Windows'] = link
            case 'xz':
                direct_download_links['Linux/UNIX'] = link
            case 'pkg':
                direct_download_links['macOS'] = link
            # case _:  # no file extension
                # direct_download_links['Other'] = link  # because 'https://www.python.org/download/other/' is making more sense than 'https://www.python.org/downloads/release/python-3102/'

    if DEBUG:
        print('Direct Download Links:', direct_download_links)

    # IDENTIFYING THE UNDERLYING OS (https://stackoverflow.com/questions/1854/python-what-os-am-i-running-on):
    # When to use os.name, sys.platform, or platform.system?: https://stackoverflow.com/a/58071295

    os = system()  # Returns the system/OS name, such as 'Linux', 'Darwin', 'Java', 'Windows'. An empty string is returned if the value cannot be determined.
    print('\n' + 'OS:', os)

    match os:
        case 'Windows':
            download_link = direct_download_links['Windows']
        case 'Linux':
            download_link = direct_download_links['Linux/UNIX']
        case 'Darwin':
            download_link = direct_download_links['macOS']
        case _:  # OS is 'Java' or '' (i.e. undetermined OS), so, in either cases, direct_download_links['Other'] i.e. 'https://www.python.org/download/other/' will do the work
            download_link = direct_download_links['Other']

    print('Download Link:', download_link)


# todo:
#  downloading
#  startup with system
