from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline


class HateModel:
    Models = {
        'mahahate-bert': 'l3cube-pune/mahahate-bert',
        'mahahate-multi-roberta': 'l3cube-pune/mahahate-multi-roberta'
    }

    def __init__(self, modelName='mahahate-bert'):
        self.modelName = modelName
        self.modelRoute = HateModel.Models[self.modelName]
        self.tokenizer = AutoTokenizer.from_pretrained(self.modelRoute)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.modelRoute)
        self.classifier = pipeline('text-classification',
                              model=self.model, tokenizer=self.tokenizer)

    def getLabels(self, text):
        result = self.classifier(text)
        self.prettyPrint(result)
        return result

    def listModels():
        modelElements = HateModel.Models
        for i in modelElements:
            print(i, ": ", modelElements[i], "\n")

    def prettyPrint(self, result):
        for dict in result:
            for i in dict:
                print("\t", i, ": ", dict[i], "\n")
