import requests
from bs4 import BeautifulSoup

# sort i  pg=i 로 변경해봄
URL = f"https://stackoverflow.com/jobs?q=python&pg="

# # 크롤링 뷰티플숲 사용:
# 1. get pages
# 2. make requests
# 3. extract jobs


## 클로링 할 페이지들 지정 function
def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find('div', {"class": "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)
    #print(last_page)
    return int(last_page)


## 클로링 할 부분들 (제목 등등)
def extract_job(html):
    title = html.find("div", {
        "class": "grid--cell fl1"
    }).find("h2", {
        "class": "mb4"
    }).find("a")["title"]
    company, location = html.find("div", {
        "class": "grid--cell fl1"
    }).find("h3", {
        "class": "fc-black-700"
    }).find_all(
        "span", recursive=False)
    company = company.get_text(strip=True)
    location = location.get_text(strip=True)
    job_id = html["data-jobid"]
    return {
        "title": title,
        "company": company,
        "location": location,
        "link": f"https://stackoverflow.com/jobs/{job_id}"
    }


## 해당 페이지에서 클롤링 할 내용 위치 찾아서 저장 하기.


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        # print(page +1 )
        print(f"scrapping Stackoverflow: page: {page}")
    result = requests.get(f"{URL}&pg={page + 1}")
    # print(result.status_code)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "-job"})
    for result in results:
        job = extract_job(result)
        jobs.append(job)
    return jobs


def get_so_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return []
