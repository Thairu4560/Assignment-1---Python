"""
Program to plot weekly temperature readings using matplotlib
"""

import matplotlib.pyplot as plt

def plot_temperatures():
    # Data
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    temperatures = [20, 22, 19, 23, 21, 24, 20]
    
    # Create figure
    plt.figure(figsize=(8, 4))
    
    # Plot data with styling
    plt.plot(days, temperatures, 
             marker='o', 
             color='red', 
             linestyle='-', 
             linewidth=2,
             markersize=8)
    
    # Add titles and labels
    plt.title('Weekly Temperature Readings', fontsize=14)
    plt.xlabel('Day of Week', fontsize=12)
    plt.ylabel('Temperature (°C)', fontsize=12)
    
    # Add grid and adjust layout
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    # Save and show plot
    plt.savefig('temperature_plot.png')
    plt.show()

if __name__ == "__main__":
    plot_temperatures()
