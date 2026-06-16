import requests

def reputation_check(server_url,pkgname,repos,urls):
    payload = {
        "pkgname": pkgname,
        "repos": repos,
        "urls": urls
    }

    return requests.post(
        f"{server_url}/pkgbuild/check",
        json=payload,
        timeout=10
    ).json()
