import requests
from bs4 import BeautifulSoup
from indeed import get_jobs as get_indeed_jobs
from stackoverflow import get_so_jobs 
from jobsave import save_to_file



#print(indeed_jobs)

stackoverflow_jobs = get_so_jobs()
indeed_jobs = get_indeed_jobs()
jobs= stackoverflow_jobs + indeed_jobs
#jobs = indeed_jobs
#jobs = stackoverflow_jobs
#print(jobs)
save_to_file(jobs)

# CSV comma seperated ValueError


