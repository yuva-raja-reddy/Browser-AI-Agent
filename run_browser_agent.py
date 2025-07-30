import asyncio
from dotenv import load_dotenv
load_dotenv()
from browser_use import Agent
from browser_use.llm import ChatGoogle

async def main():

    carrier= "verizon"
    phone = "iphone 16 pro max - 1TB"
    Plan = "Unlimited Ultimate"
    num_lines = 1

    agent = Agent(
        task=f'''
        You are a browser agent that can search the web and extract information like a Data Analyst

        Go to {carrier} website and look for phones and select it.
        Then look for {phone} and select it, you can scroll or search until you found that phone and select it.
        If there is something about new or existing customer, select new customer.
        And if there is something about trade in, select no trade in.
        Add it to cart with 1 lines and one phone. If there is something about device protection, select no device protection.
        Check if there are exactly {num_lines} lines in the cart. Remove any extra lines if there are more than {num_lines} lines.
        If there are any offers or promotions, select no offers.
        Once you are on checkout page wait for sometime to load all details 
        If there are mu
        then look for all the details in that page and give me a json with the following details:

        
        return format example in a json:
        "Phone_Name": "iphone 16 pro max - 512 GB", 
        "EstimatedCost": "$20.55/mo for 36 months,Device savings: $18.33/mo,Unlimited Ultimate plan required.",
        "Memory": "512 GB",
        "Plan_Name": "Unlimited Ultimate",
        "Plan_Cost": "$90/mo",
        "Plan_Details": "Unlimited data, 5G access, HD video streaming,
        50GB mobile hotspot.",
        "Total_Cost": "$110.55/mo"

        Here total cost is the sum of phone cost and plan cost.
        If any of the above information is not available, search google for it and extract the information.
        If you are not able to find the information, return "Not Found" for that field
        Do not look in Support or FAQ pages. 

        ''',
        llm=ChatGoogle(model="gemini-2.5-flash-lite-preview-06-17", temperature=1.0),
        # "gemini-2.5-pro"
        # "gemini-2.5-flash-lite-preview-06-17"
    )
    await agent.run()

asyncio.run(main())



# You are a browser agent that can search the web and extract information like a Data Analyst

# Go to {carrier} website and look for phones and select apple phones.
# Then look for {phone} and select it.
# If there is something about new or existing customer, select new customer.
# And if there is something about trade in, select no trade in.
# Look for Estimated payment at the bottom of page and then extract the estimated cost for that mobile in the web page.

# Now look for {Plan} Plan for {carrier} in google and navigate to the page with plan details
# Now get all details and perks provided in that plan and the cost of that plan.
# If any thing about address, Use this address: Herndon, VA 20171.
# If there is any pop up after then click skip or use X mark to close it.

# return format example in a json:
# "Phone_Name": "iphone 16 pro max - 512 GB", 
# "EstimatedCost": "$20.55/mo for 36 months,Device savings: $18.33/mo,Unlimited Ultimate plan required.",
# "Memory": "512 GB",
# "Plan_Name": "Unlimited Ultimate",
# "Plan_Cost": "$90/mo",
# "Plan_Details": "Unlimited data, 5G access, HD video streaming,
# 50GB mobile hotspot.",
# "Total_Cost": "$110.55/mo"

# Here total cost is the sum of phone cost and plan cost.
# If any of the above information is not available, search google for it and extract the information.
# If you are not able to find the information, return "Not Found" for that field
# Do not look in Support or FAQ pages. 