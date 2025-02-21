from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Integer, DateTime
from typing import Optional

Base = declarative_base()


class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    current_discount_id: Mapped[int] = mapped_column(Integer, ForeignKey("discount.id"), nullable=False)
    discount: Mapped['Discount'] = relationship('Discount', back_populates='discount', lazy="selectin")
    store_id: Mapped[int] = mapped_column(Integer, ForeignKey("store.id"), nullable=False)
    store: Mapped['Store'] = relationship("Store", back_populates='products',  lazy="selectin")
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("category.id"))
    category: Mapped['Category'] = relationship('Category', back_populates='products', lazy="selectin")
    image_url: Mapped[Optional[str]] = mapped_column(String, default=None)
    store_url: Mapped[Optional[str]] = mapped_column(String, nullable=False)


class Category(Base):
    __tablename__ = 'category'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)


class Discount(Base):
    __tablename__ = 'discount'

    id: Mapped[int] = mapped_column(primary_key=True)
    old_price: Mapped[int] = mapped_column(nullable=False)  
    new_price: Mapped[int] = mapped_column(nullable=False)  
    discount_percent: Mapped[int] = mapped_column(nullable=False)
    start_date: Mapped[DateTime] = mapped_column(nullable=True)
    end_date: Mapped[DateTime] = mapped_column(nullable=False)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("product.id"))
    product: Mapped[Product] = relationship(Product, back_populates='discount', lazy='selectin')


class Store(Base):
    __tablename__ = 'store'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    url: Mapped[str] = mapped_column(nullable=False)