import zmq
import json


class ZeroMQSocket:

    def __init__(self, topic):
        """
        Created the Subscriber Object to a ZeroMQ Topic on Port 5560.
        The Topic is passed as parameter.
        """
        self.port = "5560"
        self.topic = topic

        # Socket to talk to server
        context = zmq.Context()
        self.socket = context.socket(zmq.SUB)
        print("Connecting to server...")

        self.socket.connect(f'tcp://localhost:{self.port}')
        # Multiple Topics Subscribed
        self.socket.setsockopt_string(zmq.SUBSCRIBE, self.topic)
        print(f"Subscribe to topic {self.topic}")

    def get_topic(self):
        """
        This function gets data from the ZeroMQ 
        topic when it's made a Publish.
        The function returns a list with:
            [0]: Topic
            [1]: Topic Payload
        """
        # Receive Data from Multiple Topics
        string = self.socket.recv_multipart()
        message = string[0].decode("utf-8")
        # Split Topic and Payload
        topic, messagedata = message.split(': ', 1)
        # Remove \n character in the end of String
        messagedata = messagedata.rstrip(messagedata[-1])
        # Create Payload on JSON format (Dict)
        payload = json.loads(messagedata)

        return [topic, payload]


def main():

    print("Starting forwarder device....")

    try:
        context = zmq.Context()

        # create front end SUB socket for the forwarder coming from PUBLISHER
        subscriber = context.socket(zmq.SUB)
        # create publisher PUB socket for the forwarder coming from SUBSCRIBER
        publisher = context.socket(zmq.PUB)

        subscriber.bind("tcp://*:5550")
        subscriber.setsockopt_string(zmq.SUBSCRIBE, "")

        publisher.bind("tcp://*:5560")

        zmq.device(zmq.FORWARDER, subscriber, publisher)

    except Exception as e:
        print(e)
        print("Destroying ZMQ forwarder device.")
    finally:
        pass
        subscriber.close()
        publisher.close()
        context.term()


if __name__ == "__main__":
    main()
