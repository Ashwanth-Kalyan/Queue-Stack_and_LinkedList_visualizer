import tkinter as tk

master = tk.Tk()

class MainWindow:
    def __init__(self):
        self.master = master
        self.master.geometry("500x500")
        self.master.configure(bg="LightBlue")

        self.radius = 20
        self.x = 100  # Start from a reasonable x position
        self.y = 200
        self.linked = []  # List to store elements as (oval, text, arrow) triples
        self.arrows = []  # List to store arrows for removal

        # Buttons to navigate between data structures
        tk.Button(self.master, text="Queue", width=24, command=self.q).pack(pady=5)
        tk.Button(self.master, text="Stack", width=24, command=self.s).pack(pady=5)
        tk.Button(self.master, text="Linked List", width=24, command=self.ll).pack(pady=5)
        

    def q(self):
        self.queue = []
        self.master.destroy()
        qwindow = tk.Tk()
        qwindow.geometry("500x500")
        qwindow.configure(bg="LightGreen")

        self.qcanvas = tk.Canvas(qwindow, bg="LightGreen", width=500, height=400)
        self.qcanvas.pack()

        tk.Button(qwindow, text="Enqueue", width=24, command=self.enq).pack(pady=5)
        tk.Button(qwindow, text="Dequeue", width=24, command=self.deq).pack(pady=5)

        self.entry = tk.Entry(qwindow, width=24)
        self.entry.pack(pady=5)

    def enq(self):
        
        value = self.entry.get()
        if value:
            oval = self.qcanvas.create_oval(self.x - self.radius, self.y - self.radius,
                                            self.x + self.radius, self.y + self.radius, fill="orange")
            text = self.qcanvas.create_text(self.x, self.y, text=value, font=("Arial", 10))
            self.queue.append((oval, text))
            self.x += 60
            self.entry.delete(0, tk.END)

    def deq(self):

        if self.queue:
            oval, text = self.queue.pop(0)
            self.qcanvas.delete(oval)
            self.qcanvas.delete(text)
            self.x -= 60
            for oval, text in self.queue:
                self.qcanvas.move(oval, -60, 0)
                self.qcanvas.move(text, -60, 0)

    def s(self):

        self.stack = []
        self.y = 350
        self.x = 250

        self.master.destroy()
        self.swindow = tk.Tk()
        self.swindow.geometry("500x500")
        self.swindow.configure(bg="LightGrey")

        self.scanvas = tk.Canvas(self.swindow, bg="grey", width=500, height=400)
        self.scanvas.pack()

        tk.Button(self.swindow, text="Push", width=24, command=self.spush).pack(pady=5)
        tk.Button(self.swindow, text="Pop", width=24, command=self.spop).pack(pady=5)

        self.e = tk.Entry(self.swindow, width=24)
        self.e.pack(pady=5)

    def spush(self):

        value = self.e.get()
        if value:
            oval = self.scanvas.create_rectangle(self.x - self.radius, self.y - self.radius,
                                                 self.x + self.radius, self.y + self.radius, fill="pink")
            text = self.scanvas.create_text(self.x, self.y, text=value, font=("Arial", 10))
            self.stack.append((oval, text))
            self.y -= 40  # Move upwards for the next element
            self.e.delete(0, tk.END)

    def spop(self):

        if self.stack:
            oval, text = self.stack.pop()
            self.scanvas.delete(oval)
            self.scanvas.delete(text)
            self.y += 40  # Move downwards after popping

    def ll(self):

        self.linked = []
        self.xf = 250  
        self.xe = 190
        self.y = 200

        self.master.destroy()
        lwindow = tk.Tk()
        lwindow.geometry("500x500")
        lwindow.configure(bg="LightYellow")

        self.llcanvas = tk.Canvas(lwindow, bg="LightYellow", width=500, height=250)
        self.llcanvas.pack()

        tk.Button(lwindow, text="Add Element to Beginning", width=48, command=self.add_begin).pack(pady=5)
        tk.Button(lwindow, text="Add Element at the End", width=48, command=self.add_end).pack(pady=5)
        tk.Button(lwindow, text="Delete Element in Beginning", width=48,command=self.delete_begin).pack(pady=5)
        tk.Button(lwindow, text="Delete Element at the End", width=48,command = self.delete_end).pack(pady=5)

        self.entry = tk.Entry(lwindow, width=24)
        self.entry.pack(pady=5)

        self.pos_entry = tk.Entry(lwindow, width=24)
        self.pos_entry.pack(pady=5)
        self.pos_entry.insert(0, "Starts from 0")

    def add_end(self):

        
        value = self.entry.get()
        if value:
            oval = self.llcanvas.create_oval(self.xf - self.radius, self.y - self.radius,
                                              self.xf + self.radius, self.y + self.radius, fill="cyan")
            text = self.llcanvas.create_text(self.xf, self.y, text=value, font=("Arial", 10))
            arrow = self.llcanvas.create_line(self.xf + self.radius, self.y, self.xf + 40, self.y, arrow=tk.LAST, tags="arrow")

            self.linked.insert(0, (oval, text, arrow))
            self.entry.delete(0, tk.END)
            self.xf += 60
           

    def add_begin(self):

        
        value = self.entry.get()
        if value:
            oval = self.llcanvas.create_oval(self.xe - self.radius, self.y - self.radius,
                                              self.xe + self.radius, self.y + self.radius, fill="cyan")
            text = self.llcanvas.create_text(self.xe, self.y, text=value, font=("Arial", 10))
            arrow = self.llcanvas.create_line(self.xe + self.radius, self.y, self.xe + 40, self.y, arrow=tk.LAST, tags="arrow")

            self.linked.append((oval, text, arrow))
            self.entry.delete(0, tk.END)
            self.xe -= 60

    
    def delete_end(self):
    
        if self.linked:
            oval, text, arrow = self.linked.pop(0)
            self.llcanvas.delete(oval)
            self.llcanvas.delete(text)
            self.llcanvas.delete(arrow)
            self.xf -= 60  

    def delete_begin(self):

        if self.linked:
            oval, text, arrow = self.linked.pop()
            self.llcanvas.delete(oval)
            self.llcanvas.delete(text)
            self.llcanvas.delete(arrow)
            self.xe += 60

    
window = MainWindow()
master.mainloop()