from bson.objectid import ObjectId, InvalidId
from .database import product_collection

def product_serializer(product) -> dict:
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "price": product["price"],
        "category": product["category"],
        "description": product.get("description", "")
    }

async def create_product(product_data):
    new_product = await product_collection.insert_one(product_data)
    created_product = await product_collection.find_one({"_id": new_product.inserted_id})
    return product_serializer(created_product)

async def get_all_products():
    products = await product_collection.find().to_list(100)
    return [product_serializer(product) for product in products]

async def get_product_by_id(product_id):
    try:
        product = await product_collection.find_one({"_id": ObjectId(product_id)})
        return product_serializer(product)
    except InvalidId:
        return None

async def update_product(product_id, product_data):
    try:
        existing_product = await product_collection.find_one({"_id": ObjectId(product_id)})
    except InvalidId:
        return None
    
    if existing_product:
        await product_collection.update_one({"_id": ObjectId(product_id)}, {"$set": product_data})
        updated_product = await product_collection.find_one({"_id": ObjectId(product_id)})
        return product_serializer(updated_product)
    return None

async def delete_product(product_id):
    try:
        deleted_product = await product_collection.find_one({"_id": ObjectId(product_id)})
    except InvalidId:
        return None
    
    if deleted_product:
        await product_collection.delete_one({"_id": ObjectId(product_id)})
        return True
    return False