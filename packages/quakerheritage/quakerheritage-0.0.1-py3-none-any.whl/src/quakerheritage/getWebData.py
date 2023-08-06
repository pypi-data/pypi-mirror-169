import urllib3, pdfplumber, io, requests, re
from bs4 import BeautifulSoup, SoupStrainer


# connect to website and get list of all pdfs, removing page navigation values
def getUrls(url):
    pdfList = []
    response = requests.get(url)
    for link in BeautifulSoup(response.text, 'html.parser', parse_only=SoupStrainer('a')):
        if link.has_attr('href') and link['href'][0] != "#":
            pdfList.append(url + link['href'])
    return pdfList

# All pdfs are formatted identically and contain common parameters for core data. 
# The below isolates items 1.1-1.18 and uses a series of splitting logics to isolate the dictionary key and value

def pdfDataExtract(url):
    itemDict = {}

    http = urllib3.PoolManager()
    temp = io.BytesIO()
    temp.write(http.request("GET", url).data)
    try:    
        pdf = pdfplumber.open(temp)
        all_text = ''
        itemDict["Meeting Name"] = url.split('/')[-1].split('.')[0].replace("%20", " ")
        header_list= pdf.pages[0].extract_text().splitlines()[0:5]
        header_data = [x.strip() for x in header_list if x.strip()]
        itemDict["Meeting Full Name"] = header_data[0]
        itemDict["Meeting House Address"] = header_data[1]
        itemDict[header_data[2].split(': ')[0]] = header_data[2].split(': ')[1]

        for pdf_page in pdf.pages:
            single_page_text = pdf_page.extract_text()
            if single_page_text is not None:
                all_text += '\n' + single_page_text
        startLoc = all_text.find('1.1')
        endLoc = all_text.find('1.19')
        trimText = all_text[startLoc:endLoc]
        splitText = re.split(r"[1]\.[0-9]+", trimText)
        for item in splitText[1:]:
            splitItem = item.strip().split(': ')
            itemDict[splitItem[0]] = splitItem[1].strip()
    except:
        pass
    return itemDict
