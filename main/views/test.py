import random
from faker import Faker
import requests

# Faker kutubxonasini yaratamiz
fake = Faker()

# Tasodifiy malumotlar yaratish funksiyasi
def generate_random_candidate():
    return {
        "name": fake.name(),
        "date_of_birth": fake.date_of_birth(minimum_age=20, maximum_age=50).strftime('%Y-%m-%d'),
        "address": fake.address(),
        "experience": random.randint(1, 10),  # 1-10 yil tajriba
        "experience_name": random.choice(["Dasturlash", "Tahlil", "Dizayn", "Marketing"]),
        "skill": random.choice(["Python", "JavaScript", "Django", "React", "SQL", "PHP"]),
        "expected_salary": f"{random.randint(4, 15)} million",  # 4-15 million
        "phone_number": fake.phone_number(),
        "tg_username": f"@{fake.user_name()}",
        "description": fake.text(),
        "status": random.choice([
            "yangi", "intervyu_rejalashtirilgan", "intervyu_qilingan", 
            "taklif_berilgan", "qabul_qilingan", "rad_etilgan", "kutish"
        ]),
    }


# POST so'rovini yuborish funksiyasi
def post_random_candidate():
    url = "http://127.0.0.1:8000/api/api28/candidateview/"  # O'zingizning API URL manzilingizni kiriting
    headers = {'Content-Type': 'application/json'}
    
    # Tasodifiy candidate ma'lumotlarini yaratamiz
    candidate_data = generate_random_candidate()

    # POST so'rovini yuborish
    response = requests.post(url, json=candidate_data, headers=headers)

    # Javobni tekshirish
    if response.status_code == 201:
        print("Candidate successfully created!")
    else:
        print(f"Failed to create candidate: {response.status_code}, {response.text}")

for i in range(3):
    post_random_candidate()
