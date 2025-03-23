from app.database import product_collection
import asyncio

products_data = [
    {"name": "Teclado Mecánico", "price": 79.99, "category": "Accessories", "description": "Teclado mecánico RGB"},
    {"name": "Monitor 24''", "price": 199.99, "category": "Electronics", "description": "Monitor LED 24 pulgadas"},
    {"name": "Silla Gamer", "price": 299.99, "category": "Furniture", "description": "Silla ergonómica para gaming"}
]

async def seed_database():
    for product in products_data:
        existing_product = await product_collection.collection.find_one({"name": product["name"]})
        if not existing_product:
            await product_collection.collection.insert_one(product)
            print(f"Producto agregado: {product['name']}")
        else:
            print(f"El producto '{product['name']}' ya existe en la base de datos.")

if __name__ == "__main__":
    asyncio.run(seed_database())