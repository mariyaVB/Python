from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Animal, Feedback


def index(request):
    return render(request, 'index.html')


def feedback(request):
    if request.method == 'POST':
        text_feedback = request.POST.get('feedback')
        Feedback.objects.create(text=text_feedback)
        return HttpResponse(f'''<h2>Ваш отзыв отправлен.</h2>
                            <a href = ""><button>Вернуться назад</button></a>''')

    elif request.method == 'GET':
        result = Feedback.objects.all()
        data = {
            'feedback': result
        }
        return render(request, 'feedback.html', data)


def edit_feedback(request, feedback_id):
    feedback_data = Feedback.objects.get(id=feedback_id)
    data = {'id': feedback_id,
            'text': feedback_data.text,
            'data_created': feedback_data.data_created}
    return HttpResponse('<h1>Edit</h1>')


def delete_feedback(request, feedback_id):
    pass
    # try:
    #     Feedback.objects.get(id=feedback_id).delete()
    #     return HttpResponseRedirect("/")
    # except Person.DoesNotExist:
    #     return HttpResponseNotFound("<h2>Person not found</h2>")


class Animals:
    def __init__(self):
        self.name_cat = 'Кот в сапогах'
        self.name_dog = 'Балто'

    def __repr__(self):
        return f'Котика зовут {self.name_cat}. Песеля зовут {self.name_dog}.'


def info_pets(request, slug_pets):
    data = {'pet_name': slug_pets,
            'pet_str': 'Текст про животных',
            'pet_list': ['Котики', 'Собаки', 'Хомячки'],
            'pet_int': 1234567890,
            'pet_dict': {'cat': 'Котики', 'dog': 'Собаки'},
            'pet_obj': Animals()
            }
    if slug_pets in ['cats', 'dogs']:
        return render(request, 'pet_page.html', context=data)
    return render(request, 'page_404.html', status=404)


def petGET(request):
    user_data = request.GET.get('search_field')
    user_data3 = request.GET.get('smthfield')

    return HttpResponse(f"<h2>{user_data}</h2><div>{user_data3}</div>")


def categories(request, category_id):
    return HttpResponse(f"<h2>Категории</h2> id: {category_id}")

