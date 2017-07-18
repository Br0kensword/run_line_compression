import json, argparse


def encode(data):
	"""takes in a string representation of ASCII art, compresses it via run-length
	encoding and packages the resulting string into a JSON object for transport
	via TCP or what have you. 

	Adds / to seperate token runs in the encoded string to serve as breakpoints for
	decoding later.
	"""
	if not data:
		return False

	else:
		encoded_data = []
		token = None
		token_count = 0

		for char in data:

			if token == None:
				token = char
				token_count += 1

			elif char != token:
				encoded_data.append(token + str(token_count))
				token = char
				token_count = 1

			else:
				token_count += 1

		#need to append the last line to our encoded data
		encoded_data.append(token + str(token_count))
		encoded_string = '/'.join(encoded_data)
		#make a check if the encoded string is less than the original, if not we just send the original
		if len(encoded_string) < len(data):
			transport_dict = {'data': encoded_string, 'encode': 1}
								
		else:
			transport_dict = {'data': data, 'encode': 0}
		#converting string to python dict then converting into JSON object
		transport = json.dumps(transport_dict)		
		return transport

def decode(data):
	"""Takes in a JSON object, extracts a compressed string
	and decompresses it.

	This takes into account that / might be in the ascii art and checks 
	for empty elements in the resulting split list. If we find an empty
	element we add the / back to the next element of the split list
	"""
	if not data:
		return False

	else:
		#converting JSON into python dict then setting data to compressed string 
		encoded_data = json.loads(data)
		data = encoded_data['data']
		#if we have an encoded file we decode it otherwise we just return the original image data
		encode_flag = encoded_data['encode']

		if encode_flag == 1:
			decoded_data = ''
			token_break = False
			token_list = data.split('/')

			for pair in token_list:
				if pair != '' and token_break == False:
					token = pair[0]
					num = pair[1:]
					#for long strings concatenation might become a bottleneck
					decoded_data += token * int(num)

				elif pair == '':
					token_break = True

				else:
					#here we add back in the / that is lost during the split function above if / is in the ascii image
					token = "/"
					num = pair[0:]
					decoded_data += token * int(num)
					token_break = False

		else:
			#here we just return the unencoded data since encoding in this case was inefficient
			decoded_data = data
		return decoded_data






if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--file', dest='filename', help="add a path to a text file with ascii art")
	args = parser.parse_args()
	with open(args.filename) as image:

		data = image.read()
		image.close()
		compressed = encode(data)

		if  not compressed:
			print("There is no image or an empty file was given. Please check your file and try again") 

		else:
			uncompressed = decode(compressed)
			#uncomment the following lines to get performance analytics

			#encoded_data = json.loads(compressed)
			#encoding_check = encoded_data['encode']

			#print(data)  #display the original image
			#print("# of tokens in image before compression", len(data))
			#print("# of tokens after compression", len(compressed))
			#if encoding_check == 1: #testing if we encoded the image or not
			#	print("this is a ", (1 - len(compressed) / len(data)) , ' reduction')
			#else:
			#	print("Original file has been sent")
			#print("# of tokens uncompressed", len(uncompressed))
			print(uncompressed)