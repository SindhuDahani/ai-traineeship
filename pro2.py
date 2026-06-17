import matplotlib.pyplot as plt

# Data
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 120, 180, 200]

# Create line graph
plt.plot(months, sales)

# Add title and labels
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

# Display graph
plt.show()