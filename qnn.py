import numpy as np

class qnns:
    def __init__(self, start=[[[0, 0]]], passes=[[[[]]]], debug=False):
        self.prev_layer = start; self.passed_layer = passes; self.debug = debug
    def next_branch(self, map):
        branches = self.prev_layer
        passes = self.passed_layer
        current_passed = []
        current_branches = []
        for i in branches:
            current_branches.extend(i)
        for i in passes:
            current_passed.extend(i)
        if self.debug and len(current_passed) != len(current_branches):
            print('branches and passes are not equal')
        new_layer = []
        new_passed = []
        returns = []
        #branches organized in lists for vector
        for i in range(0, len(current_branches)): #goes through each branch [branch, branch, branch]
            new_layer.append([]); new_passed.append([]) #sets up the new list for layer and other stuff
            returns.append([])
            if self.debug:
                print(current_passed[i])
            map.extend(current_passed[i]) #includes the passed layers
            new_map = map
            for i2 in range(0, len(new_map)): #goes through each complex number
                if isinstance(new_map[i2], list): #handles if it is a entangled list
                    pass_type = None
                    complexity = None
                    for i3 in new_map[i2]:
                        if isinstance(i3, str):
                            (i3.lower().startswith('pass type:') and (pass_type := i3[i3.lower().index(':'):].lower())) or ((complexity := i3.lower()))
                        elif isinstance(i3, list):
                            vectoring = True
                    for i3 in new_map[i2]:
                        if isinstance(i3, str):
                            continue
                        elif isinstance(i3, list):
                            if isinstance(i3[0], list) or isinstance(i3[1], list) or  'vector entanglement' in i3:
                                pass_type_vector = None
                                complexity_vector = None
                                for check in i3:
                                    if isinstance(check, str):
                                        i3.pop(i3.index(check))(check.lower().startswith('pass type:') and (pass_type_vector := check[check.index(':'):]) or (complexity_vector := check.lower)) 
                                if len(i3) != 2:
                                    if self.debug:
                                        print('more then 2 values where passed through a list in vector entanglement')
                                for vector_1 in range(0, i3[0]):
                                    if complexity_vector is None or complexity_vector == 'normal' or complexity_vector == 'basic':
                                        new_value = [current_branches[i][0] + i3[0][vector_1],current_branches[i][1] + i3[1][vector_1]]
                                        index_of = None
                                        [(new_value in i4) and (index_of := [i4.index(new_value), new_layer.index(i4)]) for i4 in new_layer] 
                                        if index_of is not None:
                                            new_passed[index_of[1]][index_of[0]].append([i3[0][vector_1], i3[0][vector_1]]) # add pass types here later
                                            if self.debug:
                                                print('advanced entanglement')
                                        else:
                                            new_layer[i].append(new_value)
                                            new_passed[i].append([])
                                            returns[i].append([new_value, [new_value[0] - (2 * i3[0][vector_1]), new_value[1]], [new_value[0], new_value[1] - (2 * i3[1][vector_1])], [new_value[0] - (2 * i3[0][vector_1]), new_value[1] - (2 * i3[1][vector_1])]])
                            else:
                                pass_type = None
                                complexity = None
                                for check in i3:  
                                    if isinstance(check, str):
                                        if check.lower().startswith('pass type:'):
                                            pass_type = check[check.index(':'):]
                                        else:
                                            complexity = check
                                        i3.pop(i3.index(check))
                                if complexity == None or complexity == 'basic':
                                    new_value = [current_branches[i][0] + i3[0], current_branches[i][1] + i3[1]]  if len(i3) == 2 else [current_branches[i][0], current_branches[i][1] + i3[0]]
                                    index_of = None
                                    [(new_value in i4) and (index_of := [i4.index(new_value), new_layer.index(i4)]) for i4 in new_layer] 
                                    if index_of is not None:
                                        new_passed[index_of[1]][index_of[0]].append(new_value) # add pass types here later
                                        if self.debug:
                                            print('advanced entanglement')
                                    else:
                                        new_layer[i].append(new_value)
                                        new_passed[i].append([])
                                        returns[i].append([new_value]) #finish the return here
                        else:       
                            if complexity is None or complexity == 'basic':
                                new_value = [current_branches[i][0] + i3, current_branches[i][1]]
                                new_layer[i].append(new_value)
                                if pass_type is None:
                                    new_passed[i].append([new_value])
                                elif pass_type == 'entangled pass' or pass_type == ' entangled pass':
                                    new_passed[i].append([[i4, current_branches[i][1]] if not isinstance(i4, list) else [0, 0] for i4 in new_map[i2]])
                                    if self.debug:
                                        print('beta pass type for entanglement:')
                                        print(new_passed[i])
                                else:
                                    if self.debug:
                                        print('Invalid pass type')
                                    new_passed[i].append([])
                                returns[i].append([new_value, new_value])
                            elif complexity == 'oposite':
                                new_value = [current_branches[i][0] - abs(i3), current_branches[i][1]]
                                new_layer[i].append(new_value)
                                if pass_type is None:
                                    new_passed[i].append([new_value[0] - (-2 * abs(i3)), new_value[1]])
                                elif pass_type == 'entangled pass' or pass_type == ' entangled pass':
                                    new_passed[i].append([[-1 * i4, current_branches[i][1]] if not isinstance(i4, list) else [0, 0] for i4 in new_map[i2]])
                                    if self.debug:
                                        print('beta pass type for entanglement:')
                                        print(new_passed[i])
                                else:
                                    if self.debug:
                                        print('Invalid pass type')
                                    new_passed[i].append([])
                                returns[i].append([-1 * abs(new_value), new_value])

                else:
                    new_value = [current_branches[i][0] + new_map[i2], current_branches[i][1]]
                    index_of = None
                    [(new_value in i3) and (index_of := [i3.index(new_value), new_layer.index(i3)]) for i3 in new_layer] 
                    if index_of is not None:
                        new_passed[index_of[1]][index_of[0]].append([new_map[i2], 0])
                        if self.debug:
                            print('entangled')
                        continue
                    else:
                        if self.debug:
                            print(self.prev_layer)
                        new_layer[i].append(new_value)
                        new_passed[i].append([])
                        returns[i].append([new_value, [new_value[0] - (2 * new_map[i2]), new_value[1]]])
        self.prev_layer = new_layer;self.passed_layer = new_passed
        if self.debug:
            print(self.prev_layer);print(self.passed_layer)
        return returns




