with open('addtask3.txt', 'r') as file_in:
    with open('3_new.txt', 'w') as file_out:

        for line in file_in:
            if '\tDB' in line or '\tDW' in line or '\tDD' in line or ' in  Word ' in line:
                data = line.split('\t')
                new_data = []

                for d in data:
                    #с чего начинается
                    if ' in  Word ' in d or d.startswith('DB') or d.startswith('DW') or d.startswith('DD'):
                        if ' in  Word ' in d:
                            num, other = d.split(' in  Word ')
                            num = int(num)
                            num2, rest = other.split(',')
                            num2 = int(num2[2:])

                            if 8 <= num <= 15:
                                num -= 8
                                new_data.append('DB' + str(num2 * 2) + ',' + rest + '.' + str(num))
                            else:
                                new_data.append('DB' + str(num2 * 2 + 1) + ',' + rest + '.' + str(num))
                        else:
                            if len(d) > 3:
                                tokens = d.split(',')
                                result = []
                                for token in tokens:
                                    s = token[:2]
                                    n = int(token[2:])

                                    z = {
                                        'DB': 'DB',
                                        'DW': 'DBW',
                                        'DD': 'DBD'
                                    }[s]

                                    if s != 'DB':
                                        n *= 2
                                    result.append(z + str(n))
                                new_data.append(','.join(result))
                            else:
                                new_data.append(d)
                    else:
                        new_data.append(d)

                file_out.write('\t'.join(new_data))
            else:
                file_out.write(line)
