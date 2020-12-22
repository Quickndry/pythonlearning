indexposition = 0
accumulator = 0


def splitfile(textfile):
    with open(textfile) as document:
        lines = document.readlines()
        list_of_lines = [x.strip() for x in lines]
    return(list_of_lines)

def split_by_pattern(oneline):
    oneline_string = oneline[:5] + ' ' + oneline[5:]
    oneline_list = oneline_string.split(' ')
    return(oneline_list)

def splitlist(list_of_lines):
    list_of_oneliners = []
    for i in list_of_lines:
        list_of_oneliners.append(split_by_pattern(i))
    return list_of_oneliners

def bootupseq(list_of_oneliners):
    global indexposition
    global accumulator

    oneline = list_of_oneliners[indexposition]
    oneline.insert(0, str(indexposition))
    print(oneline)

    if len(oneline) > 4:
        print(accumulator)
        return(accumulator)

    else:
        if oneline[1] == 'acc':
            if oneline[2] == '-':
                accumulator -= int(oneline[3])
                indexposition += 1
                oneline.append('marker')
            else:
                accumulator += int(oneline[3])
                indexposition += 1
                oneline.append('marker')

        elif oneline[1] == 'jmp':
            if oneline[2] == '-':
                indexposition -= int(oneline[3])
                oneline.append('marker')
            else:
                indexposition += int(oneline[3])
                oneline.append('marker')

        else:
            indexposition += 1
            oneline.append('marker')

    bootupseq(list_of_oneliners)

list_of_lines = splitfile("bootup.txt")
list_of_oneliners = splitlist(list_of_lines)
bootupseq(list_of_oneliners)
