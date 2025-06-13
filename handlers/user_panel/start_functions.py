from aiogram import  F, types,Router
from aiogram.filters import Command
from keyboard.inline import about_us_inline_keyboard,start_inline_keyboard,return_main_keyboard

start_functions_router = Router()

welcome_message = (
    "👋 Привет! Добро пожаловать в *Okurmen Kids* — IT-академию для детей!\n\n"
    "🚀 У нас ты сможешь:\n"
    "💻 изучать *backend* и *frontend* программирование\n"
    "🌐 улучшать свой *английский язык*\n"
    "🧠 развивать мышление с помощью *методики AEM*\n\n"
    "🎓 Обучение проходит в увлекательной и дружелюбной атмосфере — мы учим через практику и игру!\n\n"
    "👨‍🏫 Готов начать путешествие в мир технологий?\n"
    "Нажми на кнопки ниже и вперёд!"
)
@start_functions_router.message(Command("start"))
async def start(message: types.Message):
    await message.answer_photo(photo=types.FSInputFile("media/logo.jpg"), caption=welcome_message, parse_mode="Markdown",
                               reply_markup=start_inline_keyboard())

@start_functions_router.callback_query(F.data == "start")
async def start_callback(query: types.CallbackQuery):
    await query.message.edit_caption(
                            caption=welcome_message,
                               parse_mode="Markdown",
                               reply_markup=start_inline_keyboard())
about_us_text = (
    "*🚀 OKURMEN KIDS — IT-академия нового поколения!*\n\n"
    "Мы не просто учим — мы вдохновляем детей изучать технологии и развиваться с интересом! 💡\n\n"
    "💻 У нас дети изучают:\n"
    "• *Frontend* и *Backend* разработку (создание сайтов и приложений)\n"
    "• *Английский язык для IT* — говорим и понимаем современные термины\n"
    "• *Методику AEM* — учим логике, креативу и уверенному мышлению\n\n"
    "🎮 И это не просто уроки — это живое обучение!\n"
    "• Играем в *Kahoot* — чтобы закрепить темы\n"
    "• Тренируем скорость на *Monkeytype*\n"
    "• Отдыхаем и развиваемся через *UNO* и другие игры\n\n"
    "🎓 Занятия проходят онлайн и оффлайн. Индивидуальный подход к каждому ребёнку!\n\n"
    "👇 Хочешь узнать больше или записаться на пробный урок?\n"
    "Жми на кнопки ниже и получи консультацию прямо сейчас!"
)

@start_functions_router.message(Command("about_us"))
async def about_us(message: types.Message):
    await message.answer_photo(photo=types.FSInputFile("media/logo.jpg"),
                               caption=about_us_text,
                               parse_mode="Markdown",
                               reply_markup=about_us_inline_keyboard())


@start_functions_router.callback_query(F.data == "about_us")
async def about_us_callback(query: types.CallbackQuery):
    await query.message.edit_caption(
                            caption=about_us_text,
                               parse_mode="Markdown",
                               reply_markup=about_us_inline_keyboard())


groups = (
    """📚 <b>БЛИЖАЙШИЕ КУРСЫ</b>:

🎓 <b>Для взрослых:</b>

🖥 <b>Frontend-разработчик</b>
📅 03.07.25 | 🕔 17:00 и 19:00  
———————————————
💻 <b>Backend-разработчик</b>
📅 27.06.25 | 🕔 17:00 и 19:00  
———————————————
📱 <b>Mobile-разработчик</b>
📅 05.07.25 | 🕖 19:00 – 00:00  
———————————————
🧪 <b>Тестировщик ПО</b>
📅 27.06.25 | 🕖 19:00 – 00:00  
———————————————
💼 <b>1С-программирование</b>
📅 28.06.25 | 🕖 19:00 – 00:00  
———————————————
📢 <b>SMM</b>
📅 02.07.25 | 🕖 19:00 – 00:00  
———————————————
🎨 <b>Graph & Motion Design</b>
📅 12.07.25 | 🕖 19:00  
———————————————
📂 <b>Проектный менеджмент</b>
📅 24.06.25 | 🕖 19:00 – 00:00  
———————————————
💡 <b>Основы программирования (вечер)</b>
📅 17.06.25 | 🕖 19:00  
———————————————

🧒 <b>Для детей:</b>

🎮 <b>Детское программирование (Victory)</b>
📅 09.06.25  
———————————————
👨‍💻 <b>Детский IT-лагерь (7–12 лет)</b>
📅 26.05.25 | 🕚 11:00  
———————————————

🔽 Выберите курс, чтобы узнать подробности."""
)


@start_functions_router.callback_query(F.data == "courses")
async def courses_callback(query: types.CallbackQuery):
    await query.message.edit_caption(caption=groups,
                                     parse_mode="html",
                                     reply_markup=return_main_keyboard())


Okurmen_kids  = (
    """<b>🎓 Окурмен Kids — будущее начинается с детства!</b>

Добро пожаловать в <b>Окурмен Kids</b> — современную IT-академию в Бишкеке, где дети от <b>9 до 15 лет</b> превращаются в уверенных пользователей технологий, начинающих программистов и креативных лидеров нового поколения.

Здесь каждый ребёнок не просто учится — он раскрывает свой потенциал, получает ценные навыки XXI века и находит вдохновение для роста!

<b>🌟 Что ждёт вашего ребёнка?</b>

<b>💻 IT-курсы нового поколения</b>
Обучение программированию, цифровой грамотности и логике с нуля. Увлекательные занятия, реальные проекты и игровая подача — чтобы учиться было интересно!

<b>🧠 Личностное развитие и soft skills</b>
Мотивационные встречи, командные игры, навыки общения и управления временем. Мы формируем уверенных, думающих и самостоятельных ребят.

<b>🌐 Английский язык для будущего</b>
Основы разговорного английского — чтобы уверенно шагать в глобальный цифровой мир.

<b>📜 Официальные сертификаты</b>
По завершении каждого курса — сертификат, подтверждающий полученные знания и успехи.

<b>📚 Обучение на кыргызском языке</b>
С использованием авторской методики <b>Гапыра Мадаминова (AEM)</b>, адаптированной под мышление детей. Даже сложные темы становятся простыми и понятными!

<b>📍 Филиалы в Ленинском районе Бишкека:</b>
🏫 Ул. Табышалиева — академия <b>Окурмен Kids</b>
🏫 Ул. Турусбекова — филиал <b>Окурмэн</b>

<b>⏰ Гибкое расписание</b>
Занятия проходят с 09:00 до 19:00 в уютных, светлых аудиториях.

<b>🎉 Атмосфера, как дома</b>
Тёплая, дружелюбная обстановка, внимание к каждому ребёнку и настоящая команда педагогов.

<b>📸 Хотите заглянуть внутрь академии?</b>
Подпишитесь на наш Instagram — живые фото, видео, отзывы и вдохновляющие истории учеников уже ждут вас!

<b>✨ Окурмен Kids — здесь начинается путь к большим целям.</b>
📩 Запишитесь уже сегодня — и подарите ребёнку уверенное будущее!
"""
)


@start_functions_router.callback_query(F.data == "Okurmen_kids")
async def Okurmen_kids_callback(query: types.CallbackQuery):
    await query.message.edit_caption(caption=Okurmen_kids ,
                                     parse_mode="html",
                                     reply_markup=return_main_keyboard())