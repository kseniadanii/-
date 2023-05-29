import os

from pydub import AudioSegment


# Функция для изменения скорости воспроизведения файла
def change_speed(file_path, speed):
    # Загрузка аудиофайла
    sound = AudioSegment.from_wav(file_path)
    # Изменение скорости воспроизведения
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    })
    # Экспорт измененного аудиофайла
    file_name, file_extension = os.path.splitext(file_path)
    new_file_path = file_name + "_изменение_скорости" + file_extension
    sound_with_altered_frame_rate.export(new_file_path, format="wav")
    print("Файл успешно сохранен:", new_file_path)


# Пример использования функции
file_path = "C:/Users/user/Downloads/песня.wav"
speed = 1.5  # Ускорить воспроизведение в 1.5 раза
change_speed(file_path, speed)
