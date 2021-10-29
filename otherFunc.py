import re
import requests

def getSubbed():
    try:
        allChanName = open('C:\\Users\\dlneh\\Documents\\home\\cs projects\\me_tube\\channelnames.txt')
        chanLinksList = allChanName.readlines()
        allChanName.close()

        namesList = []
        for info in chanLinksList:
            namesList.append(info.split('==')[0])

        return namesList

    except:
        allChanName = open('C:\\Users\\dlneh\\Documents\\home\\cs projects\\me_tube\\channelnames.txt', 'x')
        allChanName.close()
        return []


def getLists():
    try:
        allPlayName = open('C:\\Users\\dlneh\\Documents\\home\\cs projects\\me_tube\\playlistnames.txt')
        playLinksList = allPlayName.readlines()
        allPlayName.close()

        namesList = []
        for info in playLinksList:
            namesList.append(info.split('==')[0])

        return namesList

    except:
        allPlayName = open('C:\\Users\\dlneh\\Documents\\home\\cs projects\\me_tube\\playlistnames.txt', 'x')
        allPlayName.close()
        return []


def addSubbed(URL, name):
    allChanName = open('C:\\Users\\dlneh\\Documents\\home\\cs projects\\me_tube\\channelnames.txt', 'a')
    allChanName.write(name + "==" + URL + "\n")
    allChanName.close()


def addList(URL, name):
    allChanName = open('C:\\Users\\dlneh\\Documents\\home\\cs projects\\me_tube\\playlistnames.txt', 'a')
    allChanName.write(name + "==" + URL + "\n")
    allChanName.close()


def rmSubbed(name):
    allChanName = open('C:\\Users\\dlneh\\Documents\\home\\cs projects\\me_tube\\channelnames.txt', 'r')
    lines = allChanName.readlines()
    allChanName = open('C:\\Users\\dlneh\\Documents\\home\\cs projects\\me_tube\\channelnames.txt', 'w')
    for line in lines:
        if line.split('==')[0] != name:
            allChanName.write(line)
    allChanName.close()


def rmList(name):
    allChanName = open('C:\\Users\\dlneh\\Documents\\home\\cs projects\\me_tube\\playlistnames.txt', 'r')
    lines = allChanName.readlines()
    allChanName = open('C:\\Users\\dlneh\\Documents\\home\\cs projects\\me_tube\\playlistnames.txt', 'w')
    for line in lines:
        if line.split('==')[0] != name:
            allChanName.write(line)
    allChanName.close()


def getVideosLink(name):
    allChanName = open('C:\\Users\\dlneh\\Documents\\home\\cs projects\\me_tube\\channelnames.txt')
    
    while True:
        line = allChanName.readline()
        if line.split('==')[0] == name:
            return line.split('==')[1]


def getListsLink(name):
    allPlayName = open('C:\\Users\\dlneh\\Documents\\home\\cs projects\\me_tube\\playlistnames.txt')
    
    while True:
        line = allPlayName.readline()
        if line.split('==')[0] == name:
            return line.split('==')[1]


def getAllVideos(name):
    link = getVideosLink(name)
    r = requests.get(link)
    info = r.text
    
    findLinks = re.compile('"gridVideoRenderer":\{"videoId":"[a-zA-Z0-9]+","')
    allLinks = re.findall(findLinks, info)

    vidEmbed = []
    for link in allLinks:
        id = link.split('"')[5]
        vidEmbed.append('https://www.youtube.com/embed/' + id)

    return vidEmbed
    

def getVidColNums(embedList):
    numCol = 5   # 5 columns in video page
    counter = 0
    colDict = {}
    for link in embedList:
        colDict[link] = (counter % numCol) + 1
        counter += 1
    
    return colDict


    


