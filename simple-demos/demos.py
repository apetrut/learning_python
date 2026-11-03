
import sys


if __name__ == "__main__":
    args = [float(x) for x in sys.argv[1:]]
    if len(args) == 0:
        print("No arguments provided.")
    else:
        print(args[1])


try:
    from Backend.models import Product, ProductList
except ModuleNotFoundError as e:
      print("Backend module not found. Using local definitions for Product and ProductList.")
finally:
      print("Continuing with the rest of the code...")
      



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