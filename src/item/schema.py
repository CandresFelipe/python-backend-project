from pydantic import BaseModel, Field


class CreateSurveyRequest(BaseModel):
    name: str = Field(..., description="Name of the product")
    description: str = Field(..., description="Description of the product")
    price: str = Field(..., description="Price of the product with the locale currency")
    color: str = Field(..., description="Color of the product")
    size: str = Field(..., description="size of the product, this must show only one")
    image_uri: str = Field(
        ..., description="the uri to get access to the product image"
    )
