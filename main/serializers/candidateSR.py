# from rest_framework import serializers
# from main.models.candidates import Candidate

# class CandidateSerializer(serializers.ModelSerializer):
#     # SerializerMethodField bilan status_choices metodini aniqlash
#     status_choices = serializers.SerializerMethodField()
#     date_of_birth = serializers.DateField(format='%d.%m.%Y')
#     class Meta:
#         model = Candidate
#         fields = [
#             'id',
#             'name',  # Nomzod ismi
#             'date_of_birth',  # Tug'ilgan sanasi
#             'address',  # Nomzod Manzili
#             'experience',  # Tajriba yili
#             'experience_name',  # Qaysi sohalarda ishlagani
#             'skill',  # Ko'nikmalar
#             'expected_salary',  # Kutilayotgan oylik maosh miqdori (so‘m)
#             'phone_number',  # Nomzod telefon raqami
#             'tg_username',  # Nomzod telegram username
#             'description',  # Nomzod ozi haqida batafsil
#             'created_on',  # Yaratilgan sana
#             'status',
#             'status_choices',  # Nomzodning statusi
#         ]

#     def get_status_choices(self, obj):
#         # Barcha statuslar, ammo hozirgi statusni chiqarib tashlash
#         all_choices = dict(Candidate.STATUS_CHOICES)
#         all_choices.pop(obj.status, None)
#         return all_choices
    
#     # def get_date_of_birth(self, obj):
#     #     if obj.date_of_birth:
#     #         return obj.date_of_birth.strftime('%d.%m.%Y')
        