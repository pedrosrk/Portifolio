from nltk.sentiment import SentimentIntensityAnalyzer 
''' This library gives access to VADER (Valence Aware Dictionary and sEntiment Reasoner). 
A pretrained sentiment analyzer used in social media. It is more efficient in a small 
sentences. '''

class sentiment():
    def __init__(self, text=None):
        ''' Default constructor with a text atribute or 'I am happy' as default '''
        if text is None:
            self.message = 'I am happy'
        else:
            self.message = text

    def get_message(self):
        ''' Get the message. '''
        return self.message
    
    def set_message(self, text):
        ''' Set the message. '''
        self.message = text

    def show_scores(self):
        ''' Start a sentiment analyser instance throught a contructor. Give to a specific sentence 
        to the model and return a scores with sentences felling. '''
        sia = SentimentIntensityAnalyzer()
        print(sia.polarity_scores(self.message))

    def sentiment_scores(self):
        ''' Start a sentiment analyser instance throught a contructor. Give to a specific sentence 
        to the model and return a scores with sentences felling. '''
        sia = SentimentIntensityAnalyzer()
        return sia.polarity_scores(self.message)
    
    def sentiment_scores_pos(self):
        ''' Start a sentiment analyser instance throught a contructor. Give to a specific sentence 
        to the model and return a positive scores with sentences felling. '''
        sia = SentimentIntensityAnalyzer()
        pos = sia.polarity_scores(self.message)['pos']
        return pos
    
    def sentiment_scores_compound(self):
        ''' Start a sentiment analyser instance throught a contructor. Give to a specific sentence 
        to the model and return a positive scores with sentences felling. '''
        sia = SentimentIntensityAnalyzer()
        comp = sia.polarity_scores(self.message)['compound']
        return comp


