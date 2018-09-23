
import nltk

##To grab some content from the internet use urllib.request 
import urllib.request
response = urllib.request.urlopen('http://php.net/')

response.read()
html = response.read()
##As you can see from the printed output, the result contains a lot of HTML 
##tags that need to be cleaned. We can use BeautifulSoup 
##to clean the grabbed text like this:
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,"html5lib")
text = soup.get_text(strip=True)
print(text)

###Now, we have clean text from the crawled web page. Awesome, Right?

##Finally, let's convert that text into tokens by splitting the text like this:

tokens = [t for t in text.split()] 
print(tokens)

##The text is much better now. Let's calculate the frequency distribution 
##of those tokens using Python NLTK. There is a function 
##in NLTK called FreqDist() that does the job:
freq = nltk.FreqDist(tokens) 
for key,val in freq.items(): 
    print (str(key) + ':' + str(val))

##If you search the output, you'll find that the most frequent token is PHP.

##You can plot a graph for those tokens using plot function like this: 

freq.plot(20, cumulative=False)

###Now, let's modify our code and clean the tokens before plotting the graph. 
##First, we will make a copy of the list. 
##Then, we will iterate over the tokens and remove the stop words:

clean_tokens = tokens[:] 
sr = stopwords.words('english')
for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)
        
        
        