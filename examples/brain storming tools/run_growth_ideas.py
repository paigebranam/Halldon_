import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=80)

#Create a growth ideas generator

gpt.add_example(Example("""CopyAi, an AI powered copywriter for small businesses and entrepreneurs""",
"""“create a use case with a clear value proposition to show how CopyAi will help in creating content 
for small businesses and entrepreneurs who are having trouble coming up with engaging content."""))

gpt.add_example(Example("""CopyAi, an AI powered copywriter for small businesses and entrepreneurs""",
"""“build an application programming interface or API for the CopyAi platform - allowing developers 
to embed the AI as part of their programs. Assuming that there are 5,000 small businesses in the US alone, 
and each business will use the CopyAi API for a few hundred dollars a month, this means that there is an annual 
recurring revenue potential of $500,000 gross revenue per year. If the fixed costs are lowered, then there is 
potential to make more than double digit profit margins."""))

gpt.add_example(Example("""CopyAi, an AI powered copywriter for small businesses and entrepreneurs""",
"""“design an annual challenge for the top CopyAi users, to overcome a specific challenge like writing 
compelling introverts and effective sales copy. The goal is really to find out what the users do best 
and then apply it to their businesses or life goals. This will help deepen the relationship between CopyAi 
and it’s community, as they engage across challenges and gleaning each other’s advice as they help each 
other over come them."""))

gpt.add_example(Example("""CopyAi, an AI powered copywriter for small businesses and entrepreneurs""",
"""“onboard customers by giving away advertising credit to try out the product. They can then pay to keep 
using CopyAi or upgrade their plan when they start using the product and discover the value in your core offering."""))

gpt.add_example(Example("""CopyAi, an AI powered copywriter for small businesses and entrepreneurs""",
"""“integrate it with Shopify's product search . CopyAi can leverage the main benefit of Shopify's product 
search attribute. Even if merchants don't use CopyAi, they will be able to get accurate descriptions for 
their products. This will increase their conversion rate and boost their sales."""))



# Define UI configuration
config = UIConfig(description="Generate new ideas for the growth of your product",
                  button_text="Generate",
                  placeholder="Product (optional), description of product")

demo_web_app(gpt, config)