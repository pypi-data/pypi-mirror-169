from statistics import mode

class VoteClassifier:
    def __init__(self):
        self.classifiers = []

    def classify(self, items, classifiers):
        self.classifiers = classifiers
        classes = []
        for item in items:            
            algorithm_name_and_votes = self._get_algorithm_name_and_votes(item)
            votes = [vote[1] for vote in algorithm_name_and_votes]
            prediction = mode(votes)
            confidence = self._get_confidence(votes, prediction)
            classes.append((prediction, confidence, algorithm_name_and_votes))
        return classes

    def _get_confidence(self, votes, prediction):
        num_of_majority_votes = len([v for v in votes if v == prediction])
        return num_of_majority_votes / len(votes) * 100
    
    def _get_algorithm_name_and_votes(self, example):
        votes = []
        for c in self.classifiers:
            v = c.predict(example)
            name = c.__class__.__name__           
            votes.append((name, v[0]))
        return votes