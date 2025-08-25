# texts.py fayli
uz = \
"""
<b>
🎓 Pedagog.uz — o‘qituvchilar uchun resurslar platformasi!
Bu yerda siz dars ishlanmalar, metodik tavsiyalar, testlar, qo‘llanmalar va yana ko‘plab kerakli materiallarni topishingiz mumkin.
✔️ Fanlar bo‘yicha cheklanmagan resurslar
✔️ Zamonaviy o‘qituvchilarga mos yondashuv
✔️ Darslarni samarali tashkil qilish uchun qulay imkoniyatlar
Bizda yuzlab ijobiy fikrlar mavjud, lekin siz buni allaqachon eshitgansiz 😉
👇 Boshlash uchun tugmani bosing, shuningdek, kanalda obuna bo‘ling — eng yangi metodik materiallar va aksiyalar birinchi bo‘lib u yerda chiqadi!
</b>
"""

ru = \
"""
<b>
🎓 Pedagog.uz — платформа ресурсов для учителей!
Здесь вы найдёте конспекты уроков, методические рекомендации, тесты, пособия и множество других полезных материалов.
✔️ Неограниченные ресурсы по всем предметам
✔️ Современный подход для преподавателей
✔️ Удобные возможности для эффективной организации уроков
У нас сотни положительных отзывов, но вы, наверное, уже слышали об этом 😉
👇 Нажмите, чтобы начать, а также подпишитесь на канал — самые новые методические материалы и акции появляются там первыми!
</b>
"""

en = \
"""
<b>
🎓 Pedagog.uz — the resource platform for teachers!
Here you can find lesson plans, methodological guides, tests, handbooks, and many other useful materials.
✔️ Unlimited resources for all subjects
✔️ A modern approach for today’s teachers
✔️ Convenient tools to organize lessons effectively
We have hundreds of positive reviews, but you’ve probably already heard about that 😉
👇 Click to start, and don’t forget to subscribe to our channel — the hottest updates and materials always appear there first!
</b>
"""

START = {
    "uz": uz,
    "ru": ru,
    "en": en
}


HELP = \
"""
Pedagog.uz
"""


WEB_BUTTON = {
    "uz": "📚 Platformaga o‘tish",
    "ru": "📚 Перейти на платформу",
    "en": "📚 Go to the platform",
}

CHANNEL = {
    "uz": "🔔 Kanalga obuna bo‘lish",
    "ru": "🔔 Подписаться на канал",
    "en": "🔔 Subscribe to the channel",
}



COMPETITION = {
    "uz": "🏆 Siz <b>Konkurs</b> bo'limiga kirdingiz! 🎉 Omad tilaymiz!",
    "ru": "🏆 Вы вошли в раздел <b>Конкурс</b>! 🎉 Желаем удачи!",
    "en": "🏆 You have entered the <b>Competition</b> section! 🎉 Good luck!"
}


ref_phone_uz = "📱 Iltimos, pedagog.uz platformasida ro‘yxatdan o‘tgan telefon raqamingizni yuboring. \n\n📌 Format: +998 ** ** *** ** **"
ref_phone_ru = "📱 Пожалуйста, отправьте номер телефона, зарегистрированный на платформе pedagog.uz. \n\n📌 Формат: +998 ** ** *** ** **"
ref_phone_en = "📱 Please send the phone number registered on the pedagog.uz platform. \n\n📌 Format: +998 ** ** *** ** **"

REF_PHONE = {
    "uz": ref_phone_uz,
    "ru": ref_phone_ru,
    "en": ref_phone_en,
}




REF_PHONE_ACCEPTED = {
    "uz": "✅ Telefon raqamingiz qabul qilindi: {phone}",
    "ru": "✅ Ваш номер телефона принят: {phone}",
    "en": "✅ Your phone number has been accepted: {phone}",
}

REF_PHONE_INVALID = {
    "uz": "❌ Telefon raqami noto‘g‘ri. Faqat raqam yuboring va uzunligi kamida 9 ta bo‘lishi kerak.",
    "ru": "❌ Неверный номер. Отправьте только цифры, не менее 9 символов.",
    "en": "❌ Invalid number. Send only digits with at least 9 characters.",
}

REF_PHONE_ERROR = {
    "uz": "❌ Telefon raqamini yuborishda xatolik yuz berdi.",
    "ru": "❌ Произошла ошибка при отправке номера телефона.",
    "en": "❌ An error occurred while sending the phone number.",
}

REF_PHONE_NOT_FOUND = {
    "uz": "❌ Siz oldin Pedagog.uz’da ro‘yxatdan o‘tmagansiz. Iltimos, @pedagog_uzbot orqali ro‘yxatdan o‘ting.",
    "ru": "❌ Вы ещё не зарегистрированы на Pedagog.uz. Пожалуйста, зарегистрируйтесь через @pedagog_uzbot.",
    "en": "❌ You have not registered on Pedagog.uz yet. Please register via @pedagog_uzbot."
}





REF_COUNT = {
    "uz": "📊 Sizning takliflaringiz soni: <b>{count}</b> ta ✅",
    "ru": "📊 Количество ваших приглашений: <b>{count}</b> ✅",
    "en": "📊 Your total referrals: <b>{count}</b> ✅"
}


TOP_LIST_HEADER = {
    "uz": "🏆 Referallar bo‘yicha TOP ro‘yxat:",
    "ru": "🏆 ТОП пользователей по рефералам:",
    "en": "🏆 Top users by referrals:",
}

GIFTS = {
    "uz": (
        "⚡️ \"Bilimdon Ustoz\" tanlovida qatnashib Planshet yutishingizga atigi 3 kun qoldi!\n\n"
        "“Kreativ Pedagog” jamoasi tomonidan tashkil etilayotgan “Bilimdon Ustoz” tanlovi boshlanishiga juda oz vaqt qoldi! "
        "Bu siz uchun bilim va faollikni sinovdan o‘tkazish, ayni vaqtda qimmatbaho sovg‘alarni qo‘lga kiritish imkoniyatidir. "
        "Ishonamizki, siz ham bu ajoyib tanlovda ishtirok etasiz!\n\n"
        "📌 Tanlov qanday o‘tadi?\n\n"
        "1️⃣ <a href=\"{ref_link}\">https://t.me/Pedagog_uzbot</a> orqali ro‘yxatdan o‘tasiz – ism, familiya va telefon raqamingizni tasdiqlaysiz;\n"
        "2️⃣ Botda “Do‘stlarni taklif qilish” tugmasi orqali referal havola olasiz va uni hamkasblaringizga yuborasiz;\n"
        "3️⃣ Har bir taklifingiz uchun ball to‘planadi – kamida 5 ta referal to‘plaganlar 30-iyuldagi test sinovida qatnashadi;\n"
        "4️⃣ Testda eng yuqori ball va eng qisqa vaqt ko‘rsatgan TOP 10 ustoz g‘olib bo‘ladi;\n"
        "5️⃣ Testda qatnashgan faollarga esa SERTIFIKAT taqdim etiladi!\n\n"
        "🎁 Sovg‘alar ro‘yxati:\n\n"
        "🏆 Test g‘oliblari uchun:\n"
        "🔹 1-o‘rin – Zamonaviy Planshet\n"
        "🔹 2-o‘rin – 10 ta top kitoblar to‘plami\n"
        "🔹 3-o‘rin – Milliy sertifikat uchun to‘lov\n"
        "🔹 4–6-o‘rin – AirPods quloqchinlari\n"
        "🔹 7–10-o‘rin – Qimmatbaho blaknot va ruchka to‘plami\n\n"
        "💥 Eng ko‘p referal to‘plagan 20 nafar ishtirokchi uchun alohida mukofotlar:\n"
        "🥇 1-o‘rin – 400 000 so‘m\n"
        "🥈 2-o‘rin – 300 000 so‘m\n"
        "🥉 3-o‘rin – 200 000 so‘m\n"
        "🏅 4–10-o‘rinlar – 100 000 so‘m\n"
        "🎓 11–20-o‘rinlar – “Kreativ Pedagog” kursida bepul o‘qish imkoniyati!\n\n"
        "⌛ Shoshiling! Faqat 3 kun qoldi. Referal havolangizni do‘stlaringizga tarqating, bilimni sinovdan o‘tkazing va sovrinlarni qo‘lga kiriting!\n\n"
        "👉 Ro‘yxatdan o‘tish: <a href=\"{ref_link}\">https://t.me/Pedagog_uzbot</a>\n\n"
        "✔️ @pedagoglaru - Kreativ ustozlar kanali!"
    ),
    "ru": (
        "⚡️ Осталось всего 3 дня, чтобы принять участие в конкурсе «Bilimdon Ustoz» и выиграть планшет!\n\n"
        "Команда «Kreativ Pedagog» проводит конкурс «Bilimdon Ustoz»! "
        "Это отличная возможность проверить свои знания, проявить активность и получить ценные призы. "
        "Мы уверены, что вы тоже станете участником этого замечательного конкурса!\n\n"
        "📌 Как проходит конкурс?\n\n"
        "1️⃣ Зарегистрируйтесь через <a href=\"{ref_link}\">https://t.me/Pedagog_uzbot</a> – подтвердите имя, фамилию и номер телефона;\n"
        "2️⃣ В боте нажмите кнопку «Пригласить друзей», получите реферальную ссылку и поделитесь ею с коллегами;\n"
        "3️⃣ За каждое приглашение вы получаете баллы – участники с 5 и более рефералами смогут пройти тест 30 июля;\n"
        "4️⃣ ТОП-10 участников с лучшими результатами теста станут победителями;\n"
        "5️⃣ Все активные участники получат СЕРТИФИКАТЫ!\n\n"
        "🎁 Призы:\n\n"
        "🏆 Для победителей теста:\n"
        "🔹 1-е место – Современный планшет\n"
        "🔹 2-е место – Набор из 10 лучших книг\n"
        "🔹 3-е место – Оплата за Национальный сертификат\n"
        "🔹 4–6-е места – Наушники AirPods\n"
        "🔹 7–10-е места – Дорогой блокнот и ручка\n\n"
        "💥 Для 20 участников с наибольшим числом рефералов:\n"
        "🥇 1-е место – 400 000 сум\n"
        "🥈 2-е место – 300 000 сум\n"
        "🥉 3-е место – 200 000 сум\n"
        "🏅 4–10-е места – 100 000 сум\n"
        "🎓 11–20-е места – Бесплатное обучение на курсе «Kreativ Pedagog»!\n\n"
        "⌛ Поторопитесь! Осталось всего 3 дня. Делитесь ссылкой с друзьями, проявляйте активность и выигрывайте призы!\n\n"
        "👉 Регистрация: <a href=\"{ref_link}\">https://t.me/Pedagog_uzbot</a>\n\n"
        "✔️ @pedagoglaru - Канал креативных педагогов!"
    ),
    "en": (
        "⚡️ Only 3 days left to join the “Bilimdon Ustoz” contest and win a tablet!\n\n"
        "The “Kreativ Pedagog” team is launching the “Bilimdon Ustoz” contest! "
        "This is your chance to test your knowledge, show your activity, and win valuable prizes. "
        "We believe you will also take part in this amazing competition!\n\n"
        "📌 How the contest works:\n\n"
        "1️⃣ Register via <a href=\"{ref_link}\">https://t.me/Pedagog_uzbot</a> – confirm your name, surname, and phone number;\n"
        "2️⃣ In the bot, click “Invite Friends” to get your referral link and share it with your colleagues;\n"
        "3️⃣ For each invitation, you earn points – those with at least 5 referrals can join the test on July 30;\n"
        "4️⃣ The TOP-10 participants with the highest scores and fastest time will be declared winners;\n"
        "5️⃣ All active participants will receive a CERTIFICATE!\n\n"
        "🎁 Prizes:\n\n"
        "🏆 For test winners:\n"
        "🔹 1st place – Modern tablet\n"
        "🔹 2nd place – A set of 10 top books\n"
        "🔹 3rd place – National Certificate fee covered\n"
        "🔹 4th–6th places – AirPods\n"
        "🔹 7th–10th places – Premium notebook and pen set\n\n"
        "💥 For the top 20 participants with the most referrals:\n"
        "🥇 1st place – 400,000 UZS\n"
        "🥈 2nd place – 300,000 UZS\n"
        "🥉 3rd place – 200,000 UZS\n"
        "🏅 4th–10th places – 100,000 UZS\n"
        "🎓 11th–20th places – Free training in the “Kreativ Pedagog” course!\n\n"
        "⌛ Hurry up! Only 3 days left. Share your referral link, test your knowledge, and win valuable prizes!\n\n"
        "👉 Register now: <a href=\"{ref_link}\">https://t.me/Pedagog_uzbot</a>\n\n"
        "✔️ @pedagoglaru - The channel for creative teachers!"
    ),
}

REF_LINK = {
    "uz": (
        "⚡️ \"Eng yaxshi pedagog\" tanlovi boshlandi!\n\n"
        "Pedagoglar uchun bilim va faollikni oshirish maqsadida yutuqli tanlovga start berildi. "
        "G‘oliblar Pedagogik mahorat testidan o‘tish orqali aniqlanadi. Referal yig‘ing va test ishlang – sovrinlarni qo‘lga kiriting! "
        "Tanlov 10-sentyabrgacha davom etadi.\n\n"
        "🎁 Tanlov g‘oliblari quyidagicha taqdirlanadi:\n"
        "🔹 1-o‘rin – Planshet (zamonaviy o‘qituvchi ish quroli)\n"
        "🔹 2-o‘rin – 5 ta top kitoblar to‘plami\n"
        "🔹 3-o‘rin – Milliy sertifikat to‘lovini qoplab beramiz\n\n"
        "🤩 Eng ko‘p referal to‘plagan 20 nafar ishtirokchi:\n"
        "🔸 1-o‘rin – 300 000 so‘m\n"
        "🔸 2-o‘rin – 200 000 so‘m\n"
        "🔸 3-o‘rin – 100 000 so‘m\n"
        "🔸 4–10-o‘rinlar – 50 000 so‘m\n"
        "🔸 11–20-o‘rinlar – “pedagog.uz” platformasidan 1-chorak davomida resurslardan tekin foydalanish imkoniyati\n\n"
        "❗️ Tanlovda qatnashgan barcha ishtirokchilarga SERTIFIKAT beriladi!\n\n"
        "Tanlovda ishtirok etish👇\n"
        "<a href=\"{ref_link}\">https://t.me/Pedagog_uzbot</a>\n"
        "<a href=\"{ref_link}\">https://t.me/Pedagog_uzbot</a>"
    ),
    "ru": (
        "⚡️ Конкурс «Лучший педагог» стартовал!\n\n"
        "Для педагогов начался конкурс с призами, чтобы повысить знания и активность. "
        "Победители определяются по результатам теста педагогического мастерства. "
        "Собирайте рефералов, проходите тест и выигрывайте призы! "
        "Конкурс продлится до 10 сентября.\n\n"
        "🎁 Призы для победителей:\n"
        "🔹 1-е место – Планшет (современный инструмент преподавателя)\n"
        "🔹 2-е место – Набор из 5 лучших книг\n"
        "🔹 3-е место – Оплата Национального сертификата\n\n"
        "🤩 Для 20 участников с наибольшим количеством рефералов:\n"
        "🔸 1-е место – 300 000 сум\n"
        "🔸 2-е место – 200 000 сум\n"
        "🔸 3-е место – 100 000 сум\n"
        "🔸 4–10 места – 50 000 сум\n"
        "🔸 11–20 места – Бесплатный доступ к ресурсам платформы «pedagog.uz» на 1 квартал\n\n"
        "❗️ Все участники конкурса получат СЕРТИФИКАТ!\n\n"
        "Участвуйте в конкурсе👇\n"
        "<a href=\"{ref_link}\">https://t.me/Pedagog_uzbot</a>\n"
        "<a href=\"{ref_link}\">https://t.me/Pedagog_uzbot</a>"
    ),
    "en": (
        "⚡️ The “Best Teacher” contest has started!\n\n"
        "A rewarding contest has begun to help teachers enhance their knowledge and activity. "
        "Winners will be determined by passing the Pedagogical Mastery Test. "
        "Gather referrals, complete the test, and win prizes! "
        "The contest runs until September 10.\n\n"
        "🎁 Prizes for the winners:\n"
        "🔹 1st place – Tablet (a modern teaching tool)\n"
        "🔹 2nd place – A set of 5 top books\n"
        "🔹 3rd place – We cover the National Certificate fee\n\n"
        "🤩 For the top 20 participants with the most referrals:\n"
        "🔸 1st place – 300,000 UZS\n"
        "🔸 2nd place – 200,000 UZS\n"
        "🔸 3rd place – 100,000 UZS\n"
        "🔸 4th–10th places – 50,000 UZS\n"
        "🔸 11th–20th places – Free access to resources on “pedagog.uz” platform for one quarter\n\n"
        "❗️ All participants will receive a CERTIFICATE!\n\n"
        "Join the contest👇\n"
        "<a href=\"{ref_link}\">https://t.me/Pedagog_uzbot</a>\n"
        "<a href=\"{ref_link}\">https://t.me/Pedagog_uzbot</a>"
    ),
}
