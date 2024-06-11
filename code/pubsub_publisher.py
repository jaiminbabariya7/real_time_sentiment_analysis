from google.cloud import pubsub_v1
import time

project_id = 'YOUR_PROJECT_ID'
topic_id = 'YOUR_TOPIC_NAME'
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

def publish_message(message):
    data = message.encode('utf-8')
    future = publisher.publish(topic_path, data)
    print(f'Published message ID: {future.result()}')

if __name__ == '__main__':
    while True:
        message = input("Enter a message to publish: ")
        if message.lower() == 'exit':
            break
        publish_message(message)
        time.sleep(1)
