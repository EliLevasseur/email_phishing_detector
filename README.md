# 🧠 Can Python Detect a Phishing Email?

### Overview
This is a 10-day beginner Python case study exploring how simple text analysis can detect phishing emails.  
The goal: go from a rule-based keyword detector → to a basic trained model by the end.

### Tools
- Python 3  
- pandas (data exploration)  
- matplotlib (visualization)  
- scikit-learn (for final ML model)

---

### Original Project Timeline
| Day | Focus | Outcome |
|-----|--------|----------|
| 1 | Setup & dataset creation | Folder, README, first dataset |
| 2 | Load & explore data | Basic stats & text insights |
| 3 | Keyword frequencies | Visualize phishing terms |
| 4 | Rule-based detector | First detection logic |
| 5 | Accuracy & cleanup | Confusion matrix, tweaks |
| 6 | CLI packaging | Simple `predict_email.py` |
| 7 | Text → numbers | TF-IDF vectorization |
| 8 | Train ML model | Logistic Regression |
| 9 | Polish & summarize | Documentation |
| 10 | Publish & share | GitHub + LinkedIn case study |

---

### Progress Log
**Day 1:** Set up project, wrote README, made starter dataset, tested environment.  
**Day 2:** Expanded dataset to 24 rows, loaded it with pandas, explored phishing vs legit text length.  
**Day 3:** Counted keyword frequencies and saved the top phishing words visualization.  
**Day 4:** Built the rule-based detector, generated predictions, and plotted its confusion matrix.  
**Day 5:** Reviewed false positives/negatives and tightened the evaluation flow.  
**Day 6:** Added the CLI helper for quick rule-based predictions.  
**Day 7:** Created first logistic regression model and compared results to the rule based detector.  



---

### Next Steps
### 🚀 Next Steps
- **Expand the dataset** to improve generalization and reduce performance volatility on unseen emails.  
- **Fine-tune the TF-IDF and Logistic Regression model** to increase precision and stability.  
- **Experiment with additional algorithms** such as **Naive Bayes** and **Random Forest** for model comparison.  
- **Visualize and compare results** between the rule-based and ML models using updated confusion matrices and performance metrics.  
- **Package the best-performing model** into a simple **CLI or web demo** for real-world testing and sharing.  
- **Document key lessons learned** and insights in the final case study report.


---

### Author
**Eli Levasseur** — Student exploring cybersecurity, Python, and AI.  
*documenting every step to building real world projects.*
