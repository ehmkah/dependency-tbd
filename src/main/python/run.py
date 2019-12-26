# This simple script downloads all dependencies with the help of gradle.
#
#
# @author: ehmkah
#

import datetime
import os
import shutil

tempDir = '/tmp/repos'
repo = {"origin": "https://github.com/ehmkah/imgdiff.git", "dir": "imgdiff"}

###
# no modification below this line
###

clone_cmd = 'git clone ' + repo["origin"]
gradle_dependencies_cmd = './gradlew dependencies'
interested_dependencies = 'junit'


def parseDependencies():
    os.chdir(repo["dir"])
    stream = os.popen(gradle_dependencies_cmd)
    found=False;
    for line in stream.readlines():
        first_postion = line.find(interested_dependencies)
        if first_postion > -1 and found==False:
            cleanedLine = line.replace("+", "").replace("-", "").replace(" ", "").replace("\n", "")
            split = cleanedLine.split(":")
            printDepencies('imgdiff', split[2])
            found=True

def cloneRepo():
    os.system(clone_cmd)


def prepareWorkingDir():
    if (os.path.isdir(tempDir)):
        shutil.rmtree(tempDir)
    os.mkdir(tempDir)
    os.chdir(tempDir)


def printDepencies(usingLib, version):
    print("""
<tr><td>{usingLib}</td><td>{usedVersion}</td>
""".format(usingLib=usingLib, usedVersion=version)
          )


def printHeader():
    print("""
    <html><head><title>Papa - dependency</title></head>
    <body>
    <table>
    <tr><td>User</td><td>{interestedLib}</td></tr>
""".format(interestedLib=interested_dependencies))


def printFooter():
    print("""
    </table>
    <p>Generated at {generatedTime}</p>
    </body>
""".format(generatedTime=datetime.datetime.now()))


def main():
    prepareWorkingDir()
    cloneRepo()
    printHeader()
    parseDependencies()
    printFooter()


main()
