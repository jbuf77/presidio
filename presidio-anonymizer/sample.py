from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig, RecognizerResult

engine = AnonymizerEngine()

text = "My name is jbuf77, jbuf77"

result = engine.anonymize(
    text=text,
    analyzer_results=[
        RecognizerResult(entity_type="PERSON", start=11, end=17, score=0.8),
        RecognizerResult(entity_type="PERSON", start=19, end=25, score=0.8),
    ],
    operators={"PERSON": OperatorConfig("replace", {"new_value": "jbuf77"})},
)

print("text:", result.text)
print("items:")
print(result.items)
