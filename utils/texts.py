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


REF_LINK = {
    "uz": "Quyidagi havolani do‘stlaringiz bilan ulashing va bonusga ega bo‘ling!\n\n<code>{}</code>",
    "ru": "Поделитесь этой ссылкой с друзьями и получите бонус!\n\n<code>{}</code>",
    "en": "Share this link with your friends and earn a bonus!\n\n<code>{}</code>",
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
        "<b>🎁 TOP REFERENTLAR UCHUN SOVG'ALAR</b>\n"
        "<i>Pedagog.uz referral tanlovi</i>\n\n"
        "🥇 <b>1-o‘rin:</b> Qora <u>Cobalt</u> avtomobili 🚗\n"
        "🥈 <b>2-o‘rin:</b> <u>Matiz</u> avtomobili 🚘\n"
        "🥉 <b>3-o‘rin:</b> <u>iPhone 15</u> 📱\n\n"
        "<b>Qanday ishtirok etiladi?</b>\n"
        "• O‘z <b>referal havolangizni</b> do‘stlaringiz bilan ulashing.\n"
        "• Do‘stlaringiz havola orqali ro‘yxatdan o‘tsa — sizga <b>referral</b> yoziladi.\n"
        "• Eng ko‘p taklif qilgan 3 nafar ishtirokchi g‘olib bo‘ladi.\n\n"
        "<b>Qoida va shartlar</b>\n"
        "• Har bir taklif <i>faqat real va faol</i> ro‘yxatdan o‘tish bo‘lishi shart.\n"
        "• Dublikat yoki nomaqbul hisoblar <u>bekor qilinadi</u>.\n"
        "• Tadbir yakunida natijalar e’lon qilinadi.\n\n"
        "<b>Muddatlar:</b> Start — <i>e’lon qilingan sana</i>, Yakun — <i>e’lon qilingan sana</i>.\n"
        "<b>Omad!</b> Bugunoq havolangizni ulashishni boshlang! ✨"
    ),

    "en": (
        "<b>🎁 GIFTS FOR TOP REFERRERS</b>\n"
        "<i>Pedagog.uz referral challenge</i>\n\n"
        "🥇 <b>1st Place:</b> Black <u>Cobalt</u> Car 🚗\n"
        "🥈 <b>2nd Place:</b> <u>Matiz</u> Car 🚘\n"
        "🥉 <b>3rd Place:</b> <u>iPhone 15</u> 📱\n\n"
        "<b>How to participate?</b>\n"
        "• Share your <b>referral link</b> with friends.\n"
        "• When friends register via your link, you gain a <b>referral</b>.\n"
        "• Top 3 users with the highest referrals win.\n\n"
        "<b>Rules & Terms</b>\n"
        "• Each referral must be a <i>real and active</i> registration.\n"
        "• Duplicate or invalid accounts will be <u>voided</u>.\n"
        "• Results will be announced after the campaign ends.\n\n"
        "<b>Timeline:</b> Start — <i>to be announced</i>, End — <i>to be announced</i>.\n"
        "<b>Good luck!</b> Start sharing your link today! ✨"
    ),

    "ru": (
        "<b>🎁 ПОДАРКИ ДЛЯ ЛУЧШИХ РЕФЕРАЛОВ</b>\n"
        "<i>Реферальный челлендж Pedagog.uz</i>\n\n"
        "🥇 <b>1-е место:</b> Чёрный <u>Cobalt</u> 🚗\n"
        "🥈 <b>2-е место:</b> <u>Matiz</u> 🚘\n"
        "🥉 <b>3-е место:</b> <u>iPhone 15</u> 📱\n\n"
        "<b>Как участвовать?</b>\n"
        "• Делитесь своей <b>реферальной ссылкой</b> с друзьями.\n"
        "• Если друзья регистрируются по вашей ссылке — вы получаете <b>реферал</b>.\n"
        "• Побеждают 3 пользователя с наибольшим числом рефералов.\n\n"
        "<b>Правила и условия</b>\n"
        "• Каждый реферал — это <i>реальная и активная</i> регистрация.\n"
        "• Дубликаты и недействительные аккаунты будут <u>аннулированы</u>.\n"
        "• Итоги объявим по завершении кампании.\n\n"
        "<b>Сроки:</b> Старт — <i>будет объявлено</i>, Завершение — <i>будет объявлено</i>.\n"
        "<b>Удачи!</b> Начните делиться ссылкой уже сегодня! ✨"
    ),
}
