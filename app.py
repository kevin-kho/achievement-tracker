import tkinter as tk
from functools import partial

class Tracker(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.title("Achievement Tracker")
		self.geometry("500x300+200+200")
		self._create_display()
		self.total_points = 0
		self.history = []
				
	
	def _create_display(self):
		# Create the total points label and entry box
		# Need to fix. Lambda function gets reassigned if put through for loop
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
		column_descriptions = ["Task Description", "Point Value", "Click to Confirm"]
		for col, column_description in enumerate(column_descriptions):
			tk.Label(self, text=column_description).grid(row=2, column=col)

		# Create task descriptions
		for i in range(3, 8):
			tk.Entry(self, justify="center").grid(row=i, column=0)
	

		# Create point entry forms
		# Unlike the task description, we HAVE to use a second statement to place them onto the GUI
		# Reason: by calling the .grid() method at the same time as creating the entry form, it sets the data type to None
		# The None datatype conflicts with the .get() method later used in the program.
		# Unlike the task descriptions, the data must be retrievable.

		self.t1_points = tk.Entry(self, justify="center")
		self.t2_points = tk.Entry(self, justify="center")
		self.t3_points = tk.Entry(self, justify="center")
		self.t4_points = tk.Entry(self, justify="center")
		self.t5_points = tk.Entry(self, justify="center")
		for row, t in enumerate([self.t1_points, self.t2_points, self.t3_points, self.t4_points, self.t5_points], start=3):
			t.grid(row=row, column=1)

		#Create buttons to add
		#The partial function helps us pass an additional argument to the
		#add_to_total function. It makes it easier to read, and results in less stuff to write.
		#Reading more on stackoverflow, the partial function works in this case because it RETURNS
		# a callable of that function and arguments.
		# So more specifically, evaluating partial(self.add_to_total, 1)
		# Returns self.add_to_total(1) as a callable. Apparently how tk.Button is set up, the command option
		# Must contain a callable item (it's called a partial item in the docs)
		# Putting self.add_to_total(1) by itself will evaluate the function on startup
		for i in range(1, 6):
			tk.Button(self, text=f"Add to total ({i})", command = partial(self.add_to_total, i)).grid(row=i+2, column=2)

		tk.Button(self, text="(S)tart/Reset", command = self.reset_points).grid(row=8, column=0)
		tk.Button(self, text="(U)ndo", command = self.undo).grid(row=8, column=1)
		
	def add_to_total(self, i):
		point_dict = {1: self.t1_points.get(),
						2: self.t2_points.get(),
						3: self.t3_points.get(),
						4: self.t4_points.get(),
						5: self.t5_points.get()
			}
		to_add = point_dict[i]
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
		if key in (f"{i}" for i in range(1, 6)):
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