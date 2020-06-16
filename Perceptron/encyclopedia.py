# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 22:00:29 2020

@author: Onkar
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 20:04:25 2020

@author: Onkar
"""

import string

# appostrophe short-wards taken from :
# https://drive.google.com/file/d/0B1yuv8YaUVlZZ1RzMFJmc1ZsQmM/view
appos = {
"aren't" : "are not","can't" : "can not","couldn't" : "could not",
"didn't" : "did not","doesn't" : "does not","don't" : "do not",
"hadn't" : "had not","hasn't" : "has not","haven't" : "have not",
"he'd" : "he would","he'll" : "he will","he's" : "he is","i'd" : "I would",
"i'll" : "I will","i'm" : "I am","isn't" : "is not","it's" : "it is",
"it'll":"it will","i've" : "I have","let's" : "let us","mightn't" : "might not",
"mustn't" : "must not","shan't" : "shall not","she'd" : "she would",
"she'll" : "she will","she's" : "she is","shouldn't" : "should not",
"that's" : "that is","there's" : "there is","they'd" : "they would",
"they'll" : "they will","they're" : "they are","they've" : "they have",
"we'd" : "we would","we're" : "we are","weren't" : "were not",
"we've" : "we have","what'll" : "what will","what're" : "what are",
"what's" : "what is","what've" : "what have","where's" : "where is",
"who'd" : "who would","who'll" : "who will","who're" : "who are",
"who's" : "who is","who've" : "who have","won't" : "will not",
"wouldn't" : "would not","you'd" : "you would","you'll" : "you will",
"you're" : "you are","you've" : "you have","wasn't": "was not",
"we'll":"we will","didn't": "did not"
}


# stopwards taken from https://www.ranks.nl/stopwords
stopwards = [
"", "a","about","above","after","again","against","all","am","an","and",
"any","are","aren't","as","at","be","because","been","before","being","below",
"between","both","but","by","can't","cannot","could","couldn't","did","didn't",
"do","does","doesn't","doing","don't","down","during","each","few","for","from",
"further","had","hadn't","has","hasn't","have","haven't","having","he","he'd",
"he'll","he's","her","here","here's","hers","herself","himself","his","how",
"how's","i","i'd","i'll","i'm","i've","if","in","into","is","isn't","it","it's",
"its","itself","let's","me","more","most","mustn't","my","myself","no","nor",
"not","of","off","on","once","only","or","other","ought","our","ours",
"ourselves","out","over","own","same","shan't","she","she'd","she'll","she's",
"should","shouldn't","so","some","such","than","that","that's","the","their",
"theirs","them","themselves","then","there","there's","these","they","they'd",
"they'll","they're","they've","this","those","through","to","too","under",
"until","up","very","was","wasn't","we","we'd","we'll","we're","we've","were",
"weren't","what","what's","when","when's","where","where's","which","while",
"who","who's","whom","why","why's","with","won't","would","wouldn't","you",
"you'd","you'll","you're","you've","your","yours","yourself","yourselves",
"b", 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]