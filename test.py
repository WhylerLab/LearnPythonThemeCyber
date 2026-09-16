text = "Python Java Python Ruby Java Python C++"


def dicWordCounter(text):
    newlist =  text.split()

    newdic = {}


    for words in newlist:
        count = 0 
        for word in newlist:
            if word == words:
                count += 1

        newdic[words] = count

    return newdic




result = dicWordCounter(text)
print(result)