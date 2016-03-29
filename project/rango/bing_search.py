import requests

from secrets import BING_API_KEY

def run_query(search_terms):

    # root_url = 'https://api.datamarket.azure.com/Bing/Search/v1/Web?Query=%27python%27&Market=%27en-US%27'
    root_url = "https://api.datamarket.azure.com/Bing/Search/v1/"

    source = 'Web'
    market = 'en-US'
    results_per_page = 10
    offset = 0

    search_url = "{source}?Query='{query}'&$format=json&$top={res_num}&$skip={offset}&Market='{market}'".format(source=source,
            query=search_terms,
            res_num=results_per_page,
            offset=offset,
            market=market,
            )

    results = []
    username = ''
    response = requests.get(root_url + search_url, auth=(username, BING_API_KEY))
    json_response = response.json()

    for result in json_response['d']['results']:
        results.append({
            'title': result['Title'],
            'link': result['Url'],
            'summary': result['Description']
            })

    return results

def main():
    search_term = raw_input('What are you searching for? ')
    response = run_query(search_term)
    for result in response:
        print result['title'], result['link']

if __name__ == '__main__':
    main()
