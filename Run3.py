import io
import ijson

with open('Data2.json', 'r') as json_file:
    cursor = 0
    for line_number, line in enumerate(json_file):
        print ("Processing line", line_number + 1,"at cursor index:", cursor)
        line_as_file = io.StringIO(line)
        # Use a new parser for each line
        json_parser = ijson.parse(line_as_file)
        # for result in json_parser:
        #     print ("prefix=",result['prefix'], "type=",result['type'], "value=",result['value'])
        cursor += len(line)