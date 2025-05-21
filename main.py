from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove)
from config import Config, load_config
config: Config = load_config()
BOT_TOKEN: str = config.tg_bot.token
bot = Bot(BOT_TOKEN)
dp = Dispatcher()
users = {}
button_1 = KeyboardButton(text='Мужской')
button_2 = KeyboardButton(text='Женский')
keyboard_1 = ReplyKeyboardMarkup(keyboard=[[button_1, button_2]], resize_keyboard=True)
button_3 = KeyboardButton(text='Менее 4 часов')
button_4 = KeyboardButton(text='От 4 до 6 часов')
button_5 = KeyboardButton(text='От 6 до 8 часов')
button_6 = KeyboardButton(text='Более 8 часов')
keyboard_2 = ReplyKeyboardMarkup(keyboard=[[button_3], [button_4], [button_5], [button_6]], resize_keyboard=False)
button_7 = KeyboardButton(text='Менее 5 минут')
button_8 = KeyboardButton(text='От 5 до 15 минут')
button_9 = KeyboardButton(text='От 15 до 30 минут')
button_10 = KeyboardButton(text='От 30 минут до 1 часа')
button_11 = KeyboardButton(text='Более 1 часа')
keyboard_3 = ReplyKeyboardMarkup(keyboard=[[button_7], [button_8], [button_9], [button_10], [button_11]], resize_keyboard=False)
button_12 = KeyboardButton(text='Очень плохо')
button_13 = KeyboardButton(text='Плохо')
button_14 = KeyboardButton(text='Средне')
button_15 = KeyboardButton(text='Хорошо')
button_16 = KeyboardButton(text='Отлично')
keyboard_4 = ReplyKeyboardMarkup(keyboard=[[button_12], [button_13], [button_14], [button_15], [button_16]], resize_keyboard=False)
button_17 = KeyboardButton(text='Нет')
button_18 = KeyboardButton(text='Менее 30 минут')
button_19 = KeyboardButton(text='От 30 минут до 1 часа')
button_20 = KeyboardButton(text='От 1 часа до 2 часов')
button_21 = KeyboardButton(text='Более 2 часов')
keyboard_5 = ReplyKeyboardMarkup(keyboard=[[button_17], [button_18], [button_19], [button_20], [button_21]], resize_keyboard=False)
button_22 = KeyboardButton(text='Нет.')
button_23 = KeyboardButton(text='Да.')
keyboard_6 = ReplyKeyboardMarkup(keyboard=[[button_22, button_23]], resize_keyboard=True)
button_24 = KeyboardButton(text='Показать результат')
keyboard_7 = ReplyKeyboardMarkup(keyboard=[[button_24]], resize_keyboard=True)
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Ваш пол:',
        reply_markup=keyboard_1
    )
    if message.from_user.id not in users:
        users[message.from_user.id] = {
            'sex': None,
            'time_sleep': None,
            'time_fall_asleep': None,
            'sleep_quality': None,
            'physical': None,
            'smoking': None,
            'pulse': None,
            'long_illness': None,
            'long_education': None,
            'EDSS': None,
        }
@dp.message(F.text == 'Мужской')
async def process_sex_answer(message: Message):
    await message.answer(
        text='Время Вашего ночного сна:',
        #reply_markup=ReplyKeyboardRemove(),
        reply_markup=keyboard_2
    )
    users[message.from_user.id]['sex'] = 0
@dp.message(F.text == 'Женский')
async def process_sex_answer(message: Message):
    await message.answer(
        text='Время Вашего ночного сна:',
        #reply_markup=ReplyKeyboardRemove(),
        reply_markup=keyboard_2
    )
    users[message.from_user.id]['sex'] = 1
@dp.message(F.text == 'Менее 4 часов')
async def process_sleep_answer(message: Message):
    await message.answer(
        text='Время Вашего засыпания:',
        reply_markup=keyboard_3
    )
    users[message.from_user.id]['time_sleep'] = 1
@dp.message(F.text == 'От 4 до 6 часов')
async def process_sleep_answer(message: Message):
    await message.answer(
        text='Время Вашего засыпания:',
        reply_markup=keyboard_3
    )
    users[message.from_user.id]['time_sleep'] = 2
@dp.message(F.text == 'От 6 до 8 часов')
async def process_sleep_answer(message: Message):
    await message.answer(
        text='Время Вашего засыпания:',
        reply_markup=keyboard_3
    )
    users[message.from_user.id]['time_sleep'] = 3
@dp.message(F.text == 'Более 8 часов')
async def process_sleep_answer(message: Message):
    await message.answer(
        text='Время Вашего засыпания:',
        reply_markup=keyboard_3
    )
    users[message.from_user.id]['time_sleep'] = 4
@dp.message(F.text == 'Менее 5 минут')
async def process_asleep_answer(message: Message):
    await message.answer(
        text='Качество Вашего сна:',
        reply_markup=keyboard_4
    )
    users[message.from_user.id]['time_fall_asleep'] = 1
@dp.message(F.text == 'От 5 до 15 минут')
async def process_asleep_answer(message: Message):
    await message.answer(
        text='Качество Вашего сна:',
        reply_markup=keyboard_4
    )
    users[message.from_user.id]['time_fall_asleep'] = 2
@dp.message(F.text == 'От 15 до 30 минут')
async def process_asleep_answer(message: Message):
    await message.answer(
        text='Качество Вашего сна:',
        reply_markup=keyboard_4
    )
    users[message.from_user.id]['time_fall_asleep'] = 3
@dp.message(F.text == 'От 30 минут до 1 часа')
async def process_asleep_answer(message: Message):
    await message.answer(
        text='Качество Вашего сна:',
        reply_markup=keyboard_4
    )
    users[message.from_user.id]['time_fall_asleep'] = 4
@dp.message(F.text == 'Более 1 часа')
async def process_asleep_answer(message: Message):
    await message.answer(
        text='Качество Вашего сна:',
        reply_markup=keyboard_4
    )
    users[message.from_user.id]['time_fall_asleep'] = 5
@dp.message(F.text == 'Очень плохо')
async def process_quality_answer(message: Message):
    await message.answer(
        text='Занятия физической культурой в неделю:',
        reply_markup=keyboard_5
    )
    users[message.from_user.id]['sleep_quality'] = 1
@dp.message(F.text == 'Плохо')
async def process_quality_answer(message: Message):
    await message.answer(
        text='Занятия физической культурой в неделю:',
        reply_markup=keyboard_5
    )
    users[message.from_user.id]['sleep_quality'] = 2
@dp.message(F.text == 'Средне')
async def process_quality_answer(message: Message):
    await message.answer(
        text='Занятия физической культурой в неделю:',
        reply_markup=keyboard_5
    )
    users[message.from_user.id]['sleep_quality'] = 3
@dp.message(F.text == 'Хорошо')
async def process_quality_answer(message: Message):
    await message.answer(
        text='Занятия физической культурой в неделю:',
        reply_markup=keyboard_5
    )
    users[message.from_user.id]['sleep_quality'] = 4
@dp.message(F.text == 'Отлично')
async def process_quality_answer(message: Message):
    await message.answer(
        text='Занятия физической культурой в неделю:',
        reply_markup=keyboard_5
    )
    users[message.from_user.id]['sleep_quality'] = 5
@dp.message(F.text == 'Нет')
async def process_phys_answer(message: Message):
    await message.answer(
        text='Вы курите:',
        reply_markup=keyboard_6
    )
    users[message.from_user.id]['physical'] = 1
@dp.message(F.text == 'Менее 30 минут')
async def process_phys_answer(message: Message):
    await message.answer(
        text='Вы курите:',
        reply_markup=keyboard_6
    )
    users[message.from_user.id]['physical'] = 2
@dp.message(F.text == 'От 30 минут до 1 часа')
async def process_phys_answer(message: Message):
    await message.answer(
        text='Вы курите:',
        reply_markup=keyboard_6
    )
    users[message.from_user.id]['physical'] = 3
@dp.message(F.text == 'От 1 часа до 2 часов')
async def process_phys_answer(message: Message):
    await message.answer(
        text='Вы курите:',
        reply_markup=keyboard_6
    )
    users[message.from_user.id]['physical'] = 4
@dp.message(F.text == 'Более 2 часов')
async def process_phys_answer(message: Message):
    await message.answer(
        text='Вы курите:',
        reply_markup=keyboard_6
    )
    users[message.from_user.id]['physical'] = 5
@dp.message(F.text == 'Нет.')
async def process_smok_answer(message: Message):
    await message.answer(
        text='Количество пульс-терапий в анамнезе (пример: /pulse 5):',
        reply_markup=ReplyKeyboardRemove()
    )
    users[message.from_user.id]['smoking'] = 0
@dp.message(F.text == 'Да.')
async def process_smok_answer(message: Message):
    await message.answer(
        text='Количество пульс-терапий в анамнезе (пример: /pulse 5):',
        reply_markup=ReplyKeyboardRemove()
    )
    users[message.from_user.id]['smoking'] = 1

@dp.message(Command("pulse"))
async def process_pulse_answer(message: types.Message):
    text = message.text.removeprefix('/pulse ')
    if text.isdigit():
        number_1 = int(text)
        await message.answer(
        text='Продолжительность заболевания (укажите числом только полное количество лет, например: /long 5):',
    )
        users[message.from_user.id]['pulse'] = number_1
    else:
        await message.answer("Это не число, введите, пожалуйста, число!")

@dp.message(Command("long"))
async def process_long_answer(message: types.Message):
    text = message.text.removeprefix('/long ')
    if text.isdigit():
        number_2 = int(text)
        await message.answer(
        text='Продолжительность образования (укажите числом только полное число лет: школа + училище/колледж + институт + аспирантура, например: /educ 15):',
    )
        users[message.from_user.id]['long_illness'] = number_2
    else:
        await message.answer("Это не число, введите, пожалуйста, число!")

@dp.message(Command("educ"))
async def process_educ_answer(message: types.Message):
    text = message.text.removeprefix('/educ ')
    if text.isdigit():
        number_3 = int(text)
        await message.answer(
        text='Балл EDSS (заполняется врачом, укажите только число, напримпер: \n /edss 5). Если число добное, десятичную часть отделите ".":',
    )
        users[message.from_user.id]['long_education'] = number_3
    else:
        await message.answer("Это не число, введите, пожалуйста, число!")

@dp.message(Command("edss"))
async def process_edss_answer(message: types.Message):
    command_args = message.text.removeprefix('/edss ')
    # Проверяем, что текст не пустой
    if not command_args.strip():
        await message.answer("Пожалуйста, введите значение EDSS после команды /edss.")
        return
    try:
        number_4 = float(command_args)
        users[message.from_user.id]['EDSS'] = number_4
        await message.answer(
            text='Нажмите на кнопку "показать результат", чтобы увидеть возможный эффект пульс-терапии метилпреднизолоном:',
            reply_markup=keyboard_7
        )
    except ValueError:
        await message.answer("Это не число. Пожалуйста, введите числовое значение EDSS (например, 4.5 или 6)")
@dp.message(F.text == 'Показать результат')
async def process_result_answer(message: Message):
    def process_bvmtr_answer():
        x_1 = -6.562*users[message.from_user.id]['sex']
        if users[message.from_user.id]['physical'] == 1:
            x_2 = 0
        elif users[message.from_user.id]['physical'] == 2:
            x_2 = -2.562
        elif users[message.from_user.id]['physical'] == 3:
            x_2 = 8.521
        elif users[message.from_user.id]['physical'] == 4:
            x_2 = 10.474
        elif users[message.from_user.id]['physical'] == 5:
            x_2 = 2.778
        x_3 = 1.58*users[message.from_user.id]['pulse']
        x_4 = -0.74*users[message.from_user.id]['long_illness']
        bvmt_r = 3.665 + x_1 + x_2 + x_3 + x_4
        if 0 < bvmt_r <= 6.13:
            return f'{bvmt_r}, данный результат встречается у 34% и соответствует незначительному улучшению.'
        elif 6.13 < bvmt_r <= 12.95:
            return f'{bvmt_r}, данный результат встречается у 14% и соответствует умеренному улучшению.'
        elif 12.95 < bvmt_r <= 19.75:
            return f'{bvmt_r}, данный результат встречается у 2% и соответствует значительному улучшению.'
        elif bvmt_r > 19.75:
            return f'{bvmt_r}, данный результат встречается менее чем у 2% и соответствует очень значительному улучшению.'
        elif -7.49 < bvmt_r <= 0:
            return f'{bvmt_r}, данный результат встречается у 34% и соответствует незначительному ухудшению.'
        elif -14.29 < bvmt_r <= -7.49:
            return f'{bvmt_r}, данный результат встречается у 14% и соответствует умеренному ухудшению.'
        elif -21.11 <= bvmt_r <= -14.29:
            return f'{bvmt_r}, данный результат встречается у 2% и соответствует значительному ухудшению.'
        elif bvmt_r < -21.11:
            return f'{bvmt_r}, данный результат встречается менее чем у 2% и соответствует очень значительному ухудшению.'
    def process_sdmt_answer():
        if users[message.from_user.id]['physical'] == 1:
            x_5 = 0
        elif users[message.from_user.id]['physical'] == 2:
            x_5 = 8.29
        elif users[message.from_user.id]['physical'] == 3:
            x_5 = 13.67
        elif users[message.from_user.id]['physical'] == 4:
            x_5 = 2.87
        elif users[message.from_user.id]['physical'] == 5:
            x_5 = 4.53
        x_6 = -1.72*users[message.from_user.id]['EDSS']
        x_7 = 2.74*users[message.from_user.id]['time_fall_asleep']
        sdmt = -7.55 + x_5 + x_6 + x_7
        if 0 < sdmt <= 7.61:
            return f'{sdmt}, данный результат встречается у 34% и соответствует незначительному улучшению.'
        elif 7.61 < sdmt <= 15.27:
            return f'{sdmt}, данный результат встречается у 14% и соответствует умеренному улучшению.'
        elif 15.27 < sdmt <= 22.92:
            return f'{sdmt}, данный результат встречается у 2% и соответствует значительному улучшению.'
        elif sdmt > 22.92:
            return f'{sdmt}, данный результат встречается менее чем у 2% и соответствует очень значительному улучшению.'
        elif -7.68 <= sdmt <= 0:
            return f'{sdmt}, данный результат встречается у 34% и соответствует незначительному ухудшению.'
        elif -15.33 <= sdmt < -7.68:
            return f'{sdmt}, данный результат встречается у 14% и соответствует умеренному ухудшению.'
        elif -22.97 <= sdmt < -15.33:
            return f'{sdmt}, данный результат встречается у 2% и соответствует значительному ухудшению.'
        elif sdmt < -22.97:
            return f'{sdmt}, данный результат встречается менее чем у 2% и соответствует очень значительному ухудшению.'
    def process_moca_answer():
        if users[message.from_user.id]['physical'] == 1:
            x_8 = 0
        elif users[message.from_user.id]['physical'] == 2:
            x_8 = 1.4624
        elif users[message.from_user.id]['physical'] == 3:
            x_8 = 0.52
        elif users[message.from_user.id]['physical'] == 4:
            x_8 = 0.6462
        elif users[message.from_user.id]['physical'] == 5:
            x_8 = 0.0522
        x_9 = -0.3323*users[message.from_user.id]['EDSS']
        x_10 = 0.288*users[message.from_user.id]['time_fall_asleep']
        x_11 = 0.6208*users[message.from_user.id]['time_sleep']
        x_12 = 0.2094*users[message.from_user.id]['pulse']
        x_13 = -0.0423*users[message.from_user.id]['long_illness']
        moca = -1.982 + x_8 + x_9 + x_10 + x_11 + x_12 + x_13
        if 0 < moca <= 1:
            return f'{moca}, данный результат встречается у 25% и соответствует незначительному улучшению.'
        elif 1 < moca <= 3:
            return f'{moca}, данный результат встречается у 25% и соответствует умеренному улучшению.'
        elif moca > 3:
            return f'{moca}, данный результат встречается у 25% и соответствует значительному улучшению.'
        elif -1 <= moca <= 0:
            return f'{moca}, данный результат встречается у 25% и соответствует незначительному ухудшению.'
        elif -2 <= moca <= -1:
            return f'{moca}, данный результат встречается у 25% и соответствует умеренному ухудшению.'
        elif moca < -2:
            return f'{moca}, данный результат встречается у 25% значительному ухудшению.'
    def process_strup_answer():
        if users[message.from_user.id]['physical'] == 1:
            x_14 = 0
        elif users[message.from_user.id]['physical'] == 2:
            x_14 = -6.044
        elif users[message.from_user.id]['physical'] == 3:
            x_14 = 4.891
        elif users[message.from_user.id]['physical'] == 4:
            x_14 = 0.785
        elif users[message.from_user.id]['physical'] == 5:
            x_14 = -1.598
        x_15 = -4.448*users[message.from_user.id]['time_fall_asleep']
        x_16 = 0.350*users[message.from_user.id]['long_illness']
        x_17 = -1.088*users[message.from_user.id]['long_education']
        x_18 = -5.767*users[message.from_user.id]['smoking']
        strup = 26.376 + x_14 + x_15 + x_16 + x_17 + x_18
        if -7 <= strup < -5:
            return f'{strup}, данный результат встречается у 25% и соответствует незначительному улучшению.'
        elif -14 < strup < -7:
            return f'{strup}, данный результат встречается у 25% и соответствует умеренному улучшению.'
        elif strup <= -14:
            return f'{strup}, данный результат встречается у 25% и соответствует значительному улучшению.'
        elif -5 <= strup <= -1.43:
            return f'{strup}, данный результат встречается у 25% и соответствует незначительному ухудшению.'
        elif -1.43 < strup <= 18:
            return f'{strup}, данный результат встречается у 25% и соответствует умеренному ухудшению.'
        elif strup > 18:
            return f'{strup}, данный результат встречается у 25% значительному ухудшению.'
    def process_anx_answer():
        x_19 = -0.842*users[message.from_user.id]['physical']
        x_20 = -0.527*users[message.from_user.id]['long_illness']
        x_21 = -13.139*users[message.from_user.id]['smoking']
        x_22 = -7.441*users[message.from_user.id]['sex']
        x_23 = -5.363*users[message.from_user.id]['time_sleep']
        x_24 = 4.178*users[message.from_user.id]['sleep_quality']
        x_25 = -2.172*users[message.from_user.id]['EDSS']
        x_26 = 3.112*users[message.from_user.id]['pulse']
        anx = 11.36 + x_19 + x_20 + x_21 + x_22 + x_23 + x_24 + x_25 + x_26
        if 0 < anx <= 4.53:
            return f'{anx}, данный результат встречается у 34% и соответствует незначительному ухудшению.'
        elif 4.53 < anx <= 10.97:
            return f'{anx}, данный результат встречается у 14% и соответствует умеренному ухудшению.'
        elif 10.97 < anx <= 17.41:
            return f'{anx}, данный результат встречается у 2% и соответствует значительному ухудшению.'
        elif anx > 17.41:
            return f'{anx}, данный результат встречается менее чем у 2% и соответствует очень значительному ухудшению.'
        elif -8.35 <= anx <= 0:
            return f'{anx}, данный результат встречается у 34% и соответствует незначительному улучшению.'
        elif -14.79 <= anx < -8.35:
            return f'{anx}, данный результат встречается у 14% и соответствует умеренному улучшению.'
        elif -21.23 <= anx < -14.79:
            return f'{anx}, данный результат встречается у 2% и соответствует значительному улучшению.'
        elif anx < -21.23:
            return f'{anx}, данный результат встречается менее чем у 2% и соответствует очень значительному улучшению.'
    def process_depr_answer():
        x_27 = -1.06*users[message.from_user.id]['physical']
        x_28 = -3.05*users[message.from_user.id]['EDSS']
        x_29 = -9.36*users[message.from_user.id]['smoking']
        x_30 = -3.21*users[message.from_user.id]['sex']
        x_31 = 1.12*users[message.from_user.id]['pulse']
        x_32 = 1.72*users[message.from_user.id]['sleep_quality']
        depr = 4.11 + x_27 + x_28 + x_29 + x_30 + x_31 + x_32
        if 0 < depr <= 6.13:
            return f'{depr}, данный результат встречается у 34% и соответствует незначительному ухудшению.'
        elif 6.13 < depr <= 12.77:
            return f'{depr}, данный результат встречается у 14% и соответствует умеренному ухудшению.'
        elif 12.77 < depr <= 19.41:
            return f'{depr}, данный результат встречается у 2% и соответствует значительному ухудшению.'
        elif depr > 19.41:
            return f'{depr}, данный результат встречается менее чем у 2% и соответствует очень значительному ухудшению.'
        elif -7.15 <= depr <= 0:
            return f'{depr}, данный результат встречается у 34% и соответствует незначительному улучшению.'
        elif -13.79 <= depr < -7.15:
            return f'{depr}, данный результат встречается у 14% и соответствует умеренному улучшению.'
        elif -20.43 <= depr < -13.79:
            return f'{depr}, данный результат встречается у 2% и соответствует значительному улучшению.'
        elif depr < -20.43:
            return f'{depr}, данный результат встречается менее чем у 2% и соответствует очень значительному улучшению.'

    await message.answer(f'Изменение по зрительно-пространственной памяти (BVMT-R, точность 53,9%): {process_bvmtr_answer()} \n\n\n'
                         f'Изменение по темпу познавательной деятельности (SDMT, точность 48,1%): {process_sdmt_answer()} \n\n\n'
                         f'Изменения по зрительно-конструктивным навыкам (MoCA, точность 62,5%): {process_moca_answer()} \n\n\n'
                         f'Изменение по управляющим функциям (тест Струпа, точность 56,3%): {process_strup_answer()} \n\n\n'
                         f'Изменение по тревоге (опросник Цунга, точность 52%): {process_anx_answer()} \n\n\n'
                         f'Изменение по депрессии (опросник Цунга, точность 50,6%): {process_depr_answer()}',
                         reply_markup=ReplyKeyboardRemove()
                         )
if __name__ == '__main__':
    dp.run_polling(bot)
