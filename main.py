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

urlRegisterChildSchool = os.getenv('urlRegisterChildSchool')

score_list = []
bot = telebot.TeleBot(Token)

#start
@bot.message_handler(commands=['start'])
def start(message):
    start_markup = types.ReplyKeyboardMarkup()
    bt1 = types.KeyboardButton('Вычеслить средний балл')
    bt2 = types.KeyboardButton('Учителя школы')
    bt3 = types.KeyboardButton('Записать ребенка в школу')
    start_markup.row(bt1, bt2)
    start_markup.row(bt3)
    bot.send_message(message.chat.id, f'Выберите действие, {message.from_user.username}.', reply_markup=start_markup)
    bot.register_next_step_handler(message, NextChoiceMarcup)


def startDo(message):
    start_markup = types.ReplyKeyboardMarkup()
    bt1 = types.KeyboardButton('Вычеслить средний балл')
    bt2 = types.KeyboardButton('Учителя школы')
    bt3 = types.KeyboardButton('Записать ребенка в школу')
    start_markup.row(bt1, bt2)
    start_markup.row(bt3)
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
        bot.send_message(message.chat.id, f'Выбери урок.',reply_markup=MarcupTeacher)
        bot.register_next_step_handler(message, Teachers)
    elif message.text == 'Записать ребенка в школу':
        webbrowser.open(url=urlRegisterChildSchool)

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
        bot.register_next_step_handler(message, startDo)
@bot.message_handler()
def Score(message):
    if message.text == '2':
        score_list.append(2)
        bot.register_next_step_handler(message, Score)
    elif message.text == '3':
        score_list.append(3)
        bot.register_next_step_handler(message, Score)
    elif message.text == '4':
        score_list.append(4)
        bot.register_next_step_handler(message, Score)
    elif message.text == '5':
        score_list.append(5)
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
        bot.register_next_step_handler(message, startDo)
        score_list.clear()
    elif message.text != 'Готово' or message.text != '2' or message.text != '3' or message.text != '4' or message.text != '5' or message.text != 'Назад':
        bot.send_message(message.chat.id, f'Укажите корректное значение.')
        score_list.clear()
        bot.register_next_step_handler(message, Score)
bot.polling(non_stop=True)