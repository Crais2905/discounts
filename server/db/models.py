from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Integer
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
    pass


class Store(Base):
    pass