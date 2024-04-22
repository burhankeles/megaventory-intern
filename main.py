from fastapi import FastAPI, Response
import requests

from src import Product, SupplierClient, InventoryLocation, ProductSupplier, ProductClient, ProductLocation

app = FastAPI()

# URLs of the API endpoint
url_products = "https://api.megaventory.com/v2017a/Product/ProductUpdate"
url_supplier_clients = "https://api.megaventory.com/v2017a/SupplierClient/SupplierClientUpdate"
url_locations = "https://api.megaventory.com/v2017a/InventoryLocation/InventoryLocationUpdate"
url_product_supplier = "https://api.megaventory.com/v2017a/ProductSupplier/ProductSupplierUpdate"
url_product_client = "https://api.megaventory.com/v2017a/ProductClient/ProductClientUpdate"
url_product_location = "https://api.megaventory.com/v2017a/InventoryLocationStock/ProductStockUpdate"

api_key = "4df17c02ab9d966c@m148588"


@app.post("/products/insert_product")
async def insert_product(product: Product):
    # JSON data to be sent in the request
    create_product_json = {
        "APIKEY": api_key,
        "mvProduct": {
            "ProductType": "TimeRestrictedService",
            "ProductSKU": product.sku,
            "ProductDescription": product.description,
            "ProductSellingPrice": product.sale_price,
            "ProductPurchasePrice": product.purchase_price,
        },
        "mvRecordAction": "Insert",
        "mvInsertUpdateDeleteSourceApplication": "WooCommerce"
    }

    # Sending POST request with JSON data
    response = requests.post(url_products, json=create_product_json)

    # Checking the response status
    if response.status_code == 200:
        return response.json()
    else:
        resp = Response(status_code=500)
        return resp


@app.post("/products/update_product")
async def update_product(product: Product):
    # JSON data to be sent in the request
    update_product_json = {
        "APIKEY": api_key,
        "mvProduct": {
            "ProductID": product.product_id,
            "ProductType": "TimeRestrictedService",
            "ProductSKU": product.sku,
            "ProductDescription": product.description,
            "ProductSellingPrice": product.sale_price,
            "ProductPurchasePrice": product.purchase_price,
        },
        "mvRecordAction": "Update",
        "mvInsertUpdateDeleteSourceApplication": "WooCommerce"
    }

    # Sending POST request with JSON data
    response = requests.post(url_products, json=update_product_json)

    # Checking the response status
    if response.status_code == 200:
        return response.json()
    else:
        resp = Response(status_code=500)
        return resp


@app.post("/sc/insert_supplier_client")
async def insert_supplier_client(supplier_client: SupplierClient):
    insert_supplier_client_json = {
        "APIKEY": api_key,
        "mvSupplierClient": {
            "SupplierClientType": supplier_client.type,
            "SupplierClientName": supplier_client.name,
            "SupplierClientEmail": supplier_client.email,
            "SupplierClientShippingAddress": supplier_client.shipping_address,
            "SupplierClientPhone": supplier_client.phone_number,
        },
        "mvGrantPermissionsToAllUser": "true",
        "mvRecordAction": "Insert",
        "mvInsertUpdateDeleteSourceApplication": "Magento"
    }

    # Sending POST request with JSON data
    response = requests.post(url_supplier_clients, json=insert_supplier_client_json)

    # Checking the response status
    if response.status_code == 200:
        return response.json()
    else:
        resp = Response(status_code=500)
        return resp


@app.post("/sc/update_supplier_client")
async def update_supplier_client(supplier_client: SupplierClient):
    update_supplier_client_json = {
        "APIKEY": api_key,
        "mvSupplierClient": {
            "SupplierClientID": supplier_client.supplier_client_id,
            "SupplierClientType": supplier_client.type,
            "SupplierClientName": supplier_client.name,
            "SupplierClientEmail": supplier_client.email,
            "SupplierClientShippingAddress": supplier_client.shipping_address,
            "SupplierClientPhone": supplier_client.phone_number,
        },
        "mvGrantPermissionsToAllUser": "true",
        "mvRecordAction": "Update",
        "mvInsertUpdateDeleteSourceApplication": "Magento"
    }

    # Sending POST request with JSON data
    response = requests.post(url_supplier_clients, json=update_supplier_client_json)

    # Checking the response status
    if response.status_code == 200:
        return response.json()
    else:
        resp = Response(status_code=500)
        return resp


@app.post("/location/insert_location")
async def insert_location(location: InventoryLocation):
    insert_location_json = {
        "APIKEY": api_key,
        "mvInventoryLocation": {
            "InventoryLocationName": location.name,
            "InventoryLocationAbbreviation": location.abbreviation,
            "InventoryLocationAddress": location.address,
        },
        "mvRecordAction": "Insert",
        "mvInsertUpdateDeleteSourceApplication": "WooCommerce"
    }

    # Sending POST request with JSON data
    response = requests.post(url_locations, json=insert_location_json)

    # Checking the response status
    if response.status_code == 200:
        return response.json()
    else:
        resp = Response(status_code=500)
        return resp


@app.post("/location/update_location")
async def update_location(location: InventoryLocation):
    update_location_json = {
        "APIKEY": api_key,
        "mvInventoryLocation": {
            "InventoryLocationID": location.location_id,
            "InventoryLocationName": location.name,
            "InventoryLocationAbbreviation": location.abbreviation,
            "InventoryLocationAddress": location.address,
        },
        "mvRecordAction": "Update",
        "mvInsertUpdateDeleteSourceApplication": "WooCommerce"
    }

    # Sending POST request with JSON data
    response = requests.post(url_locations, json=update_location_json)

    # Checking the response status
    if response.status_code == 200:
        return response.json()
    else:
        resp = Response(status_code=500)
        return resp


@app.post("/ps/insert_product_supplier")
async def insert_product_supplier(product_supplier: ProductSupplier):
    insert_product_supplier_json = {
        "APIKEY": api_key,
        "mvProductSupplierUpdate": {
            "ProductID": product_supplier.product_id,
            "ProductSupplierID": product_supplier.supplier_id,
        },
        "mvRecordAction": "Insert"
    }

    # Sending POST request with JSON data
    response = requests.post(url_product_supplier, json=insert_product_supplier_json)

    # Checking the response status
    if response.status_code == 200:
        return response.json()
    else:
        resp = Response(status_code=500)
        return resp


@app.post("/ps/update_product_supplier")
async def update_product_supplier(product_supplier: ProductSupplier):
    update_product_supplier_json = {
        "APIKEY": api_key,
        "mvProductSupplierUpdate": {
            "ProductID": product_supplier.product_id,
            "ProductSupplierID": product_supplier.supplier_id,
            # Can be added a new attribute to update.
        },
        "mvRecordAction": "Update"
    }

    # Sending POST request with JSON data
    response = requests.post(url_product_supplier, json=update_product_supplier_json)

    # Checking the response status
    if response.status_code == 200:
        return response.json()
    else:
        resp = Response(status_code=500)
        return resp


@app.post("/pc/insert_product_client")
async def insert_product_client(product_client: ProductClient):
    insert_product_client_json = {
        "APIKEY": api_key,
        "mvProductClientUpdate": {
            "ProductID": product_client.product_id,
            "ProductClientID": product_client.client_id,
        },
        "mvRecordAction": "Insert"
    }

    # Sending POST request with JSON data
    response = requests.post(url_product_client, json=insert_product_client_json)

    # Checking the response status
    if response.status_code == 200:
        return response.json()
    else:
        resp = Response(status_code=500)
        return resp


@app.post("/pc/update_product_client")
async def update_product_client(product_client: ProductClient):
    update_product_client_json = {
        "APIKEY": api_key,
        "mvProductClientUpdate": {
            "ProductID": product_client.product_id,
            "ProductClientID": product_client.client_id,
            # Can be added a new attribute to update.
        },
        "mvRecordAction": "Update"
    }

    # Sending POST request with JSON data
    response = requests.post(url_product_client, json=update_product_client_json)

    # Checking the response status
    if response.status_code == 200:
        return response.json()
    else:
        resp = Response(status_code=500)
        return resp


@app.post("/pl/update_product_location")
async def update_product_location(product_location: ProductLocation):
    update_product_location_json = {
        "APIKEY": api_key,
        "mvProductStockUpdateList": [
            {
                "ProductSKU": product_location.product_sku,
                "ProductQuantity": product_location.product_quantity,
                "InventoryLocationID": product_location.location_id,
            }
        ]
    }

    # Sending POST request with JSON data
    response = requests.post(url_product_location, json=update_product_location_json)

    # Checking the response status
    if response.status_code == 200:
        return response.json()
    else:
        resp = Response(status_code=500)
        return resp
