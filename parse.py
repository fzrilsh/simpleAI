from bs4 import BeautifulSoup
import requests
import nltk
from string import punctuation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity 
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

class AI():
    def __init__(self, html, question):
        self.end_chat = False
        self.got_topic = False
        self.do_not_respond = True
        
        self.title = None
        self.text_data = []
        self.sentences = []
        self.para_indices = []
        self.current_sent_idx = None
        
        self.punctuation_dict = str.maketrans({p:None for p in punctuation})
        self.lemmatizer = nltk.stem.WordNetLemmatizer()
        self.stopwords = nltk.corpus.stopwords.words('english')

        self.contentHtml = requests.utils.unquote(html)
        self.question = "when indonesia independents day?"#question
        self.initHtml()

    def sinkronTokenizer(self):
        vectorizer = TfidfVectorizer(tokenizer=self.preprocess)
        self.sentences.append(self.question)
        tfidf = vectorizer.fit_transform(self.sentences)
        scores = cosine_similarity(tfidf[-1],tfidf) 
        self.current_sent_idx = scores.argsort()[0][-2]
        scores = scores.flatten()
        scores.sort()
        value = scores[-2]
        if value != 0:
            print(self.getQP()[0]+self.text_data[self.para_indices[self.current_sent_idx]] or self.sentences[self.current_sent_idx]) 
        else:
            print(False)
        del self.sentences[-1]

    def getQP(self):
        ps = nltk.PorterStemmer()
        inp_wt = []
        for w in self.question.split():
            inp_wt.append(ps.stem(w))

        q_type = []
        for i in inp_wt:
            if i in ['who', 'name of']:
                q_type.append('who ')
                list_to_search = ['he', 'she', 'they', 'Mr', 'Mrs', 'Ms']
            elif i in ['what']:
                q_type.append('what ')
            elif i in ['when']:
                q_type.append('when ')
            elif i in ['where']:
                q_type.append('where ')
            elif i in ['why']:
                q_type.append('why ')
        
        return q_type

    def initHtml(self):
        try:
            data = self.contentHtml
            soup = BeautifulSoup(data, 'html.parser')
            p_data = soup.findAll('p')
            dd_data = soup.findAll('dd')
            p_list = [p for p in p_data]
            dd_list = [dd for dd in dd_data]
            for tag in p_list+dd_list:
                a = []
                for i in tag.contents:
                    if i.name != 'sup' and i.string != None:
                        stripped = ' '.join(i.string.strip().split())
                        a.append(stripped)
                self.text_data.append(' '.join(a))
            
            for i,para in enumerate(self.text_data):
                sentences = nltk.sent_tokenize(para)
                self.sentences.extend(sentences)
                index = [i]*len(sentences)
                self.para_indices.extend(index)
            
            self.title = soup.find('h1').string
            self.got_topic = True 

            self.sinkronTokenizer()
        except Exception as e:
            print(e)
    
    def preprocess(self, text):
        text = text.lower().strip().translate(self.punctuation_dict) 
        words = nltk.word_tokenize(text)
        words = [w for w in words if w not in self.stopwords]
        return [self.lemmatizer.lemmatize(w) for w in words]

html = input()
question = input()
AI(html, question)