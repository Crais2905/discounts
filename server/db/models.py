from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Integer, DateTime, Float
from typing import Optional
from datetime import datetime

Base = declarative_base()


class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    current_discount_id: Mapped[int] = mapped_column(Integer, ForeignKey("discount.id"), nullable=False)
    discount: Mapped['Discount'] = relationship(
        'Discount', back_populates='product', lazy="selectin", foreign_keys=[current_discount_id], uselist=False
    )
    store_id: Mapped[int] = mapped_column(Integer, ForeignKey("store.id"), nullable=False)
    store: Mapped['Store'] = relationship("Store", back_populates='products',  lazy="selectin")
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("category.id"), nullable=False)
    category: Mapped['Category'] = relationship('Category', back_populates='products', lazy="selectin")
    image_url: Mapped[Optional[str]] = mapped_column(String, default=None)


class Category(Base):
    __tablename__ = 'category'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    products: Mapped[list[Product]] = relationship("Product", back_populates='category')

class Discount(Base):
    __tablename__ = 'discount'

    id: Mapped[int] = mapped_column(primary_key=True)
    old_price: Mapped[int] = mapped_column(Integer, nullable=False)  
    new_price: Mapped[int] = mapped_column(Integer, nullable=False)  
    discount_percent: Mapped[int] = mapped_column(Integer, nullable=False)
    start_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    end_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    product: Mapped[Product] = relationship(Product, back_populates='discount', lazy='selectin')


class Store(Base):
    __tablename__ = 'store'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    url: Mapped[str] = mapped_column(String, nullable=False)
    products: Mapped[list[Product]] = relationship(Product, back_populates='store')