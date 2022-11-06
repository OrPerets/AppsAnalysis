
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

# Conclusions: 

# free apps recieve higher sentiment and paid apps recieve lower sentiment rating
# People react to free apps in a positive manner

# Reviews in cluster 8 contain apps with a neutral review - not affecting the sentiment ( Sentiment is 0)
# Reviews in cluster 5 vary from -1 to 1 ( As expected)

