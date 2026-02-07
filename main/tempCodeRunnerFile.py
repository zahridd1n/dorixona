from rest_framework.response import Response

# def custom_response(data, success=True, message="Success"):
#     """
#     Umumiy javob qaytarish funksiyasi.

#     Bu funksiya har doim 'success' va 'message' qiymatlari bilan birga 
#     faqat 'data'ni qabul qiladi va Response qaytaradi.
    
#     :param data: Javobda ko'rsatilishi kerak bo'lgan ma'lumot.
#     :param success: Javobning muvaffaqiyatliligini bildiruvchi qiymat (default: True).
#     :param message: Javobdagi xabar (default: "Success").
    
#     :return: `Response` obyekti.
#     """
#     return Response({
#         'success': success,
#         'message': message,
#         'data': data
#     })