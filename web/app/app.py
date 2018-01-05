from flask import Flask, request, jsonify
from mongoengine import *
import datetime 

app = Flask(__name__)


connect(db='demo', host='demo_db')


class Note(Document):
    content = StringField()
    created_at = DateTimeField()


@app.route('/api/note', methods=['POST', 'DELETE', 'GET'])
def note_api():
    if request.method == 'POST':
    	content = request.form.get('content', None)
    	item = Note(content=content, created_at=datetime.datetime.now())
    	item.save()

    	notes = Note.objects()
    	note_list = []
    	for note in notes:
    		note_dict = {}
    		note_dict['content'] = note.content
    		note_dict['created_at'] = note.created_at
    		note_list.append(note_dict)
    	return jsonify({'notes':note_list})

    if request.method == 'GET':
    	notes = Note.objects()
    	note_list = []
    	for note in notes:
    		note_dict = {}
    		note_dict['content'] = note.content
    		note_dict['created_at'] = note.created_at
    		note_list.append(note_dict)
    	return jsonify({'notes':note_list})

    if request.method == 'DELETE':
    	Note.drop_collection()
    	return jsonify({'result':'ok'})



