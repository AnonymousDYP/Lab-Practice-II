import java.util.*;

// GameNode class representing a node in the game search problem
class GameNode implements Comparable<GameNode> {
    private int[][] state; // Current state of the game
    private int cost; // Cost to reach this node
    private int heuristic; // Heuristic value (estimated cost to reach the goal)
    private GameNode parent; // Parent node

    // Constructor
    public GameNode(int[][] state, int cost, int heuristic, GameNode parent) {
        this.state = state;
        this.cost = cost;
        this.heuristic = heuristic;
        this.parent = parent;
    }

    // Getters
    public int[][] getState() {
        return state;
    }

    public int getCost() {
        return cost;
    }

    public int getHeuristic() {
        return heuristic;
    }

    public GameNode getParent() {
        return parent;
    }

    // Calculate the total estimated cost (f = g + h)
    public int getTotalCost() {
        return cost + heuristic;
    }

    // Compare nodes based on their total cost
    @Override
    public int compareTo(GameNode other) {
        return Integer.compare(this.getTotalCost(), other.getTotalCost());
    }
}

// Game class representing the game and its rules
class Game {
    private int[][] startState; // Initial state of the game
    private int[][] goalState; // Goal state of the game

    // Constructor
    public Game(int[][] startState, int[][] goalState) {
        this.startState = startState;
        this.goalState = goalState;
    }

    // Heuristic function (Manhattan distance)
    private int calculateHeuristic(int[][] state) {
        int heuristic = 0;
        for (int i = 0; i < state.length; i++) {
            for (int j = 0; j < state[0].length; j++) {
                int value = state[i][j];
                if (value != 0) {
                    int goalRow = (value - 1) / state[0].length;
                    int goalCol = (value - 1) % state[0].length;
                    heuristic += Math.abs(i - goalRow) + Math.abs(j - goalCol);
                }
            }
        }
        return heuristic;
    }

    // Generate possible moves from a given state
    private List<int[][]> generateMoves(int[][] state) {
        List<int[][]> moves = new ArrayList<>();
        int emptyRow = -1;
        int emptyCol = -1;

        // Find the position of the empty tile (0)
        for (int i = 0; i < state.length; i++) {
            for (int j = 0; j < state[0].length; j++) {
                if (state[i][j] == 0) {
                    emptyRow = i;
                    emptyCol = j;
                    break;
                }
            }
        }

        // Generate possible moves by swapping the empty tile with its neighbors
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}}; // Up, Down, Left, Right
        for (int[] dir : directions) {
            int newRow = emptyRow + dir[0];
            int newCol = emptyCol + dir[1];

            if (newRow >= 0 && newRow < state.length && newCol >= 0 && newCol < state[0].length) {
                int[][] newState = new int[state.length][state[0].length];
                for (int i = 0; i < state.length; i++) {
                    System.arraycopy(state[i], 0, newState[i], 0, state[0].length);
                }
                newState[emptyRow][emptyCol] = newState[newRow][newCol];
                newState[newRow][newCol] = 0;
                moves.add(newState);
            }
        }

        return moves;
    }

    // A* algorithm
    public List<int[][]> solve() {
        List<int[][]> solution = new ArrayList<>();
        PriorityQueue<GameNode> openList = new PriorityQueue<>();
        Set<int[][]> closedSet = new HashSet<>();

        // Create the start node
        GameNode startNode = new GameNode(startState, 0, calculateHeuristic(startState), null);
        openList.add(startNode);

        while (!openList.isEmpty()) {
            // Get the node with the lowest total cost from the open list
            GameNode currentNode = openList.poll();
            int[][] currentState = currentNode.getState();

            // Check if the goal state is reached
            if (Arrays.deepEquals(currentState, goalState)) {
                // Build the solution path by traversing the parent nodes
                GameNode node = currentNode;
                while (node != null) {
                    solution.add(0, node.getState());
                    node = node.getParent();
                }
                break;
            }

            // Generate possible moves from the current state
            List<int[][]> moves = generateMoves(currentState);
            for (int[][] move : moves) {
                int moveCost = currentNode.getCost() + 1;
                int moveHeuristic = calculateHeuristic(move);
                GameNode newNode = new GameNode(move, moveCost, moveHeuristic, currentNode);

                // Check if the new state has not been visited or is not in the closed set
                if (!closedSet.contains(move)) {
                    openList.add(newNode);
                    closedSet.add(move);
                }
            }
        }

        return solution;
    }
}

// Main class
public class AStarAlgorithm {
    public static void main(String[] args) {
        int[][] startState = {
                {2, 8, 3},
                {1, 6, 4},
                {7, 0, 5}
        };

        int[][] goalState = {
                {1, 2, 3},
                {8, 0, 4},
                {7, 6, 5}
        };

        Game game = new Game(startState, goalState);
        List<int[][]> solution = game.solve();

        if (solution.isEmpty()) {
            System.out.println("No solution found.");
        } else {
            System.out.println("Solution:");
            for (int[][] state : solution) {
                for (int[] row : state) {
                    System.out.println(Arrays.toString(row));
                }
                System.out.println();
            }
        }
    }
}
