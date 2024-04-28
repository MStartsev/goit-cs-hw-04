def search_files(files, keywords):
    try:
        results = {keyword: [] for keyword in keywords}
        for file in files:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
                for keyword in keywords:
                    if keyword in content:
                        results[keyword].append(file)
        return results

    except Exception as e:
        print(f"Error while reading {file}: {e}")

def search_files_sequential(files, keywords):
    return search_files(files, keywords)
