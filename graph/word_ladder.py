class Solution():

	def word_ladder(self,wordList,src,dest):
		if dest not in wordList:
			return 0

		# adj = defaultdict(list)
		# wordList.append(src)

		# for word in wordList:
		# 	for i in range(len(word)):
		# 		pattern = word[:i] + "*" + word[i+1:]
		# 		adj[pattern].append(word)

		queue = [(src,1)]

		while queue:
			word,length = queue.pop(0)

			if word==dest:
				return length

			for i in range(len(word)):
				for j in "abcdefghijklmnopqrstuvwxyz":
					new_ = word[:i] + j + word[i+1:]
					if new_ in wordList:
						queue.append((new_,length+1))
						wordList.remove(new_)
		return 0



	def wordLadder2(self,wordList,src,dest):
		#will result in tle
		if dest not in wordList:
            return []

        queue = [[src]]
        if src in wordList:
            wordList.remove(src)
        while queue:
           
            removed = set()
            for _ in range(len(queue)):
                
                word_l = queue.pop(0)
                word = word_l[-1]
            
                if word==dest:
                    ans = [word_l]
                    while queue and len(queue[0])==len(word_l):
                        ne = queue.pop(0)
                        if ne[-1]==dest:
                            ans.append(ne)
                    return ans

                
                for i in range(len(word)):
                    for j in "abcdefghijklmnopqrstuvwxyz":
                        new_ = word[:i] + j + word[i+1:]
                        if new_ in wordList:
                           
                            removed.add(new_)
                            nd = word_l + [new_]
                            queue.append(nd)
            
            for ele in removed:
                wordList.remove(ele)
        return []



