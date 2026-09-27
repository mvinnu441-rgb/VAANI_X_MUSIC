# -----------------------------------------------
# 🔴 Vaani ✘ Music Project
# 🔷️ Developed & Maintained by: ᯓ꯭𝐌ʀ 𝐕ɪɴɴᴜ⍣꯭꯭𓆪꯭🝐
# 📅 Copyright © 2026 – All Rights Reserved
#
# 📖 License:
# This source code is open for educational and non-commercial use ONLY.
# Commercial use, redistribution, or modification of this source
# without prior written permission from the author is prohibited.
#
# ❤️ Made with dedication & love by ᯓ꯭𝐌ʀ 𝐕ɪɴɴᴜ⍣꯭꯭𓆪꯭🝐
# -----------------------------------------------
from pyrogram import Client, filters
import pycountry
from VAANIMUSIC import app 

@app.on_message(filters.command("get_states"))
def get_states(client, message):
    try:
        # Extract the country name from the message
        country_name = message.text.split(' ', 1)[1]
        # Fetch the country information
        country = pycountry.countries.get(name=country_name)
        # Get the states (also known as subdivisions) of the country
        states = pycountry.subdivisions.get(country_code=country.alpha_2)
        states_list = [state.name for state in states]
        # Format the states into a message
        states_message = f"States of {country_name}:\n" + "\n".join(states_list)
    except IndexError:
        # No country name was provided
        states_message = "Please provide a country name after the command, like this:\n/get_states Canada"
    except AttributeError:
        # The country was not found
        states_message = f"I couldn't find the country '{country_name}'. Please make sure it's spelled correctly."
    
    # Send the message with states
    message.reply_text(states_message)
