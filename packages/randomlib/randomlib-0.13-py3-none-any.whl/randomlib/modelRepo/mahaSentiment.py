from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline


class SentimentModel:
    Models = {
        'MarathiSentiment': 'l3cube-pune/MarathiSentiment'
    }

    def __init__(self, modelName='MarathiSentiment'):
        self.modelName = modelName
        self.modelRoute = SentimentModel.Models[self.modelName]
        self.tokenizer = AutoTokenizer.from_pretrained(self.modelRoute)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.modelRoute)
        self.classifier = pipeline('text-classification',
                              model=self.model, tokenizer=self.tokenizer)
    def getLabels(self, text):
        result = self.classifier(text)
        self.prettyPrint(result)
        return result

    def listModels():
        modelElements = SentimentModel.Models
        for i in modelElements:
            print(i, ": ", modelElements[i], "\n")

    def prettyPrint(self, result):
        for dict in result:
            for i in dict:
                print("\t", i, ": ", dict[i], "\n")
