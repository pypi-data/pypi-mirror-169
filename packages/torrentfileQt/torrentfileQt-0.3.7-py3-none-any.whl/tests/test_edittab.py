#! /usr/bin/python3
# -*- coding: utf-8 -*-

##############################################################################
# Copyright 2020 AlexPDev
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##############################################################################
"""Module for testing procedures on Check Tab."""

import pyben
import pytest

from tests import MockEvent, dir1, dir2, proc_time, ttorrent, wind


def test_fixtures():
    """Test fixtures."""
    assert dir1 and dir2 and ttorrent and wind


@pytest.mark.parametrize("field", ["announce", "name", "private", "comment"])
def test_editor_torrent_loading(field, wind, ttorrent):
    """Testing editor widget functionality."""
    editor = wind.central.editorWidget
    editor.window.central.setCurrentWidget(editor)
    param = (ttorrent, None)
    editor.fileButton.browse(param)
    proc_time()
    fields = []
    for i in range(editor.table.rowCount()):
        fields.append(editor.table.item(i, 0).text())
    assert field in fields


def test_editor_torrent_saving(wind, ttorrent):
    """Testing editor widget saving functionality."""
    editor = wind.central.editorWidget
    editor.window.central.setCurrentWidget(editor)
    proc_time()
    param = ttorrent, None
    editor.fileButton.browse(param)
    for i in range(editor.table.rowCount()):
        item1 = editor.table.item(i, 0)
        item2 = editor.table.item(i, 1)
        if item1.text() == "announce":
            item2.setText("other")
            break
    proc_time()
    editor.button.click()
    meta = pyben.load(ttorrent)
    assert meta["announce"] == "other"


def test_editor_accept_method(wind, ttorrent):
    """Test drag enter event on editor widget."""
    editor = wind.central.editorWidget
    editor.window.central.setCurrentWidget(editor)
    proc_time()
    event = MockEvent(ttorrent)
    assert editor.dragEnterEvent(event)
    event = MockEvent(None)
    assert not editor.dragEnterEvent(event)


def test_editor_move_event(wind, ttorrent):
    """Test move event on editor widget."""
    editor = wind.central.editorWidget
    editor.window.central.setCurrentWidget(editor)
    proc_time()
    event = MockEvent(ttorrent)
    assert editor.dragMoveEvent(event)
    event = MockEvent(None)
    assert not editor.dragMoveEvent(event)


def test_editor_drop_event(wind, ttorrent):
    """Test drop event on editor widget."""
    editor = wind.central.editorWidget
    editor.window.central.setCurrentWidget(editor)
    proc_time()
    event = MockEvent(ttorrent)
    assert editor.dropEvent(event)


def test_editor_drop_false(wind):
    """Test drop event on editor widget is false."""
    editor = wind.central.editorWidget
    editor.window.central.setCurrentWidget(editor)
    proc_time()
    event = MockEvent(None)
    assert not editor.dropEvent(event)


def test_editor_table_fields(wind, ttorrent):
    """Test the edit fields of table widget."""
    editor = wind.central.editorWidget
    editor.window.central.setCurrentWidget(editor)
    proc_time()
    table, found = editor.table, 0
    editor.line.setText(ttorrent)
    table.handleTorrent.emit(ttorrent)
    for i in range(table.rowCount()):
        if table.item(i, 0):
            txt = table.item(i, 0).text()
            if txt in ["httpseeds", "url-list", "announce-list"]:
                wig, found = table.cellWidget(i, 1), found + 1
                for url in ["url8", "url9"]:
                    wig.add_button.trigger()
                    wig.line_edit.setText(url)
                wig.add_button.trigger()
                lst = [wig.combo.itemText(j) for j in range(wig.combo.count())]
                assert len([i for i in ["url8", "url9"] if i in lst]) == 2
                wig.remove_button.trigger()
    proc_time()
    editor.button.click()
    assert found == 3
