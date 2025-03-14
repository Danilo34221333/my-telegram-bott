from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

TOKEN = "ТВОЙ_ТОКЕН_БОТА"  # Вставь сюда токен из @BotFather

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Создаём клавиатуру
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("🛍 Оформить заказ"))
keyboard.add(KeyboardButton("💬 Связаться с менеджером"))

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("👋 Привет! Добро пожаловать в наш магазин!\nВыберите действие:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "🛍 Оформить заказ")
async def order(message: types.Message):
    await message.answer("✅ Спасибо за заявку! Наш менеджер скоро с вами свяжется. 📞 @mg_rasprodah")

if name == "main":
    executor.start_polling(dp, skip_updates=True)