from score_prediction import predict_score
from interface import Interface
from score_prediction import handle
from setup import setup
from subprocess import call
def main():
    setup()
    score_one = predict_score.predict(True)
    score_two = predict_score.predict(False)
    handle.write_prediction(score_one, score_two)
    handle.read_prediction()



