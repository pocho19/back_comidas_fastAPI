
### Products API ###

from fastapi import APIRouter

router = APIRouter(prefix="/products",
                   tags=["products"],
                   responses={404: {"message": "No encontrado"}})

products_list = [
    "Arroz chaufa",
    "Bibimbap coreano",
    "Bondiolita entre panes",
    "Bowl de lentejas",
    "Bowl fresco",
    "El inolvidable",
    "Ensalada tropical",
    "Fideos Mingo",
    "Flower power",
    "Gallete",
    "Green bowl",
    "Healthy Caesar",
    "Healthy Caesar wrap",
    "Lasagna meet free ",
    "Mac & Cheese",
    "Nodlles orientales",
    "Pastel de bondiola",
    "Pastel de pescado",
    "Pescado a la sal",
    "Pinchos de pollo",
    "Pollito capresse",
    "Pollito citrico",
    "Pollo saltado",
    "Pollo Teriyaki",
    "Quesadillas integrales",
    "Quiche",
    "Rolls de pescado",
    "Salteado marroqui",
    "Sandwich de pollo",
    "Quesadillas",
    "Sandwich de ternera",
    "Ternera power",
    "Tex-Mex bowl",
    "Veggie burger",
    "Veggie wrap",
    "Vegie Burger",
    "Wrap de pollo",
    "Yamani bowl",
    "Producto 1",
    "Producto 2",
    "Producto 3",
    "Producto 4",
    "Producto 5",
    "- Feriado",
    "- NADA",
]


@router.get("/")
async def products():
    return products_list


@router.get("/{id}")
async def products(id: int):
    return products_list[id]
