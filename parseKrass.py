import sys


def compile_krass(krass_file_contents):
	return ""


# sys.argv should = [script name, raw file, compiled file]
if len(sys.argv) != 3:
	# this should never happen, because this is called from a shell script. 
	# If it does, theres an issue passing files along between Shell and Python

	exit(1)

raw_file = sys.argv[1]
compiled_file = sys.argv[2]

compiled_file = open(compiled_file, 'w')

contents = open(raw_file, 'r').read()

for chunk in contents.split("?::"):
	if "::?" in chunk:
		# contains a krass chunk
		tex_chunk, krass_chunk = chunk.split("::?")[0], chunk.split("::?")[1]
		
		compiled_file.write(tex_chunk)
		compiled_file.write(compile_krass(krass_chunk))

	else:
		# probably end, no krass chunk, or malformed. 
		compiled_file.write(chunk)

