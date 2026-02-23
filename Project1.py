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
if __name__ == "__main__":
    try:
        userUrl = sys.argv
        if len(userUrl) == 2:
                userUrl = sys.argv[1]
                content = loadUrl(userUrl)
                if content:
                    for i in content:
                        print(f"The {i} is --> {content[i]}")
                else:
                    print("Failed , Empty Content")
    except Exception as e:
        print(e)