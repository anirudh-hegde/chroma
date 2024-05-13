"""Tests the GUI app"""
import os
from tkinter import Tk, Canvas
from unittest.mock import MagicMock
import pytest
from chrom import main_paint, activate_paint, paint, change_color, delete
    
@pytest.fixture
def app():
    """tests the app"""
    root = Tk()
    cv = Canvas(root, width=640, height=480, bg='white')
    cv.pack()
    main_paint()
    yield root
    root.destroy()


def test_activate_paint():
    """tests activation of paint"""
    root=Tk()
    cv = Canvas(root, width=640, height=480, bg='white')
    event = MagicMock()
    event.x, event.y = 50, 50
    activate_paint(event)
    assert cv.bind.called_with('<B1-Motion>', paint)

def test_change_color():
    """tests change in color"""
    global current_color, initial_color
    initial_color = current_color
    change_color('blue')
    assert current_color == 'blue'

def test_delete():
    """tests the delete all"""
    root=Tk()
    cv = Canvas(root, width=640, height=480, bg='white')
    delete()
    assert cv.delete("all")

def test_color_buttons():
    """tests the color button"""
    global current_color
    color_buttons = app.children['!frame'].winfo_children()
    for btn in color_buttons:
        btn.invoke()
        assert current_color == btn['bg']
