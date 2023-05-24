from queue import PriorityQueue
class Puzzle:
    # Constructor.
    def __init__(self, board):
        self.board = board
        self.goal = [[1,2,3],[4,5,6],[7,8,0]]

    # Function to find the row and column of the title x.
    def find(self, x):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == x:
                    return i, j
                
    # Function to calculate manhattan distance.
    def manhattan(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 0:
                    x, y = self.find(self.board[i][j])
                    distance += abs(x-i) + abs(y-j)
        return distance
    
    # Function to compare manhattan distance
    def __lt__(self, other):
        return self.manhattan() < other.manhattan()
    
    # Function to move the title
    def move(self, x1, y1, x2, y2):
        p = Puzzle([row[:] for row in self.board])
        p.board[x1][y1], p.board[x2][y2] = p.board[x2][y2], p.board[x1][y1] 
        return p
    
    # Function to find possible moves
    def children(self):
        i, j = self.find(0)
        moves = []
        if i > 0:
            moves.append(self.move(i, j, i-1, j))
        if i < 2:
            moves.append(self.move(i, j, i+1, j))
        if j > 0:
            moves.append(self.move(i, j, i, j-1))
        if j < 2:
            moves.append(self.move(i, j, i, j+1))
        return moves
    
    # Function to check if the current state is a goal state 
    def is_goal(self):
        return self.board == self.goal
    
    # Overridden str function
    def __str__(self):
        return "\n".join([" ".join([str(x) for x in row]) for row in self.board])
        
# Function to implement A* algorithm
def a_star(start):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start))
    while not queue.empty():
        (cost, node) = queue.get()
        if node.is_goal():
            return node
        visited.add(str(node))
        for child in node.children():
            if str(child) not in visited:
                queue.put((child.manhattan()+cost, child))
    return None

# Get input from user 
board = []
for i in range(3):
    row = input(f"Enter row {i+1} of the puzzle (use space as delimiter): ").split()
    board.append([int(x) for x in row])
start = Puzzle(board)

# Solve puzzle using A* algorithm
solution = a_star(start)
if solution:
    print("Solution for the 8-Puzzle Problem is : ")
    print(solution)
else:
    print("No solution found")