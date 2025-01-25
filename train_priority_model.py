from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import pickle

# training the data with 16 training sets 
X_train = [
    "Finish the report for work",
    "Study for the upcoming exam",
    "Prepare slides for the meeting",
    "Email the professor about the assignment",
    "Clean the house and vacuum the floors",
    "Organise clothes in the wardrobe",
    "Work on a personal coding project",
    "Relax and watch a movie",
    "Call friends for a chat",
    "Read a fiction book before bed",
    "Plan the weekly grocery shopping",
    "Exercise at the gym",
    "Write a blog post for the website",
    "Meditate for 10 minutes",
    "Fix the leaking faucet",
    "Attend a family dinner",
]
y_train = [
    "High", "High", "High", "Medium", "Medium", "Medium", 
    "Medium", "Low", "Low", "Low", "Medium", "High", 
    "Medium", "Low", "Medium", "Low"
]

# pipeline using vectorizer + Naive Bayes Classifier
model = make_pipeline(CountVectorizer(), MultinomialNB())

# Train the model
model.fit(X_train, y_train)

# Save the model to a .pkl file
model_path = "task_model.pkl"
with open(model_path, "wb") as f:
    pickle.dump(model, f)

print(f"Model saved to {model_path}")