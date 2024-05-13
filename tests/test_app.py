"""Tests the GUI app"""
import os
from tkinter import Tk, Canvas
from unittest.mock import MagicMock
import pytest
# from tkinter.messagebox import showinfo
from chrom import main_paint, activate_paint, paint, change_color, delete

if os.environ.get('DISPLAY','') == '':
        # print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')
    
@pytest.fixture
def app():
    root = Tk()
    cv = Canvas(root, width=640, height=480, bg='white')
    cv.pack()
    main_paint()
    yield root
    root.destroy()


def test_activate_paint():
    root=Tk()
    cv = Canvas(root, width=640, height=480, bg='white')
    event = MagicMock()
    event.x, event.y = 50, 50
    activate_paint(event)
    assert cv.bind.called_with('<B1-Motion>', paint)

def test_change_color():
    global current_color, initial_color
    initial_color = current_color
    change_color('blue')
    assert current_color == 'blue'

def test_delete():
    root=Tk()
    cv = Canvas(root, width=640, height=480, bg='white')
    delete()
    assert cv.delete("all")

def test_color_buttons():
    global current_color
    color_buttons = app.children['!frame'].winfo_children()
    for btn in color_buttons:
        btn.invoke()
        assert current_color == btn['bg']
