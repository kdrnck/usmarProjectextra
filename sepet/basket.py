from store.models import Product
from decimal import Decimal


class Sepet():

    def __init__(self, request):
        self.session = request.session
        print (self.session.get.__dict__)
        sepet = self.session.get('skey')
        if 'skey' not in request.session:
            sepet = self.session['skey'] = {}
        self.sepet = sepet

    def add(self, product, qt):
        product_id = str(product.id)

        if product_id not in self.sepet:
            self.sepet[product_id] = {'price': str(product.price), 'qt':int(qt)}
            self.session.modified = True

    def __iter__(self):
        product_ids = self.sepet.keys()
        products = Product.products.filter(id__in=product_ids)
        sepet = self.sepet.copy()

        for product in products:
            sepet[str(product.id)]['product'] = product

        for item in sepet.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qt']
            yield item
    
    def __len__(self):
        return sum(item['qt'] for item in self.sepet.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qt'] for item in self.sepet.values())

    def clear(self, product):
        print('\033[92m In delete \033[00m')
        product_id = str(product)
        print(f'\033[94m Deleted Product"s id is {product_id}\033[00m')
        for p in product:
            p = str(p)
            if p in self.sepet:
                del self.sepet[p]
                self.session.modified=True

    def delete(self, product):
        """
        Delete item from session data
        """
        product_id = str(product)


        if product_id in self.sepet:
            del self.sepet[product_id]
            print(product_id)
            self.session.modified=True

    def update(self, product, qt):
        
        product_id = str(product)
        qt = qt
        
        if product_id in self.sepet:
            self.sepet[product_id]['qt'] = qt

        self.session.modified=True
