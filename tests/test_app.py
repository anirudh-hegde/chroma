import pytest
from tkinter import Tk, Canvas, Button
from tkinter.messagebox import showinfo
from unittest.mock import MagicMock
from chrom import main_paint, activate_paint, paint, change_color, delete
import os

@pytest.fixture
def app():
    if os.environ.get('DISPLAY','') == '':
        print('no display found. Using :0.0')
        os.environ.__setitem__('DISPLAY', ':0.0')
    root = Tk()
    cv = Canvas(root, width=640, height=480, bg='white')
    cv.pack()
    main_paint()
    yield root
    root.destroy()

root=Tk()
cv = Canvas(root, width=640, height=480, bg='white')

def test_activate_paint(app):
    event = MagicMock()
    event.x, event.y = 50, 50
    activate_paint(event)
    assert cv.bind.called_with('<B1-Motion>', paint)

def test_paint(app):
    event = MagicMock()
    event.x, event.y = 100, 100
    paint(event)
    assert cv.create_line.called

def test_change_color(app):
    global current_color
    initial_color = current_color
    change_color('blue')
    assert current_color == 'blue'

def test_delete(app):
    delete()
    assert cv.delete.called

def test_color_buttons(app):
    color_buttons = app.children['!frame'].winfo_children()
    for btn in color_buttons:
        btn.invoke()
        assert current_color == btn['bg']
