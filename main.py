from interface import Interface
from score_prediction import predict_score

def main():
    with open("prediction.txt", "w") as file:
        score_one = predict_score.predict(False)
        score_two = predict_score.predict(True)
        file.write(str(score_one) + "\n" + str(score_two))


main()
