import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=80)

#Create a product launch 

gpt.add_example(Example("""CopyAi, AI powered copywriter for small businesses and entrepreneurs""",
"""CopyAi is an AI powered copywriter for small businesses and entrepreneurs. We built the first ever AI 
engine to generate high-converting copy for any product and any audience in seconds."""))

gpt.add_example(Example("""CopyAi, AI powered copywriter for small businesses and entrepreneurs""",
"""CopyAI is an AI powered copywriter for small businesses and entrepreneurs. If you hate writing marketing copy, 
it will blow your mind. Get started free for 7 days. Unlimited usage. No beta email needed."""))

gpt.add_example(Example("""CopyAi, AI powered copywriter for small businesses and entrepreneurs""",
"""CopyAi is an AI powered copywriter for small businesses. This is not a template driven script. 
You can customize the text to your specific product(s). With CopyAi, you can have a top notch sales 
page in under 30 mins (no coding, no design skills needed). Try it now."""))

gpt.add_example(Example("""CopyAi, AI powered copywriter for small businesses and entrepreneurs""",
"""Launch The AI powered copywriter makes writing copy for any product and for any audience in seconds. 
It's truly revolutionary in how it can be used. Try it free for 7 days. No invitation needed. Unlimited usage."""))

gpt.add_example(Example("""CopyAi, AI powered copywriter for small businesses and entrepreneurs""",
"""Have you ever had the problem that you had to write a press release, blog posts, Facebook posts or 
e-mail newsletters yourself? CopyAi is an AI powered copywriter that will provide you with personalized 
content and unique ideas. Based on decades of research in cognitive science and AI, it takes"""))


# Define UI configuration
config = UIConfig(description="Create an attention grabber for launching your product",
                  button_text="Create",
                  placeholder="Product (optional), description of product")

demo_web_app(gpt, config)