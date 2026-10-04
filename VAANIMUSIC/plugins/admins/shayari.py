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
from VAANIMUSIC import app
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

# ── KripanshEmojis_by_fStikBot pack IDs ──
_KE_OK    = 6129812419028982717   # ✔️
_KE_WARN  = 6129782440157256336   # ❗
_KE_CROWN = 6129705083501293112   # 💎
_KE_BLOCK = 6129840374971112593   # ⛔
_KE_STAR  = 6129915811776698328   # ✨

def ke(eid, fb):
    return f'<emoji id={eid}>{fb}</emoji>'

spam_chats = []

EMOJI = [
    "💫💫💫💫💫",
    "🦋✨🌙💖🌈",
    "🌹🌺🌸🌼🪷",
    "💝💘💖💗💓",
    "🍓🍒🍑🍉🍇",
    "🧁🍰🍩🍪🍫",
    "☁️🌤️🌈⭐🌙",
    "🎀🧸💌🎁🎈",
    "🐼🦊🐰🐻🐱",
    "🌴🏝️🌊🐚🐬",
    "🍃🌿🍀🌱🌾",
    "🔥💎👑⚡🌟",
    "🥰😍😘😻💞",
    "🎶🎧🎤🎸🎹",
    "🍕🍟🍔🌮🍿",
    "🧋🥤🍹🍦🍭",
    "🪻💐🌷🌻🏵️",
    "🦄🧚‍♀️🪄🔮🌌",
    "❄️⛄🌨️☃️🧣",
    "🧚🌸🧋🍬🫖",
    "🥀🌷🌹🌺💐",
    "🌸🌿💮🌱🌵",
    "❤️💚💙💜🖤",
    "💓💕💞💗💖",
    "🌸💐🌺🌹🦋",
    "🍔🦪🍛🍲🥗",
    "🍎🍓🍒🍑🌶️",
    "🧋🥤🧋🥛🍷",
    "🍬🍭🧁🎂🍡",
    "🍨🧉🍺☕🍻",
    "🥪🥧🍦🍥🍚",
    🫖☕🍹🍷🥛",
    "☕🧃🍩🍦🍙",
    "🍁🌾💮🍂🌿",
    "🌨️🌥️⛈️🌩️🌧️",
    "🌷🏵️🌸🌺💐",
    "💮🌼🌻🍀🍁",
    "🧟🦸🦹🧙👸",
    "🧅🍠🥕🌽🥦",
    "🐷🐹🐭🐨🐻‍❄️",
    "🦋🐇🐀🐈🐈‍⬛",
    "🌼🌳🌲🌴🌵",
    "🥩🍋🍐🍈🍇",
    "🍴🍽️🔪🍶🥃",
    "🕌🏰🏩⛩️🏩",
    "🎉🎊🥳🪅🎆",
    "🦚🦜🦢🕊️🦩",
    "🌺🦋🌺🦋🌺",
    "💙🤍💜🩷🩵",
    "🏵️🌸💮🪷🌼",
]

####

SHAYRI = [
    " 💫**तेरी एक मुस्कान पर सारी दुनिया वार दूँ, तू कहे तो अपनी हर खुशी तुझ पर निसार दूँ।**💫 \n\n**🌹Teri ek muskaan par saari duniya waar du, tu kahe to apni har khushi tujh par nisaar du.🌹** ",
    " 💫**तुम साथ हो तो हर मुश्किल आसान लगती है, तुम्हारे बिना ये दुनिया वीरान लगती है।**💫 \n\n**🌹Tum saath ho to har mushkil aasaan lagti hai, tumhare bina ye duniya veeran lagti hai.🌹** ",
    " 💫**दिल की हर धड़कन में बस तेरा ही नाम है, मेरी हर दुआ में बस तेरा ही पैगाम है।**💫 \n\n**🌹Dil ki har dhadkan me bas tera hi naam hai, meri har dua me bas tera hi paigaam hai.🌹** ",
    " 💫**चाँद भी शरमा जाए जब तू सामने आए, तेरी एक झलक पर दिल बेकाबू हो जाए।**💫 \n\n**🌹Chaand bhi sharma jaye jab tu saamne aaye, teri ek jhalak par dil bekaabu ho jaye.🌹** ",
    " 💫**सुकून मिलता है तेरी बातों में, जन्नत दिखती है तेरी आँखों में।**💫 \n\n**🌹Sukoon milta hai teri baaton me, jannat dikhti hai teri aankhon me.🌹** ",
    " 💫**ना कोई वादा, ना कोई कसम, बस तू साथ रहना हर जनम।**💫 \n\n**🌹Na koi vaada, na koi kasam, bas tu saath rehna har janam.🌹** ",
    " 💫**तू मेरी आदत नहीं, मेरी ज़रूरत है, तेरे बिना ये ज़िंदगी अधूरी सी मूरत है।**💫 \n\n**🌹Tu meri aadat nahi, meri zarurat hai, tere bina ye zindagi adhuri si moorat hai.🌹** ",
    " 💫**इश्क़ में तेरे ऐसे खो गए हैं हम, कि खुद से ही बेखबर हो गए हैं हम।**💫 \n\n**🌹Ishq me tere aise kho gaye hain hum, ki khud se hi bekhabar ho gaye hain hum.🌹** ",
    " 💫**सुबह की पहली किरण में तेरा ही ख्याल है, रात की आखिरी नींद में भी तेरा ही जमाल है।**💫 \n\n**🌹Subah ki pehli kiran me tera hi khayal hai, raat ki aakhri neend me bhi tera hi jamaal hai.🌹** ",
    " 💫**मोहब्बत वो नहीं जो हर पल जताई जाए, मोहब्बत वो है जो खामोशी में निभाई जाए।**💫 \n\n**🌹Mohabbat wo nahi jo har pal jatayi jaye, mohabbat wo hai jo khamoshi me nibhayi jaye.🌹** ",
    " 💫**तेरे साथ बिताया हर लम्हा खास है, तू दूर होकर भी मेरे दिल के पास है।**💫 \n\n**🌹Tere saath bitaya har lamha khaas hai, tu door hokar bhi mere dil ke paas hai.🌹** ",
    " 💫**हज़ारों चेहरों में बस तुझे ही ढूँढती हैं निगाहें, तू मिल जाए तो थम जाएँ सारी राहें।**💫 \n\n**🌹Hazaron chehron me bas tujhe hi dhundhti hain nigahein, tu mil jaye to tham jayein saari raahein.🌹** ",
    " 💫**किसी को चाहना गुनाह नहीं, पर तुझे चाहना मेरी इबादत है।**💫 \n\n**🌹Kisi ko chahna gunah nahi, par tujhe chahna meri ibaadat hai.🌹** ",
    " 💫**तेरी हँसी मेरी सबसे प्यारी दवा है, तेरा साथ मेरे लिए सबसे बड़ी दुआ है।**💫 \n\n**🌹Teri hansi meri sabse pyaari dawa hai, tera saath mere liye sabse badi dua hai.🌹** ",
    " 💫**बारिश की बूँदों में भी तेरा अक्स दिखता है, हर खूबसूरत मंज़र में बस तू ही बसता है।**💫 \n\n**🌹Baarish ki boondon me bhi tera aks dikhta hai, har khoobsurat manzar me bas tu hi basta hai.🌹** ",
    " 💫**तुमसे मिलकर जाना कि सुकून क्या होता है, किसी का होकर रहना क्या होता है।**💫 \n\n**🌹Tumse milkar jaana ki sukoon kya hota hai, kisi ka hokar rehna kya hota hai.🌹** ",
    " 💫**लफ़्ज़ों में बयाँ ना हो सके जो, वो एहसास हो तुम, मेरी हर धड़कन के सबसे पास हो तुम।**💫 \n\n**🌹Lafzon me bayaan na ho sake jo, wo ehsaas ho tum, meri har dhadkan ke sabse paas ho tum.🌹** ",
    " 💫**रूठ जाओ तो मनाने का मज़ा आता है, तुम्हें हँसाकर दिल को सुकून आता है।**💫 \n\n**🌹Rooth jao to manane ka maza aata hai, tumhe hansakar dil ko sukoon aata hai.🌹** ",
    " 💫**ज़िंदगी भर का साथ चाहिए, बस तेरे हाथों में मेरा हाथ चाहिए।**💫 \n\n**🌹Zindagi bhar ka saath chahiye, bas tere haathon me mera haath chahiye.🌹** ",
    " 💫**तू जो पास हो तो हर दिन त्योहार है, तेरे बिना हर खुशी बेकार है।**💫 \n\n**🌹Tu jo paas ho to har din tyohaar hai, tere bina har khushi bekaar hai.🌹** ",
    " 💫**सितारों से सजी रात में बस तेरी याद है, तेरे बिना हर बात अधूरी, हर शाम उदास है।**💫 \n\n**🌹Sitaron se saji raat me bas teri yaad hai, tere bina har baat adhuri, har shaam udaas hai.🌹** ",
    " 💫**दोस्ती का रिश्ता भी कितना प्यारा होता है, बिना कहे हर दर्द समझ जाता है।**💫 \n\n**🌹Dosti ka rishta bhi kitna pyaara hota hai, bina kahe har dard samajh jata hai.🌹** ",
    " 💫**तेरे नाम से शुरू और तेरे नाम पर ख़त्म, मेरी हर सुबह, मेरी हर शाम।**💫 \n\n**🌹Tere naam se shuru aur tere naam par khatm, meri har subah, meri har shaam.🌹** ",
    " 💫**इश्क़ की राह में कोई मंज़िल नहीं मिलती, पर तेरे साथ चलने में ही मुझे जन्नत मिलती है।**💫 \n\n**🌹Ishq ki raah me koi manzil nahi milti, par tere saath chalne me hi mujhe jannat milti hai.🌹** ",
    " 💫**तेरी यादों का सिलसिला कभी थमता नहीं, तेरे सिवा कोई और दिल को जमता नहीं।**💫 \n\n**🌹Teri yaadon ka silsila kabhi thamta nahi, tere siva koi aur dil ko jamta nahi.🌹** ",
    " 💫**आँखों में तेरी तस्वीर बसी है, साँसों में तेरी खुशबू रची है।**💫 \n\n**🌹Aankhon me teri tasveer basi hai, saanson me teri khushboo rachi hai.🌹** ",
    " 💫**जब से तू मेरी ज़िंदगी में आया है, हर दिन मुझे हसीन नज़र आया है।**💫 \n\n**🌹Jab se tu meri zindagi me aaya hai, har din mujhe haseen nazar aaya hai.🌹** ",
    " 💫**तेरे बिना जीना अब मुमकिन नहीं, तू है तो ग़म का कोई मौसम नहीं।**💫 \n\n**🌹Tere bina jeena ab mumkin nahi, tu hai to gham ka koi mausam nahi.🌹** ",
    " 💫**हर दुआ में तेरा नाम लिया है, मैंने तुझे खुदा के नाम किया है।**💫 \n\n**🌹Har dua me tera naam liya hai, maine tujhe khuda ke naam kiya hai.🌹** ",
    " 💫**मेरी ख़ामोशी भी तुझसे बातें करती है, हर रात तेरे ख्वाबों में गुज़रती है।**💫 \n\n**🌹Meri khamoshi bhi tujhse baatein karti hai, har raat tere khwabon me guzarti hai.🌹** ",
    " 💫**तेरा नाम लबों पर आते ही मुस्कुरा देता हूँ, तेरी याद आते ही सब कुछ भुला देता हूँ।**💫 \n\n**🌹Tera naam labon par aate hi muskura deta hu, teri yaad aate hi sab kuch bhula deta hu.🌹** ",
    " 💫**इस दिल पर बस तेरा ही राज है, तू ही मेरी धड़कन, तू ही मेरा साज है।**💫 \n\n**🌹Is dil par bas tera hi raaj hai, tu hi meri dhadkan, tu hi mera saaz hai.🌹** ",
    " 💫**वक़्त बदल जाए पर मेरा प्यार ना बदलेगा, तेरे लिए मेरा इंतज़ार ना बदलेगा।**💫 \n\n**🌹Waqt badal jaye par mera pyaar na badlega, tere liye mera intezaar na badlega.🌹** ",
    " 💫**तेरे चेहरे में जो नूर है, वो चाँद में भी कहाँ, तेरी आँखों का जो सुरूर है, वो जाम में भी कहाँ।**💫 \n\n**🌹Tere chehre me jo noor hai, wo chaand me bhi kahan, teri aankhon ka jo suroor hai, wo jaam me bhi kahan.🌹** ",
    " 💫**मुझे मेरी हर खुशी तुझसे जुड़ी लगती है, तेरे बिना हर घड़ी अधूरी लगती है।**💫 \n\n**🌹Mujhe meri har khushi tujhse judi lagti hai, tere bina har ghadi adhuri lagti hai.🌹** ",
    " 💫**तू हँसे तो जहाँ हँस दे, तू रोए तो मेरा दिल भी रो दे।**💫 \n\n**🌹Tu hanse to jahan hans de, tu roye to mera dil bhi ro de.🌹** ",
    " 💫**एक तेरा साथ ही काफ़ी है मेरे लिए, बाकी सारी दुनिया बेमानी है मेरे लिए।**💫 \n\n**🌹Ek tera saath hi kaafi hai mere liye, baaki saari duniya bemaani hai mere liye.🌹** ",
    " 💫**दिल ने तुझे चुना है हज़ारों में, तू ही बसा है मेरी हर बहारों में।**💫 \n\n**🌹Dil ne tujhe chuna hai hazaron me, tu hi basa hai meri har bahaaron me.🌹** ",
    " 💫**तेरी बातों में जादू सा असर है, तेरे बिना हर रास्ता बेखबर है।**💫 \n\n**🌹Teri baaton me jaadu sa asar hai, tere bina har raasta bekhabar hai.🌹** ",
    " 💫**चाय की हर चुस्की में तेरी याद आती है, तेरे साथ की हर शाम बहुत सताती है।**💫 \n\n**🌹Chai ki har chuski me teri yaad aati hai, tere saath ki har shaam bahut satati hai.🌹** ",
    " 💫**तू मेरी दुआओं का वो हसीन असर है, जिसके बिना ये ज़िंदगी एक सफ़र है।**💫 \n\n**🌹Tu meri duaon ka wo haseen asar hai, jiske bina ye zindagi ek safar hai.🌹** ",
    " 💫**प्यार वो नहीं जो मिल जाए, प्यार वो है जो दिल में बस जाए।**💫 \n\n**🌹Pyaar wo nahi jo mil jaye, pyaar wo hai jo dil me bas jaye.🌹** ",
    " 💫**रात के अँधेरे में भी तेरा नूर नज़र आता है, तेरा हर ख्याल मुझे सुकून दे जाता है।**💫 \n\n**🌹Raat ke andhere me bhi tera noor nazar aata hai, tera har khayal mujhe sukoon de jata hai.🌹** ",
    " 💫**तेरे इश्क़ में हम सब कुछ भुला बैठे, तुझे अपनी ज़िंदगी बना बैठे।**💫 \n\n**🌹Tere ishq me hum sab kuch bhula baithe, tujhe apni zindagi bana baithe.🌹** ",
    " 💫**कुछ तो बात है तुझमें जो सबसे जुदा है, तभी तो मेरा दिल तुझ पर फ़िदा है।**💫 \n\n**🌹Kuch to baat hai tujhme jo sabse juda hai, tabhi to mera dil tujh par fida hai.🌹** ",
    " 💫**मेरे हर सवाल का जवाब हो तुम, मेरी हर कहानी का ख़्वाब हो तुम।**💫 \n\n**🌹Mere har sawaal ka jawaab ho tum, meri har kahani ka khwaab ho tum.🌹** ",
    " 💫**तेरी नज़रों ने ऐसा जादू चलाया है, दिल ने बस तुझे ही अपना बनाया है।**💫 \n\n**🌹Teri nazron ne aisa jaadu chalaya hai, dil ne bas tujhe hi apna banaya hai.🌹** ",
    " 💫**साथ तेरा हो तो सफ़र आसान है, वरना ये ज़िंदगी एक इम्तिहान है।**💫 \n\n**🌹Saath tera ho to safar aasaan hai, warna ye zindagi ek imtihaan hai.🌹** ",
    " 💫**तेरी एक हँसी पर मर जाते हैं हम, तेरे हर आँसू पर बिखर जाते हैं हम।**💫 \n\n**🌹Teri ek hansi par mar jaate hain hum, tere har aansoo par bikhar jaate hain hum.🌹** ",
    " 💫**दिल की किताब का हर पन्ना तेरे नाम है, मेरी हर सुबह, हर शाम तेरे नाम है।**💫 \n\n**🌹Dil ki kitaab ka har panna tere naam hai, meri har subah, har shaam tere naam hai.🌹** ",
    " 💫**तू ना मिले तो भी तेरा इंतज़ार रहेगा, मेरे दिल में बस तेरा ही प्यार रहेगा।**💫 \n\n**🌹Tu na mile to bhi tera intezaar rahega, mere dil me bas tera hi pyaar rahega.🌹** ",
    " 💫**फूलों की तरह तू महकती रहे, चाँद की तरह तू चमकती रहे।**💫 \n\n**🌹Phoolon ki tarah tu mehakti rahe, chaand ki tarah tu chamakti rahe.🌹** ",
    " 💫**कभी जो तू रूठे तो मना लूँगा मैं, तुझे अपनी बाँहों में छुपा लूँगा मैं।**💫 \n\n**🌹Kabhi jo tu roothe to mana lunga main, tujhe apni baahon me chhupa lunga main.🌹** ",
    " 💫**मेरी ज़िंदगी की सबसे प्यारी कहानी हो तुम, मेरे दिल की सबसे हसीन निशानी हो तुम।**💫 \n\n**🌹Meri zindagi ki sabse pyaari kahani ho tum, mere dil ki sabse haseen nishaani ho tum.🌹** ",
    " 💫**तारों से पूछा मैंने तेरा पता, चाँद ने कहा वो तो दिल में है बसा।**💫 \n\n**🌹Taaron se poocha maine tera pata, chaand ne kaha wo to dil me hai basa.🌹** ",
    " 💫**तेरे बगैर हर महफ़िल सूनी लगती है, तेरे साथ वीरानी भी जन्नत सी लगती है।**💫 \n\n**🌹Tere bagair har mehfil sooni lagti hai, tere saath veerani bhi jannat si lagti hai.🌹** ",
    " 💫**जो बात तेरी आँखों में है, वो किसी और की बातों में कहाँ।**💫 \n\n**🌹Jo baat teri aankhon me hai, wo kisi aur ki baaton me kahan.🌹** ",
    " 💫**मेरी साँसों की हर डोर तुझसे बंधी है, तू ही मेरी हर दुआ में बसी है।**💫 \n\n**🌹Meri saanson ki har dor tujhse bandhi hai, tu hi meri har dua me basi hai.🌹** ",
    " 💫**आज फिर तेरी याद ने दस्तक दी है, दिल ने फिर तुझसे मिलने की ज़िद की है।**💫 \n\n**🌹Aaj phir teri yaad ne dastak di hai, dil ne phir tujhse milne ki zid ki hai.🌹** ",
    " 💫**इश्क़ में तेरे सब कुछ मंज़ूर है, तू मेरे पास है तो हर ग़म दूर है।**💫 \n\n**🌹Ishq me tere sab kuch manzoor hai, tu mere paas hai to har gham door hai.🌹** ",
    " 💫**सब कहते हैं इश्क़ एक बीमारी है, मैंने कहा तू ही मेरी सबसे प्यारी बीमारी है।**💫 \n\n**🌹Sab kehte hain ishq ek bimaari hai, maine kaha tu hi meri sabse pyaari bimaari hai.🌹** ",
    " 💫**तेरे आने से बहारें आ गईं, मेरी सूनी ज़िंदगी में खुशियाँ छा गईं।**💫 \n\n**🌹Tere aane se bahaarein aa gayi, meri sooni zindagi me khushiyan chha gayi.🌹** ",
    " 💫**मोहब्बत की इस राह में तू मेरा हमसफ़र है, तेरे बिना हर मंज़िल बेअसर है।**💫 \n\n**🌹Mohabbat ki is raah me tu mera humsafar hai, tere bina har manzil beasar hai.🌹** ",
    " 💫**नींद आँखों से दूर और ख्वाब तेरे पास हैं, तेरी हर बात मेरे लिए खास है।**💫 \n\n**🌹Neend aankhon se door aur khwaab tere paas hain, teri har baat mere liye khaas hai.🌹** ",
    " 💫**सारी उम्र तेरे नाम लिख दी, हर सुबह हर शाम तेरे नाम लिख दी।**💫 \n\n**🌹Saari umr tere naam likh di, har subah har shaam tere naam likh di.🌹** ",
    " 💫**प्यार की कोई ज़ुबान नहीं होती, ये तो दिल की दिल से पहचान होती है।**💫 \n\n**🌹Pyaar ki koi zubaan nahi hoti, ye to dil ki dil se pehchaan hoti hai.🌹** ",
    " 💫**तू मेरा ख्वाब, तू ही मेरी हकीकत है, तुझसे ही मेरी हर खुशी की रंगत है।**💫 \n\n**🌹Tu mera khwaab, tu hi meri haqeeqat hai, tujhse hi meri har khushi ki rangat hai.🌹** ",
    " 💫**जब तक साँस है तब तक तेरा साथ चाहिए, हर जनम में बस तेरा हाथ चाहिए।**💫 \n\n**🌹Jab tak saans hai tab tak tera saath chahiye, har janam me bas tera haath chahiye.🌹** ",
    " 💫**तेरी मोहब्बत मेरी सबसे बड़ी दौलत है, तेरा साथ मेरे लिए सबसे बड़ी नेमत है।**💫 \n\n**🌹Teri mohabbat meri sabse badi daulat hai, tera saath mere liye sabse badi nemat hai.🌹** ",
]

# Command


@app.on_message(filters.command(["shayari" ], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply(f"{ke(_KE_WARN,'❗')} <b>ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs</b>")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply(f"{ke(_KE_BLOCK,'⛔')} <b>ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴜsᴇ ᴛʜɪs</b>")

    # Reply karke /shayari likho -> text_on_reply (emoji mention)
    # Sirf /shayari likho       -> text_on_cmd (shayari mention)
    if message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
    else:
        mode = "text_on_cmd"
        msg = message.text
    if chat_id in spam_chats:
        return await message.reply(f"{ke(_KE_WARN,'❗')} <b>ᴘʟᴇᴀsᴇ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴘʀᴏᴄᴇss ғɪʀsᴛ...</b>")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(SHAYRI)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


#

@app.on_message(filters.command(["shstop", "shayarioff"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply(f"{ke(_KE_WARN,'❗')} <b>ᴄᴜʀʀᴇɴᴛʟʏ ɪ'ᴍ ɴᴏᴛ ʀᴜɴɴɪɴɢ</b>")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply(f"{ke(_KE_BLOCK,'⛔')} <b>ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ sᴛᴏᴘ ᴛʜɪs</b>")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply(f"{ke(_KE_OK,'✔️')} {ke(_KE_STAR,'✨')} <b>sʜᴀʏᴀʀɪ ᴘʀᴏᴄᴇss sᴛᴏᴘᴘᴇᴅ!</b>")

