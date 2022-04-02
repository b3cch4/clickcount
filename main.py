import os
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
import argparse
load_dotenv()


def shorten_link(headers, received_link, custom_domain):
    url = {"long_url": received_link, "domain": custom_domain}
    response = requests.post(
        'https://api-ssl.bitly.com/v4/bitlinks',
        headers=headers,
        json=url
    )
    response.raise_for_status()
    return response.json().get('id')


def sum_clicks(headers, bitlink):
    params = {'unit': 'day', 'units': '-1'}
    response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary',
        params=params,
        headers=headers
    )
    response.raise_for_status()
    return response.json().get('total_clicks')


def is_bitlink(headers, bitlink):
    response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}',
        headers=headers
    )
    return response.ok


def check_link(url):
    response = requests.get(url)
    response.raise_for_status()


def cut_url_protocol(url):
    full_bitlink = urlparse(url)
    bitlink = full_bitlink.netloc + full_bitlink.path
    return bitlink


def main():
    bitly_auth_token = os.getenv('BITLY_TOKEN')
    bitly_custom_domain = os.getenv('CUSTOM_DOMAIN')
    http_headers = {
        'Authorization': f'Bearer {bitly_auth_token}'
    }
    parser = argparse.ArgumentParser()
    parser.add_argument('link')
    args = parser.parse_args()
    received_link = args.link
    try:
        check_link(received_link)
        if is_bitlink(http_headers, cut_url_protocol(received_link)):
            print(
                'Количество кликов',
                sum_clicks(http_headers, cut_url_protocol(received_link))
            )
        else:
            print('Битлинк', shorten_link(http_headers, received_link, bitly_custom_domain))
    except requests.exceptions.HTTPError:
        print('Вы ввели неправильную ссылку или неверный токен.')
    except requests.exceptions.MissingSchema:
        print("Вы не ввели протокол https:// перед ссылкой")
    except requests.exceptions.ConnectionError:
        print("Невозможно соединиться в выбраным ресурсом")
    except requests.exceptions.InvalidURL:
        print("Проверьте, введена ли ссылка после https://")


if __name__ == "__main__":
    main()
