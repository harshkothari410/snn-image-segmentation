from PIL import Image

def imageread(filename):
	file = Image.open(filename)
	pixel_values = list(file.getdata())

	# Compute H and W
	w, h = file.size

	# compute pixel matrix
	pixel_mat = [[0 for x in xrange(w)] for x in xrange(h)]
	
	count = 0

	for x in xrange(h):
		for y in xrange(w):
			# print type(pixel_values[count])
			try:
				if len( pixel_values[count] ) > 1:
					pixel_mat[x][y] = pixel_values[count][0] #check whether is 
				else:
					pixel_mat[x][y] = pixel_values[count]
				count+=1
			except:
				pixel_mat[x][y] = pixel_values[count]
				count+=1

	return pixel_mat, w, h

def imagewrite(data, w, h):
	
	final_ans = []
	count = 0
	for x in xrange(h):
		for y in xrange(w):
			final_ans.append( data[x][y] )
			count+=1

	im = Image.new('1', (w,h))
	# print im
	im.putdata(final_ans)
	im.show()

def imagesave(data, w, h, name):
	final_ans = []
	count = 0
	for x in xrange(h):
		for y in xrange(w):
			final_ans.append( data[x][y] )
			count+=1

	im = Image.new('1', (w,h))
	# print im
	im.putdata(final_ans)
	im.save(name+'.jpg')