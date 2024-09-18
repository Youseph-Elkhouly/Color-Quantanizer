import numpy as np
from PIL import Image
import copy

# Inputs:
#     img: m by n by 3 array of integers representing the color values of a photo
#     rGroups: integer representing the number of groups of red color values
#     gGroups: integer representing the number of groups of green color values
#     bGroups: integer representing the number of groups of blue color values
# constraints: 
#     1 <= rGroups, gGroups, bGroups <= 256
#     0 <= all integers in img <= 255
# Output: returns an m by n by 3 (same dimensions as input img array), 
#         with its color values quantized according to the specified group parameters
def colorQuantize(img, rGroups, gGroups, bGroups):
    img_copy = copy.deepcopy(img)
    
    def quantize(value, group):
        group_size = 256 // group

        range_max = group_size * group

        adjusted_value = min(value, range_max - 1)
        value_group = adjusted_value // group_size
        quantized_value = (value_group * group_size) + group_size // 2
        return quantized_value
    
    for i in range(len(img)):
        for j in range(len(img[0])):
            img_copy[i,j,0] = quantize(img[i,j,0], rGroups) #red 
            img_copy[i,j,1] = quantize(img[i,j,1], gGroups) #green
            img_copy[i,j,2] = quantize(img[i,j,2], bGroups) #blue
    return img_copy


# Testing and starter code provided in main(): 
def main():
    testFiles = [
        "3by3.png",
        "dog.png",    
        "cat.png"
    ]
    testArgs = [
        [[1, 1, 1], [3, 4, 5], [11, 13, 15], [256, 256, 256]],    # 3by3 test args
        [[2, 2, 2], [2, 8, 8], [2, 16, 2], [4, 4, 4], [16, 16, 16],], # dog test args
        [[3, 3, 3], [7, 1, 9], [7, 11, 9], [256, 256, 256]]  # cat test args
    ]
    testDir = "C:\\Users\\clubb\\OneDrive\\Desktop\\2910\\tests\\" # update this path with the path to your tests directory!
    
    img = Image.open(testDir + 'cat.png').convert('RGB')
    arr = np.array(img) 
    outArr = colorQuantize(arr, 3,3,3)

    testing = True
    if testing:
        for idx, testFile in enumerate(testFiles):
            for testSet in testArgs[idx]:
                testImg = Image.open(testDir + testFile).convert('RGB')
                testImgArr = np.array(testImg)
                outArr = colorQuantize(copy.deepcopy(testImgArr), testSet[0], testSet[1], testSet[2])
                testImg = Image.open(f"{testDir}{testFile[:-4]}_{testSet[0]}_{testSet[1]}_{testSet[2]}.png").convert('RGB')
                print(f"Testing {testFile[:-4]}_{testSet[0]}_{testSet[1]}_{testSet[2]}.png: ", end="")
                testArr = np.array(testImg)
                for row in range(len(testArr)):
                    for col in range(len(testArr[0])):
                        if outArr[row][col][0] != testArr[row][col][0]:
                            print("red color mismatch at row: " + str(row) + " col: " + str(col))
                            print(f'testImgArr: {testImgArr[row][col][0]}')
                            print(f'outArr: {outArr[row][col][0]} testArr: {testArr[row][col][0]}')
                            return
                        if outArr[row][col][1] != testArr[row][col][1]:
                            print("green color mismatch at row: " + str(row) + " col: " + str(col))
                            print(f'testImgArr: {testImgArr[row][col][1]}')
                            print(f'outArr: {outArr[row][col][1]} testArr: {testArr[row][col][1]}')
                            return
                        if outArr[row][col][2] != testArr[row][col][2]:
                            print("blue color mismatch at row: " + str(row) + " col: " + str(col))
                            print(f'testImgArr: {testImgArr[row][col][2]}')
                            print(f'outArr: {outArr[row][col][2]} testArr: {testArr[row][col][2]}')
                            return
                print("Passed")

    # Set saveFile to save your image,
    # e.g. saveFile = "myIMG.png" would save the image as the file "myIMG.png" in the directory where this code runs
    saveFile = "myIMG.png"
    if saveFile != "myIMG.png":
        outIMG = Image.fromarray(outArr)
        outIMG.save(saveFile)
    return 0

if __name__ == '__main__':
   main()

##########################################
# DO NOT LEAVE ANY CODE OUTSIDE ROUTINES #
# IT CAN CAUSE THE AUTOGRADER TO CRASH   #
##########################################
