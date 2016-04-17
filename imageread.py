from PIL import Image
file = Image.open("lenah.jpg")
# file.show()

a = file.load()
print a
pixel_values = list(file.getdata())
# print pixel_values
w, h = file.size
pixel_mat = [[0 for x in xrange(w)] for x in xrange(h)]
print len(pixel_values)
count = 0
for x in xrange(h):
	for y in xrange(w):
		pixel_mat[x][y] = pixel_values[count]
		count+=1


# print pixel_mat[0]

t = 5
ans = [[0 for x in xrange(w)] for x in xrange(h)]
for x in xrange(h):
	for y in xrange(w):
		# if pixel_mat[x][y] > 255:
		# 	pixel_mat[x][y] /= 255
		if pixel_mat[x][y] / 25.5 > t:
			ans[x][y] = 1
		else:
			ans[x][y] = 0

# print pixel_mat[0]
final_ans = []
count = 0
for x in xrange(h):
	for y in xrange(w):
		final_ans.append( ans[x][y] )
		count+=1	

im = Image.new('1', (w,h))
# print im['im']
im.putdata(final_ans)
im.show()
# print final_ans