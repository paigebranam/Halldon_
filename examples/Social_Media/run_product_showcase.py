import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=80)

#Create a product showcase for social media platforms

gpt.add_example(Example("""CopyAi, an AI powered copywriter for small businesses and entrepreneurs """,
"""“Hello I’m CopyAi, an automated copywriting service for small businesses and entrepreneurs. 
With our AI technology, you can easily generate high-quality unique content for a fraction of the cost."""))

gpt.add_example(Example("""CopyAi, an AI powered copywriter for small businesses and entrepreneurs """,
"""“Green Ivy Creative is an independent marketing agency that has launched the world's first AI powered copywriter. 
CopyAi, creates original content from scratch in seconds. With world-class writers on our team, we can create SEO 
friendly content for any business with over 1 million writing samples, including business documents and blog posts. 
We are currently offering a free trial, message us for more info!"""))

gpt.add_example(Example("""CopyAi, an AI powered copywriter for small businesses and entrepreneurs """,
"""“Need to write content for your website or blog? The team over at CopyAi has developed an AI powered 
copywriter to provide you with professional courses that you can publish on your site."""))

gpt.add_example(Example("""CopyAi, an AI powered copywriter for small businesses and entrepreneurs """,
"""“What if you could outsource business copy to a human-like, AI assistant? That’s what I did 
when I decided to create CopyAi. The AI formulates winning copy and headlines for my clients 
based on their specific niche and overall brand goal. All of this is done so that my clients 
can laser focus on activities that are more important to them, such as building relationships 
with their customers or focusing on marketing to social media."""))

gpt.add_example(Example("""CopyAi, an AI powered copywriter for small businesses and entrepreneurs """,
"""“I’m CopyAi. I specialize in generating content for web and social media, so you don’t have to. 
Using my advanced AI personalization technology, I can quickly and easily craft original, high-quality 
copy that converts. Who knew outsourcing could be this easy?"""))

gpt.add_example(Example("""CopyAi, an AI powered copywriter for small businesses and entrepreneurs """,
"""“Human copywriters are too expensive *and* you can’t trust them. CopyAi writes your copy while you shop or whatever."""))

# Define UI configuration
config = UIConfig(description="Create a product showcase for social media.",
                  button_text="Create",
                  placeholder="Product (optional), description of product")

demo_web_app(gpt, config)