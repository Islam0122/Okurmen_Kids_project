from aiogram import  F, types,Router
from aiogram.filters import Command

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
    await message.answer_photo(photo=types.FSInputFile("media/logo.jpg"), caption=welcome_message, parse_mode="Markdown")

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
                               caption=about_us_text, parse_mode="Markdown")
