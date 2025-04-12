import os
import gradio                as     gr
from   langchain.prompts     import PromptTemplate
from   langchain.chains      import LLMChain
from   langchain.chat_models import ChatOpenAI
from   models                import RealEstateListing, ListingCollection
from   generate_listings     import generate_listings
from   vector_store          import prepare_vector_store
from   personalization       import get_personalization_chain 
from   config                import OPENAI_API_KEY, OPENAI_API_BASE
from   utils                 import build_buyer_profile


# --------------------------
# Initialize LLM
# --------------------------
llm = ChatOpenAI(
                temperature     = 0.4,
                openai_api_key  = OPENAI_API_KEY,
                openai_api_base = OPENAI_API_BASE,
              # max_tokens      = 500 
                )

personalization_chain = get_personalization_chain(llm)

# --------------------------
# Generate listings and vector store
# --------------------------
df          = generate_listings(llm, num_listings = 50)
vectorstore = prepare_vector_store(df)


# --------------------------
# Gradio Interface Function
# --------------------------
# def home_match_app(buyer_input):
#     results = vectorstore.similarity_search(buyer_input, k=3)
#     personalized_results = [
#         personalization_chain.run(
#                                  buyer_profile       = buyer_input,
#                                  listing_description = result.page_content
#                                  )
#         for result in results
#     ]
#     return "\n\n---\n\n".join(personalized_results)

# # --------------------------
# # Gradio UI
# # --------------------------
# interface = gr.Interface(
#                 fn = home_match_app,
#                 inputs = gr.Textbox(lines=4, placeholder="Describe your dream home, lifestyle, or preferences..."),
#                 outputs     = "text",
#                 title       = "HomeMatch: Personalized Real Estate Finder",
#                 description = "Enter your preferences and let HomeMatch find personalized real estate listings just for you!"
#             )

def home_match_app(location, bedrooms, bathrooms, size, amenities, extra_description):
    # Build the dynamic buyer profile from inputs
    buyer_profile = build_buyer_profile(location, bedrooms, bathrooms, size, amenities, extra_description)

    # Perform semantic search
    results = vectorstore.similarity_search(buyer_profile, k=3)

    # Personalize results
    personalized_results = [
        personalization_chain.run(
                                  buyer_profile       = buyer_profile,
                                  listing_description = result.page_content
                                 )
        for result in results
    ]

    return "\n\n---\n\n".join(personalized_results)

interface = gr.Interface(
    fn     = home_match_app,
    inputs = [
        gr.Textbox(label = "Location" , placeholder="e.g., Munich"),
        gr.Number(label  = "Bedrooms" , precision=0),
        gr.Number(label  = "Bathrooms", precision=1),
        gr.Textbox(label = "House Size (e.g., 2000 sqft)"),
        gr.CheckboxGroup(
                         choices = ["Pool", "Garage", "Solar Panels", "Smart Home"],
                         label   = "Amenities"
                         ),
        gr.Textbox(
                    label       = "Additional Preferences",
                    placeholder = "e.g., Quiet neighborhood, natural lighting, eco-friendly materials, close to public transport.",
                    lines       = 6
                   )

    ],
    outputs     = "text",
    title       = "HomeMatch: Personalized Real Estate Finder",
    description = "Enter your desired home features and let HomeMatch find the best listings for you."
)


# --------------------------
# Launch App
# --------------------------
if __name__ == "__main__":
    interface.launch()
