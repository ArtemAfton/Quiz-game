print("Привет! Если ты попал сюда, значит тебе предстоит пройти квиз\n"
      "Верю, что ты с ним справишься) Погнали!\n"
      "Ты очнулся в тёмном лесу, перед тобой лежат два предмета:\n"
      "1) Зажигалка\n"
      "2) Спички\n"
      "Что ты возьмёшь?\n"
      )
Win = "Победа"
Defeat = "Поражение"
artifact = input()
while artifact != "1" and artifact != "2":
      print("А ты хорошо знаешь свой язык, но нужно ввести цифру выбранного ответа\n")
      artifact = input()
if artifact == "1":
      print("Отлично! Теперь у тебя есть зажигалка!\n"
            "Перед тобой два пути\n"
            "Какой ты выберешь?\n"
            "1) Налево\n"
            "2) Направо\n")
      choice = input()
      while choice != "1" and choice != "2":
            print("Ясно, память рыбки Дори...\n"
                  "Введи цифру выбранного ответа\n")
            choice = input()
      if choice == "1":
            print("Ты решил пойти налево, но перед тобой открывается ещё 3 путей:\n"
                  "1) По тропинке\n"
                  "2) По дороге\n"
                  "3) Через чащу\n"
                  "Какой путь выберешь ты?\n")
            way = input()
            while way != "1" and way != "2" and way != "3":
                  print("Ошибки делают нас сильней, но не тебя видимо.\n"
                        "ПИШИ ЦИФРУ ВЫБРАННОГО ОТВЕТА.\n")
                  way = input()
            if way == "1":
                  print(
                        "Ты идёшь по тропинке, пытаешься зажечь зажигалку, "
                        "как вдруг ты скатываешься по небольшому склону к реке.\n"
                        "Справа ты видишь мост, соединяющий два берега.\n"
                        "Где то сзади доносятся рычания. Ты прячешься под мостом.\n"
                        "Вдалеке ты видишь, как волки бегут по дороге, и к счастью они тебя не замечают.\n"
                        "Ещё ты вспоминаешь, что эта река ведёт к знакомому тебе городку.\n")
                  print(Win)
            elif way == "2":
                  print("Ты идёшь по дороге, освещённой фонарями.\n"
                        "Но неожиданно все лампочки лопаются.\n"
                        "Ты слышишь многочисленные рычания сзади...")
                  print(Defeat)
            elif way == "3":
                  print("Ты зажигаешь зажигалку, но ветер вам постоянно мешает.\n"
                        "В течении нескольких часов ты так и не выбрался из леса.\n"
                        "Вы окончательно заблудились.\n"
                        )
                  print(Defeat)
      elif choice == "2":
            print("Ты решил пойти направо. Перед тобой два пути:\n"
                  "1) Дорога\n"
                  "2) Пещера\n"
                  "Какой путь выберешь ты?")
            way2 = input()
            while way2 != "1" and way2 != "2":
                  print("Всё потому что Дора...\n"
                        "Как же всё таки не хватает Таноса...\n"
                        "П И Ш И ЦИФРУ ВЫБРАННОГО ОТВЕТА!!!!!!!!!!!!\n")
                  way2 = input()
            if way2 == "1":
                  print("Ты идёшь по дороге, разжигая зажигалку. Получилось!\n"
                        "Потом ты поджёг ветку и дальше пошёл по дороге.\n"
                        "В итоге ты выбрался из леса!\n ")
                  print(Win)
            elif way2 == "2":
                  print("Ты идёшь в пещеру. Начало темнеть, и поэтому ты начал зажигать зажигалку\n"
                        "Ты делааешь это очень долго и довольно громко, но всё же тебе удаётся её зажечь.\n"
                        "Ты смотришь вперёд, а перед тобой стоит МИШКА ФРЕДЕ. Он съедает тебя\n")
                  print(Defeat)
elif artifact == "2":
      print("Отлично! Теперь у тебя есть спички!\n"
            "Перед тобой два пути\n"
            "Какой ты выберешь?\n"
            "1) Налево\n"
            "2) Направо\n")
      choice = input()
      while choice != "1" and choice != "2":
            print("Ясно, память рыбки Дори...\n"
                  "Введи цифру выбранного ответа\n")
            choice = input()
      if choice == "1":
            print("Ты решил пойти налево, но перед тобой открывается ещё 3 путей:\n"
                  "1) По тропинке\n"
                  "2) По дороге\n"
                  "3) Через чащу\n"
                  "Какой путь выберешь ты?\n")
            way = input()
            while way != "1" and way != "2" and way != "3":
                  print("Ошибки делают нас сильней, но не тебя видимо.\n"
                        "ПИШИ ЦИФРУ ВЫБРАННОГО ОТВЕТА.\n")
                  way = input()
            if way == "1":
                  print(
                        "Ты идёшь по тропинке, пытаешься разжечь спички одну за одной, "
                        "как вдруг ты скатываешься по небольшому склону к реке.\n"
                        "Справа ты видишь мост, соединяющий два берега.\n"
                        "Где то сзади доносятся рычания. Ты прячешься под мостом.\n"
                        "Вдалеке ты видишь, как волки бегут по дороге, и к счастью они тебя не замечают.\n"
                        "Ещё ты вспоминаешь, что эта река ведёт к знакомому тебе городку.\n")
                  print(Win)
            elif way == "2":
                  print("Ты идёшь по дороге, освещённой фонарями.\n"
                        "Но неожиданно все лампочки лопаются.\n"
                        "Ты слышишь многочисленные рычания сзади...")
                  print(Defeat)
            elif way == "3":
                  print("Ты разжигаешь спички, но ветер тебе постоянно мешает.\n"
                        "В течении нескольких часов ты так и не выбрался из леса.\n"
                        "Ты окончательно заблудился.\n"
                        )
                  print(Defeat)
      elif choice == "2":
            print("Ты решил пойти направо. Перед тобой два пути:\n"
                  "1) Дорога\n"
                  "2) Пещера\n"
                  "Какой путь выберешь ты?")
            way2 = input()
            while way2 != "1" and way2 != "2":
                  print("П И Ш И ЦИФРУ ВЫБРАННОГО ОТВЕТА!!!!!!!!!!!!\n")
                  way2 = input()
            if way2 == "1":
                  print("Ты идёшь по дороге, разжигая спички. Получилось!\n"
                        "Потом ты поджёг ветку и дальше пошёл по дороге.\n"
                        "В итоге ты выбрался из леса!\n ")
                  print(Win)
            elif way2 == "2":
                  print("Ты идёшь в пещеру. Начало темнеть, и поэтому ты начал зажигать спички\n"
                        "Ты делааешь это очень долго и довольно громко, но всё же тебе удаётся их зажечь.\n"
                        "Ты смотришь вперёд, а перед тобой стоит МИШКА ФРЕДЕ. Он съедает тебя\n")
                  print(Defeat)

