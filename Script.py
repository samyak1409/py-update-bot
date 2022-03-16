from requests import get as get_request
from bs4 import BeautifulSoup


BASE_URL = 'https://www.python.org'


response = get_request(url=f'{BASE_URL}/downloads', stream=False)
# print(response.status_code); input()  # debugging

soup = BeautifulSoup(markup=response.text, features='html.parser')
# print(soup.prettify()); input()  # debugging

download_info = soup.find(name='div', class_='download-for-current-os')
# print(download_info.prettify()); input()  # debugging

all_os = download_info.find(name='p', recursive=False)
# print(all_os.prettify()); input()  # debugging
download_pages = {os.text: BASE_URL+os['href'] for os in all_os.find_all(name='a')}
print('\n' + 'download_pages:', download_pages)

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
        case _:  # no file extension
            # direct_download_links['Other'] = link  # because 'https://www.python.org/download/other/' is making more sense than 'https://www.python.org/downloads/release/python-3102/'
            latest_version = os.a.text
            print('\n' + 'latest_version:', latest_version)

print('\n' + 'direct_download_links:', direct_download_links)
