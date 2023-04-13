from xml.dom.minidom import Document
import os
import cv2


def makexml(picPath, txtPath, xmlPath):  # txt file path，xml file path，image path
    """This function is used to convert the txt annotation file in yolo format to the xml annotation file in voc format.
    """
    dic = {'0': "mango"} #class
    files = os.listdir(txtPath)
    for i, name in enumerate(files):
        xmlBuilder = Document()
        annotation = xmlBuilder.createElement("annotation")  #annotation tag
        xmlBuilder.appendChild(annotation)
        txtFile = open(txtPath + name)
        txtList = txtFile.readlines()
        img = cv2.imread(picPath + name[0:-4] + ".jpg") #image filename extension
        Pheight, Pwidth, Pdepth = img.shape

        folder = xmlBuilder.createElement("folder")  # folder tag
        foldercontent = xmlBuilder.createTextNode("mango_pic")
        folder.appendChild(foldercontent)
        annotation.appendChild(folder)  

        filename = xmlBuilder.createElement("filename")  # filename tag
        filenamecontent = xmlBuilder.createTextNode(name[0:-4] + ".jpg")
        filename.appendChild(filenamecontent)
        annotation.appendChild(filename)  

        path = xmlBuilder.createElement("path") #path tag
        pathcontent = xmlBuilder.createTextNode(picPath + name[0:-4] + ".jpg") 
        path.appendChild(pathcontent)
        
        annotation.appendChild(path)
        
        size = xmlBuilder.createElement("size")  # size tag
        width = xmlBuilder.createElement("width")  # size subtag width
        widthcontent = xmlBuilder.createTextNode(str(Pwidth))
        width.appendChild(widthcontent)
        size.appendChild(width)  

        height = xmlBuilder.createElement("height")  # size subtag height
        heightcontent = xmlBuilder.createTextNode(str(Pheight))
        height.appendChild(heightcontent)
        size.appendChild(height)  

        depth = xmlBuilder.createElement("depth")  # size subtag depth
        depthcontent = xmlBuilder.createTextNode(str(Pdepth))
        depth.appendChild(depthcontent)
        size.appendChild(depth)  

        annotation.appendChild(size) 

        for j in txtList:
            oneline = j.strip().split(" ")
            object = xmlBuilder.createElement("object")  # object tag
            picname = xmlBuilder.createElement("name")  # name tag
            namecontent = xmlBuilder.createTextNode(dic[oneline[0]])
            picname.appendChild(namecontent)
            object.appendChild(picname)  

            pose = xmlBuilder.createElement("pose")  # pose tag
            posecontent = xmlBuilder.createTextNode("Unspecified")
            pose.appendChild(posecontent)
            object.appendChild(pose)  

            truncated = xmlBuilder.createElement("truncated")  # truncated tag
            truncatedContent = xmlBuilder.createTextNode("0")
            truncated.appendChild(truncatedContent)
            object.appendChild(truncated)  

            difficult = xmlBuilder.createElement("difficult")  # difficult tag
            difficultcontent = xmlBuilder.createTextNode("0")
            difficult.appendChild(difficultcontent)
            object.appendChild(difficult)  

            bndbox = xmlBuilder.createElement("bndbox")  # bndbox tag
            xmin = xmlBuilder.createElement("xmin")  # xmin tag
            mathData = int(((float(oneline[1])) * Pwidth + 1) - (float(oneline[3])) * 0.5 * Pwidth)
            xminContent = xmlBuilder.createTextNode(str(mathData))
            xmin.appendChild(xminContent)
            bndbox.appendChild(xmin)  

            ymin = xmlBuilder.createElement("ymin")  # ymin tag
            mathData = int(((float(oneline[2])) * Pheight + 1) - (float(oneline[4])) * 0.5 * Pheight)
            yminContent = xmlBuilder.createTextNode(str(mathData))
            ymin.appendChild(yminContent)
            bndbox.appendChild(ymin)  

            xmax = xmlBuilder.createElement("xmax")  # xmax tag
            mathData = int(((float(oneline[1])) * Pwidth + 1) + (float(oneline[3])) * 0.5 * Pwidth)
            xmaxContent = xmlBuilder.createTextNode(str(mathData))
            xmax.appendChild(xmaxContent)
            bndbox.appendChild(xmax)  

            ymax = xmlBuilder.createElement("ymax")  # ymax tag
            mathData = int(((float(oneline[2])) * Pheight + 1) + (float(oneline[4])) * 0.5 * Pheight)
            ymaxContent = xmlBuilder.createTextNode(str(mathData))
            ymax.appendChild(ymaxContent)
            bndbox.appendChild(ymax)  

            object.appendChild(bndbox)  # bndbox tag end

            annotation.appendChild(object)  # object tag end

        f = open(xmlPath + name[0:-4] + ".xml", 'w')
        xmlBuilder.writexml(f, indent='\t', newl='\n', addindent='\t', encoding='utf-8')
        f.close()


if __name__ == "__main__":
    picPath = "/home/usrname/Desktop/mango_pic/"  # images file path,msut add"/" in the end
    txtPath = "/home/uarname/Desktop/mango_txt/"  # txt file path ，msut add"/" in the end
    xmlPath = "/home/usrname/Desktop/voc/"  # xml file path，msut add"/" in the end
    makexml(picPath, txtPath, xmlPath)

 
