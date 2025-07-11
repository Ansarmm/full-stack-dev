# Финальный прооект devcore 106

---
>
>
```

```

## Пошаговый путь:
>Перейти в отдельную ветку для этого проекта
>
```
git checkout -b final-project
``` 
---
>Создать первоначальную структуру проекта
```
git add .
git commit -m "initial structure"
```
---
>Добавить новую песню
>
```
git add music-library.txt
git commit -m "Add If We Have Each Other by Alec Benjamin"
```
---
>Добавить еще одну песню
>
```
git add music-library.txt
git commit -m "Add Match In The Rain by Alec Benjamin"
```
---
>Забыл добавить README
>
```
git add README.md
git commit -m amend
```
---
>Сделал коммит но забыл добавить файл в индекс
>
```
git add music-library.txt
git commit --amend --no-edit
```
---
>Мне нужно сделать git pull, но я имею изменения которые хотел бы сохранить.
>
```
git stash
```
---
>Проверил что я сделал stash правильных данных
>
```
git stash apply
git stash
```
---
>Перенести данные
>
```
git pull
git stash pop
```
---
>Cherry-pick из другой ветки
>
```
git checkout -b feature-branch
git add main.py 
git commit -m "Add main.py with welcome message"
git add main.py
git commit -m "Add new feature release alert"
git add main.py
git commit -m "Add new feature"
git checkout final-project
git cherry-pick 2614c7a
git cherry-pick a69d585
```
---
>Rebase 3 коммитов. Это полезно когда нужно объединить 3 изменения в 1 завершенный коммит.
>
```
echo "Title: Swim | Artist: Alec Benjmain | Album: Narrated For You" >> music-library.txt
git add music-library.txt
git commit -m "Add Swim by Alec Benjamin"

echo "Title: Older | Artist: Alec Benjamin | Album: (Un)Commentary" >> music-library.txt
git add music-library.txt
git commit -m "Add Older by Alec Benjamin"

echo "Title: 1994 | Artist: Alec Benjamin | Album: Narrated For You" >> music-library.txt
git add music-library.txt
git commit -m "Add 1994 by Alec Benjamin"

git rebase-i main
```
