from django.test import TestCase

# Create your tests here.
# manage.py shell
# User.objects.create_user("Mike")
# User.objects.create_user("Nick")
#
# Author.objects.create(user='Mike')
# Author.objects.create(user='Nick')
#
# Category.objects.create(name='Politics')
# Category.objects.create(name='Sport')
# Category.objects.create(name='Wasteland')
# Category.objects.create(name='Humor')
#
# news1 = Post.objects.create(author='Mike', choise='NE', title='Courier', text='Курьер, которого нашли с выстрелом в голову возле'
#                                                                       ' Гудспрингс, как сообщается, пришел в сознание и даже'
#                                                                       'полностью выздоровел. Курьер на которого действительно'
#                                                                       ' можно положиться!')
#
# art1 = Post.objects.create(author='Mike', choise='AR', title='За Республику, часть 2 - Мистер Хаус и Братство Стали и концовка',
#                     text="Мистер Хаус Полковник Мур поведает игроку, что она хочет убрать мистера Хауса. Для этого идите в Лаки 38 и поднимитесь на лифте до пентхауса. Используйте терминал, который находится слева от Хауса. Это откроет потайную дверь, ведущую в \"сердце\" Мистера Хауса. Чтобы взломать данный терминал вам потребуется 75 Науки или VIP-карта Лаки 38 (ее можно найти у Хенлона в лагере Гольф или на Заводе «Эйч-энд-Эйч тулз»), или же использовав платиновую фишку). Как только вы вы взломаете терминал, секьюритроны нападут на вас. Дальнейшие ваши действия приведут к потери возможности выполнить квест \"Казино всегда в выигрыше\". Войдите в открывшуюся комнату и активируете терминал возле лифта, это откроет вам доступ к Центру управления.   Активируйте терминал в центре управления и выберите в нем пункт \"Распечатать камеру\", чтобы вывести капсулу с телом Хауса. Далее, поговорите с ним. Возвращайтесь обратно к терминалу и выберите один из двух вариантов: Провести дезинфекцию капсулы (это отключит Хауса, но не убьет его) Отключить систему жизнедеятельности (это убьет Хауса) После того как вы приняли решение, возвращайтесь к полковнику Мур на дамбе Гувера. Игрок получит 200 очков опыта и репутацию НКР. (Секьюритроны больше не будут атаковать вас, если вы зайдете в пентхаус). Братство Стали Направляйтесь в бункер Хидден-Вэли в локации Хидден-Вэли. Хорошая репутация у Братства Стали Если игрок уже ранее имел отношения с Братством и выполнил задание \"В неведении\", то можно легко договориться о союзе Братства Стали с НКР. Подойдите к старейшине Макнамара и скажите ему, что НКР хочет их уничтожит. Он предложит перемирие с НКР. Возвращайтесь к полковнику Мур и расскажите ей, что Братство предлагает перемирие. Это позволит вам закончить данный квест и начать \"Ты почувствуешь приближение\". Вполне возможно, что вы не сможете поговорить с Макнамарой (будет появляться что-то типа Сейчас старейшина не сможет поговорить с вами, так как он слишком занят). Это решается следующим образом: выйдите из бункера и подождите примерно 3 дня. После этого попробуйте снова поговорить со старейшиной. Если и это не помогло, то воспользуйтесь командой в консоли \"set000E327C.LockdownLifted to 1\", это возобновит заново диалог. Если Хардин стал старейшиной, то не возможно будет получить положительного итога квеста. Если вы поговорите с НКР возле бункера Братства, то Мур разозлится и вы получите за это задание плохую репутацию у НКР. Не было связи с Братством Стали Если у вас не было никаких связей с Братством до этого задания, то вы должны будете уговорить рейнджера НКР не приближаться к бункеру или же возьмите с собой Веронику в спутники.  Если подождете до поздней ночи возле бункера, то к вам выйдет несколько паладинов. У них вы можете украсть карточку для входа в бункер (при этом карма не должна понизиться). Войдите в бункер, используя карточку. И с вами поговорит страж. Он попросит вас сдать им оружие. Если вы не сдадите свое оружие, то Братство будет относиться к вам враждебно. Однако если вы используете стелс-бой перед разговором со стражем и также не захотите сдать свое оружие, то сможете пробраться вглубь бункера без ущерба для своего здоровья. Далее направляйтесь на уровень 2 и убейте там любого писца и наденьте его одежду, тогда вы сможете выглядеть как писец Братства (при этом репутация Братства сделается нейтральной). Игрок может убить всех в бункере, чтобы собрать карточки для активации самоуничтожения бункера.  Обратите внимание, что некоторые члены Братства, имеющие высокий чин, например, старейшины, распознают вас независимо от того одеты ли вы в писца или нет.   Если Вероника ваш спутник, то Братство не станет к вам враждебным. Даже если вы одеты как гражданин НКР.  Если игрок предупреждает Рейнджера о Братстве, то, зайдя в бункер, игрок будет убит. Если репутация НКР у вас маленькая, то рейнджер не захочет с вами говорить и вам придется убить его по поручению Харленда.  Найдите ключ-карту Как только вы получили расположение Братства вы можете войти в бункер. Как только вы вошли туда. Вам нужно будет найти 3 ключ-карты, для того чтобы получить пароль к функции самоуничтожению бункера или вы можете использовать 100 Науки чтобы взорвать бункер. Вы должны будете войти на уровень 2 и там вы найдете старейшину Макмарана, паладина Хардина (или паладина Рамоса, в зависимости от вашего выбора) и писца Ларса Таггарта. У старейшины легче всего украсть ключ-карту, так как он сидит в своем кресле. Хардина можно найти в одной из трех спален бункера, там он будет стоять или сидеть за своим компьютером. Украдите у него карту. Далее вернитесь на уровень 1 и пройдите вперед до левого коридора и зайдите в комнату Самоуничтожения бункера, где вы можете найти Таггарта. Вам понадобится стелс-бой, чтобы украсть у него ключ-карту. Если у вас нет стелс-боя, то вам придется подождать пока девушка в этой комнате не отвернется или не отойдет.  Если Кэсс находится у вас в спутниках, то она начнет говорить с этой девушкой, ну а вы в свою очередь сможете спокойно украсть карту.  Активация самоуничтожения бункера Как только вы получили все ключ-карты, возвращайтесь в комнату, где вы нашли Таггарта и получите код в терминале генераторе ключей (зеленый терминал), рядом с терминалом для самоликвидацией (синий терминал). Далее, используйте полученный код для активации самоликвидации бункера. После этого вы станете врагом Братства. Обязательно перед уничтожением бункера украдите у охранника старейшины ключ, чтобы вы смогли покинуть бункер. Если вы не украдете ключ, то вам придется взламывать дверь бункера (требуется 100 Взлома). Теперь, включите самоуничтожение и направляйтесь на уровень 1.  Как только вы выйдите из бункера, он взорвется, и возможно, что возле бункера вас будут поджидать члены Братства, перед тем как вы вернетесь к Мур.  Альтернативный вариант: вы можете легко пройти квест, если вы просто убьете всех внутри бункера. Можно только убить главных членов Братства Стали и квест все равно будет считаться выполненным.  Защита президента Кимбола Мур попросит вас поговорить с рейнджером Грантом о защите Кимбола, во время его визита на дамбу Гувера. Так начнется квест \"Ты почувствуешь приближение\". Вернитесь к полковнику Мур и скажите ей, что вы готовы сражаться за НКР.  Ваши действия таковы:  Залезьте в карман к подозрительному персонажу, недавно вошедшего в эту локацию, и там вы увидите отказоустойчивое взрывное устройство. Возьмите его и отдайте его Гранту. После этого Грант скажет, что его рейнджеры разберутся с ним, но как только они подойдут к нему, он убьет одного из рейнджеров, тем самым вызовет панику. (если вы поговорите с Грантом, то он может вам дать полный доступ к дамбе, но для этого вы должны быть кумиром НКР. Данный доступ позволит вам пройти на вертолетную площадку и использовать свое оружие на территории дамбы). Если вы оставите в покое этого подозрительно человека во время выступления Гранта, то снайпер легиона убьет рейнджера на первой башне [первый за президентом] и попробует убить президента. Убейте его и скажите Гранту по рации о покушении на президента. Он отменит выступление. Если президент в данный момент эвакуирован, то на него нападет член Легиона, под видом инженера. Его нужно убить до того как он достигнет президента, так как он сможет убить его с одного удара. Поднимайтесь на вертолётную площадку и ждите прибытия президентского винтокрыла. Появится инженер и заминирует винтокрыл. Взаимодействуйте с винтокрылом и выберите «осмотреть» для того чтобы найти бомбу. Обезвредьте бомбу, либо стащите детонатор из кармана инженера. Бегите вниз и доложите Гранту. Он прервёт речь президента, промажет и попадёт в рейнджера. После чего Президент бросится к винтокрылу и улетит. Это завершит квест. Поговорите с таинственным инженером и он сразу же станет враждебным. Убейте его. Если Рекс является вашим спутником идите на крышу. Вы увидите техника рядом с дверью на лестницу. Заговорите с ним и выберите опцию, связанную с Рексом. После предложите ему пройти с вами. Техник станет враждебным и вы можете его убить без потери репутации (или позволить рейнджерам убить его). Снимите с тела аварийный детонатор и возвращайтесь к Гранту. Квест выполнен. Кроме того, если у вас имеется перк \"Друг животных (1)\", то вы сможете взять с собой в помощь несколько собак НКР, находящихся рядом с дамбой."
#
# art2 = Post.objects.create(author='Nick', choise='AR', title='Большая гора', text='Снежный шар можно найти на метеорологической станции X-17. В поселении Хиггса следуйте по подиуму, который приведет в комнату с терминалом, который используется для активации теста погоды. Снежный шар будет расположен на консоли компьютеря прямо напротив входа.')
#
