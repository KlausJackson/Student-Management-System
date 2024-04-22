def merge_files(input_prefix, output_file):
    with open(output_file, 'w') as merged_file:
        for i in range(1, 5):
            filename = f"{input_prefix}_{i}.py"
            with open(filename, 'r') as f:
                merged_file.write(f.read())

    print("Files merged successfully.")


input_prefix = "_icons_rc"  # Prefix of the input files
output_file = "_icons_rc.py"  # Name of the merged output file

merge_files(input_prefix, output_file)
