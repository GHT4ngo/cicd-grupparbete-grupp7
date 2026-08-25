import requests


def sok_hallplats(namn):
    url = "https://transport.integration.sl.se/v1/sites?expand=true"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    sites = response.json()

    traffar = []

    for site in sites:
        if namn.lower() in site["name"].lower():
            traffar.append(
                {
                    "id": site["id"],
                    "name": site["name"],
                }
            )
    
    return traffar


#test
if __name__ == "__main__":
    results = sok_hallplats("slussen")
    print(f"{len(results)} has found")
    for result in results:
        print(result)