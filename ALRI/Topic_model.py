#Generic Code for Topic Modeling
#May need to customize and advance later

from bertopic import BERTopic
import os
#storing documents into array to load into model
folder = r"C:\Users\12058\.vscode\ALRI\analysis_ghost\analysis_ghost"

documents = []
for doc in os.listdir(folder):
    if doc.endswith(".txt"):
        with open(os.path.join(folder, doc), "r", encoding="utf-8") as file:
            documents.append(file.read())

#NOTES: BERTopic call handles embedding and clustering
#Can customize with different embedding models after initial evaluation
topic_model = BERTopic()

#fits model on docs + creates topic for each document
topics, probs = topic_model.fit_transform(documents)

#testing
print(topic_model.get_topic_info())


