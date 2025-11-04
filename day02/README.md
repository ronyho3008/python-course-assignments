## in class assignment
[circle area](https://github.com/ronyho3008/python-course-assignments/blob/main/day02/lesson.py)

I started the assignment by converting the code from lesson to circle area
Then I asked the Chatgpt to help me understand why my code dosn't give the accepted resullts 
I used this promt:
אני רוצה לכתוב פונקציה לחישוב שטח מעגל בפיתון - מה אני מפספסת או עושה לא נכון?
def calculate_area(self):
        """Calculate and display the circle area"""
        try:
            # Get values from entries
            radius_str = self.radius_entry.get().strip()
            pai_str = self.pai_entry.get().strip()
            
            # Check if fields are empty
            if not radius_str or not pai_str:
                messagebox.showerror("Error", "Please enter both radius and pai values.")
                return
            
            # Convert to float
            radius = float(radius_str)
            pai = float(pai_str)
            
            # Check for negative values
            if radius <= 0 or pai <= 0:
                messagebox.showerror("Error", "radius and pai must be positive numbers.")
                return
            
            # Calculate area
            area = circle_area(radius, pai)

print(f"The area of the circle is: {area:.2f}")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for radius and pai.")

<span style="color: red;">I was eventually able to clean up the code and come up with a simple way to calculate the area of ​​a circle </span> 
            


