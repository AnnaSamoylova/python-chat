import sys
import math
import struct
import socket
import select
import threading

_SERVER_HOST = '127.0.0.1' # server
_SERVER_PORT = 10000

class ChatClient(threading.Thread):
	RECV_BUFFER = 4096
	RECV_MSG_LEN = 4
	
	def __init__(self, serv_host, serv_port):
		"""
		Initializes a new ChatServer.

		:param host: the host on which the client is bounded
		:param port: the port on which the client is bounded
		"""
		threading.Thread.__init__(self)
		self.serv_host = serv_host
		self.serv_port = serv_port
		self.message = None;
		self.running = True  # tells whether the server should run
		
	def _bind_client_socket(self):
		"""
		Creates the client socket and binds it to the given host and port.
		"""
		self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
	def _connect_to_server(self):
		try:
			self.client_socket.connect((self.serv_host, self.serv_port))
		except:
			print("Unable to connect to server: " + self.serv_host + ":" + self.serv_port)
			sys.exit()
	
	def _send_to_server(self, msg):
		"""
		Prefixes each message with a 4-byte length before sending.

		:param sock: the incoming socket
		:param msg: the message to send
		"""
		# Packs the message with 4 leading bytes representing the message length
		msg = struct.pack('>I', len(msg)) + msg.encode()
		# Sends the packed message
		self.client_socket.send(msg)

	def _receive_from_server(self):
		"""
		Receives an incoming message from the client and unpacks it.

		:param sock: the incoming socket
		:return: the unpacked message
		"""
		data = None
		# Retrieves the first 4 bytes from the message
		tot_len = 0
		while tot_len < self.RECV_MSG_LEN:
			msg_len = self.client_socket.recv(self.RECV_MSG_LEN)
			tot_len += len(msg_len)
		# If the message has the 4 bytes representing the length...
		if msg_len:
			data = ''
			# Unpacks the message and gets the message length
			msg_len = struct.unpack('>I', msg_len)[0]
			tot_data_len = 0
			while tot_data_len < msg_len:
				# Retrieves the chunk i-th chunk of RECV_BUFFER size
				chunk = self.client_socket.recv(self.RECV_BUFFER)
				# If there isn't the expected chunk...
				if not chunk:
					data = None
					break # ... Simply breaks the loop
				else:
					# Merges the chunks content
					data += chunk.decode()
					tot_data_len += len(chunk)
		return data
	
	def _run(self):
		"""
		Actually runs the client.
		"""
		print("Client is running. Please input you nickname:)")
		while self.running:
			# Gets the list of sockets which are ready to be read through select non-blocking calls
			# The select has a timeout of 0.5 seconds, because need some time to send messages
			try:
				ready_to_read, ready_to_write, in_error = select.select([self.client_socket], [], [], 0.5)
			except socket.error:
				continue
			else:
				for sock in ready_to_read:
					# If the socket instance is the server socket...
					if sock == self.client_socket:
						try:
							data = self._receive_from_server()
							if not data:
								print('\nDisconnected from chat server')
								break
							else:
								#print data
								print(data)
						except socket.error:
							break
				# send message
				if self.message is not None:
					try:
						self._send_to_server(self.message)
					except:
						print('\nMessage send error')
						break
					finally:
						self.message = None
		self.stop()

	def stop(self):
		"""
		Stops the client by setting the "running" flag before closing
		the socket connection.
		"""
		self.running = False
		self.client_socket.close()
	
	def input_message(self, msg):
		self.message = msg
					
	def run(self):
		"""Given server host and a port, binds the socket and runs the client.
		"""
		self._bind_client_socket()
		self._connect_to_server()
		self._run()
		
def main():
	"""
	The main function of the program. It creates and runs a new ChatClient.
	"""
	chat_client = ChatClient(_SERVER_HOST, _SERVER_PORT)
	chat_client.start()
	while True:
		msg = input()
		chat_client.input_message(msg)

if __name__ == '__main__':
	"""The entry point of the program. It simply calls the main function.
	"""
	main()