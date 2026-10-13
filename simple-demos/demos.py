try:
    from Backend.models import Product, ProductList
except ModuleNotFoundError:
    class Product(BaseModel):
        model_config = ConfigDict(extra="allow", populate_by_name=True)

        id: str
        categoryId: str
        name: str | None = None
        description: str | None = None
        categoryName: str | None = None
        contentVector: list[float] | None = None

    class ProductList(BaseModel):
        items: list[Product] = []
