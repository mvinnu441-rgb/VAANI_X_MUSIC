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
def get_readable_time(seconds: int) -> str:
    count = 0
    readable_time = ""
    time_list = []
    time_suffix_list = ["s", "ᴍ", "ʜ", "ᴅᴀʏs"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        readable_time += time_list.pop() + ", "

    time_list.reverse()
    readable_time += ":".join(time_list)

    return readable_time
