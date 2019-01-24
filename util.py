import csv


def flattenjson(b, delim):
    val = {}
    for key in b.keys():
        if isinstance(b[key], dict):
            get = flattenjson(b[key], delim)
            for sub_key in get.keys():
                val[key + delim + sub_key] = get[sub_key]
        else:
            val[key] = b[key]
    return val


def to_csv(fname, result):
    input = list(map(lambda x: flattenjson(x, "_"), result))
    columns = list(set(x for y in input for x in y.keys()))
    with open(fname, 'w') as out_file:
        csv_w = csv.writer(out_file)
        csv_w.writerow(columns)
        for i_r in input:
            csv_w.writerow(map(lambda x: i_r.get(x, ""), columns))
