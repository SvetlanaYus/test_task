import emoji
import uuid
import datetime


# id = []
# print(my_id)
# print(emoji.demojize('😬'))
# time = str(datetime.datetime.now())[11:]
# time = time.split(':')



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
    time = ''.join(time)
    time = time.split('.')
    time = time[0]
    if message_dem in GOOD:
        print('Привет! Как хорошо, когда у человека хорошее настроение!')
        try:
            second_query = input()
            second_query = emoji.demojize(second_query)
            time_2 = str(datetime.datetime.now())[11:]
            time_2 = time_2.split(':')
            time_2 = ''.join(time_2)
            time_2 = time_2.split('.')
            time_2 = time_2[0]
            if int(time_2) - int(time) < 100:
                if second_query in GOOD:
                    print('Хорошо, когда настреоние всегда на высоте!')
                elif second_query in BAD:
                    print('Переменчивое у Вас настроение')
                elif second_query in ANGRY:
                    print('Думаю, Вам стоит помедитировать, вся злость испарится')
                else:
                    print('Совсем не понимаю людей')
            
        except second_query is None:
            my_id = uuid.uuid1()

    elif message_dem in BAD:
        print('Привет! Видимо, у Вас что-то стряслось. Не грустите')
        try:
            second_query = input()
            second_query = emoji.demojize(second_query)
            time_2 = str(datetime.datetime.now())[11:]
            time_2 = time_2.split(':')
            time_2 = ''.join(time_2)
            time_2 = time_2.split('.')
            time_2 = time_2[0]
            if int(time_2) - int(time) < 100:
                if second_query in GOOD:
                    print('Вау! Я рад, что Вы стали бодрее')
                elif second_query in BAD:
                    print('А ну не раскисать')
                elif second_query in ANGRY:
                    print('Не думал я, что разгвооры со мной так влияют на настреоние...')
                else:
                    print('Совсем перестал понимать человека')
            
        except second_query is None:
            my_id = uuid.uuid1()
    elif message_dem in ANGRY:
        print('Ну привет, человек не в настроении')
        try:
            second_query = input()
            second_query = emoji.demojize(second_query)
            time_2 = str(datetime.datetime.now())[11:]
            time_2 = time_2.split(':')
            time_2 = ''.join(time_2)
            time_2 = time_2.split('.')
            time_2 = time_2[0]
            if int(time_2) - int(time) < 100:
                if second_query in GOOD:
                    print('У людей всегда настроение поднимается, когда со мной поговорят')
                elif second_query in BAD:
                    print('Эх, веселее Вы не стали..')
                elif second_query in ANGRY:
                    print('Медитация - вот выход')
                else:
                    print('Совсем перестал людей понимать')
                    
        except second_query is None:
            my_id = uuid.uuid1()
    else:
        print('Не понимаю Вас совсем, но здравствуйте')
        my_id = uuid.uuid1() # or uuid.uuid4()

       
        
        


