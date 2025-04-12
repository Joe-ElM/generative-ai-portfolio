from langchain.prompts     import PromptTemplate
from langchain.chains      import LLMChain


personalization_template = """
You are a helpful and professional real estate assistant. Rewrite the following property listing to align with the buyer's preferences.

Buyer’s profile and preferences:
{buyer_profile}

Original property listing:
{listing_description}

Guidelines:
- Start with a clear and engaging title for the listing.
- Keep the description concise and to the point (around 3 to 5 sentences).
- Focus only on factual details and features relevant to the buyer’s preferences.
- Do not invent or assume details that are not in the original listing.
- Avoid flowery or exaggerated language or fabrications..
- Ensure the final description is practical and helpful.

- After the description, include fictional broker details at the end of each listing:
  - Broker name (invent a realistic name).
  - Contact phone number (invent a professional-looking number).
  - Email address (invent a realistic-looking professional email).

Example broker info:
Broker: Sarah Thompson, Future Homes Realty
Contact: (555) 123-4567 | sarah.thompson@futurehomes.com

Generate the personalized listing below:
"""


personalization_prompt = PromptTemplate(
                                        input_variables = ["buyer_profile", "listing_description"],
                                        template        = personalization_template,
                                       )

def get_personalization_chain(llm):
    return LLMChain(llm    = llm, 
                    prompt = personalization_prompt)

