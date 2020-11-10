"""
1
-

Viết 1 script để liệt kê tất cả các GitHub repository của 1 user:

Ví dụ với user ``pymivn``, sử dụng dữ liệu ở JSON format tại
https://api.github.com'''/users/pymivn/repos

Câu lệnh của chương trình có dạng::

  python3 githubrepos.py username

Gợi ý:

Sử dụng các thư viện:

- requests
- sys or argparse
"""
import argparse
import requests
import json

parser = argparse.ArgumentParser()
parser.add_argument('user',help="tu khoa",type=str)
args = parser.parse_args()

def crawl(user):
    url = "https://api.github.com/users/{}/repos".format(user)
    r = requests.get(url)
    if r.status_code == 200:
        result = [data["name"] for data in json.loads(r.text)]
    else:
        result = "Invalid user"
    return result

def main():
    user = args.user
    print(crawl(user))

if __name__ == "__main__":
    main()