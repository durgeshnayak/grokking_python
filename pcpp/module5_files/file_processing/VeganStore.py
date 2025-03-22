import xml.etree.ElementTree as ET


class VeganStore:
    def __init__(self, filename):
        self.filename = filename

    def generate_products(self):
        shop = ET.Element('shop')
        category = ET.SubElement(shop, 'category', {'name': 'Vegan Products'})
        product_1 = ET.SubElement(category, 'product', {'name': 'Good Morning Sunshine'})
        type_1 = ET.SubElement(product_1, 'type')
        type_1.text = 'cereals'
        producer_1 = ET.SubElement(product_1, 'producer')
        producer_1.text = 'OpenEDG Testing Service'
        price_1 = ET.SubElement(product_1, 'price')
        price_1.text = '9.90'
        currency_1 = ET.SubElement(product_1, 'currency')
        currency_1.text = 'USD'

        product_2 = ET.SubElement(category, 'product', {'name': 'Spaghetti Veganietto'})
        type_2 = ET.SubElement(product_2, 'type')
        type_2.text = 'pasta'
        producer_2 = ET.SubElement(product_2, 'producer')
        producer_2.text = 'Programmers Eat Pasta'
        price_2 = ET.SubElement(product_2, 'price')
        price_2.text = '15.49'
        currency_2 = ET.SubElement(product_2, 'currency')
        currency_2.text = 'EUR'

        product_3 = ET.SubElement(category, 'product', {'name': 'Fantastic Almond Milk'})
        type_2 = ET.SubElement(product_3, 'type')
        type_2.text = 'beverages'
        producer_3 = ET.SubElement(product_3, 'producer')
        producer_3.text = 'Drinks4Coders Inc.'
        price_3 = ET.SubElement(product_3, 'price')
        price_3.text = '19.75'
        currency_3 = ET.SubElement(product_3, 'currency')
        currency_3.text = 'USD'


        tree = ET.ElementTree(shop)
        tree.write(self.filename,'utf-8', True)


vegan_store = VeganStore('vegan_store.xml')
vegan_store.generate_products()
