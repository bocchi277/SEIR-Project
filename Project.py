from bs4 import BeautifulSoup
import requests
import sys


def loadUrl(userUrl):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        htmlFile  = requests.get(userUrl,headers=headers, timeout=4)
    except requests.RequestException:
        return None
    if(htmlFile.status_code == 200):
        content = htmlFile.text
        soup = BeautifulSoup(content, 'html.parser')
        title_tag  = soup.find('title')
        title = title_tag.text if title_tag else "No Tag Found"
        bodyTag = soup.find('body')
        bodyText = bodyTag.get_text(separator=" ", strip=True) if bodyTag else "Body is Not there"
        links = [link.get('href') for link in soup.find_all('a') if link.get('href')]
        return {"title": title, "bodyText" : bodyText, "Links": links}
    else:
        print(f"Error the status code is {htmlFile.status_code}, either enter valid url or try again")
        return None

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
    stopWords = {"i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"}
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
        if len(userUrl) == 2:
            userUrl = sys.argv[1]
            content = loadUrl(userUrl)
            for i in content:
                print(f"The {i} is --> {content[i]}")
        elif len(userUrl) >= 3:
            userUrl1 = sys.argv[1]
            userUrl2 = sys.argv[2]
            simhashCompare(userUrl1, userUrl2)
        else:
            userUrl = None
    except Exception as e:
        print(e)