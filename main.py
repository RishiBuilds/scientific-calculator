import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("750x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#1a1a2e")
        
        self.current_expression = ""
        self.total_expression = ""
        self.is_dark_mode = True
        self.history = []
        self.memory = 0
        
        self.dark_colors = {
            "bg": "#1a1a2e",
            "display_bg": "#16213e",
            "history_bg": "#0f3460",
            "btn_bg": "#16213e",
            "btn_fg": "white",
            "digit_btn_bg": "#533483",
            "operator_btn_bg": "#e94560",
            "special_btn_bg": "#4a90e2",
            "equals_btn_bg": "#f39c12",
            "memory_btn_bg": "#16a085",
            "fg": "white",
            "border": "#4a90e2"
        }
        
        self.light_colors = {
            "bg": "#f5f6fa",
            "display_bg": "#ffffff",
            "history_bg": "#e8e8e8",
            "btn_bg": "#dcdde1",
            "btn_fg": "#2c2c54",
            "digit_btn_bg": "#a8e6cf",
            "operator_btn_bg": "#ffd3b6",
            "special_btn_bg": "#d4b5e8",
            "equals_btn_bg": "#ffaaa5",
            "memory_btn_bg": "#c7f0db",
            "fg": "#2c2c54",
            "border": "#a8e6cf"
        }
        
        self.colors = self.dark_colors
        
        self.key_mapping = {
            "0": "0", "1": "1", "2": "2", "3": "3", "4": "4",
            "5": "5", "6": "6", "7": "7", "8": "8", "9": "9",
            "KP_0": "0", "KP_1": "1", "KP_2": "2", "KP_3": "3", "KP_4": "4",
            "KP_5": "5", "KP_6": "6", "KP_7": "7", "KP_8": "8", "KP_9": "9",
            "plus": "+", "KP_Add": "+", 
            "minus": "-", "KP_Subtract": "-",
            "asterisk": "*", "KP_Multiply": "*",
            "slash": "/", "KP_Divide": "/",
            "period": ".", "KP_Decimal": ".",
            "asciicircum": "^",
            "percent": "%",
            "parenleft": "(", "parenright": ")",
            "Return": "=", "KP_Enter": "=",
            "BackSpace": "backspace",
            "Escape": "clear",
            "e": "e",
            "p": "π",
            "s": "sin(",
            "c": "cos(",
            "t": "tan(",
            "l": "log(",
            "n": "ln(",
            "r": "sqrt("
        }
        
        self.create_layout()
        self.bind_keys()
        
    def bind_keys(self):
        """Bind keyboard keys to calculator functions"""
        self.root.bind("<Key>", self.key_pressed)
        
    def key_pressed(self, event):
        """Handle keyboard input"""
        key = event.keysym
        
        if key in self.key_mapping:
            value = self.key_mapping[key]
            if value == "=":
                self.evaluate()
            elif value == "backspace":
                self.backspace()
            elif value == "clear":
                self.clear()
            else:
                self.add_to_expression(value)
        
    def create_layout(self):
        self.main_frame = tk.Frame(self.root, bg=self.colors["bg"])
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.display_frame = tk.Frame(self.main_frame, bg=self.colors["bg"])
        self.display_frame.pack(fill=tk.X, pady=10)
        
        self.history_frame = tk.Frame(self.main_frame, bg=self.colors["history_bg"], width=220, 
                                    bd=1, relief=tk.SOLID, borderwidth=2, 
                                    highlightbackground=self.colors["border"])
        self.history_frame.pack(side=tk.LEFT, fill=tk.BOTH, pady=5, padx=5)
        self.history_frame.pack_propagate(False)
        
        history_header = tk.Frame(self.history_frame, bg=self.colors["history_bg"])
        history_header.pack(fill=tk.X, pady=5)
        
        self.history_label = tk.Label(history_header, text="📜 History", font=("Segoe UI", 13, "bold"), 
                                     bg=self.colors["history_bg"], fg=self.colors["fg"])
        self.history_label.pack(side=tk.LEFT, padx=10)
        
        clear_history_btn = tk.Button(history_header, text="🗑️", bg=self.colors["btn_bg"], 
                                    fg=self.colors["btn_fg"], font=("Arial", 10),
                                    command=self.clear_history, relief=tk.FLAT, bd=0)
        clear_history_btn.pack(side=tk.RIGHT, padx=5)
        
        self.history_scrollbar = tk.Scrollbar(self.history_frame)
        self.history_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.history_listbox = tk.Listbox(self.history_frame, bg=self.colors["history_bg"], 
                                         fg=self.colors["fg"], width=28, height=18,
                                         bd=0, highlightthickness=0,
                                         font=("Consolas", 9),
                                         yscrollcommand=self.history_scrollbar.set)
        self.history_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.history_scrollbar.config(command=self.history_listbox.yview)
        
        self.calculator_frame = tk.Frame(self.main_frame, bg=self.colors["bg"])
        self.calculator_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        display_container = tk.Frame(self.display_frame, bg=self.colors["display_bg"], 
                                  bd=2, relief=tk.SOLID, borderwidth=2, 
                                  highlightbackground=self.colors["border"])
        display_container.pack(fill=tk.X, padx=5)
        
        self.total_expression_label = tk.Label(display_container, text="", anchor="e", 
                                             bg=self.colors["display_bg"], fg="#888",
                                             font=("Arial", 12), padx=15, pady=5)
        self.total_expression_label.pack(fill=tk.X)
        
        self.current_expression_label = tk.Label(display_container, text="0", anchor="e", 
                                               bg=self.colors["display_bg"], fg=self.colors["fg"],
                                               font=("Arial", 28, "bold"), padx=15, pady=5)
        self.current_expression_label.pack(fill=tk.X)
        
        self.buttons_frame = tk.Frame(self.calculator_frame, bg=self.colors["bg"])
        self.buttons_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        button_bar = tk.Frame(self.display_frame, bg=self.colors["bg"])
        button_bar.pack(fill=tk.X, pady=5)
        
        self.theme_button = tk.Button(button_bar, text="☀️ Light Mode", 
                                    bg=self.colors["btn_bg"], fg=self.colors["btn_fg"],
                                    font=("Arial", 10, "bold"), width=14, 
                                    bd=1, relief=tk.RAISED, borderwidth=1,
                                    highlightbackground=self.colors["border"],
                                    activebackground=self.colors["btn_bg"],
                                    activeforeground=self.colors["btn_fg"],
                                    command=self.toggle_theme, cursor="hand2")
        self.theme_button.pack(side=tk.RIGHT, padx=5)
        
        self.create_buttons()
        
    def create_buttons(self):
        self.buttons_frame.columnconfigure(tuple(range(6)), weight=1, uniform="column")
        self.buttons_frame.rowconfigure(tuple(range(9)), weight=1, uniform="row")
        
        # Row 0: Memory functions
        self.create_button("MC", 0, 0, bg=self.colors["memory_btn_bg"], func=lambda: self.memory_clear())
        self.create_button("MR", 0, 1, bg=self.colors["memory_btn_bg"], func=lambda: self.memory_recall())
        self.create_button("M+", 0, 2, bg=self.colors["memory_btn_bg"], func=lambda: self.memory_add())
        self.create_button("M-", 0, 3, bg=self.colors["memory_btn_bg"], func=lambda: self.memory_subtract())
        self.create_button("⌫", 0, 4, bg=self.colors["special_btn_bg"], func=self.backspace)
        self.create_button("C", 0, 5, bg=self.colors["special_btn_bg"], func=self.clear)
        
        # Row 1: Advanced functions
        self.create_button("sin", 1, 0, bg=self.colors["special_btn_bg"], func=lambda: self.add_to_expression("sin("))
        self.create_button("cos", 1, 1, bg=self.colors["special_btn_bg"], func=lambda: self.add_to_expression("cos("))
        self.create_button("tan", 1, 2, bg=self.colors["special_btn_bg"], func=lambda: self.add_to_expression("tan("))
        self.create_button("log", 1, 3, bg=self.colors["special_btn_bg"], func=lambda: self.add_to_expression("log("))
        self.create_button("ln", 1, 4, bg=self.colors["special_btn_bg"], func=lambda: self.add_to_expression("ln("))
        self.create_button("√", 1, 5, bg=self.colors["special_btn_bg"], func=lambda: self.add_to_expression("sqrt("))
        
        # Row 2: More functions and parentheses
        self.create_button("asin", 2, 0, bg=self.colors["special_btn_bg"], func=lambda: self.add_to_expression("asin("))
        self.create_button("acos", 2, 1, bg=self.colors["special_btn_bg"], func=lambda: self.add_to_expression("acos("))
        self.create_button("atan", 2, 2, bg=self.colors["special_btn_bg"], func=lambda: self.add_to_expression("atan("))
        self.create_button("(", 2, 3, bg=self.colors["operator_btn_bg"])
        self.create_button(")", 2, 4, bg=self.colors["operator_btn_bg"])
        self.create_button("^", 2, 5, bg=self.colors["operator_btn_bg"], func=lambda: self.add_to_expression("^"))
        
        # Row 3: Constants and power
        self.create_button("π", 3, 0, bg=self.colors["special_btn_bg"], func=lambda: self.add_to_expression("π"))
        self.create_button("e", 3, 1, bg=self.colors["special_btn_bg"], func=lambda: self.add_to_expression("e"))
        self.create_button("x²", 3, 2, bg=self.colors["special_btn_bg"], func=lambda: self.add_to_expression("^2"))
        self.create_button("x³", 3, 3, bg=self.colors["special_btn_bg"], func=lambda: self.add_to_expression("^3"))
        self.create_button("xⁿ", 3, 4, bg=self.colors["special_btn_bg"], func=lambda: self.add_to_expression("^"))
        self.create_button("÷", 3, 5, bg=self.colors["operator_btn_bg"], func=lambda: self.add_to_expression("/"))
        
        # Row 4-6: Number pad
        self.create_button("7", 4, 0, bg=self.colors["digit_btn_bg"])
        self.create_button("8", 4, 1, bg=self.colors["digit_btn_bg"])
        self.create_button("9", 4, 2, bg=self.colors["digit_btn_bg"])
        self.create_button("!", 4, 3, bg=self.colors["special_btn_bg"], func=lambda: self.add_to_expression("!"))
        self.create_button("1/x", 4, 4, bg=self.colors["special_btn_bg"], func=lambda: self.one_over_x())
        self.create_button("×", 4, 5, bg=self.colors["operator_btn_bg"], func=lambda: self.add_to_expression("*"))
        
        self.create_button("4", 5, 0, bg=self.colors["digit_btn_bg"])
        self.create_button("5", 5, 1, bg=self.colors["digit_btn_bg"])
        self.create_button("6", 5, 2, bg=self.colors["digit_btn_bg"])
        self.create_button("%", 5, 3, bg=self.colors["operator_btn_bg"])
        self.create_button("±", 5, 4, bg=self.colors["special_btn_bg"], func=self.toggle_sign)
        self.create_button("-", 5, 5, bg=self.colors["operator_btn_bg"])
        
        self.create_button("1", 6, 0, bg=self.colors["digit_btn_bg"])
        self.create_button("2", 6, 1, bg=self.colors["digit_btn_bg"])
        self.create_button("3", 6, 2, bg=self.colors["digit_btn_bg"])
        self.create_button("CE", 6, 3, bg=self.colors["special_btn_bg"], func=self.clear_entry)
        self.create_button(".", 6, 4, bg=self.colors["digit_btn_bg"])
        self.create_button("+", 6, 5, bg=self.colors["operator_btn_bg"])
        
        # Row 7: Zero and equals
        self.create_button("0", 7, 0, bg=self.colors["digit_btn_bg"], columnspan=2)
        self.create_button("=", 7, 2, bg=self.colors["equals_btn_bg"], func=self.evaluate, columnspan=4)
        
    def create_button(self, text, row, column, bg, fg=None, func=None, columnspan=1):
        if fg is None:
            fg = self.colors["btn_fg"]
        
        if func is None:
            func = lambda: self.add_to_expression(text)
            
        button = tk.Button(self.buttons_frame, text=text, font=("Arial", 12, "bold"),
                         bg=bg, fg=fg, bd=1, relief=tk.RAISED, borderwidth=2,
                         highlightbackground=self.colors["border"],
                         activebackground=self.lighten_color(bg),
                         activeforeground=fg,
                         command=func,
                         cursor="hand2")
        button.grid(row=row, column=column, columnspan=columnspan, sticky="nsew", padx=3, pady=3, ipadx=1, ipady=2)
        return button
    
    def lighten_color(self, color):
        """Lighten a hex color"""
        if color.startswith("#"):
            r = min(255, int(color[1:3], 16) + 30)
            g = min(255, int(color[3:5], 16) + 30)
            b = min(255, int(color[5:7], 16) + 30)
            return f"#{r:02x}{g:02x}{b:02x}"
        return color
        
    def add_to_expression(self, value):
        self.current_expression += value
        self.update_display()
    
    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_display()
    
    def clear_entry(self):
        self.current_expression = ""
        self.update_display()
    
    def clear_history(self):
        self.history = []
        self.history_listbox.delete(0, tk.END)
    
    def backspace(self):
        self.current_expression = self.current_expression[:-1]
        self.update_display()
    
    def toggle_sign(self):
        if self.current_expression and self.current_expression != "0":
            if self.current_expression.startswith("-"):
                self.current_expression = self.current_expression[1:]
            else:
                self.current_expression = "-" + self.current_expression
        self.update_display()
    
    def one_over_x(self):
        try:
            val = float(self.current_expression) if self.current_expression else 0
            if val == 0:
                self.current_expression = "Error"
            else:
                self.current_expression = str(1 / val)
            self.update_display()
        except:
            self.current_expression = "Error"
            self.update_display()
    
    def memory_clear(self):
        self.memory = 0
    
    def memory_recall(self):
        self.current_expression = str(self.memory)
        self.update_display()
    
    def memory_add(self):
        try:
            val = float(self.current_expression) if self.current_expression else 0
            self.memory += val
        except:
            pass
    
    def memory_subtract(self):
        try:
            val = float(self.current_expression) if self.current_expression else 0
            self.memory -= val
        except:
            pass
    
    def factorial(self, n):
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")
        result = 1
        for i in range(1, int(n) + 1):
            result *= i
        return result
    
    def evaluate(self):
        if not self.current_expression:
            return
            
        self.total_expression = self.current_expression
        
        expression = self.current_expression
        expression = expression.replace("π", str(math.pi))
        expression = expression.replace("e", str(math.e))
        expression = expression.replace("^", "**")
        expression = expression.replace("sin(", "math.sin(")
        expression = expression.replace("cos(", "math.cos(")
        expression = expression.replace("tan(", "math.tan(")
        expression = expression.replace("asin(", "math.asin(")
        expression = expression.replace("acos(", "math.acos(")
        expression = expression.replace("atan(", "math.atan(")
        expression = expression.replace("log(", "math.log10(")
        expression = expression.replace("ln(", "math.log(")
        expression = expression.replace("sqrt(", "math.sqrt(")
        
        # Handle factorial
        while "!" in expression:
            import re
            match = re.search(r'(\d+(?:\.\d+)?)!', expression)
            if match:
                num = float(match.group(1))
                fact = self.factorial(num)
                expression = expression.replace(match.group(0), str(fact))
            else:
                break
        
        try:
            result = eval(expression)
            # Format the result
            if isinstance(result, float):
                if result.is_integer():
                    result = int(result)
                else:
                    result = round(result, 10)
            
            history_entry = f"{self.total_expression} = {result}"
            self.history.append(history_entry)
            self.history_listbox.insert(tk.END, history_entry)
            self.history_listbox.see(tk.END)
            
            self.current_expression = str(result)
            self.update_display()
        except Exception as e:
            self.current_expression = "Error"
            self.update_display()
    
    def update_display(self):
        if not self.current_expression:
            self.current_expression_label.config(text="0")
        else:
            display_text = self.current_expression
            # Truncate if too long
            if len(display_text) > 30:
                display_text = display_text[:27] + "..."
            self.current_expression_label.config(text=display_text)
        self.total_expression_label.config(text=self.total_expression)
    
    def toggle_theme(self):
        if self.is_dark_mode:
            self.colors = self.light_colors
            self.theme_button.config(text="🌙 Dark Mode")
        else:
            self.colors = self.dark_colors
            self.theme_button.config(text="☀️ Light Mode")
        
        self.is_dark_mode = not self.is_dark_mode
        self.apply_theme()
    
    def apply_theme(self):
        self.root.configure(bg=self.colors["bg"])
        self.main_frame.config(bg=self.colors["bg"])
        self.display_frame.config(bg=self.colors["bg"])
        self.history_frame.config(bg=self.colors["history_bg"], highlightbackground=self.colors["border"])
        self.calculator_frame.config(bg=self.colors["bg"])
        self.buttons_frame.config(bg=self.colors["bg"])
        
        # Update all labels
        for widget in self.display_frame.winfo_children():
            if isinstance(widget, tk.Frame):
                for child in widget.winfo_children():
                    if isinstance(child, tk.Label):
                        child.config(bg=self.colors["display_bg"])
                        
        self.total_expression_label.config(bg=self.colors["display_bg"], fg="#888")
        self.current_expression_label.config(bg=self.colors["display_bg"], fg=self.colors["fg"])
        self.history_label.config(bg=self.colors["history_bg"], fg=self.colors["fg"])
        self.history_listbox.config(bg=self.colors["history_bg"], fg=self.colors["fg"])
        
        self.theme_button.config(bg=self.colors["btn_bg"], fg=self.colors["btn_fg"], 
                               highlightbackground=self.colors["border"],
                               activebackground=self.lighten_color(self.colors["btn_bg"]),
                               activeforeground=self.colors["btn_fg"])
        
        # Update button colors
        for widget in self.buttons_frame.winfo_children():
            if isinstance(widget, tk.Button):
                text = widget.cget("text")
                current_bg = widget.cget("bg")
                
                # Determine new background based on button type
                if text.isdigit() or text == ".":
                    new_bg = self.colors["digit_btn_bg"]
                elif text in ["+", "-", "×", "÷", "(", ")", "^", "%"]:
                    new_bg = self.colors["operator_btn_bg"]
                elif text == "=":
                    new_bg = self.colors["equals_btn_bg"]
                elif text in ["MC", "MR", "M+", "M-"]:
                    new_bg = self.colors["memory_btn_bg"]
                elif text in ["C", "⌫", "CE"]:
                    new_bg = self.colors["special_btn_bg"]
                else:
                    new_bg = self.colors["special_btn_bg"]
                
                widget.config(bg=new_bg, fg=self.colors["btn_fg"], 
                            highlightbackground=self.colors["border"],
                            activebackground=self.lighten_color(new_bg),
                            activeforeground=self.colors["btn_fg"])

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()