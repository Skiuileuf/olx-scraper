import requests
import os
import argparse

def scrape_olx(query, max_results=1000, limit=50):
    limit = min(limit, 50) # OLX limits the number of results per request to 50
    os.makedirs("api", exist_ok=True)

    for offset in range(0, max_results, limit):
        response = requests.get(f'https://www.olx.ro/api/v1/offers?offset={offset}&limit={limit}&query={query}')

        filename = f"api/olx-{offset}-{limit}-{query}.json"
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Downloaded {filename}")

def main():
    parser = argparse.ArgumentParser(description="Scrape OLX listings")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--max_results", type=int, default=1000, help="Maximum number of results to fetch")
    parser.add_argument("--limit", type=int, default=50, help="Number of results per request")

    args = parser.parse_args()

    scrape_olx(args.query, args.max_results, args.limit)

if __name__ == "__main__":
    main()