from score_prediction import predict_score
from interface import Interface
from score_prediction import handle

def main():
    score_one = predict_score.predict(False)
    score_two = predict_score.predict(True)
    handle.write_prediction(score_one, score_two)
    handle.read_prediction()



main()
