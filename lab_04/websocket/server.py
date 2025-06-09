import random
import tornado.ioloop
import tornado.web
import tornado.websocket

# WebSocket server class
class WebSocketServer(tornado.websocket.WebSocketHandler):
    clients = set()

    def open(self):
        WebSocketServer.clients.add(self)

    def on_close(self):
        WebSocketServer.clients.remove(self)

    @classmethod
    def send_message(cls, message: str):
        print(f"Sending message {message} to {len(cls.clients)} client(s).")
        for client in cls.clients:
            client.write_message(message)

# Random word selector class
class RandomWordSelector:
    def __init__(self, word_list):
        self.word_list = word_list  # Initialize with a list of words

    def sample(self):
        return random.choice(self.word_list)  # Randomly select a word

# Main application function
def main():
    app = tornado.web.Application(
        [(r"/websocket/", WebSocketServer)],  # WebSocket route
        websocket_ping_interval=10,  # Interval for pinging clients
        websocket_ping_timeout=30,  # Timeout for the ping
    )
    app.listen(8888)  # Listen on port 8888

    io_loop = tornado.ioloop.IOLoop.current()  # Get the current I/O loop

    word_selector = RandomWordSelector(['apple', 'banana', 'orange', 'grape', 'melon'])  # Word list

    # Create a periodic callback to send a random word every 3 seconds (3000 milliseconds)
    periodic_callback = tornado.ioloop.PeriodicCallback(
        lambda: WebSocketServer.send_message(word_selector.sample()), 3000
    )
    periodic_callback.start()  # Start periodic callback

    io_loop.start()  # Start the I/O loop

# Entry point for the application
if __name__ == "__main__":
    main()
