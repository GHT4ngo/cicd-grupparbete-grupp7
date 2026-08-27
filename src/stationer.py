import requests


def hamta_hallplatser():
    url = "https://transport.integration.sl.se/v1/sites"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()

def sok_hallplats(namn, hallplatser=None):
    if hallplatser is None:
        hallplatser = hamta_hallplatser()

    traffar = []
    for site in hallplatser:
        if namn.lower() in site["name"].lower():
            traffar.append({"id": site["id"], "name": site["name"]})
    return traffar


#test
if __name__ == "__main__":
    results = sok_hallplats("slussen")
    print(f"{len(results)} result has found")
    for result in results:
        print(result)