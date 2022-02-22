from scholarly import scholarly
import pandas as pd

out_ = []
year = input("Please enter year of search: ")

with open('faculty.txt') as f:
    faculty = f.readlines()

for i in range(len(faculty)):
    faculty[i] = faculty[i].rstrip()

for i in faculty:
    search_query = scholarly.search_author(i)
    author = scholarly.fill(next(search_query), sections=['publications'])
    for j in author['publications']:
        if 'pub_year' in j['bib']:
            if j['bib']['pub_year'] == year:
                j = scholarly.fill(j)
                out_.append({'Author':j['bib']['author'], 'Title':j['bib']['title'], 'Publication_year':j['bib']['pub_year']})
                if 'pub_url' in j:
                    out_[-1]['url'] = j['pub_url']
                if 'conference' in j['bib']:
                    out_[-1]['conference'] = j['bib']['conference']
                if 'journal' in j['bib']:
                    out_[-1]['journal'] = j['bib']['journal']
                if 'publisher' in j['bib']:
                    out_[-1]['publisher'] = j['bib']['publisher']

df = pd.DataFrame(out_)   

df.to_csv('pubs.csv')
