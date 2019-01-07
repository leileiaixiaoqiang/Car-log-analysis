import  xml.etree.ElementTree as ET
class Field():
    def __init__(self):
        #字段的默认单位
        pass
class xmlParse():
    def __init__(self,filepath,Frame_Name):
        self.file=filepath
        self.Frame_Name=Frame_Name

        self._root_()
        self._frame_()

    #取出根节点
    def _root_(self):
        et=ET.parse(self.file)
        self.root=et.getroot()

    #取出frame
    def _frame_(self):
        Frames=self.root.findall("./Body/Frame")
        #寻找指定的Frame
        for Frame in Frames:
            Frame_Name=Frame.findall('Label')[0].text
            if Frame_Name==self.Frame_Name:
                self.Frame=Frame
        if not self.Frame:
            print('您所查找的Frame不存在')

    #取出当前所有Field对象，并给对象挂载相应的属性
    def getTmplate(self):
        #xml中的fields
        xml_fields=self.Frame.findall('Field')
        #解析出来的所有fields其实就二进制字符串的翻译模板
        tmplate=[]
        #f为xml中的field对象
        for f in xml_fields:
            #为每个有用的field加属性
            field=Field()

            #field的name
            field.Name=f.find('Label').text
            #直接挂载Computation的所有属性
            field.Type=f.find('Computation/Type').text
            field.First_bit_position=f.find('Computation/First_bit_position').text
            field.Bit_count=f.find('Computation/Bit_count').text
            '''
            这里注意并不是所有的语句都支持 用if直接判断存在与否,有的时候就要用not None来实现
            '''
            if f.find('Computation/Quantum') is not None:
                field.Quantum=eval(f.find('Computation/Quantum').text)
            #由于display的儿子不一样,所以暂时不提取text
            field.Display=f.find('Display')
            tmplate.append(field)
        return tmplate

    #获取所有的enumerated标签
    def getEnumerates(self):
        enumerates = self.root.findall('Body/Enumerated')
        res = {}
        for i in enumerates:
            #这个是为了忽略大小写
            key = i.find('Label').text.lower()
            values = i.findall('Value')
            temp = {}
            for value in values:
                code = eval(value.find('Code').text)
                label = value.find('Label').text
                temp[code] = label
            res[key] = temp
        return res