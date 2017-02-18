#Python2.7
#Program that returns the no of search results found in www.ecosia.org (Search engine)
from urllib2 import urlopen #Getting the source code
key_word="+".join(raw_input("Enter the KeyWord..").split()) #Asking the keyword
Link="https://www.ecosia.org/search?q="+key_word #Attaching the keyword to the link
response=urlopen(Link) #Opening the link.. Requires internet connection
page_source=response.read() #Reading 
start=page_source.index('''<div class="search-filters-text pull-left">''')
end=page_source.index('''<span data-trans-id="results_results">''')
result=page_source[start+len('''<div class="search-filters-text pull-left">'''):end].strip() #Source Code lies between the start and end
print "The number of results found is..",result #Printing the result.. :-) Nice and Easy