from homework_app.models import Category, Product

def create_categories():
    Category.objects.create(category_name="ubrania", slug="CLOTHES")
    Category.objects.create(category_name="odżywki", slug="SUPLE")
    Category.objects.create(category_name="żywność", slug="FOOD")
    Category.objects.create(category_name="wakację", slug="HOOLIDAY")
    Category.objects.create(category_name="nauka", slug="LEARNING")
    Category.objects.create(category_name="alcohol", slug="ALC")
    Category.objects.create(category_name="transport", slug="TRA")
    Category.objects.create(category_name="technologia", slug="IT")
    Category.objects.create(category_name="dodatki", slug="ACC")

def create_products():
    Product.objects.create(name="koszulka", description="ubranie - koszulka", price="10", vat="0.22", stock="100")
    Product.objects.create(name="spodnie", description="spodnie DIESEL", price="99", vat="0.22", stock="78")
    Product.objects.create(name="krawat", description="krawat w kratkę", price="29", vat="0.21", stock="11")
    Product.objects.create(name="czapka", description="zimowa czapka", price="9.99", vat="0.30", stock="45")
    Product.objects.create(name="rękawiczki", description="rękawiczki letnie", price="19", vat="0.43", stock="44")
    Product.objects.create(name="coca-cola", description="napój coca-cola 1L", price="12.99", vat="0.20", stock="1000")
    Product.objects.create(name="fanta", description="napój fanta 0.5L", price="4.99", vat="0.11", stock="22")
    Product.objects.create(name="piwo", description="harnas 0.5L", price="3.34", vat="0.40", stock="100")
    Product.objects.create(name="python", description="kurs Python", price="11999.99", vat="0.23", stock="100")
    Product.objects.create(name="java", description="kurs Java", price="12999.99", vat="0.23", stock="100")
    Product.objects.create(name="c++", description="kurs c++", price="10999.99", vat="0.23", stock="100")