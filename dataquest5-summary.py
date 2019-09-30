#%% [markdown]
# # Storytelling Through Data Visualization
# ## Improviing Plot Aesthetics

#%%
# Generating one line graph
import pandas as pd
import matplotlib.pyplot as plt

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
plt.plot(women_degrees['Year'], women_degrees['Biology'])
plt.show()

#%%
# Generating two lines graph
fig = plt.figure()
men_biology = 100 - women_degrees['Biology']

plt.plot(women_degrees['Year'], women_degrees['Biology'], c = 'blue', label = 'Women')
plt.plot(women_degrees['Year'], men_biology, c = 'red', label = 'Men')

plt.legend(loc = "upper right")
plt.title("Percentage of Biology Degrees Awarded By Gender")
plt.show()

#%%
# Customize the appearane of the ticks

fig, ax = plt.subplots()
ax.plot(women_degrees['Year'], women_degrees['Biology'], label='Women')
ax.plot(women_degrees['Year'], 100-women_degrees['Biology'], label='Men')

ax.tick_params(bottom="off", top="off", left="off", right="off")
ax.set_title('Percentage of Biology Degrees Awarded By Gender')
ax.legend(loc="upper right")
plt.show()

#%%
# Remove the Spines in the Chart

fig, ax = plt.subplots()
ax.plot(women_degrees['Year'], women_degrees['Biology'], label='Women')
ax.plot(women_degrees['Year'], 100-women_degrees['Biology'], label='Men')
ax.tick_params(bottom="off", top="off", left="off", right="off")
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

ax.legend(loc='upper right')
ax.set_title('Percentage of Biology Degrees Awarded By Gender')
plt.show()

#%% [markdown]
# Another way of removing spines

for key, spine in ax.spines.items():
    spine.set_visible(False)

#%%
# Generating 2x2 graph with no tick and no spines

major_cats = ['Biology', 'Computer Science', 'Engineering', 'Math and Statistics']
fig = plt.figure(figsize=(12, 12))

for sp in range(0,4):
    ax = fig.add_subplot(2,2,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[major_cats[sp]], c='blue', label='Women')
    ax.plot(women_degrees['Year'], 100-women_degrees[major_cats[sp]], c='green', label='Men')
    ax.set_title(major_cats[sp])
    ax.tick_params(bottom="off", top="off", left="off", right="off")
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0, 100)

# Calling pyplot.legend() here will add the legend to the last subplot that was created.
plt.legend(loc='upper right')
plt.show()

#%% [markdown]
# ## Color, Layout nd Annotations