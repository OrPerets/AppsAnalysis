
from variables import *
from functions import read_file
import matplotlib.pyplot as plt 


normalized_data = os.path.join(FILE_PATH, "unsupervised_dummy.xlsx")
normalized_df = read_file(normalized_data)

groups = normalized_df.groupby("Cluster")

group5 = groups.get_group(5)
group1 = groups.get_group(1)
plt.hist(group5["Sentiment"], alpha=0.7, label="5")
plt.hist(group1["Sentiment"], alpha=0.7, label="1")
plt.xlim(-2,2)
plt.legend()
plt.show()

group8 = groups.get_group(8)
plt.hist(group5["Sentiment"], alpha=0.7, label="5")
plt.hist(group8["Sentiment"], alpha=0.7, label="8")
plt.legend()
plt.show()


print("FINISHED")