from rest_framework.response import Response

def custom_response(data, success=True, message="Success"):
    """
    Umumiy javob qaytarish funksiyasi.

    Bu funksiya har doim 'success' va 'message' qiymatlari bilan birga 
    faqat 'data'ni qabul qiladi va Response qaytaradi.
    
    :param data: Javobda ko'rsatilishi kerak bo'lgan ma'lumot.
    :param success: Javobning muvaffaqiyatliligini bildiruvchi qiymat (default: True).
    :param message: Javobdagi xabar (default: "Success").
    
    :return: `Response` obyekti.
    """
    return Response({
        'success': success,
        'message': message,
        'data': data
    })




import requests

# def send_message():
#     # URL va parametrlarga kerakli qiymatlarni o'rnatish
#     url = 'http://localhost:8000/api/api28/send_message/en/'
#     params = {
#         'name': 'John Doe',
#         'phone': '1234567890'
#     }

#     # POST so'rovini yuborish
#     response = requests.post(url, params=params)

#     # Javobni chop etish
#     print(response.json())  # Yuborilgan so'rovning javobini chop etamiz

# # Funksiyani chaqirish
# send_message()
