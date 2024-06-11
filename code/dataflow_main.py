import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions
from google.cloud import language_v1

class AnalyzeSentiment(beam.DoFn):
    def __init__(self):
        super(AnalyzeSentiment, self).__init__()
        self.client = language_v1.LanguageServiceClient()

    def process(self, element):
        document = language_v1.Document(content=element, type_=language_v1.Document.Type.PLAIN_TEXT)
        sentiment = self.client.analyze_sentiment(request={'document': document}).document_sentiment
        yield {'text': element, 'score': sentiment.score}

def run():
    pipeline_options = PipelineOptions()
    pipeline_options.view_as(StandardOptions).streaming = True

    with beam.Pipeline(options=pipeline_options) as p:
        input_topic = 'projects/YOUR_PROJECT_ID/topics/YOUR_TOPIC_NAME'

        messages = (p
                    | 'Read from Pub/Sub' >> beam.io.ReadFromPubSub(topic=input_topic)
                    | 'Decode' >> beam.Map(lambda x: x.decode('utf-8'))
                    | 'Analyze Sentiment' >> beam.ParDo(AnalyzeSentiment())
                    | 'Print Results' >> beam.Map(print))

if __name__ == '__main__':
    run()
