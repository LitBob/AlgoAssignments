def parse_brute_line(line):
    parts = line.split(', ')
    data = {p.split(': ')[0]: p.split(': ')[1] for p in parts}
    return data

def parse_brute_file(filename):
    with open(filename, 'r') as file:
        file_name = file.readline().strip().replace("data/", "")
        return {line.split()[0]: parse_brute_line(line.split()[1]) for line in file if line.strip()}

def parse_attempt_file(filename):
    with open(filename, 'r') as file:
        headers = file.readline().strip().split('\t')[1:]
        return {line.split('\t')[0]: dict(zip(headers, line.strip().split('\t')[1:])) for line in file}

def compare_files(brute_file, attempt_file):
    brute_data = parse_brute_file(brute_file)
    attempt_data = parse_attempt_file(attempt_file)

    header_map = {'A': 'alternate', 'F': 'few', 'M': 'many', 'N': 'none', 'S': 'some'}

    mismatches = []
    for instance, brute_values in brute_data.items():
        if instance in attempt_data:
            attempt_values = attempt_data[instance]
            for header, brute_key in header_map.items():
                if brute_key in brute_values and header in attempt_values:
                    if str(brute_values[brute_key]).lower() != str(attempt_values[header]).lower():
                        mismatches.append(instance)
                        break

    return mismatches

# Usage
brute_file = 'brute-force.txt'
attempt_file = 'output-2023-11-27 18:28:42.220062.txt'
mismatched_instances = compare_files(brute_file, attempt_file)
print("Mismatched instances:", mismatched_instances)
