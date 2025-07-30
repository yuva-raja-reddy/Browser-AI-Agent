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
        You are a browser agent that can search the web and extract information like a Data Analyst. Your goal is to gather Verizon plan and device details accurately and output them in a strict JSON format matching the metrics below.

        Steps to follow:
        1. Go to the Verizon website (verizon.com) and navigate to the phones section.
        2. Search for and select the phone: {phone}. Scroll or use site search if needed until you find it.
        3. If prompted for new/existing customer, select new customer.
        4. Select no trade-in.
        5. Add the phone to cart with {num_lines} lines and one phone only.
        6. If prompted for device protection, select no.
        7. Ensure exactly {num_lines} lines are in the cart; remove any extras.
        8. If there are offers, promotions, or add-ons (e.g., watches, hotspots), decline them unless they are part of the core plan.
        9. Proceed to the checkout or plan selection page. Select the plan: {Plan}.
        10. Wait 10-15 seconds for the page to fully load all pricing, details, and totals.
        11. Extract all details from the page, focusing on the metrics listed below. Use tools like Verizon's plan calculator if available on the site for estimates.
        12. If any metric is incomplete on the site, search Google for "Verizon {Plan} details" or "Verizon {phone} pricing" and extract from reliable results (e.g., official Verizon pages or calculators). Do not use support, FAQ, or forum pages.
        13. Calculate Estimated_Total_Cost as the sum of plan price + mobile/device price (per month).
        14. For Why_Verizon, create 4-5 bullet points based on site content or key selling points from searches.
        15. If any info is truly not found, use "Not Found" for that field.
        16. Output ONLY the JSON object below – no extra text.

        Return strictly in this JSON format:
        
        "Phone_Name": "Extracted phone name, e.g., iPhone 16 Pro Max - 1TB",
        "Estimated_Total_Cost": "Monthly total: plan price + mobile price, e.g., $110.55/mo (plan price + mobile price)",
        "Line_Charge": "Cost per line, e.g., $90/mo per line for Unlimited Ultimate",
        "Auto_Pay_Discount": "Details if available, e.g., $10/mo discount with Auto Pay",
        "Device_Payment": "Monthly device payment, e.g., $30.55/mo for 36 months",
        "Data_Plan": "Selected plan name, e.g., Unlimited Ultimate",
        "Other_Devices": "Details on add-ons like watches/hotspots, e.g., Up to 50% off watch or tablet plans",
        "Talk_Text": "Details, e.g., Unlimited talk and text nationwide",
        "Video_Streaming": "Quality details, e.g., HD video streaming (up to 720p)",
        "Mobile_Hotspot": "Details, e.g., 50GB high-speed per line, then unlimited at reduced speeds",
        "International": "Roaming details, e.g., Unlimited in Mexico/Canada; $5/day elsewhere",
        "Key_Features": "List of perks, e.g., Unlimited 5G data, included streaming services",
        "Fees": "Details, e.g., $35 activation fee per line",
        "Coverage": "Details, e.g., Nationwide 5G and 4G LTE",
        "Why_Verizon": ["Bullet point 1", "Bullet point 2", "Bullet point 3", "Bullet point 4"]
        

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