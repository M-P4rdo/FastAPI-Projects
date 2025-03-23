from fastapi import APIRouter, HTTPException
from app import schemas, crud

router = APIRouter(prefix="/products", tags=["Productos"])

@router.get("/")
async def list_products():
    return await crud.get_all_products()

@router.post("/")
async def add_product(product: schemas.ProductSchema):
    return await crud.create_product(product.dict())

@router.get("/{id}")
async def retrieve_product(id: str):
    product = await crud.get_product_by_id(id)
    if product is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product

@router.put("/{id}")
async def modify_product(id: str, product: schemas.ProductSchema):
    updated_product = await crud.update_product(id, product.dict())
    if updated_product is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return updated_product

@router.delete("/{id}")
async def remove_product(id: str):
    if await crud.delete_product(id):
        return {"message": "Producto eliminado"}
    raise HTTPException(status_code=404, detail="Producto no encontrado")
