from interface import Interface
from setup import setup
from score_prediction import predict_score, handle


def run_prediction():
    score_one = predict_score.predict(True)
    score_two = predict_score.predict(False)
    handle.write_prediction(score_one, score_two)
    handle.read_prediction()


def main():
    setup()
    Interface().run()


main()
