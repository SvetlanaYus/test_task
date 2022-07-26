import emoji
import uuid
import datetime


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
    my_id = uuid.uuid1() # or uuid.uuid4()
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
                    elif second_query in ANGRY:
                        print('Думаю, Вам стоит помедитировать, вся злость испарится')
                    else:
                        print('Совсем не понимаю людей')
        except second_query is None:
            print('Конец')

    elif message_dem in BAD:
        print('Привет! Видимо, у Вас что-то стряслось. Не грустите')
    elif message_dem in ANGRY:
        print('Ну привет, человек не в настроении')
        try:
            second_query = input()
            second_query = emoji.demojize(second_query)
            time_2 = str(datetime.datetime.now())[11:]
            time_2 = time_2.split(':')
            for i in range(len(time)):
                if int(time_2[1]) - int(time[1]) <= 1:
                    if second_query in GOOD:
                        print('У людей всегда настроение поднимается, когда со мной поговорят')
                    elif second_query in BAD:
                        print('Эх, веселее Вы не стали..')
                    elif second_query in ANGRY:
                        a = 'Медитация - вот выход'
                        print(a)
                    else:
                        print('Совесем перестал людей понимать')
        except second_query is None:
            print('Конец')
    else:
        print('Не понимаю Вас совсем')
        my_id = uuid.uuid1() # or uuid.uuid4()

       
        
        


