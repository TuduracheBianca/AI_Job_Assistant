import json
from src.ai_agent import generate_cover_letter
from src.web_agent import simulate_job_application
with open("data/my_profile.json","r") as file:
    profile = json.load(file)
    profile_format=json.dumps(profile, indent=4)
    # print(profile_format)

with open("data/job_description.txt","r") as file:
    job_description = file.read()

cover_letter=generate_cover_letter(profile_format,job_description)
print(cover_letter)
simulate_job_application("Bianca", "email@test", cover_letter)
