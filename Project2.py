from Project1 import loadUrl, sys
def countFreq(bodyText):
    bodyText = bodyText.lower()
    cleaned = []
    for character in bodyText:
        if character.isalnum():
            cleaned.append(character)
        else:
            cleaned.append(" ")
    wordText = "".join(cleaned)
    wordList = wordText.split()
    freq = dict()
    for word in wordList:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq
def hash_func(word):
    p = 53
    m = 2**64
    hash_val = 0
    p_power = 1
    for c in word:
        hash_val = (hash_val + ord(c) * p_power) % m
        p_power = (p_power * p) % m
    return hash_val
def simHash(freq):
    weight = [0]*64
    stopWords = {
    "a","about","above","according","across","after","afterwards","again","against",
    "albeit","all","almost","alone","along","already","also","although","always",
    "am","among","amongst","an","and","another","any","anybody","anyhow","anyone",
    "anything","anyway","anywhere","apart","are","around","as","at","be","became",
    "because","become","becomes","becoming","been","before","beforehand","behind",
    "being","below","beside","besides","between","beyond","both","but","by","can",
    "cannot","canst","certain","cf","choose","contrariwise","cos","could","cu",
    "day","do","does","doesn't","doing","dost","doth","down","dual","during","each",
    "either","else","elsewhere","enough","et","etc","even","ever","every","everybody",
    "everyone","everything","everywhere","except","far","farther","farthest","few",
    "first","for","formerly","forth","forward","from","further","furthermore",
    "furthest","get","go","had","hardly","has","hast","hath","have","he","hence",
    "henceforth","her","here","hereabouts","hereafter","hereby","herein","hereto",
    "hereupon","hers","herself","him","himself","his","hither","hitherto","how",
    "however","howsoever","i","ie","if","in","inasmuch","indeed","indoors","inside",
    "insomuch","instead","into","inward","inwards","is","it","its","itself","just",
    "kind","last","latter","latterly","less","lest","let","like","little","many",
    "may","maybe","me","meantime","meanwhile","might","more","moreover","most",
    "mostly","much","must","my","myself","namely","need","neither","never",
    "nevertheless","next","no","nobody","none","nonetheless","noone","nor","not",
    "nothing","notwithstanding","now","nowadays","nowhere","of","off","often","ok",
    "on","once","one","only","onto","or","other","others","otherwise","ought",
    "our","ours","ourselves","out","outside","over","own","perhaps","plenty",
    "quite","rather","really","round","said","same","see","seeing","seem",
    "seemed","seeming","seems","seen","seldom","several","she","should","since",
    "so","some","somebody","somehow","someone","something","sometime","sometimes",
    "somewhat","somewhere","still","such","than","that","the","their","them",
    "themselves","then","there","thereabout","thereabouts","thereafter","thereby",
    "therefore","therein","thereof","thereon","thereto","thereupon","these","they",
    "this","those","though","through","throughout","thru","thus","thy","thyself",
    "till","to","together","too","toward","towards","under","underneath","unless",
    "unlike","until","up","upon","upward","upwards","us","use","used","using",
    "very","via","want","was","we","well","were","what","whatever","when","whence",
    "whenever","where","whereabouts","whereafter","whereas","whereat","whereby",
    "wherefore","wherefrom","wherein","whereinto","whereof","whereon","whereto",
    "whereunto","whereupon","wherever","whether","which","while","whilst","whither",
    "who","whoever","whole","whom","whose","why","will","with","within","without",
    "would","ye","yet","you","your","yours","yourself","yourselves"
}
    for word in freq:
        if word in stopWords:
            continue
        else:
            hashed = format(hash_func(word), '064b')
            for bit in range(64):
                if hashed[bit] == "1":
                    weight[bit] += freq[word]
                else:
                    weight[bit] -= freq[word]
    final = ""
    for bit in weight:
        if bit <= 0:
            final += "0"
        else:
            final += "1"
    return final
def simhashCompare(url1, url2):
    try:
        load1 = loadUrl(url1)
        load2 = loadUrl(url2)
        if not load1 and not load2:
            print("Failed to load both links")
            return
        elif not load1:
            print("Failed to load Link 1")
            return
        elif not load2:
            print("Failed to load link 2")
            return
        freq1 = countFreq(load1['bodyText'])
        freq2 = countFreq(load2['bodyText'])
        simHash1 = simHash(freq1)
        simHash2 = simHash(freq2)
        same_bit  = 0
        for bit in range(len(simHash1)):
            if simHash1[bit] == simHash2[bit]:
                same_bit += 1
        print(f"Simhash of Url 1 is {simHash1} \nSimhash for url 2 is { simHash2}\n Comman bits in both out of 64 is {same_bit}")

    except Exception as e:
        print(e)



if __name__ == "__main__":
    try:
        userUrl = sys.argv
        if len(userUrl) >= 3:
            userUrl1 = sys.argv[1]
            userUrl2 = sys.argv[2]
            simhashCompare(userUrl1, userUrl2)
        else:
            userUrl = None
    except Exception as e:
        print(e)