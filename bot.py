from aiogram import Bot, Dispatcher
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
import asyncio
from baza import *
import os
from datetime import datetime

print("Testlart //////////////////////////////////")
print("Python>>>>>>>>>>>>>", Python)
print("C++>>>>>>>>>>>>>", C_plus)
print("C#>>>>>>>>>>>>>", C_sharp)

print("////////////////////////////////////////////")
# Bot tokeni
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

# Bot va Dispatcher obyektlarini yaratish
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Global o'zgaruvchilar
soni = 0
tanlangan_javoblar = []
current_test = None  # Boshlang'ich test nomi
test_data = []  # Tanlangan testni saqlash uchun ro'yxat
azoligi = False
test_count = 0
Foydalanuvchi = []
t_javob = 0


@dp.message(Command(commands=["start"]))
async def Kanalga_qoshish(message: Message):
    response = ("Botdan foydalanish uchun oldin quyidagi kanalga a'zo bo'lishingiz kerak.\n\n")
    kanal_button = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Kanal havolasi', url=f"https://t.me/{CHANNEL_ID}")],
        [InlineKeyboardButton(text="A'zolikni Tekshirish", callback_data="kanalga_azoligi")]
    ])

    await message.answer(response, reply_markup=kanal_button)


@dp.callback_query(lambda c: c.data == "kanalga_azoligi")
async def check_membership(callback_query: CallbackQuery):
    global azoligi
    user_id = callback_query.from_user.id
    try:
        kanalga_qoshilganligi = await bot.get_chat_member("@daston_sultonov", user_id)
        if kanalga_qoshilganligi.status in ["member", "administrator", "creator"]:
            azoligi = True
            keyboard = ReplyKeyboardMarkup(
                keyboard=[
                    [KeyboardButton(text="\U0001F40D Python"),
                     KeyboardButton(text="\U0001F4BB JavaScript"),
                     KeyboardButton(text="\U0001F4BC Java")],
                    [KeyboardButton(text="\U0001F4BB C++"), KeyboardButton(text="\U0001F537 C#"),
                     KeyboardButton(text="\U0001F4BC GO")],
                    [KeyboardButton(text="\U0001F4D8 TypeScript"), KeyboardButton(text="\U0001F4D3 Kotlin"),
                     KeyboardButton(text="\U0001F4D6 PHP")],
                    [KeyboardButton(text="\U0001F4C3 Bot haqida ma'lumot")]
                ],
                resize_keyboard=True,
                one_time_keyboard=True
            )

            response = f"Assalomu alaykum {callback_query.message.from_user.first_name}\n\n! Botga xush kelibsiz! O'zingiz bilgan dasturlash tilini tanlang. "
            await callback_query.message.answer(response, reply_markup=keyboard)
            # ismi = callback_query.from_user.first_name
            # familiasi = callback_query.from_user.last_name
            # username = callback_query.from_user.username
            # azo_bolgan_vaqti = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            #
            # Foydalanuvchi.append(
            #     f"ismi: {ismi}\nfamiliasi: {familiasi}\nusername: {username}\nazo_bolgan_vaqti: {azo_bolgan_vaqti}")
            #
            # print(Foydalanuvchi)
        else:
            await callback_query.answer("Siz kanalga a'zo bo'lmagansiz. Iltimos, quyidagi kanalga a'zo bo'ling.")
    except Exception as e:
        await callback_query.answer(
            f"Xatolik yuz berdi: {str(e)}. Iltimos, bir necha daqiqadan keyin qayta urinib ko'ring.")


@dp.message(Command(commands=["test"]))
async def test_command(message: Message):
    global azoligi
    if azoligi == True:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="\U0001F40D Python"),
                 KeyboardButton(text="\U0001F4BB JavaScript"),
                 KeyboardButton(text="\U0001F4BC Java")],
                [KeyboardButton(text="\U0001F4BB C++"), KeyboardButton(text="\U0001F537 C#"),
                 KeyboardButton(text="\U0001F4BC GO")],
                [KeyboardButton(text="\U0001F4D8 TypeScript"), KeyboardButton(text="\U0001F4D3 Kotlin"),
                 KeyboardButton(text="\U0001F4D6 PHP")],
                [KeyboardButton(text="\U0001F4C3 Bot haqida ma'lumot")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
        response = f"Assalomu alaykum {message.from_user.first_name}! Botimizga xush kelibsiz! Quyidagi menyudan tanlang:"
        await message.answer(response, reply_markup=keyboard)
    else:
        response = "Siz kanalga a'zo bo'lmagansiz. Iltimos, kanalga qo'shiling va qaytadan sinab ko'ring."
        kanal_button = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Kanal havolasi', url=f"https://t.me/{CHANNEL_ID}")],
            [InlineKeyboardButton(text="A'zolikni Tekshirish", callback_data="kanalga_azoligi")]
        ])
        await message.answer(response, reply_markup=kanal_button)


@dp.message()
async def choose_test_type(message: Message):
    global current_test, soni, test_data, t_javob
    soni = 0  # Har bir yangi test boshlanganda savollarni boshidan boshlash

    if azoligi == True:
        if message.text in ["\U0001F40D Python", "\U0001F4BB JavaScript", "\U0001F4BC Java", "\U0001F4BB C++",
                            "\U0001F537 C#", "\U0001F4BC GO", "\U0001F4D8 TypeScript", "\U0001F4D3 Kotlin",
                            "\U0001F4D6 PHP"]:

            current_test = None
            if message.text == "\U0001F40D Python":
                current_test = "python"
            elif message.text == "\U0001F4BB JavaScript":
                current_test = "java_script"
            elif message.text == "\U0001F4BC Java":
                current_test = "java"
            elif message.text == "\U0001F4BB C++":
                current_test = "c_plyus"
            elif message.text == "\U0001F537 C#":
                current_test = "c_sharp"
            elif message.text == "\U0001F4BC GO":
                current_test = "go"
            elif message.text == "\U0001F4D8 TypeScript":
                current_test = "typescript"
            elif message.text == "\U0001F4D3 Kotlin":
                current_test = "kotlin"
            elif message.text == "\U0001F4D6 PHP":
                current_test = "php"
            soni = 0
            tanlangan_javoblar.clear()
            # Test sonini tanlash
            test_count_keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="10 ta test", callback_data="10_tests")],
                [InlineKeyboardButton(text="20 ta test", callback_data="20_tests")],
                [InlineKeyboardButton(text="30 ta test", callback_data="30_tests")]
            ])
            await message.answer(f"{message.from_user.first_name} dasturlash tilidagi testlar sonini tanlang:",
                                 reply_markup=test_count_keyboard)
        elif message.text == "\U0001F4C3 Bot haqida ma'lumot":
            await info(message)
        else:
            await message.answer("Tanlangan dasturlash tilini tanlashda xatolik yuz berdi. Iltimos, qayta tanlang.")

    else:
        response = "Siz kanalga a'zo bo'lmagansiz. Iltimos, kanalga qo'shiling va qaytadan sinab ko'ring."
        kanal_button = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Kanal havolasi', url=f"https://t.me/{CHANNEL_ID}")],
            [InlineKeyboardButton(text="A'zolikni Tekshirish", callback_data="kanalga_azoligi")]
        ])
        await message.answer(response, reply_markup=kanal_button)


@dp.callback_query(lambda c: c.data in ["10_tests", "20_tests", "30_tests"])
async def choose_test_count(callback_query: CallbackQuery):
    global current_test, test_data, test_count, soni
    test_count = 10  # Default test soni
    if callback_query.data == "20_tests":
        test_count = 20
    elif callback_query.data == "30_tests":
        test_count = 30

    # Testlarni tanlash
    if current_test == "python":
        test_data = Python[:test_count]  # Tanlangan test soni bo'yicha testlarni kesib olish
    elif current_test == "C_plyus":
        test_data = C_plus[:test_count]
    elif current_test == "C_sharp":
        test_data = C_sharp[:test_count]
    elif current_test == "java_script":
        test_data = JavaScript[:test_count]
    elif current_test == "java":
        test_data = Java[:test_count]
    elif current_test == "type_script":
        test_data = TypeScript[:test_count]
    elif current_test == "golang":
        test_data = Golang[:test_count]
    elif current_test == "kotlin":
        test_data = Kotlin[:test_count]
    elif current_test == "php":
        test_data = PHP[:test_count]
    soni = 0
    print(test_data)
    row = test_data[soni]
    savol = f"{soni + 1}. {row[1]}"

    # Javob variantlari uchun tugmalar yaratish
    keyboard = InlineKeyboardBuilder()

    # Matnni qisqartirish (agar matn 30 ta belgidan uzun bo'lsa, "..." qo'shiladi)
    option_a = row[2] if len(row[2]) <= 30 else row[2][:30] + "..."
    option_b = row[3] if len(row[3]) <= 30 else row[3][:30] + "..."
    option_c = row[4] if len(row[4]) <= 30 else row[4][:30] + "..."

    # Tugmalarni qo'shish (HTML formatlash yordamida)
    keyboard.button(text=f"<b>{option_a}</b>", callback_data='option_a', parse_mode="HTML")
    keyboard.button(text=f"<b>{option_b}</b>", callback_data='option_b', parse_mode="HTML")
    keyboard.button(text=f"<b>{option_c}</b>", callback_data='option_c', parse_mode="HTML")

    # Tugmalarni tartibga solish
    keyboard.adjust(1)  # Tugmalarni bir qatorda joylashtirish

    # Savolni va tugmalarni yuborish
    await callback_query.message.answer(savol, reply_markup=keyboard.as_markup())


@dp.callback_query(lambda c: c.data in ["option_a", "option_b", "option_c"])
async def javoblarni_olish(callback_query: CallbackQuery):
    global soni, current_test, tanlangan_javoblar, test_data

    # Test tugaganini tekshirish
    if soni >= len(test_data):
        await callback_query.answer("Test tugadi. Iltimos, yakunlash tugmasini bosing.")
        return

    # Javobni tanlash
    if callback_query.data == "option_a":
        tanlangan_javoblar.append("a")
    elif callback_query.data == "option_b":
        tanlangan_javoblar.append("b")
    elif callback_query.data == "option_c":
        tanlangan_javoblar.append("c")

    # Savolni keyingisi bilan yangilash
    soni += 1

    if soni < len(test_data):  # Savol soni test uzunligidan oshmasligi kerak
        row = test_data[soni]
        savol = f"{soni + 1}. {row[1]}"

        keyboard = InlineKeyboardBuilder()
        keyboard.button(text=row[2], callback_data='option_a')
        keyboard.button(text=row[3], callback_data='option_b')
        keyboard.button(text=row[4], callback_data='option_c')
        keyboard.adjust(1)

        await callback_query.message.edit_text(savol, reply_markup=keyboard.as_markup())
    else:
        # Test yakunlanganda natija chiqarish

        finish_keyboard = InlineKeyboardBuilder()
        finish_keyboard.button(text="Testni yakunlash", callback_data="testni_yakunlash")
        finish_keyboard.adjust(1)
        await callback_query.message.edit_text("Test tugadi. Yakunlash tugmasini bosing.",
                                               reply_markup=finish_keyboard.as_markup())


@dp.callback_query(lambda c: c.data == "testni_yakunlash")
async def testni_yakunlash(callback_query: CallbackQuery):
    global soni, current_test, tanlangan_javoblar, test_data, test_count, t_javob

    # Testning to'g'ri javoblari
    if current_test == "python":
        togri_javoblar = Togri_javoblar_Python[:test_count]
    elif current_test == "C_plyus":
        togri_javoblar = Togri_javoblar_C_plus[:test_count]
    elif current_test == "C_sharp":
        togri_javoblar = Togri_javoblar_C_sharp[:test_count]
    elif current_test == "java_script":
        togri_javoblar = Togri_javoblar_JavaScript[:test_count]
    elif current_test == "java":
        togri_javoblar = Togri_javoblar_Java[:test_count]
    elif current_test == "type_script":
        togri_javoblar = Togri_javoblar_TypeScript[:test_count]
    elif current_test == "golang":
        togri_javoblar = Togri_javoblar_Golang[:test_count]
    elif current_test == "kotlin":
        togri_javoblar = Togri_javoblar_Kotlin[:test_count]
    elif current_test == "php":
        togri_javoblar = Togri_javoblar_PHP[:test_count]
    else:
        await   callback_query.message.answer("Bu test bo'yicha ma'lumot topilmadi.")
        return

    # Ro'yxatlar uzunligini tekshirish
    if len(tanlangan_javoblar) != len(togri_javoblar):
        await callback_query.message.answer(
            "Xatolik yuz berdi: javoblar soni to'g'ri kelmayapti. Iltimos, testni qaytadan boshlang.")
        return

    # Natijani hisoblash
    natija = []
    for i in range(len(togri_javoblar)):
        if tanlangan_javoblar[i] == togri_javoblar[i]:
            natija.append(f"{i + 1}-savol: ✅ To'g'ri javob")
            t_javob += 1
        else:
            natija.append(f"{i + 1}-savol: ❌ Notog'ri javob. To'g'ri javob: {togri_javoblar[i]}")

    # Natijani chiqarish
    response = (f"Test yakunlandi. {callback_query.from_user.first_name}\n {test_count} ta testdan natijangiz:\n\n"
                "Quyidagi natijalar:\n\n"
                f"{'\n\n'.join(natija)}\n\n"
                f"✅ {t_javob} ta testga to'g'ri javob berdingiz. 👍\n\n"
                f"❌ {test_count - t_javob} ta testga notog'ri javob berdingiz. 😒\n\n"
                )

    finish_keyboard = InlineKeyboardBuilder()
    finish_keyboard.button(text="Testni qaytadan boshlash", callback_data="testni_qayta_yuklash")
    finish_keyboard.adjust(1)
    await callback_query.message.answer(response, reply_markup=finish_keyboard.as_markup())
    soni = 0
    tanlangan_javoblar.clear()
    t_javob = 0


@dp.callback_query(lambda d: d.data == "testni_qayta_yuklash")
async def test_qaytadan(callback_query: CallbackQuery):
    if callback_query.data == "testni_qayta_yuklash":
        # Inline tugmalarni yaratish
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="\U0001F40D Python"),
                 KeyboardButton(text="\U0001F4BB JavaScript"),
                 KeyboardButton(text="\U0001F4BC Java")],
                [KeyboardButton(text="\U0001F4BB C++"), KeyboardButton(text="\U0001F537 C#"),
                 KeyboardButton(text="\U0001F4BC GO")],
                [KeyboardButton(text="\U0001F4D8 TypeScript"), KeyboardButton(text="\U0001F4D3 Kotlin"),
                 KeyboardButton(text="\U0001F4D6 PHP")],
                [KeyboardButton(text="\U0001F4C3 Bot haqida ma'lumot")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )

        # Javobni yuborish
        response = f"Assalomu alaykum {callback_query.from_user.first_name}! Botimizga xush kelibsiz! Quyidagi menyudan tanlang:"
        await callback_query.message.answer(response, reply_markup=keyboard)

        # Testni qayta yuklash va o'zgaruvchilarni tozalash
        # Masalan, `tanlangan_javoblar` yoki boshqa global o'zgaruvchilarni tozalash
        global soni, tanlangan_javoblar, current_test
        soni = 0
        tanlangan_javoblar.clear()
        current_test = None  # Yoki kerakli boshqa o'zgaruvchini tozalash


@dp.message(Command("info"))
async def info(message: Message):
    info_message = """
    👋 **Salom!** Bizning dasturlash tilari bo'yicha test botimizga xush kelibsiz! 🎉

    💻 **Nima qilish mumkin?**
    - Python, Java, C++, JavaScript va boshqa ko'plab dasturlash tillarida testlar yechishingiz mumkin.
    - Har bir til bo'yicha maxsus testlar mavjud, ularda o'z bilimlaringizni sinab ko'rishingiz mumkin.

    📚 **Dasturlash tillari:**
    - **Python** 🐍
    - **JavaScript** 💻
    - **Java** 💼
    - **C++** 💻
    - **C#** 🔷
    - **TypeScript** 📚
    - **GO** 💼
    - **Kotlin** 📓
    - **PHP** 📖

    📝 **Testlarni boshlash uchun:** Sizga kerakli dasturlash tilini tanlang va testga kirish uchun tugmani bosing.

    📩 **Savollaringiz bo'lsa, biz bilan bog'laning!**
     Test ishlash uchun ** /test ** buyruqini yuboring
    """
    if message.text == "\U0001F4C3 Bot haqida ma'lumot":
        await message.answer(info_message)
    else:
        await message.reply(info_message)


if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
