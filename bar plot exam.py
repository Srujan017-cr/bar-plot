#bar plot (Vertical)
import matplotlib.pyplot as plt
import seaborn as sns
#Creating a style
sns.set_style('darkgrid')
#Assigning the values for barplot
x = [2014, 2015, 2016, 2017, 2018, 2019]
y = [18500, 12700, 600, 14560, 8550, 11420]
colors=['orange', 'yellow', 'green', 'blue', 'pink', 'red']
#Creating a horizontal bar plot
plt.barh(x, y, color=colors)
#Adding title and Labels
plt.title('Barplot')
plt.xlabel("Gross amount")
plt.ylabel("Year")
#Display the plot
plt.show()