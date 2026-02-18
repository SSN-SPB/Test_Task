import joblib

model = joblib.load("random_forest_model.pkl")


def fraud_check(transaction_features, model, threshold=0.07):
    """
    transaction_features: list of 10 numeric values
    threshold: probability cutoff for fraud
    """
    prob_fraud = model.predict_proba([transaction_features])[0][1]

    if prob_fraud >= threshold:
        return {"decision": "manual_review", "fraud_probability": float(prob_fraud)}
    else:
        return {"decision": "auto_approve", "fraud_probability": float(prob_fraud)}

def log_decision(tx_id, result):
    print(f"[LOG] tx_id={tx_id} decision={result['decision']} prob={result['fraud_probability']:.2f}")


# Example: a new incoming transaction
new_transaction = [250.0, 2, 1, 5, 0.2, 10, 4.5, 0.9, 1, 2]

result = fraud_check(new_transaction, model)
print(result)
log_decision("TX_99123", result)