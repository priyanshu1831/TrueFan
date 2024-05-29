from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from .schemas import ProductCreate, Product
from .crud import get_product, get_products, create_product, update_product, delete_product

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/products/{product_id}", response_model=Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = get_product(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.get("/products/", response_model=list[Product])
def read_products(db: Session = Depends(get_db)):
    return get_products(db)

@app.post("/products/", response_model=Product)
def create_product_endpoint(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)

@app.put("/products/{product_id}", response_model=Product)
def update_product_endpoint(product_id: int, product: ProductCreate, db: Session = Depends(get_db)):
    return update_product(db, product_id, product)

@app.delete("/products/{product_id}")
def delete_product_endpoint(product_id: int, db: Session = Depends(get_db)):
    delete_product(db, product_id)
    return {"detail": "Product deleted"}
