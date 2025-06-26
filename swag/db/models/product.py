from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Enum, Float
from .. import db
import enum

class ProductCategory(enum.Enum):
    pants="pants",
    top="top",
    skirt="skirt"
    accessories="accessories"
    shoes="shoes"


class Product(db.Model): 
    __tablename__ = "products"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    photo_url: Mapped[str] = mapped_column(String(200), nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    price:Mapped[int] = mapped_column(Integer(), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer(), nullable=False)
    description: Mapped[str] = mapped_column(String(200), nullable=False)
    category: Mapped[ProductCategory] = mapped_column(Enum(ProductCategory), nullable=False) 