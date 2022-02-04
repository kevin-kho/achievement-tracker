import tkinter as tk
from functools import partial

class Tracker(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.title("Achievement Tracker")
		self.geometry("500x500+500+500")
		self.createDisplay()
		self.total_points = 0
		self.history = []
				
	
	def createDisplay(self):
		# Create the total points label and entry box
		tk.Label(self, text="Total Points").grid(row=0, column=1)
		self.score = tk.Label(self, text="0")
		self.score.grid(row=1, column=1)
		self.score.bind('1', lambda event: self.hotkey(event, "1"))
		self.score.bind('2', lambda event: self.hotkey(event, "2"))
		self.score.bind('3', lambda event: self.hotkey(event, "3"))
		self.score.bind('4', lambda event: self.hotkey(event, "4"))
		self.score.bind('5', lambda event: self.hotkey(event, "5"))
		self.score.bind('u', lambda event: self.hotkey(event, "u"))
		self.score.bind('s', lambda event: self.hotkey(event, "s"))
		

		# Create the column descriptions
		tk.Label(self, text="Task Description").grid(row=2, column=0)
		tk.Label(self, text="Point Value").grid(row=2, column=1)
		tk.Label(self, text="Click to Confirm").grid(row=2, column=2)

		# Create task descriptions
		tk.Entry(self, justify="center").grid(row=3, column=0)
		tk.Entry(self, justify="center").grid(row=4, column=0)
		tk.Entry(self, justify="center").grid(row=5, column=0)
		tk.Entry(self, justify="center").grid(row=6, column=0)
		tk.Entry(self, justify="center").grid(row=7, column=0)
	

		# Create point entry forms
		# Unlike the task description, we HAVE to use a second statement to place them onto the GUI
		# Reason: by calling the .grid() method at the same time as creating the entry form, it sets the data type to None
		# The None datatype conflicts with the .get() method later used in the program.
		# Unlike the task descriptions, the data must be retrievable.
		self.t1_points = tk.Entry(self, justify="center")
		self.t1_points.grid(row=3, column=1)
		self.t2_points = tk.Entry(self, justify="center")
		self.t2_points.grid(row=4, column=1)
		self.t3_points = tk.Entry(self, justify="center")
		self.t3_points.grid(row=5, column=1)
		self.t4_points = tk.Entry(self, justify="center")
		self.t4_points.grid(row=6, column=1)
		self.t5_points = tk.Entry(self, justify="center")
		self.t5_points.grid(row=7, column=1)
		
		

		#Create buttons to add
		#The partial function helps us pass an additional argument to the
		#add_to_total function. It makes it easier to read, and results in less stuff to write.
		#Reading more on stackoverflow, the partial function works in this case because it RETURNS
		# a callable of that function and arguments.
		# So more specifically, evaluating partial(self.add_to_total, 1)
		# Returns self.add_to_total(1) as a callable. Apparently how tk.Button is set up, the command option
		# Must contain a callable item (it's called a partial item in the docs)
		# Putting self.add_to_total(1) by itself will evaluate the function on startup
		tk.Button(self, text="Add to total (1)", command = partial(self.add_to_total, 1)).grid(row=3, column=2)
		tk.Button(self, text="Add to total (2)", command = partial(self.add_to_total, 2)).grid(row=4, column=2)
		tk.Button(self, text="Add to total (3)", command = partial(self.add_to_total, 3)).grid(row=5, column=2)
		tk.Button(self, text="Add to total (4)", command = partial(self.add_to_total, 4)).grid(row=6, column=2)
		tk.Button(self, text="Add to total (5)", command = partial(self.add_to_total, 5)).grid(row=7, column=2)

		tk.Button(self, text="(S)tart/Reset", command = self.reset_points).grid(row=8, column=0)
		tk.Button(self, text="(U)ndo", command = self.undo).grid(row=8, column=1)
		
	def add_to_total(self, i):
		if i == 1:
			to_add = self.t1_points.get()
		elif i == 2:
			to_add = self.t2_points.get()
		elif i == 3:
			to_add = self.t3_points.get()
		elif i == 4:
			to_add = self.t4_points.get()
		elif i == 5:
			to_add = self.t5_points.get()
		try:
			self.total_points += int(to_add)
			self.history.append(to_add)
		except ValueError:
			self.total_points += 0
		self.score["text"] = str(self.total_points)
		self.score.focus()
		

	def reset_points(self):
		self.total_points = 0
		self.score["text"] = self.total_points
		self.history = []
		self.score.focus()

	def undo(self):
		try:
			if self.total_points - int(self.history[-1]) < 0:
				raise IndexError
			else: 
				self.total_points -= int(self.history.pop())
		except IndexError:
				self.total_points = 0
		self.score["text"] = self.total_points
		self.score.focus()

	def hotkey(self, event, key):
		if key == "1":
			self.add_to_total(int(key))
		elif key == "2":
			self.add_to_total(int(key))
		elif key == "3":
			self.add_to_total(int(key))
		elif key == "4":
			self.add_to_total(int(key))
		elif key == "5":
			self.add_to_total(int(key))
		elif key == "u":
			self.undo()
		elif key == "s":
			self.reset_points()
		

def main():
	my_gui = Tracker()
	my_gui.mainloop()


if __name__ == '__main__':
	main()