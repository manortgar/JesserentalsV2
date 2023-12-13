import os
import random
from faker import Faker
from django.utils.text import slugify

# Configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djecommerce.settings.development')
import django
django.setup()

# Importación de modelos después de configurar Django
from core.models import Item, CATEGORY_CHOICES, FABRICANTE_CHOICES, DISPONIBILITY_CHOICES, LABEL_CHOICES

fake = Faker()
"""
def get_random_image_path():
    # Ruta a la carpeta de imágenes en la raíz del proyecto
    image_folder_path_cat = os.path.join(os.getcwd(), 'images/cat')
    image_folder_path_john = os.path.join(os.getcwd(), 'images/john deere')
    image_folder_path_komatsu = os.path.join(os.getcwd(), 'images/komatsu')
    image_folder_path_sany = os.path.join(os.getcwd(), 'images/sany')
    image_folder_path_xcmg = os.path.join(os.getcwd(), 'images/xcmg')



    # Lista de archivos en la carpeta de imágenes
    image_files_komatsu = [f for f in os.listdir(image_folder_path_komatsu) if os.path.isfile(os.path.join(image_folder_path_komatsu, f))]
    image_files_cat = [f for f in os.listdir(image_folder_path_cat) if os.path.isfile(os.path.join(image_folder_path_cat, f))]
    image_files_sany = [f for f in os.listdir(image_folder_path_sany) if os.path.isfile(os.path.join(image_folder_path_sany, f))]
    image_files_xcmg = [f for f in os.listdir(image_folder_path_xcmg) if os.path.isfile(os.path.join(image_folder_path_xcmg, f))]
    image_files_john = [f for f in os.listdir(image_folder_path_john) if os.path.isfile(os.path.join(image_folder_path_john, f))]

    # Selecciona una imagen al azar de la lista
    random_image_komatsu = random.choice(image_files_komatsu)
    random_image_cat = random.choice(image_files_cat)
    random_image_sany = random.choice(image_files_sany)
    random_image_xcmg = random.choice(image_files_xcmg)
    random_image_john = random.choice(image_files_john)

    if variable == komatsu:
        return os.path.join("/", random_image_komatsu)
"""

def get_random_image_path(marca):
    # Mapeo de marcas a carpetas de imágenes
    brand_image_folders = {
        'cat': 'images/cat',
        'john deere': 'images/john deere',
        'komatsu': 'images/komatsu',
        'sany': 'images/sany',
        'xcmg': 'images/xcmg',
    }

    # Obtén la carpeta de imágenes correspondiente a la marca
    image_folder_path = os.path.join(os.getcwd(), brand_image_folders.get(marca.lower(), ''))

    # Verifica si la carpeta de imágenes existe
    if not os.path.exists(image_folder_path):
        raise ValueError(f"No se encontró la carpeta de imágenes para la marca: {marca}")

    # Lista de archivos en la carpeta de imágenes
    image_files = [f for f in os.listdir(image_folder_path) if os.path.isfile(os.path.join(image_folder_path, f))]

    # Verifica si hay imágenes en la carpeta
    if not image_files:
        raise ValueError(f"No hay imágenes en la carpeta de la marca: {marca}")

    # Selecciona una imagen al azar de la lista
    random_image = random.choice(image_files)

    # Devuelve la ruta completa de la imagen
    return os.path.join("/", random_image)

'''
def generate_random_item():
    title = fake.word()
    price = round(random.uniform(10, 1000), 2)
    fabricante = random.choice(FABRICANTE_CHOICES)[0]
    category = random.choice(CATEGORY_CHOICES)[0]
    label = random.choice(LABEL_CHOICES)[0]
    slug = slugify(title)
    description = fake.text()
    image = get_random_image_path()
    disponibility = random.choice(DISPONIBILITY_CHOICES)[0]
    selected = random.choice([True, False])

    item = Item.objects.create(
        title=title,
        price=price,
        fabricante=fabricante,
        category=category,
        label=label,
        slug=slug,
        description=description,
        image=image,
        disponibility=disponibility,
        selected=selected
    )

    print(f"Item creado: {item}")

if __name__ == "__main__":
    # Define el número de elementos aleatorios que deseas crear
    num_items_to_create = 10

    # Crea los elementos aleatorios
    for _ in range(num_items_to_create):
        generate_random_item(komatsu)
'''

def generate_random_item(marca):

    

    title = f"{fake.word()} {marca}"  # Ajusta el título para incluir la m
    price = round(random.uniform(10, 1000), 2)
    if marca == FABRICANTE_CHOICES[0]:
        fabricante = FABRICANTE_CHOICES[3]
    category = random.choice(CATEGORY_CHOICES)
    label = random.choice(LABEL_CHOICES)
    slug = slugify(title)
    description = fake.text()
    image = get_random_image_path(marca)
    disponibility = random.choice(DISPONIBILITY_CHOICES)
    selected = random.choice([True, False])


    item = Item.objects.create(
        title=title,
        price=price,
        fabricante=fabricante,
        category=category,
        label=label,
        slug=slug,
        description=description,
        image=image,
        disponibility=disponibility,
        selected=selected
    )

    print(f"Item creado: {item}")

    # Resto del código para crear el objeto Item en la base de datos

if __name__ == "__main__":
    # Define el número de elementos aleatorios que deseas crear para cada marca
    num_items_to_create_per_brand = 5

    # Crea los elementos aleatorios para cada marca
    for marca in FABRICANTE_CHOICES:
        for _ in range(num_items_to_create_per_brand):
            generate_random_item('CAT')
            generate_random_item('KMT')
            generate_random_item('X')
            generate_random_item('JD')
            generate_random_item('S')