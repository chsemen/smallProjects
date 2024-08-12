# smallProjects 2

Подключение через ssh к репозитории
1. Генерация ключей 
ssh-keygen -t rsa -b 4096 -C "ch-semen@rambler.ru" 
или с указанием имени файла
ssh-keygen -t rsa -b 4096 -C "ch-semen@rambler.ru" -O C:\Users\semen/.ssh/id_rsa2

2. Войти в репозиторий, например, chsemen/smallProjects, выбрать Setting
Выбрать Deploy key и добавить там открытый ключ.

3. Клонирование удаленной репозитории в локальную папку, если несколько ключей
git clone git@github.com:chsemen/smallProjects.git -c core.sshCommand="ssh -i C:/Users/semen/.ssh/id_rsa2"