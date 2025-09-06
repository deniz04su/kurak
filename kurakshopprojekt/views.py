from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import Product, Category, ProductMedia
from .forms import ProductMediaForm, SignUpForm, ProfileForm, CustomUserCreationForm
from django.core.files.base import ContentFile
import base64
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Product, ProductReaction, ProductComment
from django.views.decorators.csrf import csrf_exempt
import json

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


@csrf_exempt
def react_product(request, product_id):
    if request.method == "POST":
        data = json.loads(request.body)
        reaction_type = data.get("reaction")  # "like" же "dislike"
        user = request.user
        product = get_object_or_404(Product, id=product_id)

        reaction, created = ProductReaction.objects.update_or_create(
            user=user,
            product=product,
            defaults={"reaction": reaction_type}
        )

        return JsonResponse({"status": "ok", "reaction": reaction_type})

@csrf_exempt
def comment_product(request, product_id):
    if request.method == "POST":
        data = json.loads(request.body)
        content = data.get("content")
        user = request.user
        product = get_object_or_404(Product, id=product_id)

        comment = ProductComment.objects.create(
            user=user,
            product=product,
            content=content
        )

        return JsonResponse({"status": "ok", "comment": comment.content})








@csrf_exempt
def dosum_chat(request):
    if request.method == "POST":
        data = json.loads(request.body)
        msg = data.get("message", "").lower()

        # Жөнөкөй эрежелер
        if "кийим" in msg:
            answer = "Бул кийим сага абдан жарашат 👕✨"
        elif "бут кийим" in msg:
            answer = "Бул бут кийим сага бир аз чоң көрүнөт, бирок стилдүү."
        else:
            answer = "Мен сага жардам берүүгө даярмын, досум 🙂"

        return JsonResponse({"answer": answer})

    return JsonResponse({"error": "POST гана кабыл алынат"}, status=400)


def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # же башка башкы баракчаң
    else:
        form = SignUpForm()
    return render(request, 'kurakshopprojekt/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')  # же башка башкы баракчаң



def index(request):
    return render(request, 'kurakshopprojekt/index.html')


def home(request):
    return render(request, 'home.html')


# Главная страница
def main_page(request):
    categories = Category.objects.all()
    featured_products = Product.objects.filter(available=True)[:8]  # топ 8 продукта
    return render(request, 'kurakshopprojekt/main_page.html', {
        'categories': categories,
        'featured_products': featured_products
    })

# Список продуктов
def product_list(request):
    products = Product.objects.all()

    price_filter = request.GET.get('price')
    if price_filter == 'low':
        products = products.order_by('price')
    elif price_filter == 'high':
        products = products.order_by('-price')

    available_filter = request.GET.get('available')
    if available_filter == 'yes':
        products = products.filter(available=True)
    elif available_filter == 'no':
        products = products.filter(available=False)

    rating_sort = request.GET.get('rating')
    if rating_sort == 'high':
        products = products.order_by('-rating')
    elif rating_sort == 'low':
        products = products.order_by('rating')

    return render(request, 'kurakshopprojekt/product_list.html', {'products': products})

# Поиск
def search_view(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(name__icontains=query)
    return render(request, 'kurakshopprojekt/search.html', {'query': query, 'products': products})

# Профиль пользователя
@login_required
def profile_view(request):
    return render(request, 'kurakshopprojekt/profile.html', {'user': request.user})

# Кадр с камерой
def camera_view(request):
    if request.method == 'POST':
        image_data = request.POST.get('image_data')
        if image_data:
            format, imgstr = image_data.split(';base64,')
            data = ContentFile(base64.b64decode(imgstr), name='photo.png')
            print("Сүрөт серверге келди!")
    return render(request, 'kurakshopprojekt/camera.html')

# Загрузка медиа для продукта
def upload_media(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        files = request.FILES.getlist('file')
        for f in files:
            ProductMedia.objects.create(
                product=product,
                file=f,
                is_video=f.content_type.startswith('video')
            )
        return redirect('product_list')
    form = ProductMediaForm()
    return render(request, 'kurakshopprojekt/upload_media.html', {'form': form, 'product': product})

# Регистрация с формами
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect("login")
    else:
        form = SignUpForm()
        profile_form = ProfileForm()
    return render(request, "kurakshopprojekt/signup.html", {"form": form, "profile_form": profile_form})

# Вход
def login_view(request):
    if request.method == 'POST':
        username
