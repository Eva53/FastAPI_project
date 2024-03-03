from pydantic import BaseModel, field_validator
from pydantic_core import PydanticCustomError

from .books import ReturnedBook

__all__ = ["IncomingSeller", "ReturnedAllSellers", "ReturnedSeller", "ReturnedSellerWithBooks"]


# Базовый класс "Продавец", содержащий поля, которые есть во всех классах-наследниках.
class BaseSeller(BaseModel):
    first_name: str
    last_name: str
    email: str


# Класс для валидации входящих данных. Не содержит id так как его присваивает БД.
class IncomingSeller(BaseSeller):
    password: str


# Класс, валидирующий исходящие данные. Он уже содержит id, но не содержит password для безопасности
class ReturnedSeller(BaseSeller):
    id: int


# Класс, валидирующий исходящие данные. Он уже содержит id, но не содержит password для безопасности
class ReturnedSellerWithBooks(BaseSeller):
    id: int
    books: list[ReturnedBook]


# Класс для возврата массива объектов "Продавец"
class ReturnedAllSellers(BaseModel):
    sellers: list[ReturnedSeller]
