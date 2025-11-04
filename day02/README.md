## Class assignment
[circle area](https://github.com/ronyho3008/python-course-assignments/blob/main/day02/lesson.py)

I started the assignment by converting the code from lesson to circle area.
![circle](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzwcwNFlnSE-6rQJ34-hmEqFZ14r57CX7Dgw&s)

Then I asked the Chatgpt to help me understand why my code dosn't give the accepted resullts.

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

I was eventually able to clean up the code and come up with a simple way to calculate the area of ​​a circle :)

## Home assignment
### Dilution calculator
The code I worte using ChetGPT creates a graphical dilution calculator that determines how much stock solution and buffer are required to achieve a desired final concentration and volume. In my lab work I do many expiraments using different solutions with different concentrations and spends a lot of time calculating the needed volumes. This code already helped me in one of my expiraments which is very very cool!!

Unfortunately, after finishing writing the code, I discovered that another classmate had also written code that did a similar thing... I'm still glad I got to learn and experiment and also build a calculator that suits my needs in the lab.

![dilution](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQtM-ktPmb0GqejbYzvSkkRpZp9AIhQZXn4w&s)


            


