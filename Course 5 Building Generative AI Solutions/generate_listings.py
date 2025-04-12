import pandas as pd
from fastapi.encoders import jsonable_encoder
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.output_parsers import PydanticOutputParser
from models import ListingCollection

parser = PydanticOutputParser(pydantic_object=ListingCollection)

def generate_listings(llm, num_listings=5):
    # Define parser
    parser = PydanticOutputParser(pydantic_object=ListingCollection)

    # Define diverse neighborhoods and features
    neighborhoods = [
        "Munich City Center", "Schwabing", "Maxvorstadt", "Glockenbachviertel", "Bogenhausen", "Haidhausen", "Sendling", "Isarvorstadt", "Laim", "Moosach"
    ]

    property_types = [
        "Modern Eco-Friendly Home", "Luxury Villa", "Family House", "Contemporary Townhouse", "Spacious Apartment", "Charming Duplex"
    ]

    amenities_options = [
        "Pool", "Garage", "Solar Panels", "Smart Home Technology", "Energy-Efficient Windows", "Large Garden", "Home Office", "Rooftop Terrace"
    ]

    # Build prompt
    prompt_template = f"""
    Generate {{num_listings}} unique and richly detailed real estate listings in JSON format matching the schema:
    {{format_instructions}}

    Each listing must include:
    - A vivid, engaging property description capturing architecture, unique features, interior design, and lifestyle.
    - A neighborhood description highlighting community features like parks, cafes, schools, transport, culture, and atmosphere.
    - Prices between $400,000 and $1,500,000.
    - House sizes between 1,500 sqft and 4,500 sqft.
    - Bedrooms between 2 and 6.
    - Bathrooms between 1 and 4.5.
    - Use random selections of amenities from: {', '.join(amenities_options)}.
    - Neighborhoods should be selected from: {', '.join(neighborhoods)}.
    - Property types should include variety: {', '.join(property_types)}.

    Guidelines:
    - Ensure each listing feels distinct and not repetitive.
    - Vary tone and phrasing between listings.
    - Maintain professionalism and realism.

    Number of listings: {{num_listings}}
    """

    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["num_listings"],
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run(num_listings=num_listings)
    result = parser.parse(response)

    df = pd.DataFrame(jsonable_encoder(result.listings))
    df.to_csv("listings.csv", index=False)

    return df
