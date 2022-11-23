from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_predict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import log_loss
from cleanlab.classification import CleanLearning
from cleanlab.filter import find_label_issues
import pandas as pd

balance = True
if balance:
  train_df = pd.read_csv("model_data/balanced_train.csv", delimiter=",", header=None,
                         names=["label", "warning"])
  test_df = pd.read_csv("model_data/balanced_test.csv", delimiter=",", header=None,
                        names=["label", "warning"])
else:
  train_df = pd.read_csv("model_data/train.csv", delimiter=",", header=None,
                         names=["label", "warning"])
  test_df = pd.read_csv("model_data/test.csv", delimiter=",", header=None,
                        names=["label", "warning"])


df = pd.concat([train_df, test_df], axis=0)
# print(df.warning.values.shape)

# X = vectorizer.fit_transform(df.warning.values)
# X = X.toarray()
# print(X.shape)
# print(X.toarray())

label_map = {
  "close":0,
  "open":1,
  "unkown":2

}
warnings = df.warning.values
labels = df.label.map(label_map).values
# print(labels)

vectorizer = TfidfVectorizer(min_df=3,max_df=0.9,ngram_range=(1,2),token_pattern= '(\S+)')

vec_warnings = vectorizer.fit_transform(warnings)
# print(vec_warnings.shape)
# print(vectorizer.get_feature_names())

train_x, test_x, train_y, test_y = train_test_split(warnings, labels, test_size=0.25, random_state=2046)

mnb_model = MultinomialNB()
lr_model = LogisticRegression()
dt_model = DecisionTreeClassifier()

# print(predicts.shape)
# print(predicts)
# feature = cv.fit_transform(train_x)
# print(feature.shape)
# print(feature)

#朴素贝叶斯模型
MNB_pipeline = Pipeline([
                ('tfidf', TfidfVectorizer(min_df=3,max_df=0.9,ngram_range=(1,2),token_pattern= '(\S+)')),
                ('clf', OneVsRestClassifier(MultinomialNB())),
            ])
# do not have method predict_proba
# SVC_pipeline = Pipeline([
#                 ('tfidf', TfidfVectorizer(min_df=5,max_df=0.9,ngram_range=(1,2),token_pattern= '(\S+)')),
#                 ('clf', OneVsRestClassifier(SVC())),
#             ])

LR_pipeline = Pipeline([
                ('tfidf', TfidfVectorizer(min_df=3,max_df=0.9,ngram_range=(1,2),token_pattern= '(\S+)')),
                ('clf', OneVsRestClassifier(LogisticRegression())),
            ])

# GNB_pipeline = Pipeline([
#                 ('tfidf', TfidfVectorizer(min_df=5,max_df=0.9,ngram_range=(1,2),token_pattern= '(\S+)')),
#                 ('clf', OneVsRestClassifier(GaussianNB())),
#             ])

DT_pipeline = Pipeline([
                ('tfidf', TfidfVectorizer(min_df=3,max_df=0.9,ngram_range=(1,2),token_pattern= '(\S+)')),
                ('clf', OneVsRestClassifier(DecisionTreeClassifier())),
            ])

def model_clean(model):

  num_crossval_folds = 5
  pred_probs = cross_val_predict(model, vec_warnings, labels,
                                 cv=num_crossval_folds, method="predict_proba")

  loss = log_loss(labels, pred_probs)  # score to evaluate probabilistic predictions, lower values are better
  print(f"Cross-validated estimate of log loss: {loss:.3f}")

  predicted_labels = pred_probs.argmax(axis=1)

  # print(predicted_labels)

  acc = accuracy_score(labels, predicted_labels)

  print(f"Cross-validated estimate of accuracy on held-out data: {acc}")

  issues = CleanLearning(model).find_label_issues(vec_warnings, labels)

  print(issues)

  ranked_label_issues = find_label_issues(labels, pred_probs,
                                          return_indices_ranked_by="self_confidence")

  print(f"Cleanlab found {len(ranked_label_issues)} label issues.")
  print("Here are the indices of the top 15 most likely label errors:\n"
        f"{ranked_label_issues[:15]}")

  check_issues_labels(ranked_label_issues)


def pipeline_model_clean(pipeline):
  num_crossval_folds = 5
  pred_probs = cross_val_predict(pipeline, warnings, labels,
                                 cv=num_crossval_folds, method="predict_proba")

  loss = log_loss(labels, pred_probs)  # score to evaluate probabilistic predictions, lower values are better
  print(f"Cross-validated estimate of log loss: {loss:.3f}")

  predicted_labels = pred_probs.argmax(axis=1)

  # print(predicted_labels)

  acc = accuracy_score(labels, predicted_labels)

  print(f"Cross-validated estimate of accuracy on held-out data: {acc}")

  issues = CleanLearning(pipeline).find_label_issues(warnings, labels)

  print(issues)

  ranked_label_issues = find_label_issues(labels, pred_probs,
                                          return_indices_ranked_by="self_confidence")

  print(f"Cleanlab found {len(ranked_label_issues)} label issues.")
  print("Here are the indices of the top 15 most likely label errors:\n"
        f"{ranked_label_issues[:15]}")

  check_issues_labels(ranked_label_issues)

def check_issues_labels(ranked_label_issues):
  count_close = 0
  count_open = 0
  for i in ranked_label_issues:
    if(df.label.values[i] == 'close'):
      count_close += 1
    elif (df.label.values[i] == 'open'):
      count_open += 1
  print(f"close: {count_close}  open: {count_open}")

if __name__ == '__main__':
  # print("test")
  # print(df.label.values)
  # print(df.label.values[0])
  # pipeline_model_clean(LR_pipeline)
  model_clean(mnb_model)


