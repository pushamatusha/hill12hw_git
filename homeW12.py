import os
import string
import shutil

from HomeWork12.films_titles import films_titles
from HomeWork12.films_awards import films_awards

os.mkdir("Harry Potter") # Директорія Гаррі Поттер

for film in films_titles["results"]:
    film_title = film["title"].replace(":", "")
    film_directory = os.path.join("Harry Potter", film_title)
    os.mkdir(film_directory)
    print(f"Створено дерикторію '{film_title}'") # Папки з назв фільмів

for film in films_titles["results"]:
    film_title = film["title"].replace(":", "")
    film_directory = os.path.join("Harry Potter", film_title)

    for letter in string.ascii_uppercase:
        letter_directory = os.path.join(film_directory, letter)
        os.mkdir(letter_directory) # папки за алфавітом в папках з фільмами

# список нагород для кожного фільму...
list_name = []
for film in films_awards:
    for mv in film['results']:
      if mv['movie']['imdb_id'] == id:
        list_name.append({'type': mv['type'],
                      'award_name': mv['award_name'],
                      'award': mv['award']
                      })
list_name = list(sorted(list_name, key = lambda fil_aw: fil_aw['award_name']))

# далі я створюю файл з даними тхт,відкриваю, записую, закриваю.
for name_award in list_name:
    if os.path.isfile(name_award['award_name'] + '.txt'):
      name_award_obj = open(name_award['award_name']+'.txt', 'a')
      name_award_obj.write(name_award['award'] + '\n')
      name_award_obj.close()
    else:
      name_award_obj = open(name_award['award_name']+'.txt', 'w')
      name_award_obj.write(name_award['award'] + '\n')
      name_award_obj.close()

# гуляю по списку за алфавітом
    aw_list = list(os.walk('.'))
    for awards_file in aw_list[0][2]:
        for letter in string.ascii_uppercase:
            if awards_file.startswith(letter): # переношу файл в папку з літерами
                shutil.move(os.path.abspath(awards_file), letter)

# чи тут теж треба відкривати і закривати кожну папку...








