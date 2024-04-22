import requests

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

if __name__ == '__main__':
    # Adding products
    url_insert_product = 'http://127.0.0.1:8005/products/insert_product'
    url_insert_client = 'http://127.0.0.1:8005/clients/insert_client'
    url_insert_supplier_client = 'http://127.0.0.1:8005/sc/insert_supplier_client'
    url_insert_location = 'http://127.0.0.1:8005/location/insert_location'
    url_insert_product_client = 'http://127.0.0.1:8005/pc/insert_product_client'
    url_insert_product_supplier = 'http://127.0.0.1:8005/ps/insert_product_supplier'
    url_insert_product_location = 'http://127.0.0.1:8005/pl/update_product_location'

    data_product1 = {
        'sku': 33221265511,
        'description': 'Nike shoes',
        'sale_price': 99.99,
        'purchase_price': 44.99,
    }

    data_product2 = {
        'sku': 1122233322,
        'description': 'Adidas shoes',
        'sale_price': 99.99,
        'purchase_price': 44.99,
    }

    data_client = {
        'type': 'Client',
        'name': 'ba2ddb34uss',
        'email': 'b2add34bsis@asd.com',
        'phone_number': 2321312312312,
    }

    data_supplier = {
        'type': 'Supplier',
        'name': 'odydd234sssse',
        'email': ' sdd2ss@ex34amplt.com',
        'phone_number': 222322232,
    }

    data_location = {
        'abbreviation': '3sd2',
        'name': '22',
        'address': '33',
    }

    product_1 = requests.post(url_insert_product, json=data_product1, headers=headers).json()
    product_2 = requests.post(url_insert_product, json=data_product2, headers=headers).json()
    client = requests.post(url_insert_supplier_client, json=data_client, headers=headers).json()
    supplier = requests.post(url_insert_supplier_client, json=data_supplier, headers=headers).json()
    location = requests.post(url_insert_location, json=data_location, headers=headers).json()

    print(product_1, product_2, client, supplier, location)

    data_product_supplier = {
        'supplier_id': supplier['mvSupplierClient']['SupplierClientID'],
        'product_id': product_1['mvProduct']['ProductID']
    }

    data_product_client = {
        'client_id': client['mvSupplierClient']['SupplierClientID'],
        'product_id': product_2['mvProduct']['ProductID']
    }

    product_client = requests.post(url_insert_product_client, json=data_product_client, headers=headers).json()
    product_supplier = requests.post(url_insert_product_supplier, json=data_product_supplier, headers=headers).json()

    print(product_client, product_supplier)

    data_product_location = {
        'product_sku': product_1['mvProduct']['ProductSKU'],
        'product_quantity': 5,
        'location_id': location['mvInventoryLocation']['InventoryLocationID']
    }

    product_location = requests.post(url_insert_product_location, json=data_product_location, headers=headers).json()

    print(product_location)
