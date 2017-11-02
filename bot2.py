from client import ChatClient
import time

_SERVER_HOST = '127.0.0.1' # server
_SERVER_PORT = 10000

def main():
	chat_client = ChatClient(_SERVER_HOST, _SERVER_PORT)
	chat_client.start()
	time.sleep(10)

	print("Misha")
	chat_client.input_message("Misha")
	
	while True:
		time.sleep(10)
		print("Nice to meet you I'm Misha")
		chat_client.input_message("Nice to meet you I'm Misha")

if __name__ == '__main__':
	main()