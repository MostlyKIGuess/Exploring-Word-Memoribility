import random
import re


# Extract words using regular expressions 
# words = re.findall(r'\b\w+\b', report_text.lower()) 


# --- Word Selection & MCQ Generation ---

extremely_recallable = ["memorability", "recall", "probability", "words", "analysis", "dataset",
                       "semantic", "properties", "frequency", "length", "concreteness", "arousal",
                       "valence", "animacy", "usefulness", "correlation", "regression", "model",
                       "distribution", "visualization", "figures", "participants", "sessions",
                       "lexical", "affective", "statistical", "relationship", "variables", "findings",
                       "hypothesis", "effects", "cognitive", "neural", "brain", "regions", "encoding",
                       "retrieval", "attention", "dnn", "models", "interaction", "predict", "key",
                       "explored", "suggests", "observed", "influence", "significant", "plot", "matrix",
                      "properties"]

mildly_recallable = ["information", "experiments", "conducted", "properties", "examined", "bins", "violin", "box", "plot",
                     "scatterplot", "correlation", "matrix", "regression", "model", "interaction", "effect", "bands", "multifaceted", "nature","judgments", "output","patterns", "density", "comparisons","output", "indicates", "levels", "jointly", "influence",
                    "cross", "linguistic", "compared", "datasets", "available", "accessible", "transparency", "reproducibility",
                    "comprises", "sessions", "calculated","normed", "encompassing", "features", "dimensions", "operationalized", "metric", "retrievability", "exploratory",
                    "visualizations", "characteristics", "histograms", "density", "estimates", "correlations", "coefficient"]

hard_to_recall = [ "operationalizations", "quantiles", "kernel", "tapers", "pairwise", "lmplot", "conjunctions", "interdisciplinary", "orthographic", "phonological", "epiphenomenon",
                 "monogamous", "operationalized"]

unknown_words = ["jazz", "rhythm", "blizzard", "galaxy", "oxygen", "equation", "algorithm", "quantum",
                 "microphone", "strawberry"]  # These aren't in the report





all_word_sets = [extremely_recallable, mildly_recallable, hard_to_recall, unknown_words ]
all_words = set()

for word_set in all_word_sets:
    all_words.update(word_set)


num_questions = 20
num_questions_per_category = num_questions // len(all_word_sets)
score = 0

categories = {
    "Extremely Recallable": extremely_recallable,
    "Mildly Recallable": mildly_recallable,
    "Hard to Recall": hard_to_recall,
    "Unknown": unknown_words
}

all_known_words = extremely_recallable + mildly_recallable + hard_to_recall
random.shuffle(all_known_words)


print("\nWelcome to the Word Recall Challenge!\n")
print("First, carefully read the report provided. Pay close attention to the words used in the data analysis sections.") # User reads report.
input("Press Enter when you're ready to begin the recall test...") # Press enter to continue
# Questions for known words (mixed categories)

for i in range(num_questions ):
    word = all_known_words[i]
    category_name = [cat for cat, word_list in categories.items() if word in word_list][0] 

    recall_response = input(f"Do you recall the word '{word.title()}' being mentioned in the report? (y/n): ").lower()


    if recall_response == "y":
        score += 1
        print(f"Correct. '{word.title()}' is classified as a '{category_name}' word.")  # Provide feedback with the category
    else:
        print(f"Incorrect. '{word.title()}' *was* mentioned. It's categorized as '{category_name}'. Review the report.")


print("\n--- Quiz Results ---")
print(f"Your final score: {score}/{num_questions_per_category * len(categories)}")

print("\nKey takeaway:  Our memory for words is influenced by multiple factors, including how salient they are in a given context.") # Final message
print("Active engagement with the analysis and its key terms strengthens these memory connections.")