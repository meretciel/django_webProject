
def convert_row_to_dict(df, idx):
    my_dict = dict()

    for col in df.columns:
        my_dict[col] = df.ix[idx,col]

    return my_dict



def convert_dict_to_JSON(model, pk, fields):
    # open the object
    lines = ['{']

    # make record of the model and the pk
    lines.append('  "model": "{}",'.format(model))
    lines.append('  "pk": "{}",'.format(pk))

    # record of the fields
    lines.append('  "fields": {')

    # iterate the fields
    num_of_fields = len(fields)
    count = 0
    for field, value in fields.items():
        count += 1
        if count < num_of_fields:
            lines.append('      "{_field}": "{_value}",'.format(_field=field, _value=value))
        else:
            lines.append('      "{_field}": "{_value}"'.format(_field=field, _value=value))

    lines.append('  }')

    # close the object
    lines.append('}')

    return '\n'.join(lines)


def convert_DataFrame_to_JSON(df, model, filename=None):
    # open the list
    objects = []
    pk = 0
    for idx in df.index:
        pk += 1
        objects.append(convert_dict_to_JSON(model,str(pk), convert_row_to_dict(df,idx)))


    # write to the disk
    if not filename is None:
        _file = open(filename,'w')
        _file.writelines('[')
        for obj in objects[:-1]:
            _file.write(obj)
            _file.write(',\n')

        _file.writelines(objects[-1] + '\n]')
        _file.close()
    else:
        raise IOError('Please specify the filename to write!')

