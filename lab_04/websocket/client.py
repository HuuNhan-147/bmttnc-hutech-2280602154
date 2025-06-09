import tornado.ioloop
import tornado.websocket

class WebSocketClient:
    def __init__(self, io_loop):
        self.connection = None
        self.io_loop = io_loop

    def start(self):
        self.connect_and_read()

    def stop(self):
        self.io_loop.stop()

    def connect_and_read(self):
        print("Connecting and reading...")
        tornado.websocket.websocket_connect(
            url="ws://localhost:8888/websocket/",  # URL của WebSocket server
            callback=self.maybe_retry_connection,  # Callback khi kết nối thành công
            on_message_callback=self.on_message,  # Callback khi nhận tin nhắn
            ping_interval=10,  # Thời gian gửi ping đến server
            ping_timeout=30,  # Thời gian chờ phản hồi từ server
        )

    def maybe_retry_connection(self, future) -> None:
        try:
            self.connection = future.result()  # Nhận kết nối WebSocket nếu thành công
            print("Connected to WebSocket server.")
        except Exception as e:
            print(f"Could not connect, retrying in 3 seconds... Error: {e}")
            self.io_loop.call_later(3, self.connect_and_read)  # Thử kết nối lại sau 3 giây

    def on_message(self, message):
        if message is None:
            print("Disconnected, reconnecting...")
            self.connect_and_read()
            return

        print(f"Received word from server: {message}")
        self.connection.read_message(callback=self.on_message)  # Tiếp tục đọc tin nhắn

def main():
    io_loop = tornado.ioloop.IOLoop.current()  # Lấy I/O loop hiện tại
    client = WebSocketClient(io_loop)  # Tạo đối tượng client WebSocket

    io_loop.add_callback(client.start)  # Gọi hàm start của client
    io_loop.start()  # Bắt đầu vòng lặp I/O

if __name__ == "__main__":
    main()  # Chạy chương trình
