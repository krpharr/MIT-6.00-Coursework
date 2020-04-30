import matplotlib.pyplot as plt

plt.plot([100,200,300,400], [100,200,300,400])
plt.axis([0, 1600, 0, 800])
plt.title('Time to clean % of room with n robots')
plt.xlabel('Room area')
plt.ylabel('Timesteps')
plt.show()
