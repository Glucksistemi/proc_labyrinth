import wx
import random
import maps


class View(wx.Panel):
    dc = None

    def __init__(self, parent):
        super(View, self).__init__(parent)
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_KEY_DOWN, self.on_key_down)
        self.matrix = maps.create_level_map(50,20)

    def on_size(self, event):
        event.Skip()
        self.Refresh()

    def on_paint(self, event):
        w, h = self.GetClientSize()
        dc = wx.AutoBufferedPaintDC(self)
        dc.Clear()
        dc.SetBrush(wx.BLACK_BRUSH)
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[x])):
                if self.matrix[x][y] == maps.WALL:
                    xp = x*15
                    yp = y*15
                    dc.DrawRectangle(xp, yp, 15, 15)


    def on_key_down(self, event):
        if event.KeyCode == wx.WXK_F5:
            self.matrix = maps.create_level_map(50,20)
        self.Refresh()


class Frame(wx.Frame):
    def __init__(self):
        super(Frame, self).__init__(None)
        self.SetTitle('My Title')
        self.SetClientSize((750, 300))
        self.Center()
        self.view = View(self)


def main():
    app = wx.App(False)
    frame = Frame()
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()