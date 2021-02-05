import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.6,
          max_tokens=80)


#Create a catchy e-mail subject line

gpt.add_example(Example("""Detangle Spray, This special milky detangler spray. A few spritzes lubricates hair strands to make styling easier. 
Hair feels soft and lightly nourished. For all hair types.""",
"""SOFT HAIR!"""))

gpt.add_example(Example("""Detangle Spray, This special milky detangler spray. A few spritzes lubricates hair strands to make styling easier. 
Hair feels soft and lightly nourished. For all hair types.""",
"""The best hairspray to ever walk the earth!?"""))

gpt.add_example(Example("""Detangle Spray, This special milky detangler spray. A few spritzes lubricates hair strands to make styling easier. 
Hair feels soft and lightly nourished. For all hair types.""",
"""Your hair can look this good, too."""))

gpt.add_example(Example("""Detangle Spray, This special milky detangler spray. A few spritzes lubricates hair strands to make styling easier. 
Hair feels soft and lightly nourished. For all hair types.""",
"""How Your Hair Will Love You"""))

gpt.add_example(Example("""diamond ring, This lovely promise ring for her shimmers with a diamond accent set in a pretty sterling silver band.""",
"""It's about to get real between you two. #engagement"""))

gpt.add_example(Example("""diamond ring, A cluster of round diamonds is flanked by rows of additional round diamonds in this elegant 
engagement ring for her, crafted in 10K white gold. More diamonds grace the profile for a touch of sparkle from every angle. 
The ring totals 1/3 carat in diamond weight.""",
"""Her dazzling smile is only outshone by her new ring!"""))

gpt.add_example(Example("""diamond ring, A cluster of round diamonds is flanked by rows of additional round diamonds in this elegant 
engagement ring for her, crafted in 10K white gold. More diamonds grace the profile for a touch of sparkle from every angle. 
The ring totals 1/3 carat in diamond weight.""",
"""Sheer sparkle in a traditional style"""))

gpt.add_example(Example("""diamond ring, A cluster of round diamonds is flanked by rows of additional round diamonds in this elegant 
engagement ring for her, crafted in 10K white gold. More diamonds grace the profile for a touch of sparkle from every angle. 
The ring totals 1/3 carat in diamond weight.""",
"""Diamonds found in nature are 100% natural and conflict-free."""))




# Define UI configuration
config = UIConfig(description="Create a catchy e-mail subject line",
                  button_text="Create",
                  placeholder="Product (optional), Description of product.")

demo_web_app(gpt, config)