# IMPORTS:

from requests import get as get_request, RequestException
from bs4 import BeautifulSoup
from sys import version
from platform import system
from tkinter.messagebox import askyesno, showinfo
from webbrowser import open as wb_open
from time import sleep


# ATTRIBUTES:

# print('\n' + version); input()  # debugging
current_version = version.split()[0]

BASE_URL = 'https://www.python.org'
DEBUG = True  # (default: True)
SCRIPT_NAME = 'Python Update Assistant'


# SENDING REQUEST AND GETTING RESPONSE:

print('\n' + f'Getting the data from {BASE_URL}...')
first_try = True
while True:
    try:
        response = get_request(url=f'{BASE_URL}/downloads', stream=False)
    except RequestException as e:
        if first_try:  # don't print the error message repeatedly
            print('\n' + f'{type(e).__name__}:', e.__doc__.split('\n')[0], 'Trying again (every second) in the background...')
            first_try = False
        sleep(1)  # take a breath
    else:
        break
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
    print('\n' + 'Latest version is already installed.')
else:
    print('\n' + 'Version update is available.')
    if askyesno(title='Python Update', message=f'Hey! Here\'s your personal {SCRIPT_NAME} :) \n\nPython interpreter version ({latest_version}) is available for update, may I download it now?'):

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
        if not os:
            os = 'Unknown'
        print('\n' + 'OS:', os)

        match os:
            case 'Windows':
                download_link = direct_download_links['Windows']
            case 'Linux':
                download_link = direct_download_links['Linux/UNIX']
            case 'Darwin':
                download_link = direct_download_links['macOS']
            case _:  # OS is 'Java' or 'Unknown' (i.e. undetermined OS), so, in either cases, direct_download_links['Other'] i.e. 'https://www.python.org/download/other/' will do the work
                download_link = direct_download_links['Other']

        print('Download Link:', download_link)

        # STARTING DOWNLOAD:

        wb_open(url=download_link)

        if download_link != direct_download_links['Other']:
            print('\n' + 'Download started in default browser.')
            showinfo(title='Python Update', message=f'Download has been started in your browser. \n\nOnce it completes, open the downloaded file and install it in order to complete the update. \n\nI hope you liked my work. \n\nSee you later! \n- {SCRIPT_NAME}')

        else:  # if not direct download link
            print('\n' + 'Download Page opened in default browser.')
            showinfo(title='Python Update', message=f'As your OS ({os}) falls under the category of specialized and/or older platforms, "Download Python for Other Platforms" page has been opened in your browser. \n\nFrom the listed platforms there, download Python for your OS. \n\nOnce the download completes, open the file and install it in order to complete the update. \n\nI hope you liked my work. \n\nSee you later! \n- {SCRIPT_NAME}')

    else:
        print('\n' + 'Update postponed.')


print('\n' + 'Bye!')
