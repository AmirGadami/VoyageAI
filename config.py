from dotenv import  load_dotenv
import os




ticket_prices = {
    "london": "$799",
    "paris": "$899",
    "tokyo": "$1400",
    "berlin": "$499",
    "new_york": "$650",
    "los_angeles": "$750",
    "sydney": "$1600",
    "dubai": "$1200",
    "rome": "$850",
    "singapore": "$1300",
    "toronto": "$700",
    "bangkok": "$1100",
    "madrid": "$780",
    "hong_kong": "$1250",
    "amsterdam": "$820",
    "istanbul": "$950",
    "seoul": "$1350",
    "cairo": "$880",
    "rio_de_janeiro": "$980",
    "cape_town": "$1450",
    "beijing": "$1380",
    "mexico_city": "$900",
    "buenos_aires": "$1050",
    "moscow": "$1200",
    "vienna": "$830",
    "lisbon": "$810",
    "são_paulo": "$1020",
    "prague": "$790",
    "stockholm": "$860",
    "helsinki": "$870",
    "oslo": "$890",
    "budapest": "$740",
    "warsaw": "$720",
    "brussels": "$805",
    "zurich": "$880",
    "geneva": "$895",
    "athens": "$910",
    "jakarta": "$1250",
    "manila": "$1220",
    "kuala_lumpur": "$1180",
    "taipei": "$1280",
    "ho_chi_minh_city": "$1120",
    "hanoi": "$1110",
    "mumbai": "$1150",
    "delhi": "$1170",
    "bangalore": "$1190",
    "chennai": "$1160",
    "santiago": "$1080",
    "bogota": "$980",
    "lima": "$970",
    "auckland": "$1650",
    "nairobi": "$1320",
    "lagos": "$1400",
    "doha": "$1250",
    "riyadh": "$1275"
}

cities = list(ticket_prices.keys())

GPT_MODEL = "gpt-4o-mini"
CLAUDE_MODEL = "claude-3-haiku-20240307"

price_function = {
    "name": "get_ticket_price",
    "description": "Get the price of a return ticket to the destination city. Call this whenever you need to know the ticket price, for example when a customer asks 'How much is a ticket to this city'",
    "parameters": {
        "type": "object",
        "properties": {
            "destination_city": {
                "type": "string",
                "description": "The city that the customer wants to travel to",
            },
        },
        "required": ["destination_city"],
        "additionalProperties": False
    }
}

tools = [{"type": "function", "function": price_function}]




gpt_system = "You are a helpful AI assistant working for a travel agency. \
You assist customers with booking tickets,and knowing the flight prices. short conversation, only answer 2 questions. start with short greeting"
claude_system = (
    f"You are a curious customer who wants to travel and get ticket price information. "
    f"Pick **one random city** from this list: {', '.join(cities)}. "
    "Directly ask for the ticket price for that city. "
    "Do not say you're choosing or picking a city. "
    "You only ask 2 questions and do not mention another city. Keep it natural and short."
)



load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
