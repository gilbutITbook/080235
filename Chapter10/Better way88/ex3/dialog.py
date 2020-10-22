# dialog.py
import app

class Dialog:
    def __init__(self):
        ...
    
save_dialog = Dialog()
    
def show():
    ...

def configure():
    save_dialog.save_dir = app.prefs.get('save_dir')
