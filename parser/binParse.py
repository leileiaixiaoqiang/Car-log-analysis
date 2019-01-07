import  time
import  re
import  os
class binParser():
    def __init__(self,file_path,tmplate,enumerates):
        self.file_path=file_path
        self.fp=open(self.file_path, 'rb')


        self.tmplate=tmplate
        self.enumerates=enumerates
        self._recordSize=self._getRecordSize()
        self.file_size=os.path.getsize(file_path)


    def _getRecordSize(self):
        temp = self.fp.read(5000)
        s1 = temp.hex()
        pattern = s1[0:8]
        res = re.finditer(pattern, s1)
        last = 0
        out = []
        for i in res:
            start = i.start() // 2
            diff = start - last
            if diff > 17:
                if diff in out:
                    self.fp.seek(0)
                    return last
                out.append(diff)
                last = start

    def _extractInt_(self,Compute_Type,Quantum,field_bin_str):
        if Compute_Type == 'Unsigned_integer':
            res = int(field_bin_str, 2) * Quantum
        elif Compute_Type == 'Signed_integer':
            if field_bin_str[0] == '0':
                res = int(field_bin_str, 2) * Quantum
            else:
                bin_length = len(field_bin_str[1:])
                if bin_length==0:
                    res=-1
                else:
                    res = -(2 ** bin_length - int(field_bin_str[1:], 2)) * Quantum
        return res

    def _extractShowData_(self,field_int,Display,bit_count,field_bin_str):
        display_type=Display.find('Type').text
        # 后面把下面这个判断做成字典来调用
        if display_type == 'Decimal':
            Decimal_count=Display.find('Decimal_count')
            if Decimal_count is not None:
                temp='{:.'+Decimal_count.text+'f}'
                show_data = temp.format(field_int)
            else:
                show_data =int(field_int)
        elif display_type == 'Hexadecimal':
            count = int(bit_count/4)
            show_data = hex(field_int).replace('0x', '').zfill(count)
        elif display_type == 'Binary':
            count = bit_count
            show_data = bin(field_int).replace('0b', '').zfill(count)
        elif display_type == 'Date':
            # 如果是时间要重新取数,只用取前面的32位
            bin_str_field = field_bin_str[0:32]
            temp = int(bin_str_field, 2)
            # 2209017560是1900/01/01 00:00:00的时间戳
            if temp >2209017600:
                timeStamp = temp - 2209017600
                localtime = time.localtime(timeStamp)
                show_data = time.strftime('%Y/%m/%d', localtime)
            else:
                show_data = '1900/01/01'
        elif display_type == 'Time':
            bin_str_field = field_bin_str[0:32]
            temp = int(bin_str_field, 2)
            # 2209017560是1900/01/01 00:00:00的时间戳
            if temp >2209017600:
                timeStamp = temp - 2209017600
                localtime = time.localtime(timeStamp)
                show_data = time.strftime('%H:%M:%S', localtime)
            else:
                show_data = '00:00:00'
        elif display_type == "Enumerated":
            Enumerated_name =Display.find('Enumerated_label').text.lower()
            value_sets = self.enumerates[Enumerated_name]
            show_data=value_sets.get(field_int,"? key : %d"%field_int)
        return show_data

    def fetchOneData(self):
        self.fp.read(31)
        # # 一条记录1848字节,转换成二进制的字符串
        Syn_MulPages = self.fp.read(self._recordSize-31).hex()
        bin_str = bin(eval('0x'+Syn_MulPages)).replace('0b', '').zfill( (self._recordSize-31)* 8)
        bin_str = bin(eval('0x'+Syn_MulPages)).replace('0b', '')
        res = []
        for i in self.tmplate:
            start = eval(i.First_bit_position)
            if start>=11168:
                start+=248
            end = eval(i.Bit_count) + start
            field_name = i.Name
            # if field_name=="DisableLatency         " or field_name=='Available              ':
            #     print(bin_str[start:end],' ->',start)
            field_bin_str = bin_str[start:end]
            if not hasattr(i,"Quantum"):
                quantum=1
            else:
                quantum=i.Quantum

            field_int = self._extractInt_(i.Type,quantum, field_bin_str)
            show_data = self._extractShowData_(field_int, i.Display, eval(i.Bit_count), field_bin_str)
            # print(field_name+'  '+field_bin_str+" "+str(show_data)+" "+str(quantum))
            # res.append((field_name,i.Display.find('Type').text,show_data))
            if i.Display.find("Type").text=="Enumerated":
                kind=i.Display.find('Enumerated_label').text
            else:
                kind=i.Display.find("Type").text

            res.append((field_name,(kind,show_data)))
        return res

    '''
    fetchOneData返回的是一个字典,键对应栏位名称,值对应栏位值
    fetchAllData调用fetchOneData
    '''
    def fetchAllData(self):
        res=[]
        count=0
        while self.fp.tell()<self.file_size:
            data=self.fetchOneData()
            count+=1
            print("第%d条"%count)
            res.append(data)
        self.close()
        return res
    def close(self):
        self.fp.close()

