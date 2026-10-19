"""
ModuleSearch.py - Quick Module Search & Palette for Cecilia5
Allows sound designers to instantly search and open any module with Cmd+K / Ctrl+K.
"""
import wx
import os
import Resources.CeciliaLib as CeciliaLib
from .constants import *

class ModuleSearchDialog(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, -1, "Quick Module Search",
                           size=(500, 420),
                           style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
        self.SetBackgroundColour(wx.Colour(BACKGROUND_COLOUR))
        self.parent = parent
        self.all_modules = []  # List of tuples: (display_label, category, name, full_path, is_builtin)

        self._load_modules()
        self._build_ui()
        self._filter_list("")
        self.CenterOnParent()

    def _load_modules(self):
        root, directories, files = CeciliaLib.buildFileTree()
        for d in directories:
            for f in sorted(files.get(d, [])):
                name = os.path.splitext(f)[0]
                full_path = os.path.join(MODULES_PATH, d, f)
                display = "[%s]  %s" % (d, name)
                self.all_modules.append((display, d, name, full_path, True))

        prefPath = CeciliaLib.getVar("prefferedPath")
        if prefPath:
            for path in prefPath.split(';'):
                path = CeciliaLib.ensureNFD(path)
                if os.path.isdir(path):
                    cat = os.path.split(path)[1]
                    for f in os.listdir(path):
                        if f.endswith("." + FILE_EXTENSION):
                            name = os.path.splitext(f)[0]
                            full_path = os.path.join(path, f)
                            display = "[Custom: %s]  %s" % (cat, name)
                            self.all_modules.append((display, cat, name, full_path, False))

    def _build_ui(self):
        sizer = wx.BoxSizer(wx.VERTICAL)

        header = wx.StaticText(self, -1, "Search & Open Module (Type to filter, Enter to load):")
        header.SetFont(wx.Font(11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        header.SetForegroundColour(wx.Colour(WHITE_COLOUR))
        sizer.Add(header, 0, wx.ALL, 10)

        self.search_ctrl = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER)
        self.search_ctrl.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        self.search_ctrl.SetBackgroundColour(wx.Colour(POPUP_BACK_COLOUR))
        self.search_ctrl.SetForegroundColour(wx.Colour(WHITE_COLOUR))
        sizer.Add(self.search_ctrl, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 10)

        self.list_box = wx.ListBox(self, -1, style=wx.LB_SINGLE | wx.LB_ALWAYS_SB)
        self.list_box.SetFont(wx.Font(11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        self.list_box.SetBackgroundColour(wx.Colour("#22252A"))
        self.list_box.SetForegroundColour(wx.Colour("#E0E0E0"))
        sizer.Add(self.list_box, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        hint = wx.StaticText(self, -1, "Tip: Use Up/Down arrows to select, Enter to open, Esc to cancel.")
        hint.SetFont(wx.Font(9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL))
        hint.SetForegroundColour(wx.Colour(LIGHTGREY_COLOUR))
        sizer.Add(hint, 0, wx.ALL, 8)

        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.open_btn = wx.Button(self, wx.ID_OK, "Open Module")
        self.cancel_btn = wx.Button(self, wx.ID_CANCEL, "Cancel")
        btn_sizer.Add(self.cancel_btn, 0, wx.RIGHT, 8)
        btn_sizer.Add(self.open_btn, 0)
        sizer.Add(btn_sizer, 0, wx.ALIGN_RIGHT | wx.ALL, 10)

        self.SetSizer(sizer)

        self.search_ctrl.Bind(wx.EVT_TEXT, self.on_text_change)
        self.search_ctrl.Bind(wx.EVT_KEY_DOWN, self.on_key_down)
        self.list_box.Bind(wx.EVT_LISTBOX_DCLICK, self.on_double_click)
        self.list_box.Bind(wx.EVT_KEY_DOWN, self.on_key_down)

        wx.CallAfter(self.search_ctrl.SetFocus)

    def on_text_change(self, event):
        query = self.search_ctrl.GetValue().strip().lower()
        self._filter_list(query)

    def _filter_list(self, query):
        self.list_box.Clear()
        self.filtered_modules = []
        for item in self.all_modules:
            display, cat, name, path, is_builtin = item
            if not query or (query in display.lower()) or (query in cat.lower()) or (query in name.lower()):
                self.filtered_modules.append(item)
                self.list_box.Append(display)

        if self.filtered_modules:
            self.list_box.SetSelection(0)

    def on_key_down(self, event):
        key = event.GetKeyCode()
        if key == wx.WXK_DOWN:
            sel = self.list_box.GetSelection()
            if sel < self.list_box.GetCount() - 1:
                self.list_box.SetSelection(sel + 1)
            return
        elif key == wx.WXK_UP:
            sel = self.list_box.GetSelection()
            if sel > 0:
                self.list_box.SetSelection(sel - 1)
            return
        elif key in [wx.WXK_RETURN, wx.WXK_NUMPAD_ENTER]:
            self.on_open()
            return
        elif key == wx.WXK_ESCAPE:
            self.EndModal(wx.ID_CANCEL)
            return
        event.Skip()

    def on_double_click(self, event):
        self.on_open()

    def on_open(self):
        sel = self.list_box.GetSelection()
        if sel != wx.NOT_FOUND and sel < len(self.filtered_modules):
            selected_item = self.filtered_modules[sel]
            self.EndModal(wx.ID_OK)
            mainFrame = CeciliaLib.getVar("mainFrame")
            if mainFrame:
                mainFrame.onOpen(selected_item[3], selected_item[4])
        else:
            self.EndModal(wx.ID_CANCEL)
