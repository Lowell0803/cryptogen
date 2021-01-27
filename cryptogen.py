from tkinter import *
from tkinter import ttk
import tkinter.font
import tkinter.messagebox

import random
import threading

class Main_Frame:

	def __init__(self, root):
		root.title('CryptoGen')
		root.resizable(0, 0)

		sw = root.winfo_screenwidth()
		sh = root.winfo_screenheight()

		w = 700
		h = 448

		x = (sw/2) - (w/2)
		y = (sh/2) - (h/2)

		root.geometry('%dx%d+%d+%d' % (w, h, x, y))

		logoFont = tkinter.font.Font(family="Scream Real", size=36)

		self.filename = "img/main_frame.gif"
		self.bg_image = PhotoImage(file=self.filename)

		self.cv = Canvas(width=w, height=h, borderwidth=0, highlightthickness=0)
		self.cv.pack(side='top', fill='both', expand='yes')
		self.cv.create_image(0, 0, image=self.bg_image, anchor='nw')

		self.cv.create_text(510, 85, text="CryptoGen", font=logoFont)

		#----- Tips -----#
		tips_font = tkinter.font.Font(family="Verdana", size=10)

		self.cv_tips = Canvas(width=240, height=120, bg="white")
		self.cv_tips.place(x=60, y=220)

		self.index = 0

		def next():
			self.text.config(state=NORMAL)

			if self.index == 0:
				next_tip = """Make your password long. Short \npasswords are vulnerable to \nbrute-force attacks."""
			elif self.index == 1:
				next_tip = """Try making your password a \nnonsense phrase. """
			elif self.index == 2:
				next_tip = """Include numbers, symbols, and \nuppercase and lowercase letters."""
			elif self.index == 3:
				next_tip = """Avoid using obvious personal \ninformation."""
			elif self.index == 4:
				next_tip = """Do not reuse passwords. Use \nunique passwords for everything."""
			elif self.index == 5:
				next_tip = """Start using a password manager to store your passwords."""
			elif self.index == 6:
				next_tip = """Keep your password confidential. Don't give your passwords to \nanyone else."""
			elif self.index == 7:
				next_tip = """Do not forget to change your \npasswords regularly."""
				self.index -= 8

			self.text.delete('1.0', END)
			self.text.insert(END, next_tip)

			self.index += 1

			self.text.config(state=DISABLED)

		self.text = Text(self.cv_tips, height=4, width=28, borderwidth=0, font=tips_font)
		self.text.place(x=12,y=35)

		def interval_next():
			threading.Timer(3.0, interval_next).start()
			next()

		interval_next()

		root.iconbitmap('img/cryptogen_icon.ico')


class Password_Random:

	def __init__(self, root):
		def generate():
			characters = "0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
			length = int(self.combobox_var.get())
			new_password = " "
		 
			for i in range(length):
				next_index = random.randrange(len(characters))
				new_password = new_password + characters[next_index]

			self.entry.focus()
			self.entry_var.set(new_password)

		root.title('CryptoGen')
		root.resizable(0, 0)

		sw = root.winfo_screenwidth()
		sh = root.winfo_screenheight()

		w = 700
		h = 428

		x = (sw/2) - (w/2)
		y = (sh/2) - (h/2)

		root.geometry('%dx%d+%d+%d' % (w, h, x, y))

		entry_font = tkinter.font.Font(family="Montserrat", size=14)
		button_font = tkinter.font.Font(family="Montserrat", size=15, weight="bold")
		combobox_font = tkinter.font.Font(family="Montserrat", size=15, weight="bold")

		self.filename = "img/cryptogen.gif"
		self.bg_image = PhotoImage(file=self.filename)

		self.cv_random = Canvas(width=w, height=h, borderwidth=0, highlightthickness=0)
		self.cv_random.pack(side='top', fill='both', expand='yes')
		self.cv_random.create_image(0, 0, image=self.bg_image, anchor='nw')

		self.entry_var = StringVar()

		self.entry = Entry(self.cv_random, font=entry_font, textvariable=self.entry_var, state="readonly")
		self.entry.place(x=161, y=100)

		self.combobox_var = IntVar()

		self.combobox = ttk.Combobox(self.cv_random, width=4, font=combobox_font, textvariable=self.combobox_var, 
			values=["  " + str(x) for x in range(1,21)], state="readonly")
		self.combobox.place(x=344, y=160)
		self.combobox.current(7)

		self.button = Button(self.cv_random, width=12, text="GENERATE", font=button_font, bg="white", fg="black", 
			borderwidth=0, relief="sunken", command=generate)
		self.button.place(x=163, y=155)

		#----- Tips -----#
		tips_font = tkinter.font.Font(family="Verdana", size=10)

		self.cv_tips = Canvas(width=260, height=120, bg="white")
		self.cv_tips.place(x=160, y=265)

		self.index = 0

		def next():
			self.text.config(state=NORMAL)

			if self.index == 0:
				next_tip = """Make your password long. Short \npasswords are vulnerable to \nbrute-force attacks."""
			elif self.index == 1:
				next_tip = """Try making your password a \nnonsense phrase. """
			elif self.index == 2:
				next_tip = """Include numbers, symbols, and \nuppercase and lowercase letters."""
			elif self.index == 3:
				next_tip = """Avoid using obvious personal \ninformation."""
			elif self.index == 4:
				next_tip = """Do not reuse passwords. Use \nunique passwords for everything."""
			elif self.index == 5:
				next_tip = """Start using a password manager to store your passwords."""
			elif self.index == 6:
				next_tip = """Keep your password confidential. Don't give your passwords to \nanyone else."""
			elif self.index == 7:
				next_tip = """Do not forget to change your \npasswords regularly."""
				self.index -= 8

			self.text.delete('1.0', END)
			self.text.insert(END, next_tip)

			self.index += 1

			self.text.config(state=DISABLED)

		self.text = Text(self.cv_tips, height=4, width=28, borderwidth=0, font=tips_font)
		self.text.place(x=20,y=35)

		def interval_next():
			threading.Timer(3.0, interval_next).start()
			next()

		interval_next()

		root.iconbitmap('img/cryptogen_icon.ico')


class Password_Info:

	def __init__(self, root):
		def generate():
			self.listbox.delete(0, END)

			first_pw = None
			second_pw = None
			third_pw = None
			fourth_pw = None
			fifth_pw = None
			sixth_pw = None
			seventh_pw = None
			eighth_pw = None
			ninth_pw = None
			tenth_pw = None

			fname = str(self.fname_var.get()).lower().replace(" ","")
			lname = str(self.lname_var.get()).lower().replace(" ","")
			month = str(self.cbox_month_var.get())
			day = str(self.cbox_day_var.get())

			if len(month) == 1:
				month = "0" + month
			if len(day) == 1:
				day = "0" + day

			first_pw = fname + "_" + lname + month
			second_pw = fname + "_" + lname + day
			third_pw = fname + "_" + lname + month + day
			fourth_pw = fname + "." + lname + month
			fifth_pw = fname + "." + lname + day
			sixth_pw = fname + "." + lname + month + day
			seventh_pw = month + fname + day
			eighth_pw = month + lname + day
			ninth_pw = fname + month + day
			tenth_pw = lname + month + day

			self.listbox.insert(0, first_pw)
			self.listbox.insert(0, second_pw)
			self.listbox.insert(0, third_pw)
			self.listbox.insert(0, fourth_pw)
			self.listbox.insert(0, fifth_pw)
			self.listbox.insert(0, sixth_pw)
			self.listbox.insert(0, seventh_pw)
			self.listbox.insert(0, eighth_pw)
			self.listbox.insert(0, ninth_pw)
			self.listbox.insert(0, tenth_pw)

		root.title('CryptoGen')
		root.resizable(0, 0)

		sw = root.winfo_screenwidth()
		sh = root.winfo_screenheight()

		w = 700
		h = 428

		x = (sw/2) - (w/2)
		y = (sh/2) - (h/2)

		root.geometry('%dx%d+%d+%d' % (w, h, x, y))

		label_font = tkinter.font.Font(family="Bebas Kai", size=14)
		entry_font = tkinter.font.Font(family="Montserrat", size=14)
		listbox_font = tkinter.font.Font(family="Montserrat", size=14)
		button_font = tkinter.font.Font(family="Montserrat", size=15, weight="bold")
		combobox_font = tkinter.font.Font(family="Montserrat", size=15, weight="bold")

		self.filename = "img/cryptogen.gif"
		self.bg_image = PhotoImage(file=self.filename)

		self.cv_info = Canvas(width=w, height=h, borderwidth=0, highlightthickness=0)
		self.cv_info.pack(side='top', fill='both', expand='yes')
		self.cv_info.create_image(0, 0, image=self.bg_image, anchor='nw')

		self.label_fname = Label(self.cv_info, text="First Name", font=label_font)
		self.label_fname.place(x=165, y=100)

		self.fname_var = StringVar()
		self.lname_var = StringVar()

		self.entry_fname = Entry(self.cv_info, font=entry_font, textvariable=self.fname_var)
		self.entry_fname.place(x=258, y=100, width=165)

		self.label_lname = Label(self.cv_info, text="Last Name", font=label_font)
		self.label_lname.place(x=166, y=145)

		self.entry_lname = Entry(self.cv_info, font=entry_font, textvariable=self.lname_var)
		self.entry_lname.place(x=258, y=145, width=165)

		self.label_bdate = Label(self.cv_info, text="Birthdate", font=label_font)
		self.label_bdate.place(x=166, y=190)

		self.cbox_month_var = IntVar()
		self.cbox_day_var = IntVar()

		self.combobox_month = ttk.Combobox(self.cv_info, width=4, font=combobox_font, textvariable=self.cbox_month_var, 
			values=[" " + str(x) for x in range(1,13)], state="readonly")
		self.combobox_month.place(x=258, y=188)
		self.combobox_month.current(0)

		self.combobox_day = ttk.Combobox(self.cv_info, width=4, font=combobox_font, textvariable=self.cbox_day_var, 
			values=[" " + str(x) for x in range(1,32)], state="readonly")
		self.combobox_day.place(x=344, y=188)
		self.combobox_day.current(0)

		self.button = Button(self.cv_info, width=12, text="GENERATE", font=button_font, bg="white", fg="black", 
			borderwidth=0, relief="sunken", command=generate)
		self.button.place(x=163, y=235, width=260, height=42)

		self.listbox = Listbox(self.cv_info, font=listbox_font, borderwidth=0, relief=FLAT)
		self.listbox.place(x=161, y=295, height=90)

		self.scrollbar = ttk.Scrollbar(self.cv_info, orient="vertical", command=self.listbox.yview)
		self.scrollbar.place(x=406, y=295, height=90)

		self.listbox.config(yscrollcommand=self.scrollbar.set)

		def check():
			m_value = int(str(self.cbox_month_var.get()).strip())
			d_value = int(str(self.cbox_day_var.get()).strip())

			if m_value == 1 or m_value == 3 or m_value == 5 or m_value == 7 or m_value == 8 or m_value == 10 or m_value == 12:
				self.combobox_day.configure(values=[" " + str(x) for x in range(1,32)])
			elif m_value == 2:
				if d_value == 31 or d_value == 30:
					self.combobox_day.current(28)
				self.combobox_day.configure(values=[" " + str(x) for x in range(1,30)])
			else:
				if d_value == 31:
					self.combobox_day.current(29)
				self.combobox_day.configure(values=[" " + str(x) for x in range(1,31)])

		def interval_check():
			threading.Timer(0.1, interval_check).start()
			check()

		interval_check()

		root.iconbitmap('img/cryptogen_icon.ico')


class Password_Word:

	def __init__(self, root):
		def generate():
			#random from this string / can use same char repeatedly
			'''characters = str(self.entry_word_var.get())
			length = len(characters)
			new_password = " "
		 
			for i in range(length):
				next_index = random.randrange(len(characters))
				new_password = new_password + characters[next_index]'''

			new_password = str(self.entry_word_var.get())
			new_password_list = list(new_password)

			random.shuffle(new_password_list)

			new_password = ''.join(new_password_list)

			self.entry_word.focus()
			self.entry_var.set(new_password)

		root.title('CryptoGen')
		root.resizable(0, 0)

		sw = root.winfo_screenwidth()
		sh = root.winfo_screenheight()

		w = 700
		h = 428

		x = (sw/2) - (w/2)
		y = (sh/2) - (h/2)

		root.geometry('%dx%d+%d+%d' % (w, h, x, y))

		entry_font = tkinter.font.Font(family="Montserrat", size=14)
		entry_word_font = tkinter.font.Font(family="Montserrat", size=10)
		button_font = tkinter.font.Font(family="Montserrat", size=11, weight="bold")

		self.filename = "img/cryptogen.gif"
		self.bg_image = PhotoImage(file=self.filename)

		self.cv_word = Canvas(width=w, height=h, borderwidth=0, highlightthickness=0)
		self.cv_word.pack(side='top', fill='both', expand='yes')
		self.cv_word.create_image(0, 0, image=self.bg_image, anchor='nw')

		self.entry_var = StringVar()

		self.entry = Entry(self.cv_word, font=entry_font, textvariable=self.entry_var, state="readonly")
		self.entry.place(x=161, y=100)

		self.entry_word_var = StringVar()

		self.entry_word = Entry(self.cv_word, font=entry_word_font, textvariable=self.entry_word_var)
		self.entry_word.place(x=300, y=157, width=125, height=30)

		self.button = Button(self.cv_word, width=12, text="GENERATE", font=button_font, bg="white", fg="black", 
			borderwidth=0, relief="sunken", command=generate)
		self.button.place(x=161, y=155)

		#----- Tips -----#
		tips_font = tkinter.font.Font(family="Verdana", size=10)

		self.cv_tips = Canvas(width=260, height=120, bg="white")
		self.cv_tips.place(x=160, y=265)

		self.index = 0

		def next():
			self.text.config(state=NORMAL)

			if self.index == 0:
				next_tip = """Make your password long. Short \npasswords are vulnerable to \nbrute-force attacks."""
			elif self.index == 1:
				next_tip = """Try making your password a \nnonsense phrase. """
			elif self.index == 2:
				next_tip = """Include numbers, symbols, and \nuppercase and lowercase letters."""
			elif self.index == 3:
				next_tip = """Avoid using obvious personal \ninformation."""
			elif self.index == 4:
				next_tip = """Do not reuse passwords. Use \nunique passwords for everything."""
			elif self.index == 5:
				next_tip = """Start using a password manager to store your passwords."""
			elif self.index == 6:
				next_tip = """Keep your password confidential. Don't give your passwords to \nanyone else."""
			elif self.index == 7:
				next_tip = """Do not forget to change your \npasswords regularly."""
				self.index -= 8

			self.text.delete('1.0', END)
			self.text.insert(END, next_tip)

			self.index += 1

			self.text.config(state=DISABLED)

		self.text = Text(self.cv_tips, height=4, width=28, borderwidth=0, font=tips_font)
		self.text.place(x=20,y=35)

		def interval_next():
			threading.Timer(3.0, interval_next).start()
			next()

		interval_next()

		root.iconbitmap('img/cryptogen_icon.ico')


def main_frame():
	def switch_to_random():
		root.destroy()
		password_random()
	def switch_to_info():
		root.destroy()
		password_info()
	def switch_to_word():
		root.destroy()
		password_word()
		
	root = Tk()

	main_frame = Main_Frame(root)

	button_font = tkinter.font.Font(family="Montserrat", size=14, weight="bold")

	button_pass_random = Button(root, width=23, anchor="w", text=" Generate Random Password", font=button_font, 
		bg="white", fg="black", borderwidth=0, command=switch_to_random, cursor="hand2")
	button_pass_random.place(x=355,y=160)
	button_pass_info = Button(root, width=23, anchor="w", text=" Generate From Information", font=button_font, 
		bg="white", fg="black", borderwidth=0, command=switch_to_info, cursor="hand2")
	button_pass_info.place(x=355,y=230)
	button_pass_word = Button(root, width=23, anchor="w", text=" Generate From a Word", font=button_font, 
		bg="white", fg="black", borderwidth=0, command=switch_to_word, cursor="hand2")
	button_pass_word.place(x=355,y=300)

	root.mainloop()


def password_random():
	def switch_to_main(event):
		root_pr.destroy()
		main_frame()

	root_pr = Tk()

	password_random = Password_Random(root_pr)

	back_font = tkinter.font.Font(family="Montserrat", size=8)

	back_to_main = Label(root_pr, text="Back to main page...", font=back_font, bg="#e4e4e4", fg="black", cursor="hand2")
	back_to_main.bind('<Button-1>', switch_to_main)
	back_to_main.place(x=5, y=400)

	root_pr.mainloop()


def password_info():
	def switch_to_main(event):
		root_pi.destroy()
		main_frame()

	root_pi = Tk()

	password_random = Password_Info(root_pi)

	back_font = tkinter.font.Font(family="Montserrat", size=8)

	back_to_main = Label(root_pi, text="Back to main page...", font=back_font, bg="#e4e4e4", fg="black", cursor="hand2")
	back_to_main.bind('<Button-1>', switch_to_main)
	back_to_main.place(x=5, y=400)

	root_pi.mainloop()


def password_word():
	def switch_to_main(event):
		root_pw.destroy()
		main_frame()

	root_pw = Tk()

	password_random = Password_Word(root_pw)

	back_font = tkinter.font.Font(family="Montserrat", size=8)

	back_to_main = Label(root_pw, text="Back to main page...", font=back_font, bg="#e4e4e4", fg="black", cursor="hand2")
	back_to_main.bind('<Button-1>', switch_to_main)
	back_to_main.place(x=5, y=400)

	root_pw.mainloop()


main_frame()
