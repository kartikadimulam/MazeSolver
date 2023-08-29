'''
maze = [
['+','+','+','+','G','+'],
['+',' ','+',' ',' ','+'],
['+',' ',' ',' ','+','+'],
['+',' ','+','+',' ','+'],
['+',' ',' ',' ',' ','+'],
['+','+','+','+','+','+'] ]

'''

from Stack import Stack


def solveMaze(maze, xposition, yposition):

    s = Stack()
    s.push([xposition, yposition])
    goal = False
    stepcount = 1
    maze[xposition][yposition]= stepcount
    
    while goal == False:

        xposition = s.peek()[0]
        yposition = s.peek()[1]
        
        #check north
        if maze[xposition-1][yposition] == ' ':
            stepcount += 1
            maze[xposition-1][yposition] = stepcount
            s.push([xposition-1, yposition])
            
        #check west
        elif maze[xposition][yposition-1]==' ':
            stepcount += 1
            maze[xposition][yposition-1] = stepcount
            s.push([xposition, yposition-1])

        #check south
        elif maze[xposition+1][yposition] == ' ':
            stepcount += 1
            maze[xposition+1][yposition] = stepcount
            s.push([xposition+1, yposition])
            
        #check east
        elif maze[xposition][yposition+1] == ' ':
            stepcount += 1
            maze[xposition][yposition+1] = stepcount
            s.push([xposition, yposition+1])

            
        #possibly near the goal
        elif maze[xposition-1][yposition]=='G':
            goal = True
        elif maze[xposition+1][yposition]=='G':
            goal = True
        elif maze[xposition][yposition-1]=='G':
            goal = True
        elif maze[xposition][yposition+1]=='G':
            goal=True

        else:
            s.pop()

        if s.isEmpty():
            return False
                      

    return goal


         
