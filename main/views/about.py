from main.models.candidates import Candidate
from main.serializers.candidateSR import CandidateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.db.models import Q



class FunctionalView(APIView):
    
    @staticmethod
    def send_response(data, status, message,count=int):
        
        response_data = {
            'message': message,
            'status': status,
            'data': data
        }
        if count is not None:
            response_data['count_candidates'] = count
        
        return Response(response_data)



class CandidateView(APIView):

    def get(self, request):
        # Parametrlarni olish
        ordering = request.GET.get('ordering', None)
        status_filter = request.GET.get('status', None)

        # Kandidates listini olish
        candidates = self.get_filtered_candidates(ordering, status_filter)

        # Serializerga o'zgartirish
        serializer = CandidateSerializer(candidates, many=True)
        response_data = self.format_response(serializer.data, candidates.count())

        return Response(response_data, status=status.HTTP_200_OK)

    def get_filtered_candidates(self, ordering=None, status_filter=None):
        candidates = Candidate.objects.all()

        if status_filter:
            candidates = candidates.filter(status=status_filter)

        if ordering:
            candidates = candidates.order_by(ordering)

        return candidates

    def format_response(self, candidate_data, count=None):
        data = {'candidates': candidate_data}
        if count:
            data['count_candidates'] = count

        return {
            'message': 'success',
            'status': 'true',
            'data': data
        }

    def post(self, request):
        serializer = CandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Candidate created successfully',
                'status': 'true',
                'data': serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            response_data = {
                'message': 'Invalid data',
                'status': 'false',
                'data': serializer.errors
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

class CandidateUpdate(APIView):
    
    def get(self, request, id):
        if id:
            try:
                candidate = Candidate.objects.get(id=id)
                serializer = CandidateSerializer(candidate)
                data = {'candidates': [serializer.data]}
            except Candidate.DoesNotExist:
                raise NotFound("Candidate with this ID does not exist.")
            response_data = {
            'message': 'success',
            'status': 'true',
            'data': data
        }
        return Response(response_data)
            

    def put(self, request, id):
        # Nomzodni yangilash
        try:
            candidate = Candidate.objects.get(id=id)
            serializer = CandidateSerializer(candidate, data=request.data)
            if serializer.is_valid():
                serializer.save()
                response_data = {
                    'message': 'Candidate updated successfully',
                    'status': 'true',
                    'data': serializer.data
                }
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                response_data = {
                    'message': 'Invalid data',
                    'status': 'false',
                    'data': serializer.errors
                }
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        except Candidate.DoesNotExist:
            raise NotFound("Candidate with this ID does not exist.")
    def patch(self, request, id):
        try:
            candidate = Candidate.objects.get(id=id)
            # Faqat kiritilgan fieldni yangilash
            serializer = CandidateSerializer(candidate, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                response_data = {
                    'message': 'Candidate updated successfully',
                    'status': 'true',
                    'data': serializer.data
                }
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                response_data = {
                    'message': 'Invalid data',
                    'status': 'false',
                    'data': serializer.errors
                }
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        except Candidate.DoesNotExist:
            raise NotFound("Candidate with this ID does not exist.")

    def delete(self, request, id):
        # Nomzodni o'chirish
        try:
            candidate = Candidate.objects.get(id=id)
            candidate.delete()
            response_data = {
                'message': 'Candidate deleted successfully',
                'status': 'true'
            }
            return Response(response_data, status=status.HTTP_204_NO_CONTENT)
        except Candidate.DoesNotExist:
            raise NotFound("Candidate with this ID does not exist.")
        

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Foydalanuvchini autentifikatsiya qilish
        user = authenticate(request, username=username, password=password)
        if user:
            # Token yaratish yoki olish
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'message': 'Token created successfully' if created else 'Token already exists',
                'status': True,
                'token': f"Token {token.key}",
                'username': username,
            }, status=status.HTTP_200_OK)

        return Response({
            'message': 'Invalid credentials',
            'status': False,
        }, status=status.HTTP_401_UNAUTHORIZED)
        





class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Tokenni o'chirish
        request.user.auth_token.delete()
        return Response({
            "message": "Successfully logged out",
            "status": True
        }, status=status.HTTP_200_OK)
        

class SearchView(APIView):
    def transliterate(self, text, direction="to_cyrillic"):
        """
        Kirill va lotin o'rtasida harflarni transliteratsiya qiladi.
        direction:
            - "to_cyrillic" - lotindan kirillga
            - "to_latin" - kirilldan lotinga
        """
        cyrillic_to_latin = {
            'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D',
            'Е': 'E', 'Ё': 'Yo', 'Ж': 'Zh', 'З': 'Z', 'И': 'I',
            'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
            'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
            'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'Ts', 'Ч': 'Ch',
            'Ш': 'Sh', 'Щ': 'Sch', 'Ы': 'Y', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya',
            'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
            'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
            'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch',
            'ш': 'sh', 'щ': 'sch', 'ы': 'y', 'э': 'e', 'ю': 'yu', 'я': 'ya',
        }
        latin_to_cyrillic = {v: k for k, v in cyrillic_to_latin.items()}

        mapping = cyrillic_to_latin if direction == "to_latin" else latin_to_cyrillic

        # Har bir harfni transliteratsiya qilish
        return ''.join([mapping.get(char, char) for char in text])

    def get(self, request):
        # O'quvchidan so'rovni olish
        query = request.GET.get('search')

        # Kirillga va lotinga transliteratsiya qilish
        cyrillic_query = self.transliterate(query, "to_cyrillic")
        latin_query = self.transliterate(query, "to_latin")

        # Nomzodlarni so'rov bo'yicha qidirish
        candidates = Candidate.objects.filter(
            Q(name__icontains=cyrillic_query) | 
            Q(name__icontains=latin_query) | 
            Q(phone_number__icontains=query)
        )

        # Natijani serializatsiya qilish
        serializer = CandidateSerializer(candidates, many=True)

        # Javobni yuborish
        return FunctionalView.send_response(
            serializer.data, status='true', message="Successfully", count=candidates.count()
        )