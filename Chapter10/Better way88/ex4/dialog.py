# dialog.py
class Dialog:
    def __init__(self):
        ...
    
save_dialog = Dialog()
    
def show():
    import app # 동적 임포트
    save_dialog.save_dir = app.prefs.get('save_dir')
    ...