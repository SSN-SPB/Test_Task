# from googlesearch import search as search_in_google
from googlesearch import search


def run_library():
    # query = "best python libraries"
    #
    # links = list(search_in_google(query, num_results=10))
    #
    # print(links)
    query = "data science roadmap"
    # results = search(query, advanced=True, num_results=3)
    results = search(
        "data science roadmap",
        advanced=True,
        num_results=3,
        sleep_interval=5
    )

    for r in results:
        print("Title:", r.title if r else "N/A")
        print("URL:", r.url if r else "N/A")
        print("Description:", r.description if r else "N/A")
        print("-" * 40)

if __name__ == "__main__":
    run_library()
