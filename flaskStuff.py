from flask import Flask, render_template, request
from otherFunc import getSubbed, getLists, addSubbed, addList, rmList, rmSubbed, getAllVideos, getVidColNums

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('mainpage.html', chanNamesList=getSubbed(), playNamesList=getLists())

@app.route('/add', methods=['GET', 'POST'])
def add():
    return render_template('addpage.html')

@app.route('/addthanks', methods=['POST'])
def thanks():
    inputType = request.form['type']
    if inputType == 'Channel':
        addSubbed(request.form['URL'], request.form['name'])
    elif inputType == 'Playlist':
        addList(request.form['URL'], request.form['name'])
    else:
        print('error: input type is not playlist or channel')

    return render_template('thanks.html')

@app.route('/rm', methods=['GET', 'POST'])
def rm():
    return render_template('removepage.html', chanNamesList=getSubbed(), playNamesList=getLists())

@app.route('/rmthanks', methods=['GET', 'POST'])
def rmthanks():
    inputType = request.form['type']

    if inputType == 'channel':
        chanNamesList=getSubbed()
        for chanName in chanNamesList:
            try:
                chan =  request.form['channel_' + chanName]
                rmSubbed(chan)
            except:
                print(chanName + " stays")
    elif inputType == 'playlist':
        playNamesList=getLists()
        for playName in playNamesList:
            try:
                play = request.form['playlist_' + playName]
                rmList(play)
            except:
                print(playName + " stays")
    else:
        print("error: remove type is not playlist or channel")
    
    return render_template('thanks.html')

@app.route('/channel/<name>')
def channel(name):
    return render_template('channelvideos.html', embedDict=getVidColNums(getAllVideos(name)))

if __name__ == '__main__':
    app.run(debug=True)