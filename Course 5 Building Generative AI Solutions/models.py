# from pydantic import BaseModel, Field
# from typing   import List

# class RealEstateListing(BaseModel):
#     neighborhood            : str   = Field(..., description="Neighborhood name")
#     price                   : str   = Field(..., description="Property price (formatted as $X,XXX,XXX)")
#     bedrooms                : int   = Field(..., description="Number of bedrooms")
#     bathrooms               : float = Field(..., description="Number of bathrooms")
#     house_size              : str   = Field(..., description="House size in square feet")
#     property_type           : str   = Field(..., description="Type of property (house, condo, etc.)")
#     description             : str   = Field(..., description="Detailed property description")
#     neighborhood_description: str   = Field(..., description="Description of the neighborhood")

#     class Config:
#         # Updated config keys for Pydantic v2.x
#         str_min_length = 1
#         str_strip_whitespace = True
from pydantic import BaseModel, Field
from typing import List

class RealEstateListing(BaseModel):
    neighborhood: str
    price: str
    bedrooms: int
    bathrooms: float
    house_size: str
    property_type: str
    description: str
    neighborhood_description: str

class ListingCollection(BaseModel):
    listings: List[RealEstateListing] = Field(..., description="Collection of real estate listings")


