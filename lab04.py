
maze = [
['+','+','+','+','G','+'],
['+',' ','+',' ',' ','+'],
['+',' ',' ',' ','+','+'],
['+',' ','+','+',' ','+'],
['+',' ',' ',' ',' ','+'],
['+','+','+','+','+','+'] ]

from Stack import Stack
s = Stack()
def solveMaze(maze, xposition, yposition):

    goal = False
    stepcount = 1
    maze[xposition][yposition]= stepcount
    
    while goal == False:
        position = maze[xposition][yposition]
        s.push(xposition)
        s.push(yposition)
        
        #check north
        if maze[xposition-1][yposition] == ' ':
            stepcount += 1
            s.push(stepcount)
            maze[xposition-1][yposition] = stepcount
            xposition -= 1
            
        #check west
        elif maze[xposition][yposition-1]==' ':
            stepcount += 1
            s.push(stepcount)
            maze[xposition][yposition-1] = stepcount
            yposition -= 1

        #check south
        elif maze[xposition+1][yposition] == ' ':
            stepcount += 1
            s.push(stepcount)
            maze[xposition+1][yposition] = stepcount
            xposition += 1
            
        #check east
        elif maze[xposition][yposition+1] == ' ':
            stepcount += 1
            s.push(stepcount)
            maze[xposition][yposition+1] = stepcount
            yposition += 1

            
        #maybe ur near the goal
        elif maze[xposition-1][yposition]=='G':
            goal = True
            s.pop()
        elif maze[xposition+1][yposition]=='G':
            goal = True
            s.pop()
        elif maze[xposition][yposition-1]=='G':
            goal = True
            s.pop()
        elif maze[xposition][yposition+1]=='G':
            goal=True
            s.pop()

            
        #lets go back
        else:

            if maze[xposition-1][yposition] == stepcount-1:
                xposition -= 1
                s.push(xposition)
            elif maze[xposition+1][yposition] == stepcount-1:
                xposition += 1
                s.push(xposition)
            elif maze[xposition][yposition-1]==stepcount-1:
                yposition -= 1
                s.push(yposition)
            elif maze[xposition][yposition+1]==stepcount-1:
                yposition += 1
                s.push(yposition)
            
            
            

    return goal


         
