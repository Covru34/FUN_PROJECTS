def writeTextSong():
    singer = input("Вкажіть автора: ")
    songName = input("Вкажіть назву пісні: ")
    line1 = input("Напишіть перший рядок тексту: ")
    line2 = input("Напишіть другий рядок тексту: ")
    line3 = input("Напишіть третій рядок тексту: ")

    with open("Song_Info.txt", "a", encoding="utf-8") as fileWriter:
        fileWriter.write(f"{singer}\n")
        fileWriter.write(f"{songName}\n")
        fileWriter.write(f"{line1}\n")
        fileWriter.write(f"{line2}\n")
        fileWriter.write(f"{line3}\n")

def clearTextSong():
    fileWriter = open("Song_Info.txt", "w", encoding="utf-8")
    fileWriter.close()

def readTextSong():
    with open("Song_Info.txt", "r", encoding="utf-8") as fileRead:
        lines = fileRead.read().splitlines()

    i = 0
    lines_per_song = 5  # автор + назва + 3 рядки тексту
    countSong = 1
    countLines = len(lines)

    while i + lines_per_song <= countLines:
        print(f"***{countSong}***\n")
        print("---Автор---")
        print(f"--->{lines[i]}<---")
        print("---Пісня---")
        for j in range(1, lines_per_song):
            print(lines[i+j])
        print("\n")
        
        i += lines_per_song
        countSong += 1

action = -1
while action!=0:
    print("0>Вихід")
    print("1>Додати пісню")
    print("2>Показати усі пісні")
    print("3>Очистити усі пісні")
    print("->_", end="")
    action = int(input())
    match action:
        case 1:
            writeTextSong()
            print("---Додали нову пісню---")
        case 2:
            print("---Показуємо усіх абонентів---\n")
            readTextSong()
        case 3:
            clearTextSong()
            print("---Очистили весь список---")