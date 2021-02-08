import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app

# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100)


##Generate feature to benefit for product


gpt.add_example(Example("""AirPods Max, Introducing AirPods Max — a perfect balance of exhilarating high-fidelity audio 
and the effortless magic of AirPods. The ultimate personal listening experience is here.""",
"""A deeper richer bass, an expansive soundstage, and less distortion make listening to your favorite music with AirPods Max a treat for the ears."""))

gpt.add_example(Example("""AirPods Max, Introducing AirPods Max — a perfect balance of exhilarating high-fidelity audio 
and the effortless magic of AirPods. The ultimate personal listening experience is here.""",
"""Experience wireless audio the way it’s meant to be heard with AirPods Max"""))

gpt.add_example(Example("""AirPods Max, Introducing AirPods Max — a perfect balance of exhilarating high-fidelity audio 
and the effortless magic of AirPods. The ultimate personal listening experience is here.""",
"""AirPods Max sound better than the original AirPods, feature world-class noise cancellation and come with TrueWireless™ technology."""))

gpt.add_example(Example("""AirPods Max, Introducing AirPods Max — a perfect balance of exhilarating high-fidelity audio 
and the effortless magic of AirPods. The ultimate personal listening experience is here.""",
"""Listen to more of your music than ever, in unparalleled quality, with no wires."""))

gpt.add_example(Example("""Bento Lunch Box Container, slim design but it is also more than enough space, 
sometimes too much. The biggest plus is that it is BPA free and FDA approved. A huge win when trying to eat clean!""",
"""Perfect size for my two year old. More space than I thought but with a slim design, it doesn’t take up too much room in my diaper bag."""))

gpt.add_example(Example("""Bento Lunch Box Container, slim design but it is also more than enough space, 
sometimes too much. The biggest plus is that it is BPA free and FDA approved. A huge win when trying to eat clean!""",
"""If you are a parent you understand how you want the best for your child. The Bento Box is perfect for little hands. 
It promotes portion control and healthy eating habits."""))

gpt.add_example(Example("""Bento Lunch Box Container, slim design but it is also more than enough space, 
sometimes too much. The biggest plus is that it is BPA free and FDA approved. A huge win when trying to eat clean!""",
"""Because the 3 compartment, 6 separate container is so much bigger, it takes less time to pack the lunchbox up."""))





# Define UI configuration
config = UIConfig(description="Create feature to benefits for your product",
                  button_text="Create",
                  placeholder="Enter product description and name")

demo_web_app(gpt, config)