import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app

# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100)

gpt.add_example(Example("""Data science intern, Analyzing and modeling data to show trends in tweets.""",
"""Intro: I am a senior at Northwestern University studying Mathematics and Computer Science. I have been interested in analytical data for a long time. 
Last summer, I interned at Twitter, Inc. where I worked on a counterterrorism team focusing on ISIS's use of social media to further their agenda. 
The team used my expertise in big data to determine the regional locations from which ISIS was tweeting and to model the most influential accounts 
for the terrorist organization.
My specific duties included analyzing tweets, building models using statistical software, and helping to create charts that demonstrated how 
ISIS was using social media to recruit new members and spread their message.
Experience: I am very proficient in R, Python, C++, MATLAB and SAS for statistical analysis and modeling."""))

gpt.add_example(Example("""Data science intern, Analyzing and modeling data to show trends in tweets.""",
"""Intro: I am very interested in your open data science intern position. I have a proven track record of leveraging big data to create 
value and improve business decisions.
Experience: During my tenure at XYZ College, I worked as a data analyst on several projects including:
Creating statistical models to predict stock prices based on financial information from the past decade
Analyzing trending topics on Twitter to determine which tweets are most engaging and which celebrities drive the most traffic based on their followers
End: Thank you for your time. I look forward to speaking with you about this opportunity. If you would like to see examples of my work, my Github profile URL is attached.
Last Name, First Name"""))

gpt.add_example(Example("""Marketing manager, analyzing industry trends and demand for products and services and creating a 
successful strategy to market the product or service that lead to an increase in sales.""",
"""Intro: I am very interested in the Marketing Manager position with ABC Marketing Group. I believe that my 
education and experience make me an ideal candidate for the position.
Experience: During my tenure at XYZ College, I developed a passion for marketing and public relations. I have sought out 
multiple opportunities to develop my marketing skills. For example, last summer, I interned at the National Sculpture 
Society in New York City. My position entailed developing web pages and slideshows publicizing the success of the society's 
artists. I was able to utilize my web authoring skills to assist the organization in their goal to promote sculpture. Due to 
my strong communication skills, I have been given even more responsibilities. For example, I now public"""))


gpt.add_example(Example("""Marketing manager, analyzing industry trends and demand for products and services and creating a 
successful strategy to market the product or service that lead to an increase in sales.""",
"""Intro: I would like to be considered for the Marketing Manager position with ABC Marketing Group. I am confident 
that my experience in marketing and business development will help me be successful in this role.
Experience: My experience includes working in both the manufacturing and service industries in various marketing, 
sales, and management positions. I have successfully led teams of five to 15 individuals, managed budgets of $2 million 
to $20 million, created strategic plans, and consulted with senior executives in large organizations. In each position, 
I was responsible for designing and implementing marketing strategies for products ranging from $150 million to $50 billion in annual sales.
Experience also includes direct interaction with several Fortune 500 companies as key account manager.
End: Thank you for your consideration"""))


gpt.add_example(Example("""UX designer, I have experience in user experience research, creating user interfaces through wire framing, 
and have a degree in graphic design and communications.""",
"""Intro: I am a recent graduate of the University of California, Berkeley with a Bachelor’s degree in Graphic Design and Communications. 
With my education, I have gained skills in user experience research, creating user interfaces, and graphic design.
Experience: My internship at Apple Inc. in the User Experience group gave me hands-on experience with user research. My first project 
involved conducting research on teenagers’ use of social media through surveys and interviews. I was able to create a preliminary set 
of wireframes that showed the flow for a new app that would be designed to meet teens' needs.
I have also gained experience through completing visual designs in Adobe Illustrator and Photoshop. I have completed multiple projects 
involving brochure, poster, and"""))

gpt.add_example(Example("""UX designer, I have experience in user experience research, creating user interfaces through wire framing, 
and have a degree in graphic design and communications.""",
"""Intro: I have over five years of experience in user experience design and usability testing. I am currently working as a UX designer 
for a small start-up, but I'm interested in moving to a larger organization that will allow me to utilize my skills to the fullest potential.
Experience: My experience includes creating wireframes, prototypes, and user flows. I have conducted user research using both quantitative and 
qualitative methods. I have worked with my company's developers to create features using HTML5, CSS3, Javascript, JQuery, and Ajax.
Experience with Photoshop, InDesign, Illustrator.
End: I would like the opportunity to discuss this position further with you. Please contact me at 555-555-5555 or by email"""))






# Define UI configuration
config = UIConfig(description="Create a cover letter.",
                  button_text="Create",
                  placeholder="Tell me the role you're applying for and what experience makes you a good candidate.")

demo_web_app(gpt, config)
