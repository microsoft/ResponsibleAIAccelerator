from promptflow import tool
import re

@tool
def grade(groundtruth: str, prediction: str):
    substrings = ["Business","PersonalFinance","BankingandfinanceDebtmarket","StockMarketupdates","Cryptocurrency","Realestate","FinancialRegulations"]
    pattern = re.compile('|'.join(map(re.escape, substrings)), re.IGNORECASE)
    prediction = re.sub(r'[^A-Za-z]','',prediction)
    match = re.search(pattern, prediction)
    prediction = match.group(0) if match else prediction
    groundtruth = re.sub(r'[^A-Za-z]','',groundtruth)
    return "Correct" if groundtruth.lower() == prediction.lower() else "Incorrect"