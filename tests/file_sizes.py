import os

size_list = {
	'http://imgur.com/a/TPbjI': 0,
	'http://i.imgur.com/uAQwWz3.png': 85401,
	'https://gfycat.com/RegalFrighteningIsabellinewheatear': 2201577,
	'http://imgur.com/a/fNmS3': 259480,
	'http://wehavekookies.tumblr.com/post/171206791864/shak%C3%A4ste': 819161
}

# Check all file sizes to be sure all downloaders are properly functioning.
# Does not confirm the # of files, but leaves that to the 'file_names' tester.


def run_test(re):
	eles = re.get_elements()
	for e in eles:
		# noinspection PyProtectedMember
		for u, f in e._file_map.items():
			if os.path.isdir(f):
				continue
			# print("'%s':%i," % (u, os.path.getsize(f) ));
			if u not in size_list or os.path.getsize(f) != size_list[u]:
				return 'Invalid URL filesize: [%s]!=[%i]' % (u, os.path.getsize(f)), 1  # !cover
	return '', 0
