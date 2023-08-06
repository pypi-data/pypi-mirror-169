import platform
import os
import requests
import shutil
import zipfile


def install(linux_version: int = 1051186, windows_version: int = 1051150):
    system = platform.system().lower()

    if system == 'windows':
        version = windows_version
        appdata_dir_path = os.getenv('APPDATA')
        chromiums_dir_path = os.path.join(appdata_dir_path, '..', 'Local', 'chromiums')
        download_url = f'https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Win_x64%2F{version}%2Fchrome-win.zip?&alt=media'
        chromium_file_path = os.path.join('chrome-win', 'chrome.exe')
    elif system == 'linux':
        version = linux_version
        chromiums_dir_path = os.path.join('/tmp', 'chromiums')
        download_url = f'https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Linux_x64%2F{version}%2Fchrome-linux.zip?&alt=media'
        chromium_file_path = os.path.join('chrome-linux', 'chrome')

    chromium_dir_path = os.path.join(chromiums_dir_path, str(version))
    chromium_file_path = os.path.join(chromium_dir_path, chromium_file_path)

    if not os.path.isdir(chromiums_dir_path):
            os.mkdir(chromiums_dir_path)

    if not os.path.isdir(chromium_dir_path):
        os.mkdir(chromium_dir_path)

        try:
            print(f'Start download chromium version {version}...')
            response = requests.get(download_url)
            chromium_zip_path = os.path.join(chromium_dir_path, f'{str(version)}.zip')

            with open(chromium_zip_path, 'wb') as f:
                f.write(response.content)

            print(f'Finish download chromium version {version}.')
            print(f'Start unzip...')
            zip = zipfile.PyZipFile(chromium_zip_path)
            zip.extractall(chromium_dir_path)
            zip.close()
            os.remove(chromium_zip_path)
            print(f'Finish.')
        except Exception as error:
            print(f'Install error：{error}')

            if os.path.isdir(chromium_dir_path):
                shutil.rmtree(chromium_dir_path)

            raise RuntimeError(error)

    return chromium_file_path
