import matplotlib.pyplot as plt


x = ['10:00', '12:00', '14:00', '16:00', '18:00', '20:00', '22:00']
y = ['5', '10', '15', '20', '25', '30', '35']

plt.plot(x,y)
plt.yticks(y)
plt.xticks(x)


# Create the plot
plt.plot( linestyle = 'dotted')

# Add title and axis labels
plt.title('Time Series Plot')
plt.xlabel('2 hour intervals')
plt.ylabel('Number of interactions')


plt.show()
