from evernote.api.client import EvernoteClient
from evernote.edam.notestore.ttypes import NoteFilter, NotesMetadataResultSpec

filter = NoteFilter()
fieldsNeeded = NotesMetadataResultSpec(includeTitle=True,includeAttributes=True)
dev_token = "S%3Ds1%3AU%3D96499%3AE%3D17f184c54aa%3AC%3D177c09b24e8%3AP%3D1cd%3AA%3Den-devtoken%3AV%3D2%3AH%3Daed1f40bb587994c176d8bf2855879db"
client = EvernoteClient(token=dev_token)
userStore = client.get_user_store()
user = userStore.getUser()
noteStore = client.get_note_store()
notebooks = noteStore.listNotebooks()
notes = noteStore.findNotesMetadata(filter,0,10,fieldsNeeded)
print user.username
for n in notebooks:
    print n.name

for n in notes.notes:
    print n.guid , n.title , n.created
    note = noteStore.getNote( n.guid,True,False,False,False)
    print note.content


def print_hi(name):

    print 'Hi, ' + name


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
