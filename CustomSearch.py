import pprint
from googleapiclient.discovery import build

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

Number_of_search_results = 3

def CustomSearch():

  service = build("customsearch", "v1", developerKey="AIzaSyB4C2LHbCFjrllbIP3FDZNoF1l-EoiMvAU")

  response = service.cse().list(
      q='example.dll', num = Number_of_search_results, 
      cx='014532782513412153458:b5ytho-ixgm',
    ).execute()

  #pprint.pprint(response)

  print('Amount of search results: %s\n' % response['searchInformation']['formattedTotalResults'])
  for i in range(Number_of_search_results):
    print('result url: %s \nresult snippet: %s \n' % (response['items'][i]['formattedUrl'], response['items'][i]['snippet']))

if __name__ == '__main__':
  CustomSearch()