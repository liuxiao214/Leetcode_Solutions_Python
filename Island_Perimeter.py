def isLandPerimeter(grid):
	sum=0
	lenl=len(grid)
	for i in range(0,lenl):
		lens=len(grid[i])
		if lenl==1 and lens==1:
			if grid[0][0]==1:
				sum=4
				break
		elif lenl==1 and lens>1:
			for j in range(0,lens):
				if grid[i][j]==1 and i==0 and j==0:
					sum=sum+3
					if grid[i][j+1]==0:
						sum=sum+1
				elif grid[i][j]==1 and i==lenl-1 and j==lens-1:
					sum=sum+3
					if grid[i][j-1]==0:
						sum=sum+1
				else:
					if grid[i][j]==1:
						sum=sum+2
						if grid[i][j-1]==0:
							sum=sum+1
						if grid[i][j+1]==0:
							sum=sum+1
		elif lenl>1 and lens==1:
			for j in range(0,lens):
				if grid[i][j]==1 and i==0 and j==0:
					sum=sum+3
					if grid[i+1][j]==0:
						sum=sum+1
				elif grid[i][j]==1 and i==lenl-1 and j==lens-1:
					sum=sum+3
					if grid[i-1][j]==0:
						sum=sum+1
				else:
					if grid[i][j]==1:
						sum=sum+2
						if grid[i-1][j]==0:
							sum=sum+1
						if grid[i+1][j]==0:
							sum=sum+1
		else:
			for j in range(0,lens):
				if grid[i][j]==1 and i==0 and 0<j and j<lens-1:
					sum=sum+1
					if grid[i][j-1]==0:
						sum=sum+1
					if grid[i][j+1]==0:
						sum=sum+1
					if grid[i+1][j]==0:
						sum=sum+1
				elif grid[i][j]==1 and 0<i and i<lenl-1 and j==0:
					sum=sum+1
					if grid[i-1][j]==0:
						sum=sum+1
					if grid[i+1][j]==0:
						sum=sum+1
					if grid[i][j+1]==0:
						sum=sum+1
				elif grid[i][j]==1 and i==lenl-1 and 0<j and j<lens-1:
					sum=sum+1
					if grid[i][j-1]==0:
						sum=sum+1
					if grid[i][j+1]==0:
						sum=sum+1
					if grid[i-1][j]==0:
						sum=sum+1
				elif grid[i][j]==1 and 0<i and i<lenl-1 and j==lens-1:
					sum=sum+1
					if grid[i-1][j]==0:
						sum=sum+1
					if grid[i+1][j]==0:
						sum=sum+1
					if grid[i][j-1]==0:
						sum=sum+1
				elif grid[i][j]==1 and i==0 and j==0:
					sum=sum+2
					if grid[i+1][j]==0:
						sum=sum+1
					if grid[i][j+1]==0:
						sum=sum+1
				elif grid[i][j]==1 and i==lenl-1 and j==lens-1:
					sum=sum+2
					if grid[i-1][j]==0:
						sum=sum+1
					if grid[i][j-1]==0:
						sum=sum+1
				elif grid[i][j]==1 and i==0 and j==lens-1:
					sum=sum+2
					if grid[i+1][j]==0:
						sum=sum+1
					if grid[i][j-1]==0:
						sum=sum+1
				elif grid[i][j]==1 and i==lenl-1 and j==0:
					sum=sum+2
					if grid[i-1][j]==0:
						sum=sum+1
					if grid[i][j+1]==0:
						sum=sum+1
				else:
					if grid[i][j]==1:
						if grid[i][j-1]==0:
							sum=sum+1
						if grid[i][j+1]==0:
							sum=sum+1
						if grid[i-1][j]==0:
							sum=sum+1
						if grid[i+1][j]==0:
							sum=sum+1
	return sum
a=[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
b=[[1]]
c=[[1],[0],[0],[0]]
d=[[1,1,1,1]]
print isLandPerimeter(a)
print isLandPerimeter(b)
print isLandPerimeter(c)
print isLandPerimeter(d)
