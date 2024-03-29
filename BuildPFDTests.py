from random import randint

# WAY 1:
#num_tasks = randint(1, 10)
#num_lines = randint(1, num_tasks)
#
#print str(num_tasks) + " " + str(num_lines)
#
## Generates num_lines of input
#test_task_list = [[]]*num_tasks
#for iterator in range(0,num_lines):
#
#    # Make sure we generate a random task and that we don't overwrite an already instantiated task
#    random_task = -1
#    while random_task == -1 or test_task_list[random_task] != []:
#        random_task = randint(1, num_tasks)
#
#    # Generate a random predecessor list of length=random_predecessor_number
#    random_predecessor_count = randint(1, num_tasks)
#    rand_pred_list = []
#    rand_pred_list.append(random_task)
#    rand_pred_list.append(random_predecessor_count)
#    # Generate random_predecessor_count number of random predecessors
#    for i in range (1, random_predecessor_count+1):
#        random_predecessor = -1
#        # Make sure we generate a random task, we don't have duplicates, and that we don't use the task we're assigning to (this increases our chances of a DAG)
#        while random_predecessor == -1 or random_predecessor in rand_pred_list or random_predecessor == random_task:
#            random_predecessor = randint(1, num_tasks)
#        rand_pred_list.append(random_predecessor)
#
#for line in test_task_list:
#    if line != []:
#        print ' '.join(map(str, line[1:]))


#WAY 2:
#http://ipython.org/ipython-doc/dev/parallel/dag_dependencies.html
#def find_satisfied(dag):
#    satisfied = []
#    for index, n in enumerate(dag):
#        if n == []:
#            satisfied.append(index)
#    return satisfied
#
#def find_connected(n, dag):
#    connected = []
#    for list in dag:
#        if n in list[2:]:
#            connected.append(list[0])
#    return connected
#
#
#def is_dag(dag):
#    # L: Empty list where we put the sorted elements
#    sorted = []
#    # Q: Set of all nodes with no incoming edges
#    satisfied = find_satisfied(dag)
#    while satisfied != []:
#        n = satisfied[0]
#        # insert n into L
#        sorted.append(n)
#        sorted.sort()
#        # remove a node n from Q
#        satisfied = satisfied[1:]
#
#        connected = find_connected(n, dag)
#        # for each node m with an edge e from n to m
#        for node in connected:
#            # remove edge e from the graph
#            dag[node].remove(n)
#            # if m has no other incoming edges then
#            if dag[node] == []:
#                # insert m into Q
#                satisfied.append(node)
#    # if graph has edges then
#        return False
#    else:
#        return True
#
#def random_dag(nodes, edges):
#    """Generate a random Directed Acyclic Graph (DAG) with a given number of nodes and edges."""
#    dag = [[]] * nodes
#    while edges > 0:
#        a = randint(0,nodes-1)
#        b=a
#        while b==a:
#            b = randint(0,nodes-1)
#        dag[a].append(b)
#        if is_dag(dag):
#            edges -= 1
#        else:
#            # we closed a loop!
#            dag[a].remove(b)
#    return dag
#
#verticies = randint(0, 10)
#total_dependencies = randint(0,10)
#dag = random_dag(verticies, total_dependencies)
#print dag


# WAY 3:
for num in range(0, 1000):
    tasks   = randint(0, 100)
    matrix  = []
    for n in range(0, tasks):
        matrix.append([0]*tasks)

    for c in range(1, tasks):
        for r in range(1, tasks):
            if r > c:
                edge = randint(0,1)
                matrix[r][c] = edge

    #for row in matrix:
    #    print row
    #print

    task_list = []
    for task, row in enumerate(matrix):
        task_row = []
        for index, value in enumerate(row):
            if value:
                task_row.append(index)
        if task_row:
            task_row.insert(0, len(task_row))
            task_row.insert(0, task)
            task_list.append(task_row)

    print str(tasks) + " " + str(len(task_list))
    for line in task_list:
        print ' '.join(map(str, line[0:]))
    print



