import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.8,
          max_tokens=80)

#Create thank you notes


gpt.add_example(Example("""Customer, for their purchase""",
"""Thank you so much for your purchase. Having your business will help us expand our customer base which will have a huge impact on us."""))

gpt.add_example(Example("""Customer, for their purchase""",
"""Thank you so much for your purchase. I hope you love this new product!"""))

gpt.add_example(Example("""Customer, for their purchase""",
"""Thank you so much for your purchase. I hope you love this new product!"""))

gpt.add_example(Example("""Customer, for their feedback""",
"""Thank you for their feedback for our new product. This feedback is an important part of the process to create a great product that people use."""))

gpt.add_example(Example("""Customer, for their feedback""",
"""Thank you for your feedback. Your post helps me to know what parts of my business I need to improve on and where I am doing well. 
I care about your success as much as my own. Please reach out to me if you have any questions about [my company]."""))


# Define UI configuration
config = UIConfig(description="Create a Thank You Note",
                  button_text="Create",
                  placeholder="Who are we thanking, what are we thanking them for? (I.e.: Customer, for their purchase.")

demo_web_app(gpt, config)