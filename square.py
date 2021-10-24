class Square:
    lower_bound = "_"
    left_bound = "|"
    right_bound = "|"
    marked = False
    distance = 0
    lower_bound_with_end = "\u0332!"
    lower_bound_with_start = "\u0332?"
    lower_bound_with_path = "\u0332*"
 
    def __str__(self):
        return self.left_bound + self.lower_bound + self.right_bound
 
    def path_mark(self):
        if self.lower_bound == self.lower_bound_with_end or \
                self.lower_bound == self.lower_bound_with_start or \
                self.lower_bound == "!" or self.lower_bound == "?":
            pass
        else:
            if self.lower_bound == "_":
                self.lower_bound = self.lower_bound_with_path
            elif self.lower_bound == " ":
                self.lower_bound = "*"
 
    def start(self):
        self.lower_bound = self.lower_bound_with_start
 
    def finish(self):
        if self.lower_bound == "_":
            self.lower_bound = self.lower_bound_with_end
        else:
            self.lower_bound = "?"
 
    def clear_left_bound(self):
        self.left_bound = " "
 
    def clear_right_bound(self):
        self.right_bound = " "
 
    def clear_lower_bound(self):
        if self.lower_bound == self.lower_bound_with_end:
            self.lower_bound = "!"
        elif self.lower_bound == self.lower_bound_with_start:
            self.lower_bound = "?"
        else:
            self.lower_bound = " "
