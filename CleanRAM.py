def AllChildren(window):
    _list = window.winfo_children()

    for item in _list:
        if item.winfo_children():
            _list.extend(item.winfo_children())
    return _list

def CleanUp(window):
    widget_list = AllChildren(window)
    for item in widget_list:
        item.destroy()

def ClearRAM(names):
    for widget in names:
        widget.destroy()