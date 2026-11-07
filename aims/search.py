def search_by_title(dvd_list, keyword):
    results = []
    for dvd in dvd_list:
        # Sử dụng .lower() trên cả tiêu đề và từ khóa để chuyển hết về chữ thường
        if keyword.lower() in dvd.title.lower():
            results.append(dvd)
    return results
