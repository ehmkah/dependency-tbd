# This simple script downloads all dependencies with the help of gradle.
#
#
# @author: ehmkah
#

import os
import shutil

tempDir = '/tmp/repos'
repo = {"origin": "https://github.com/ehmkah/imgdiff.git", "dir": "imgdiff"}

###
# no modification below this line
###

clone_cmd = 'git clone ' + repo["origin"]
gradle_dependencies_cmd = './gradlew dependencies >>dependencies'


def cloneRepo():
    os.system(clone_cmd)
    os.chdir(repo["dir"])
    os.system(gradle_dependencies_cmd)


def prepareWorkingDir():
    if (os.path.isdir(tempDir)):
        shutil.rmtree(tempDir)
    os.mkdir(tempDir)
    os.chdir(tempDir)


prepareWorkingDir()
cloneRepo()
