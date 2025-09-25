import csv

input_csv = "review_data.csv"
output_txt = "insert_review.txt"
table_name = "review"
max_rows = 36483

with open(input_csv, encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    header = next(reader)
    rows = []
    for i, row in enumerate(reader):
        if i >= max_rows:
            break
        values = []
        for val in row:
            if val == "":
                values.append("NULL")
            else:
                # Escapa aspas simples e envolve em aspas simples
                escaped = val.replace("'", "''")
                values.append(f"'{escaped}'")
        rows.append(f"({', '.join(values)})")

query = f"INSERT INTO {table_name} ({', '.join(header)}) VALUES\n" + ",\n".join(rows) + ";"

with open(output_txt, "w", encoding="utf-8") as f:
    f.write(query)
