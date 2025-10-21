import tkinter as tk

class ScrollableFrameContainer(tk.Frame):
    """
    Adapted version of https://sqlpey.com/python/tkinter-scrollable-frames/ by 7th September 2025

    A custom Frame that makes its internal content scrollable.
    Designed to replace standard tk.Frame instances.
    """
    def __init__(self, parent, color, **options):
        tk.Frame.__init__(self, parent, **options)

        colTheme = color

        window_height = parent.winfo_height()
        self.max_canvas_height = window_height - min(window_height//10, 50) #only for testing that high, normal 20

        # Vertical scrollbar setup
        v_scrollbar = tk.Scrollbar(self, orient="vertical")
        v_scrollbar.pack(side="right", fill="y")

        # Canvas setup for scrolling
        self.canvas_widget = tk.Canvas(self, borderwidth=0, highlightthickness=0, background=colTheme, yscrollcommand=v_scrollbar.set)
        self.canvas_widget.pack(side="left", fill="both", expand=True)

        # Configure scrollbar to control canvas view
        v_scrollbar.config(command=self.canvas_widget.yview)

        # Frame to hold scrollable content, placed within the canvas
        self.scrollable_content_frame = tk.Frame(self.canvas_widget, background=self.canvas_widget.cget('bg'))
        self.canvas_widget.create_window((0, 0), window=self.scrollable_content_frame, anchor="nw")

        # Bind configure event to dynamically adjust scroll region
        self.scrollable_content_frame.bind("<Configure>", self.on_frame_content_configure)
        self.canvas_widget.bind_all("<MouseWheel>", self.handle_mousewheel_scroll) # bind_all is important here

    
    # refer to https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/event-handlers.html for information
    # about the event class 

    def on_frame_content_configure(self, event):
        """Update the canvas's scrollable region to fit the content frame"""
        # set scrollregion to the coordinates of the rectangle fitting the whole canvas content 
        self.canvas_widget.configure(scrollregion=self.canvas_widget.bbox("all"))

        # set canvas size to size of the inner frame 
        self.canvas_widget.config(
            width = self.scrollable_content_frame.winfo_reqwidth(),
            height = min(self.scrollable_content_frame.winfo_reqheight(), self.max_canvas_height)  
        )
        

    def handle_mousewheel_scroll(self, event): 
        # be careful: the delta things works only for Windows and will malfunction in Linux/iOS
        self.canvas_widget.yview_scroll(int(-1*(event.delta/120)), "units")
       
