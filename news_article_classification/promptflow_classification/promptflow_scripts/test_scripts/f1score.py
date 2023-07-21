from promptflow import tool
from collections import Counter
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import f1_score

def calculate_f1_score_single(ground_truth, prediction):
    # f1 score calculation using the metrics score
    f1_macro = f1_score([ground_truth],[prediction], average = 'micro')
    return f1_macro

@tool
def compute_f1_score(ground_truth: str, prediction: str) -> str:

    import string
    import re
    
    def normalize_text_prediction(prediction) -> str:
        """Lower text and remove punctuation, articles and extra whitespace."""
        substrings = ["business","personalfinance","bankingandfinancedebtmarket","stockmarketupdates","cryptocurrency","realestate","financialregulations"]
        pattern = re.compile('|'.join(map(re.escape, substrings)), re.IGNORECASE)
        prediction_1 = re.sub(r'[^A-Za-z]','',prediction)
        match = re.search(pattern, prediction_1)
        prediction_2 = match.group(0) if match else prediction_1
        prediction_2 = prediction_2.lower()
        return prediction_2

    def normalize_text_groundtruth(ground_truth) -> str:
        groundtruth = re.sub(r'[^A-Za-z]','',ground_truth)
        groundtruth = groundtruth.lower()
        return groundtruth

    substrings = ["business","personalfinance","bankingandfinancedebtmarket","stockmarketupdates","cryptocurrency","realestate","financialregulations"]
    prediction_tokens = normalize_text_prediction(prediction)
    reference_tokens = normalize_text_groundtruth(ground_truth)
    label_encoder = LabelEncoder()
    label_encoder.fit(substrings)
    ground_truth_label = label_encoder.transform([reference_tokens])[0]

    try:
        prediction_label = label_encoder.transform([prediction_tokens])[0]
    except ValueError:
        prediction_label = -1

    # Calculate the F1 score for the single data point
    f1 = calculate_f1_score_single(ground_truth_label, prediction_label)
    return f1
