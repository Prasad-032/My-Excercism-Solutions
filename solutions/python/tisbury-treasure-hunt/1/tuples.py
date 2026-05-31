def get_coordinate(record):
    return record[1]

def convert_coordinate(coordinate):
    return (coordinate[0], coordinate[1])

def compare_records(azara_record, rui_record):
    return convert_coordinate(azara_record[1]) == rui_record[1]

def create_record(azara_record, rui_record):
    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    else:
        return "not a match"

def clean_up(combined_record_group):
    report = ""
    for record in combined_record_group:
        cleaned = record[:1] + record[2:]
        report += str(cleaned) + "\n"
    return report      
        
        
        