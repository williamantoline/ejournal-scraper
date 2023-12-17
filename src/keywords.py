import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import config


primary_keywords = config.primary_keywords.split(",")
filepath = config.storage_path
min_freq = config.minimum_frequency


def writeResult(file, map, x, y):
    for key in map.keys():
        if (map[key] > min_freq):
            file.write(str(key) + "," + str("{:.2f}%".format(map[key] / x * 100)) 
            + "," + str("{:.2f}%".format(map[key] / y * 100)) + "\n")


def exec(filename):
    input_file = filepath + str(filename) + ".titles.txt"
    primaries = secondaries = {}
    x = y = 0

    with open(input_file, "r") as file:
        for row in file:
            if (len(row) == 0):
                continue
            x += 1
            words = row[2:len(row)-2].lower().split()
            for word in words:
                y += 1
                if word in primary_keywords:
                    if word in primaries:
                        primaries[word] += 1
                    else:
                        primaries[word] = 1
                else:
                    if word in secondaries:
                        secondaries[word] += 1
                    else:
                        secondaries[word] = 1

    primaries = dict(sorted(primaries.items(), key=lambda item: item[1], reverse=True))
    secondaries = dict(sorted(secondaries.items(), key=lambda item: item[1], reverse=True))

    with open(filepath + str(filename) + ".keywords.txt", "w") as file:
        file.write("word,n / articles,n / words\n")
        writeResult(file, primaries, x, y)
        writeResult(file, secondaries, x, y)
