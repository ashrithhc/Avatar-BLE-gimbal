import xml.etree.ElementTree as myParser

valueSet = {}
handle_value = {}

def addThisData(proto):

    tempVal = ''
    tempHandle = ''
    for field in proto.findall('field'):
        if field.get('name') == 'btatt.handle':
            tempHandle = field.get('showname').split()[1]
            if tempHandle not in handle_value.keys():
                handle_value[tempHandle] = set()
        if field.get('name') == 'btatt.value':
            tempVal = field.get('value')
            if tempVal not in valueSet.keys():
                valueSet[tempVal] = 1
            else:
                valueSet[tempVal] += 1
            handle_value[tempHandle].add(tempVal)

def parseFile(e):
    for packet in e.findall('packet'):
        for proto in packet.findall('proto'):
            if proto.get('name') == 'btatt':
                addThisData(proto)

input_file_list = ['pdmlfile']
for input_file in input_file_list:
    e = myParser.parse(input_file).getroot()
    parseFile(e)

print (handle_value)