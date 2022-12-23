from typing import List
import time

class Tree:
    def __init__(self, height: int, position: (int, int)):
        self._height: int = height
        self._position: (int, int) = position

    def setHeight(self, height: int):
        self._height = height

    def getHeight(self) -> int:
        return self._height

    def getPosition(self) -> (int, int):
        return self._position

    def setPosition(self, new_position):
        self._position = new_position

class Forest:
    def __init__(self):
        self._trees = []
        self._width = 0
        self._height = 0

    def addTree(self, tree: Tree):
        self._trees.append(tree)

    def getTrees(self) -> List[Tree]:
        return self._trees

    def getInsideTrees(self) -> List[Tree]:
        return [x for x in self.getTrees() if 0 < x.getPosition()[0] < self.getHeight() and 0 < x.getPosition()[1] < self.getWidth()]

    def getWidth(self) -> int:
        return self._width

    def getHeight(self) -> int:
        return self._height

    def calculateForestDimensions(self):
        self._width = max([tree.getPosition()[1] for tree in self.getTrees()])
        self._height = max([tree.getPosition()[0] for tree in self.getTrees()])

    def checkVisibility(self, tree: Tree) -> bool:
        def loop(array: List[Tree]) -> bool:
            visibility = False

            for i in array:
                if tree.getHeight() > i.getHeight():
                    visibility = True
                else:
                    visibility = False
                    break

            return visibility

        tree_pos = tree.getPosition()
        horizontal_list = []
        vertical_list = []

        for x in self.getTrees():
            if x.getPosition()[0] == tree_pos[0]:
                horizontal_list.append(x)
            if x.getPosition()[1] == tree_pos[1]:
                vertical_list.append(x)

        horizontal_left = horizontal_list[:tree.getPosition()[1]]
        horizontal_right = horizontal_list[tree.getPosition()[1] + 1:]
        vertical_left = vertical_list[:tree.getPosition()[0]]
        vertical_right = vertical_list[tree.getPosition()[0] + 1:]

        if loop(horizontal_left) or loop(horizontal_right) or loop(vertical_left) or loop(vertical_right):
            return True
        else:
            return False


if __name__ == '__main__':
    start_time = time.time()

    # create new forest
    forest = Forest()

    # add trees to forest
    input = open("input.txt").read()
    for line_idx, line in enumerate(input.split("\n")):
        for char_idx, char in enumerate(line):
            forest.addTree(Tree(char, (line_idx, char_idx)))

    # calculate forest dimensions
    forest.calculateForestDimensions()

    # check visibility for all inside Trees
    count = 0
    for i in forest.getInsideTrees():
        if forest.checkVisibility(i):
            count += 1

    print(f"Number of visible Trees: {count + (2 * forest.getWidth()) + (2 * forest.getHeight())} found in {time.time()-start_time}s")
