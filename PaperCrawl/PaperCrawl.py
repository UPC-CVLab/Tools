import lxml
from lxml import etree
import requests
import csv

from tqdm import tqdm

url = "https://proceedings.icml.cc/paper/2020"#论文网站

prefix = "https://proceedings.icml.cc/paper/2020/file/"#pdf文件路径前缀

# 通过xpath解析所需内容
html = requests.get(url)
html.encoding = 'utf-8'
selector = etree.HTML(html.text)
titlelist = selector.xpath("/html/body/div/div[1]/ul/li/a")
authorlit = selector.xpath("/html/body/div/div[1]/ul/li/i")
print(len(titlelist))

# CSV文件写入
csv_obj = open('ICML2020.csv', 'w', newline='', encoding="utf-8")
print('Writing Start……')
csv.writer(csv_obj).writerow(["num", "Authors", "Title","Link"])

for t in tqdm(range(len(titlelist))):
    linkhash = titlelist[t].get("href").split("/")[-1]
    data = {
        "Title":titlelist[t].text,
        "Author":authorlit[t].text,
        "Link":prefix + linkhash + "-Paper.pdf"
    }
    # print(data)
    csv.writer(csv_obj).writerow([t+1,data['Author'],data['Title'],data['Link']])
    # print(str(t+1)+'line finished')

csv_obj.close()
print("finshed")