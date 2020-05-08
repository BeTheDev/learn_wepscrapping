import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = "https://www.indeed.com/jobs?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&as_src=&radius=0&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch#"


def get_last_page():
    result = requests.get(URL)

    #print(indeed_result)
    #print(indeed_result.text)
    soup = BeautifulSoup(result.text, "html.parser")

    # print(indeed_soup)

    pagination = soup.find("div", {"class": "pagination"})

    # print(pagination)

    links = pagination.find_all("a")

    # print(pages)
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
    #pages.append(link.find("span"))
    # [0:5] range 지정 , [:-1] 일경우 뒤에서 -1

# 최종 페이지 확인하기 위해 -1 실행
#print(pages[-1])

    max_pages = pages[-1]
    return max_pages


# range()

# print(range(max_page))

# for n in range(max_page):
# for n in range(max_page):
#print (n) # 0~19 나옴

# print(f"start={n*50}")

# def extract_indeed_jobs(last_page):
# 	for page in range(last_page):
# 		result=requests.get(f"{INDEED_URL}&start={page*LIMIT}")
# 		print(result.status_code)

# def extract_indeed_jobs(last_page):
# 	for page in range(last_page):
# 		print(f"&start={page*LIMIT}")

# def extract_job(html):
#     title = html.find("h2", {"class": "title"}).find("a")["title"]
#     company = html.find(str("span", {"class": "company"}))
#     if company is not None:
#         company_anchor = company.find(str("a"))
#         if company_anchor is not None:
#             company = str(company_anchor.string)
#         else:
#             company = str(company.string)
#         company = company.strip()
#         location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
#         job_id = html["data-jk"]
#         return {
#             'title': title,
#             'company': company,
#             'location': location,
#             'link': f"https://www.indeed.com/jobs?as_and=python&as_phr&as_any&as_not&as_ttl&as_cmp&jt=all&st&as_src&radius=0&fromage=any&limit=50&sort&psf=advsrch&from=advancedsearch&vjk={job_id}="
#         }


def extract_job(html):
    title = html.find('h2', {"class": "title"}).find("a")["title"]
    company = html.find("span", {"class": "company"})
    company_atag = company.find("a")
    if company_atag is not None:
        company = str(company_atag.string)
    else:
        company = (str(company.string))
    company = company.strip()
    location = html.find('div', {"class": "recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    return {
        "title": title,
        "company": company,
        "location": location,
        "link": f"https://www.indeed.com/viewjob?jk={job_id}"
    }


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"scrapping Indeed: page: {page}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs():
	last_page= get_last_page()
	jobs= extract_jobs(last_page)
	return jobs
