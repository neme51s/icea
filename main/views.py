from django.shortcuts import render
from django.http import FileResponse, Http404
import os

def get_language(request):
    """Определяем язык из параметра или куки"""
    lang = request.GET.get('lang', request.COOKIES.get('icea_lang', 'ru'))
    return lang if lang in ['ru', 'en'] else 'ru'

def render_with_lang(request, template_name, context=None):
    """Вспомогательная функция для рендеринга с языком"""
    lang = get_language(request)
    
    # Создаем полный путь к шаблону
    template_path = f'{lang}/{template_name}'
    
    # Подготавливаем контекст
    if context is None:
        context = {}
    context['lang'] = lang
    
    # Рендерим ответ
    response = render(request, template_path, context)
    
    # Устанавливаем куку с языком
    response.set_cookie('icea_lang', lang, max_age=365*24*60*60)  # 1 год
    
    return response

def home(request):
    return render_with_lang(request, 'home.html')

def about_company(request):
    return render_with_lang(request, 'about_company.html')

def about_clients(request):
    return render_with_lang(request, 'about_clients.html')

def about_partners(request):
    return render_with_lang(request, 'about_partners.html')

def services_valuation(request):
    return render_with_lang(request, 'services_valuation.html')

def services_consulting(request):
    return render_with_lang(request, 'services_consulting.html')

def services_trainings(request):
    return render_with_lang(request, 'services_trainings.html')

def services_legal(request):
    return render_with_lang(request, 'services_legal.html')

def contacts(request):
    return render_with_lang(request, 'contacts.html')

def download_profile(request):
    """Скачивание профиля компании"""
    lang = get_language(request)
    # Здесь будет логика для скачивания файла
    # Пока просто редирект на страницу компании
    return render_with_lang(request, 'about_company.html')

def download_company_profile(request):
    """Скачивание профиля компании"""
    lang = get_language(request)
    
    # Путь к файлу
    file_path = os.path.join('static', 'files', 'company_profile.pptx')
    
    # Проверяем существование файла
    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Type'] = 'application/vnd.openxmlformats-officedocument.presentationml.presentation'
        response['Content-Disposition'] = f'attachment; filename="ICEA_Company_Profile_{lang.upper()}.pptx"'
        return response
    else:
        # Если файла нет, показываем сообщение
        if lang == 'ru':
            message = "Файл временно недоступен. Пожалуйста, свяжитесь с нами для получения профиля компании."
        else:
            message = "File is temporarily unavailable. Please contact us to get the company profile."
        
        return render_with_lang(request, 'about_company.html', {'download_error': message})