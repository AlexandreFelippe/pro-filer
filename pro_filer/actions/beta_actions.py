def is_match(search_term, file_name, case_sensitive=True):
    if not case_sensitive:
        search_term = search_term.lower()
        file_name = file_name.lower()

    return search_term in file_name


def show_deepest_file(context):
    if "all_files" not in context or not context["all_files", []]:
        print("No files found")
    else:
        deepest_file = max(context["all_files"], key=lambda x: x.count('/'))
        print(f"Deepest file: {deepest_file}")


def find_file_by_name(context, search_term, case_sensitive=True):
    if not search_term:
        return []

    found_files = []

    for path in context["all_files"]:
        file_name = path.split("/")[-1]

        if is_match(search_term, file_name, case_sensitive):
            found_files.append(path)

    return found_files
