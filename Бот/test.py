import emoji
import uuid
import datetime

my_id = uuid.uuid1() # or uuid.uuid4()
id = []
# print(my_id)
# print(emoji.demojize('😬'))
time = str(datetime.datetime.now())[11:]
time = time.split(':')
# print(time)

GOOD = [':grinning_face:', ':grinning_face_with_big_eyes:', ':grinning_face_with_smiling_eyes:', ':beaming_face_with_smiling_eyes:']
BAD = [':unamused_face:', ':disappointed_face:']
ANGRY = [':angry_face_with_horns:', ':grimacing_face:']

a = 1
while a == 1:
    message = input()
    message_dem = emoji.demojize(message)
    time = str(datetime.datetime.now())[11:]
    time = time.split(':')
    # print(time)
    if message_dem in GOOD:
        print('Привет! Как хорошо, когда у человека хорошее настроение!')
        try:
            second_query = input()
            second_query = emoji.demojize(second_query)
            time_2 = str(datetime.datetime.now())[11:]
            time_2 = time_2.split(':')
            for i in range(len(time)):
                # print(time_2, int(time_2[1]), int(time[1]))
                if int(time_2[1]) - int(time[1]) <= 1:
                    if second_query in GOOD:
                        print('Хорошо, когда настреоние всегда на высоте!')
                    elif second_query in BAD:
                        print('Переменчивое у Вас настроение')
                    else:
                        print('Думаю, Вам стоит помедитировать, вся злость испарится')
        except second_query is None:
            print('Конец')

    elif message_dem in BAD:
        print('Привет! Видимо, у Вас что-то стряслось. Не грустите')
    elif message_dem in ANGRY:
        print('Ну привет, человек не в настроении')
    else:
        a = 0
        print('Совсем я разучился понимать человеческий язык...')

       
        
        


