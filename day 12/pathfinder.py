def pathfinder(world_matrix, start, stop):
	"""
	Solution to #30DOC day 12 python intermediate
	"""
	# input validation block
	assert type(world_matrix) == list
	assert type(start) == tuple
	assert type(stop) == tuple
	for i in world_matrix:
		assert all(map(lambda x: isinstance(x,int), i))
		assert all(map(lambda x: x == 0 or x == 1, i))
	start, stop = [start[0], start[1]], [stop[0], stop[1]]
	rem = lambda n: world_matrix[n[0]][n[1]] == 1
	assert rem(start) and rem(stop)
	
	# function definition block
	def get_neighbors(pos):
		
		def is_valid(arr):
			if (arr[0] < 0 or arr[0] >= len(world_matrix)) or (arr[1] < 0 or arr[1] >= len(world_matrix[0])):
				return False
			return True
		
		steps = [[1, 0], [0, 1], [-1, 0], [0, -1]] # this can be edited to allow for diagonal movement
		
		neighbors = [[pos[0] + step[0], pos[1] + step[1]] for step in steps]
		
		neighbors = [neighbor for neighbor in neighbors if is_valid(neighbor)]
		
		return neighbors
	
	
	def solve(pos, path, depth, steps=0):
		neighbors = get_neighbors(pos)
		for curr in neighbors:
			if curr in path or int(world_matrix[curr[0]][curr[1]]) == 0:
				continue
			path_ = path+[curr]
			if curr == stop and (len(path) < len(stats['ans']) or len(stats['ans']) == 0):
				stats[f'ans'] = path_
				stats['steps'] = steps + 1
			elif len(stats['ans']) >= len(path_) or len(stats['ans']) == 0:
				solve(curr, path_, depth+1, steps+1)
	
	# main block
	stats = {'steps': 0, 'ans': []}
	solve(start, [start], 0)
	if len(stats['ans']) == 0:
		raise AssertionError
	# print(stats['ans'])
	return stats['steps']