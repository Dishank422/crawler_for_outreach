from scholarly import scholarly
import pandas as pd

out_ = []
year = input("Please enter year of search: ")
print("It may take a few minutes")

# Reading the list of faculties
with open('faculty.txt') as f:
    faculties = f.readlines()

# reading the archive of papers
df = pd.read_csv('archive.csv')
# extracting the title column
archive = df['Title'].to_numpy()

# removing the newline character from end
archive = [ title.rstrip() for title in archive ]

# removing the newline character from end
faculties = [ faculty.rstrip() for faculty in faculties ]

for faculty in faculties:
    search_query = scholarly.search_author(faculty)
    author = scholarly.fill(next(search_query), sections=['publications'])
    for publication in author['publications']:
        if 'pub_year' in publication['bib']:
            if publication['bib']['pub_year'] == year and publication['bib']['title'] not in archive:
                publication = scholarly.fill(publication)
                out_.append({'Author':publication['bib']['author'],\
                     'Title':publication['bib']['title'], 'Publication_year':publication['bib']['pub_year']})
                if 'pub_url' in publication:
                    out_[-1]['url'] = publication['pub_url']
                if 'conference' in publication['bib']:
                    out_[-1]['conference'] = publication['bib']['conference']
                if 'journal' in publication['bib']:
                    out_[-1]['journal'] = publication['bib']['journal']
                if 'publisher' in publication['bib']:
                    out_[-1]['publisher'] = publication['bib']['publisher']
                # adds a counter to number of papers being added
                print('+',end='', flush=True)
print()

df = pd.DataFrame(out_)   

df.to_csv('pubs.csv')

# appending the new papers in archive
df.to_csv('archive.csv',mode='a',header=False, index=False)

