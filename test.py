import wx

class Example(wx.Frame):
	
	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs) 
			
		self.InitUI()
		
	def InitUI(self):	
		self.SetSize((300, 200))
		self.SetTitle('Message box')
		self.Centre()
		self.Show(True)

def main():
	ex = wx.App()
	Example(None)
	ex.MainLoop()

if __name__ == "__main__":
	main()
