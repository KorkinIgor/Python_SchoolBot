import telebot
from dotenv import load_dotenv
import os
from telebot import types
import numpy as np
import webbrowser

load_dotenv()

Token = os.getenv('TOKEN')

TeachersOfRussianAndLiterature = os.getenv('TeachersOfRussianAndLiterature')
TeachersMath = os.getenv('TeachersMath')
TeachersTechnology = os.getenv('TeachersTechnology')
BiologyTeacher = os.getenv('BiologyTeacher')
PrimarySchoolTeachers = os.getenv('PrimarySchoolTeachers')
TeacherEnglish = os.getenv('TeacherEnglish')
TeachersInformatics = os.getenv('TeachersInformatics')
TeachersHistory = os.getenv('TeachersHistory')
TeachersLifeSafety = os.getenv('TeachersLifeSafety')
TeachersMusic = os.getenv('TeachersMusic')
TeacherChemistry = os.getenv('TeacherChemistry')
TeacherPhysicalEducation = os.getenv('TeacherPhysicalEducation')
TeacherGeography = os.getenv('TeacherGeography')
TeacherArt = os.getenv('TeacherArt')
saitSchool = os.getenv('saitSchool')
urlRegisterChildSchool = os.getenv('urlRegisterChildSchool')
text_pointRussianLanguage = os.getenv('pointRussianLanguage')
text_pointMathematics = os.getenv('pointMathematics')
text_pointPhysics = os.getenv('pointPhysics')
text_pointChemistry = os.getenv('pointChemistry')
text_pointBiology = os.getenv('pointBiology')
text_pointLiterature = os.getenv('pointLiterature')
text_pointGeography = os.getenv('pointGeography')
text_pointHistory = os.getenv('pointHistory')
text_pointInformatics = os.getenv('pointInformatics')


score_list = []
bot = telebot.TeleBot(Token)

#start
@bot.message_handler(commands=['start'])
def start(message):
    start_markup = types.ReplyKeyboardMarkup()
    bt1 = types.KeyboardButton('Вычеслить средний балл')
    bt2 = types.KeyboardButton('Учителя школы')
    bt3 = types.KeyboardButton('Сайт школы')
    bt4 = types.KeyboardButton('Баллы ОГЭ')
    start_markup.row(bt1, bt2)
    start_markup.row(bt3, bt4)
    bot.send_message(message.chat.id, f'Выберите действие, {message.from_user.username}.', reply_markup=start_markup)
    bot.register_next_step_handler(message, NextChoiceMarcup)


@bot.message_handler()
def NextChoiceMarcup(message):
    if message.text == 'Вычеслить средний балл':
        ScoreMarcup = types.ReplyKeyboardMarkup()
        ScoreTwo = types.KeyboardButton('2')
        ScoreThree = types.KeyboardButton('3')
        ScoreFour = types.KeyboardButton('4')
        ScoreFive = types.KeyboardButton('5')
        ReadyButton = types.KeyboardButton('Готово')
        BackButton = types.KeyboardButton('Назад')
        ScoreMarcup.row(ScoreTwo, ScoreThree)
        ScoreMarcup.row(ScoreFour, ScoreFive)
        ScoreMarcup.row(ReadyButton)
        ScoreMarcup.row(BackButton)
        bot.send_message(message.chat.id, f'Укажите в ряд свои оценки', reply_markup=ScoreMarcup)
        bot.register_next_step_handler(message, Score)
    elif message.text == 'Учителя школы':
        MarcupTeacher = types.ReplyKeyboardMarkup()
        TeachersOfRussianAndLiteratureBt = types.KeyboardButton('Учителя русского языка и литературы')
        TeachersMathBt = types.KeyboardButton('Учителя математики')
        TeachersTechnologyBt = types.KeyboardButton('Учителя технологии')
        BiologyTeacherBt = types.KeyboardButton('Учителя биологии')
        PrimarySchoolTeachersBt = types.KeyboardButton('Учителя начальной школы')
        TeacherEnglishBt = types.KeyboardButton('Учителя англиского языка')
        TeachersInformaticsBt = types.KeyboardButton('Учителя информатики')
        TeachersHistoryBt = types.KeyboardButton('Учителя истории и обществознания')
        TeachersLifeSafetyBt = types.KeyboardButton('Учителя ОБЖ')
        TeachersMusicBt = types.KeyboardButton('Учителя музыки')
        TeacherChemistryBt =  types.KeyboardButton('Учителя химии')
        TeacherPhysicalEducationBt = types.KeyboardButton('Учителя физкультуры')
        TeacherGeographyBt = types.KeyboardButton('Учителя географии')
        TeacherArtBt = types.KeyboardButton('Учителя Изо')
        BackButton = types.KeyboardButton('Назад')
        MarcupTeacher.row(TeachersOfRussianAndLiteratureBt, TeachersMathBt, TeacherEnglishBt)
        MarcupTeacher.row(BiologyTeacherBt, PrimarySchoolTeachersBt, TeachersTechnologyBt)
        MarcupTeacher.row(TeachersInformaticsBt, TeachersHistoryBt, TeachersLifeSafetyBt)
        MarcupTeacher.row(TeachersMusicBt, TeacherChemistryBt, TeacherPhysicalEducationBt)
        MarcupTeacher.row(TeacherGeographyBt, TeacherArtBt)
        MarcupTeacher.row(BackButton)
        bot.send_message(message.chat.id, f'Выбери урок:',reply_markup=MarcupTeacher)
        bot.register_next_step_handler(message, Teachers)
    elif message.text == 'Сайт школы':
        bot.send_message(message.chat.id, f'Сайт: {saitSchool}')
    elif message.text == 'Баллы ОГЭ':
        SchoolSubject = types.InlineKeyboardMarkup()
        RussianLanguage_bt = types.InlineKeyboardButton('Русский язык', callback_data='RussianLanguage_bt')
        Mathematics_bt = types.InlineKeyboardButton('Математика', callback_data='Mathematics_bt')
        Physics_bt = types.InlineKeyboardButton('Физика', callback_data='Physics_bt')
        Chemistry_bt = types.InlineKeyboardButton('Химия', callback_data='Chemistry_bt')
        Biology_bt = types.InlineKeyboardButton('Биология', callback_data='Biology_bt')
        Literature_bt = types.InlineKeyboardButton('Литература', callback_data='Literature_bt')
        Geography_bt = types.InlineKeyboardButton('География', callback_data='Geography_bt')
        History_bt = types.InlineKeyboardButton('История', callback_data='History_bt')
        Informatics_bt = types.InlineKeyboardButton('Информатика', callback_data='Informatics_bt')
        SchoolSubject.row(RussianLanguage_bt, Mathematics_bt, Physics_bt)
        SchoolSubject.row(Chemistry_bt, Biology_bt, Literature_bt)
        SchoolSubject.row(Geography_bt, History_bt, Informatics_bt)
        bot.send_message(message.chat.id, f'Предметы:', reply_markup=SchoolSubject)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message_OGE_Point(callback):
    if callback.data == 'RussianLanguage_bt':
        bot.send_message( callback.message.chat.id, text_pointRussianLanguage)
    elif callback.data == 'Mathematics_bt':
        bot.send_message( callback.message.chat.id, text_pointMathematics)
    elif callback.data == 'Physics_bt':
        bot.send_message(callback.message.chat.id, text_pointPhysics)
    elif callback.data == 'Chemistry_bt':
        bot.send_message(callback.message.chat.id, text_pointChemistry)
    elif callback.data == 'Biology_bt':
        bot.send_message(callback.message.chat.id, text_pointBiology)
    elif callback.data == 'Literature_bt':
        bot.send_message(callback.message.chat.id, text_pointLiterature)
    elif callback.data == 'Geography_bt':
        bot.send_message(callback.message.chat.id, text_pointGeography)
    elif callback.data == 'History_bt':
        bot.send_message(callback.message.chat.id, text_pointHistory)
    elif callback.data == 'Informatics_bt':
        bot.send_message(callback.message.chat.id, text_pointInformatics)


def Teachers(message):
    if message.text == 'Учителя русского языка и литературы':
        bot.send_message(message.chat.id, f'{TeachersOfRussianAndLiterature}')
        bot.register_next_step_handler(message, Teachers)
    elif message.text == 'Учителя математики':
        bot.send_message(message.chat.id, f'{TeachersMath}')
        bot.register_next_step_handler(message, Teachers)
    elif message.text == 'Учителя технологии':
        bot.send_message(message.chat.id, f'{TeachersTechnology}')
        bot.register_next_step_handler(message, Teachers)
    elif message.text == 'Учителя технологии':
        bot.send_message(message.chat.id, f'{TeachersTechnology}')
        bot.register_next_step_handler(message, Teachers)
    elif message.text == 'Учителя биологии':
        bot.send_message(message.chat.id, f'{BiologyTeacher}')
        bot.register_next_step_handler(message, Teachers)
    elif message.text == 'Учителя англиского языка':
        bot.send_message(message.chat.id, f'{TeacherEnglish}')
        bot.register_next_step_handler(message, Teachers)
    elif message.text == 'Учителя информатики':
        bot.send_message(message.chat.id, f'{TeachersInformatics}')
        bot.register_next_step_handler(message, Teachers)
    elif message.text == 'Учителя истории и обществознания':
        bot.send_message(message.chat.id, f'{TeachersHistory}')
        bot.register_next_step_handler(message, Teachers)
    elif message.text == 'Учителя ОБЖ':
        bot.send_message(message.chat.id, f'{TeachersLifeSafety}')
        bot.register_next_step_handler(message, Teachers)
    elif message.text == 'Учителя начальной школы':
        bot.send_message(message.chat.id, f'{PrimarySchoolTeachers}')
        bot.register_next_step_handler(message, Teachers)
    elif message.text == 'Учителя музыки':
        bot.send_message(message.chat.id, f'{TeachersMusic}')
        bot.register_next_step_handler(message, Teachers)
    elif message.text == 'Учителя химии':
        bot.send_message(message.chat.id, f'{TeacherChemistry}')
        bot.register_next_step_handler(message, Teachers)
    elif message.text == 'Учителя физкультуры':
        bot.send_message(message.chat.id, f'{TeacherPhysicalEducation}')
        bot.register_next_step_handler(message, Teachers)
    elif message.text == 'Учителя географии':
        bot.send_message(message.chat.id, f'{TeacherGeography}')
        bot.register_next_step_handler(message, Teachers)
    elif message.text == 'Учителя Изо':
        bot.send_message(message.chat.id, f'{TeacherArt}')
        bot.register_next_step_handler(message, Teachers)
    elif message.text == 'Назад':
        bot.register_next_step_handler(message, start)
@bot.message_handler()
def Score(message):
    if message.text == '2':
        score_list.append(2)
        bot.register_next_step_handler(message, Score)
        score_list.clear()
    elif message.text == '3':
        score_list.append(3)
        bot.register_next_step_handler(message, Score)
    elif message.text == '4':
        score_list.append(4)
        bot.register_next_step_handler(message, Score)
    elif message.text == '5':
        score_list.append(5)
        bot.register_next_step_handler(message, Score)
    elif len(score_list) == 0 and message.text == 'Готово':
        bot.send_message(message.chat.id, f'Введите оценки')
        bot.register_next_step_handler(message, Score)
    elif message.text == 'Готово':
        average = np.mean(score_list)
        normal_average = round(average, 2)
        if normal_average < 2.5 :
            bot.send_message(message.chat.id, f'Ваш средний балл: {normal_average}, у вас выходит 2')
            score_list.clear()
            bot.register_next_step_handler(message, Score)
        if 2.5 < normal_average < 3.5:
            bot.send_message(message.chat.id, f'Ваш средний балл: {normal_average}, у вас выходит 3')
            score_list.clear()
            bot.register_next_step_handler(message, Score)
        if 3.5 < normal_average < 4.5:
            bot.send_message(message.chat.id, f'Ваш средний балл: {normal_average}, у вас выходит 4')
            score_list.clear()
            bot.register_next_step_handler(message, Score)
        if normal_average > 4.5:
            bot.send_message(message.chat.id, f'Ваш средний балл: {normal_average}, у вас выходит 5')
            score_list.clear()
            bot.register_next_step_handler(message, Score)
        score_list.clear()
    elif message.text == 'Назад':
        bot.register_next_step_handler(message, start)
    elif message.text != 'Готово' or message.text != '2' or message.text != '3' or message.text != '4' or message.text != '5' or message.text != 'Назад':
        bot.send_message(message.chat.id, f'Укажите корректное значение.')
        score_list.clear()
        bot.register_next_step_handler(message, Score)
bot.polling(non_stop=True)