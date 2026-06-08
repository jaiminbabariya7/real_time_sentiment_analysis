# Real-Time Sentiment Analysis Pipeline

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![GCP](https://img.shields.io/badge/GCP-Pub%2FSub%20%7C%20Dataflow-4285F4?logo=googlecloud)
![Transformers](https://img.shields.io/badge/Transformers-HuggingFace-yellow?logo=huggingface)
![Apache Beam](https://img.shields.io/badge/Apache%20Beam-Dataflow-orange?logo=apachebeam)
![License](https://img.shields.io/badge/License-MIT-green)

> Real-time social media sentiment analysis: streaming ingestion via Pub/Sub → Apache Beam / Dataflow transforms → transformer-based NLP classification → BigQuery results + live dashboard.

## Architecture
```
Social Media / Event Stream
        ↓
Google Cloud Pub/Sub
  └── Topic: raw-text-events
        ↓
Apache Beam (Cloud Dataflow)
  ├── Read from Pub/Sub (streaming)
  ├── Text preprocessing (clean, tokenise)
  ├── Sentiment classification (DistilBERT)
  └── Write to BigQuery + GCS archive
        ↓
BigQuery: sentiment_results table
        ↓
Real-Time Dashboard (Data Studio / Flask)
```

## Sentiment Classification
Uses a fine-tuned **DistilBERT** model for 3-class sentiment:
- 😊 **Positive** — confidence score + label
- 😐 **Neutral** — ambiguous or factual text
- 😞 **Negative** — complaint or critical text

## Project Structure
```
├── code/
│   ├── pubsub_publisher.py    # Simulates event stream
│   └── dataflow_main.py       # Apache Beam pipeline
├── requirements.txt
├── project_architecture       # Architecture diagram
└── workflow                   # Pipeline workflow docs
```

## Setup
```bash
git clone https://github.com/jaiminbabariya7/real_time_sentiment_analysis
cd real_time_sentiment_analysis && pip install -r requirements.txt
export GOOGLE_APPLICATION_CREDENTIALS=path/to/sa.json
export GCP_PROJECT_ID=your-project
# Start publisher
python code/pubsub_publisher.py
# Deploy Dataflow pipeline
python code/dataflow_main.py --runner=DataflowRunner --project=$GCP_PROJECT_ID
```

## Skills Demonstrated
`Apache Beam` · `Cloud Dataflow` · `Pub/Sub` · `NLP` · `Transformers` · `BigQuery` · `Streaming` · `Python`
